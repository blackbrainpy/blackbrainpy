# -*- coding: utf-8 -*-
"""Generates activity.svg, stats.svg and builds.svg in the GENZ TECH Terminal style
from live GitHub API data. Run by .github/workflows/stats.yml."""
import os, json, datetime, urllib.request

LOGIN = os.environ.get("GH_LOGIN", "blackbrainpy")
TOKEN = os.environ.get("GH_TOKEN", "")
D = os.path.dirname(os.path.abspath(__file__))

# GENZ TECH 'Terminal' tokens. Accent is reserved - Signal only for
# indices, the prompt, and single data highlights. No glows, no shadows.
YEL = "#FF4D00"   # Signal
MAG = "#FF4D00"   # Signal (single accent - no second colour)
CYA = "#8A8D91"   # Mist, for language labels
BG  = "#0A0B0C"   # Void
INK = "#F2F2F0"   # Bone
HAIR = "#1D1F22"
MID = "#A9ABAE"
LOW = "#7D8084"
MONO = "'IBM Plex Mono','SF Mono','Consolas','DejaVu Sans Mono',monospace"
BLACK = "'IBM Plex Mono','SF Mono','Consolas',monospace"

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
.hd{font-family:@BLACK@;font-weight:600;font-size:17px;letter-spacing:-0.01em;fill:@INK@}
.big{font-family:@BLACK@;font-weight:600;font-size:34px;fill:@INK@}
.m{font-family:@MONO@;font-weight:500;font-size:11px;letter-spacing:0.07em}
.v{font-family:'IBM Plex Sans','Segoe UI',Arial,sans-serif;font-size:14px;fill:@MID@}
@keyframes dr{0%{stroke-dashoffset:2600}100%{stroke-dashoffset:0}}
@keyframes fi{0%{opacity:0}100%{opacity:.22}}
.ln{stroke-dasharray:2600;animation:dr 2.6s ease-out forwards}
.ar{animation:fi 2.6s ease-out forwards;opacity:0}
</style>
<linearGradient id="ag" x1="0" y1="0" x2="0" y2="1">
<stop offset="0" stop-color="@YEL@" stop-opacity="0.42"/>
<stop offset="1" stop-color="@YEL@" stop-opacity="0"/></linearGradient>
</defs>""".replace("@BLACK@", BLACK).replace("@MONO@", MONO).replace(
    "@YEL@", YEL).replace("@INK@", INK).replace("@MID@", MID)

def frame(w, h, title, right):
    return ('<rect width="%d" height="%d" fill="%s"/>\n'
            '<text class="m" x="28" y="42" fill="%s">'
            '<tspan fill="%s">// </tspan>%s</text>\n'
            '<text class="m" x="%d" y="42" fill="%s" text-anchor="end">%s</text>\n'
            '<line x1="28" y1="60" x2="%d" y2="60" stroke="%s" stroke-width="1"/>\n'
            % (w, h, BG, LOW, YEL, title, w - 28, LOW, right, w - 28, HAIR))

def tail(w, h):
    return '</svg>\n'

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
    s += frame(W, H, "activity &#183; last 30 days", "peak %d/day" % mx)
    for i in range(5):
        y = yt + (yb - yt) * i / 4.0
        s += '<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="1"/>\n' % (x0, y, x1, y, HAIR)
        s += '<text class="m" x="%d" y="%.1f" fill="%s" text-anchor="end">%d</text>\n' % (x0 - 12, y + 4, LOW, round(mx * (4 - i) / 4.0))
    s += '<path d="%s" fill="url(#ag)" class="ar"/>\n' % area
    s += '<path d="%s" fill="none" stroke="%s" stroke-width="2.5" class="ln"/>\n' % (line, YEL)
    for i in range(len(pts)):
        if pts[i][1] == mx:
            s += '<circle cx="%.1f" cy="%.1f" r="5" fill="%s"/>\n' % (xs[i], ys[i], MAG)
    for i in range(0, len(pts), 6):
        s += '<text class="m" x="%.1f" y="%d" fill="%s" text-anchor="middle">%s</text>\n' % (xs[i], yb + 24, LOW, pts[i][0][5:])
    s += '<text class="m" x="%d" y="%d" fill="%s">DAYS</text>\n' % (x0, yb + 48, LOW)
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
             # GITHUB_TOKEN in Actions only sees public data, so these are
             # public-only counts. Labelled as such rather than overstated.
             ("PUBLIC STARS", stars),
             ("PUBLIC REPOS", user["repositories"]["totalCount"]),
             ("FOLLOWERS", user["followers"]["totalCount"])]
    s = head(W, H, "Data streams")
    s += frame(W, H, "telemetry &#183; rolling 12 months", "%d contributions" % cal["totalContributions"])
    for i, (k, v) in enumerate(tiles):
        x = 62 + (i % 3) * 390
        y = 92 + (i // 3) * 108
        s += ('<g transform="translate(%d,%d)">\n'
              '<rect x="0" y="-34" width="3" height="52" fill="%s"/>\n'
              '<text class="big" x="18" y="0">%s</text>\n'
              '<text class="m" x="20" y="20" fill="%s">%s</text>\n</g>\n'
              % (x, y, '#26282B', v, LOW, k))
    s += ('<g transform="translate(62,290)">\n'
          '<text class="m" x="0" y="0" fill="%s">current streak</text>\n'
          '<text class="m" x="180" y="0" fill="%s">%d DAYS</text>\n'
          '<text class="m" x="330" y="0" fill="%s">longest streak</text>\n'
          '<text class="m" x="520" y="0" fill="%s">%d DAYS</text>\n'
          '<text class="m" x="670" y="0" fill="%s">window start</text>\n'
          '<text class="m" x="830" y="0" fill="%s">%s</text>\n</g>\n'
          % (LOW, INK, cur, LOW, INK, lng, LOW, INK, ds[0][0] if ds else "-"))
    s += tail(W, H)
    return s

def builds(user):
    repos = [r for r in user["repositories"]["nodes"]
             if not r["isPrivate"] and r["name"].lower() != LOGIN.lower()][:4]
    W, H = 1200, 60 + 68 * len(repos) + 30
    s = head(W, H, "Active builds")
    s += frame(W, H, "repo scan &#183; public", "%d tracked" % len(repos))
    for i, r in enumerate(repos):
        y = 84 + i * 68
        lang = (r["primaryLanguage"] or {}).get("name") or "TEXT"
        desc = esc(r["description"] or "no description on file")
        if len(desc) > 78:
            desc = desc[:75] + "..."
        s += ('<g transform="translate(62,%d)">\n'
              '<rect x="0" y="-20" width="3" height="44" fill="%s"/>\n'
              '<text class="hd" x="18" y="0">%s</text>\n'
              '<text class="v" x="18" y="22">%s</text>\n'
              '<text class="m" x="900" y="0" fill="%s">%s</text>\n'
              '<text class="m" x="1076" y="0" fill="%s" text-anchor="end">stars %d</text>\n'
              '<text class="m" x="1076" y="22" fill="%s" text-anchor="end">forks %d</text>\n'
              '<line x1="0" y1="34" x2="1076" y2="34" stroke="%s" stroke-width="1"/>\n</g>\n'
              % (y, YEL, esc(r["name"]), desc, CYA, lang.lower(), INK,
                 r["stargazerCount"], LOW, r["forkCount"], HAIR))
    s += tail(W, H)
    return s

if __name__ == "__main__":
    u = gql()
    ds = days(u)
    write("activity.svg", activity(ds))
    write("stats.svg", stats(u, ds))
    write("builds.svg", builds(u))
