# -*- coding: utf-8 -*-
"""Generates activity.svg, stats.svg and builds.svg in the Edgerunners style
from live GitHub API data. Run by .github/workflows/stats.yml."""
import os, json, datetime, urllib.request

LOGIN = os.environ.get("GH_LOGIN", "blackbrainpy")
TOKEN = os.environ.get("GH_TOKEN", "")
D = os.path.dirname(os.path.abspath(__file__))

YEL, MAG, CYA, BG, INK = "#FCEE0A", "#FF003C", "#00E5FF", "#08070a", "#EDEAE0"
MONO = "'Consolas','SF Mono','DejaVu Sans Mono',monospace"
BLACK = "'Arial Black','Helvetica Neue',Impact,sans-serif"

Q = """
query($login:String!){
  user(login:$login){
    followers{totalCount}
    contributionsCollection{
      totalCommitContributions
      totalPullRequestContributions
      totalIssueContributions
      contributionCalendar{
        totalContributions
        weeks{ contributionDays{ date contributionCount } }
      }
    }
    repositories(first:100, ownerAffiliations:OWNER, isFork:false,
                 orderBy:{field:PUSHED_AT,direction:DESC}){
      totalCount
      nodes{ name description stargazerCount forkCount isPrivate
             primaryLanguage{name} }
    }
  }
}
"""

def gql():
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": Q, "variables": {"login": LOGIN}}).encode(),
        headers={"Authorization": "bearer " + TOKEN,
                 "Content-Type": "application/json",
                 "User-Agent": "blackbrainpy-profile"})
    return json.load(urllib.request.urlopen(req))["data"]["user"]

def days(user):
    out = []
    for w in user["contributionsCollection"]["contributionCalendar"]["weeks"]:
        for d in w["contributionDays"]:
            out.append((d["date"], d["contributionCount"]))
    out.sort()
    return out

def streaks(ds):
    cur = lng = run = 0
    for _, c in ds:
        run = run + 1 if c > 0 else 0
        lng = max(lng, run)
    for _, c in reversed(ds):
        if c > 0:
            cur += 1
        else:
            break
    return cur, lng

def esc(s):
    return (s or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def write(name, body):
    with open(os.path.join(D, name), "wb") as fh:
        fh.write(body.encode("utf-8"))
    print("wrote %-16s %6d bytes" % (name, len(body.encode("utf-8"))))

CHROME = """<defs>
<style>
.hd{font-family:@BLACK@;font-weight:900;font-size:16px;letter-spacing:2px;fill:@YEL@}
.big{font-family:@BLACK@;font-weight:900;font-size:38px;fill:@YEL@}
.m{font-family:@MONO@;font-size:11px;letter-spacing:3px}
.v{font-family:@MONO@;font-size:13px;fill:@INK@}
@keyframes bl{0%,49%{opacity:1}50%,100%{opacity:.12}}
@keyframes dr{0%{stroke-dashoffset:2600}100%{stroke-dashoffset:0}}
@keyframes fi{0%{opacity:0}100%{opacity:.30}}
.bk{animation:bl 1.2s infinite steps(1)}
.ln{stroke-dasharray:2600;animation:dr 2.6s ease-out forwards}
.ar{animation:fi 2.6s ease-out forwards;opacity:0}
</style>
<pattern id="gg" width="40" height="40" patternUnits="userSpaceOnUse">
<path d="M40 0H0V40" fill="none" stroke="@YEL@" stroke-width="0.5" opacity="0.08"/></pattern>
<pattern id="ss" width="3" height="3" patternUnits="userSpaceOnUse">
<rect width="3" height="1.4" fill="#000" opacity="0.45"/></pattern>
<linearGradient id="ag" x1="0" y1="0" x2="0" y2="1">
<stop offset="0" stop-color="@YEL@" stop-opacity="0.55"/>
<stop offset="1" stop-color="@YEL@" stop-opacity="0"/></linearGradient>
</defs>""".replace("@BLACK@", BLACK).replace("@MONO@", MONO).replace("@YEL@", YEL).replace("@INK@", INK)

def frame(w, h, title, right):
    return ('<rect width="%d" height="%d" fill="%s"/>\n'
            '<rect width="%d" height="%d" fill="url(#gg)"/>\n'
            '<rect x="40" y="26" width="3" height="%d" fill="%s" opacity="0.5"/>\n'
            '<text class="m" x="60" y="34" fill="%s" opacity="0.45">%s</text>\n'
            '<circle cx="%d" cy="30" r="3.5" fill="%s" class="bk"/>\n'
            '<text class="m" x="%d" y="34" fill="%s" opacity="0.45" text-anchor="end">%s</text>\n'
            % (w, h, BG, w, h, h - 52, YEL, YEL, title, w - 48, MAG, w - 60, YEL, right))

def tail(w, h):
    return ('<g stroke="%s" stroke-width="2" fill="none" opacity="0.8">'
            '<path d="M%d 20 L%d 20 L%d 36"/><path d="M%d %d L%d %d L%d %d"/></g>\n'
            '<rect width="%d" height="%d" fill="url(#ss)" opacity="0.5"/>\n</svg>\n'
            % (YEL, w - 40, w - 24, w - 24, w - 40, h - 20, w - 24, h - 20, w - 24, h - 36, w, h))

def head(w, h, label):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" '
            'role="img" aria-label="%s">\n%s\n' % (w, h, w, h, label, CHROME))

def activity(ds):
    W, H = 1200, 330
    pts = ds[-30:]
    mx = max([c for _, c in pts]) or 1
    x0, x1, yb, yt = 70, 1130, 268, 76
    xs = [x0 + (x1 - x0) * i / float(len(pts) - 1) for i in range(len(pts))]
    ys = [yb - (yb - yt) * (c / float(mx)) for _, c in pts]
    line = " ".join("%s%.1f,%.1f" % ("M" if i == 0 else "L", xs[i], ys[i]) for i in range(len(pts)))
    area = line + " L%.1f,%.1f L%.1f,%.1f Z" % (xs[-1], yb, xs[0], yb)
    s = head(W, H, "Neural activity log")
    s += frame(W, H, "NEURAL ACTIVITY LOG // LAST 30 DAYS", "PEAK %d/DAY" % mx)
    for i in range(5):
        y = yt + (yb - yt) * i / 4.0
        s += '<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="1" opacity="0.10"/>\n' % (x0, y, x1, y, YEL)
        s += '<text class="m" x="%d" y="%.1f" fill="%s" opacity="0.4" text-anchor="end">%d</text>\n' % (x0 - 12, y + 4, YEL, round(mx * (4 - i) / 4.0))
    s += '<path d="%s" fill="url(#ag)" class="ar"/>\n' % area
    s += '<path d="%s" fill="none" stroke="%s" stroke-width="2.5" class="ln"/>\n' % (line, YEL)
    for i in range(len(pts)):
        if pts[i][1] == mx:
            s += '<circle cx="%.1f" cy="%.1f" r="5" fill="%s"/>\n' % (xs[i], ys[i], MAG)
    for i in range(0, len(pts), 6):
        s += '<text class="m" x="%.1f" y="%d" fill="%s" opacity="0.4" text-anchor="middle">%s</text>\n' % (xs[i], yb + 24, YEL, pts[i][0][5:])
    s += '<text class="m" x="%d" y="%d" fill="%s" opacity="0.35">DAYS</text>\n' % (x0, yb + 48, YEL)
    s += tail(W, H)
    return s

def stats(user, ds):
    W, H = 1200, 330
    c = user["contributionsCollection"]
    cal = c["contributionCalendar"]
    repos = user["repositories"]["nodes"]
    stars = sum(r["stargazerCount"] for r in repos)
    cur, lng = streaks(ds)
    tiles = [("COMMITS", c["totalCommitContributions"]),
             ("PULL REQUESTS", c["totalPullRequestContributions"]),
             ("ISSUES", c["totalIssueContributions"]),
             ("STARS EARNED", stars),
             ("REPOSITORIES", user["repositories"]["totalCount"]),
             ("FOLLOWERS", user["followers"]["totalCount"])]
    s = head(W, H, "Data streams")
    s += frame(W, H, "TELEMETRY // ROLLING 12 MONTHS", "%d CONTRIBUTIONS" % cal["totalContributions"])
    for i, (k, v) in enumerate(tiles):
        x = 62 + (i % 3) * 390
        y = 92 + (i // 3) * 108
        s += ('<g transform="translate(%d,%d)">\n'
              '<rect x="0" y="-34" width="3" height="52" fill="%s" opacity="0.55"/>\n'
              '<text class="big" x="18" y="0">%s</text>\n'
              '<text class="m" x="20" y="20" fill="%s" opacity="0.5">%s</text>\n</g>\n'
              % (x, y, MAG, v, YEL, k))
    s += ('<g transform="translate(62,290)">\n'
          '<text class="m" x="0" y="0" fill="%s" opacity="0.5">CURRENT STREAK</text>\n'
          '<text class="m" x="180" y="0" fill="%s">%d DAYS</text>\n'
          '<text class="m" x="330" y="0" fill="%s" opacity="0.5">LONGEST STREAK</text>\n'
          '<text class="m" x="520" y="0" fill="%s">%d DAYS</text>\n'
          '<text class="m" x="670" y="0" fill="%s" opacity="0.5">WINDOW START</text>\n'
          '<text class="m" x="830" y="0" fill="%s">%s</text>\n</g>\n'
          % (YEL, INK, cur, YEL, INK, lng, YEL, INK, ds[0][0] if ds else "-"))
    s += tail(W, H)
    return s

def builds(user):
    repos = [r for r in user["repositories"]["nodes"]
             if not r["isPrivate"] and r["name"].lower() != LOGIN.lower()][:4]
    W, H = 1200, 60 + 68 * len(repos) + 30
    s = head(W, H, "Active builds")
    s += frame(W, H, "REPO SCAN // PUBLIC", "%d TRACKED" % len(repos))
    for i, r in enumerate(repos):
        y = 84 + i * 68
        lang = (r["primaryLanguage"] or {}).get("name") or "TEXT"
        desc = esc(r["description"] or "no description on file")
        if len(desc) > 78:
            desc = desc[:75] + "..."
        s += ('<g transform="translate(62,%d)">\n'
              '<rect x="0" y="-20" width="3" height="44" fill="%s" opacity="0.7"/>\n'
              '<text class="hd" x="18" y="0">%s</text>\n'
              '<text class="v" x="18" y="22" opacity="0.7">%s</text>\n'
              '<text class="m" x="900" y="0" fill="%s" opacity="0.75">%s</text>\n'
              '<text class="m" x="1076" y="0" fill="%s" text-anchor="end">STARS %d</text>\n'
              '<text class="m" x="1076" y="22" fill="%s" opacity="0.5" text-anchor="end">FORKS %d</text>\n'
              '<line x1="0" y1="34" x2="1076" y2="34" stroke="%s" stroke-width="1" opacity="0.10"/>\n</g>\n'
              % (y, YEL, esc(r["name"]), desc, CYA, lang.upper(), YEL,
                 r["stargazerCount"], YEL, r["forkCount"], YEL))
    s += tail(W, H)
    return s

if __name__ == "__main__":
    u = gql()
    ds = days(u)
    write("activity.svg", activity(ds))
    write("stats.svg", stats(u, ds))
    write("builds.svg", builds(u))
