# -*- coding: utf-8 -*-
"""GENZ TECH 'Terminal' brand system -> profile SVGs.
Tokens per design_handoff_genztech/README.md. No glows, no shadows,
accent reserved. Run: python build.py"""
import os
D = os.path.dirname(os.path.abspath(__file__))

VOID    = "#0A0B0C"
PANEL   = "#0E0F11"
PANEL2  = "#101216"
HAIR    = "#1D1F22"
BORDER  = "#26282B"
SIGNAL  = "#FF4D00"
BONE    = "#F2F2F0"
TEXTHI  = "#E7E7E5"
BODY    = "#C7C8CA"
TEXTMID = "#A9ABAE"
MIST    = "#8A8D91"
TEXTLOW = "#7D8084"
FAINT   = "#6B6E72"

MONO = "'IBM Plex Mono','SF Mono','Consolas','DejaVu Sans Mono',monospace"
SANS = "'IBM Plex Sans','Segoe UI','Helvetica Neue',Arial,sans-serif"

CSS = """
.mono{font-family:@MONO@}
.sans{font-family:@SANS@}
.disp{font-family:@MONO@;font-weight:600;letter-spacing:-0.03em;fill:@BONE@}
.sec{font-family:@MONO@;font-weight:600;font-size:22px;letter-spacing:-0.02em;fill:@BONE@}
.kick{font-family:@MONO@;font-weight:600;font-size:11px;letter-spacing:0.18em;fill:@SIGNAL@}
.lab{font-family:@MONO@;font-weight:600;font-size:11px;letter-spacing:0.16em;fill:@TEXTLOW@}
.meta{font-family:@MONO@;font-weight:500;font-size:11px;letter-spacing:0.07em;fill:@TEXTLOW@}
.dek{font-family:@SANS@;font-size:15px;fill:@TEXTMID@}
.hl{font-family:@SANS@;font-weight:500;font-size:19px;fill:@TEXTHI@}
.idx{font-family:@MONO@;font-weight:600;font-size:13px;fill:@SIGNAL@}
.val{font-family:@MONO@;font-weight:600;font-size:34px;fill:@BONE@}
@keyframes blink{0%,55%{opacity:1}56%,100%{opacity:0}}
.cur{animation:blink 1.1s steps(1) infinite}
""".replace("@MONO@", MONO).replace("@SANS@", SANS).replace("@BONE@", BONE
    ).replace("@SIGNAL@", SIGNAL).replace("@TEXTLOW@", TEXTLOW).replace(
    "@TEXTMID@", TEXTMID).replace("@TEXTHI@", TEXTHI)

DEFS = """<defs>
<style>@CSS@</style>
<pattern id="stripe" width="34" height="34" patternUnits="userSpaceOnUse" patternTransform="rotate(135)">
<rect width="34" height="34" fill="@PANEL2@"/><rect width="14" height="34" fill="#ffffff" opacity="0.04"/>
</pattern>
</defs>""".replace("@CSS@", CSS).replace("@PANEL2@", PANEL2)


def head(w, h, label, bar=False):
    """bar=True draws the 2px Signal rule. Brand pins it to the top of a
    *page*, so only the header carries it - repeating it on every section
    would make the accent ambient, which the guide forbids."""
    s = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" '
         'role="img" aria-label="%s">\n%s\n<rect width="%d" height="%d" fill="%s"/>\n'
         % (w, h, w, h, label, DEFS, w, h, VOID))
    if bar:
        s += '<rect x="0" y="0" width="%d" height="2" fill="%s"/>\n' % (w, SIGNAL)
    return s


def wordmark(x, y, size=26, cursor=False):
    """<genz/>tech - slash always Signal, 'tech' in Mist."""
    s = ('<text class="mono" x="%d" y="%d" font-weight="600" font-size="%d" letter-spacing="-0.02em">'
         '<tspan fill="%s">&lt;genz</tspan><tspan fill="%s">/</tspan>'
         '<tspan fill="%s">&gt;</tspan><tspan fill="%s">tech</tspan></text>\n'
         % (x, y, size, BONE, SIGNAL, BONE, MIST))
    if cursor:
        s += ('<rect x="%d" y="%d" width="%d" height="%d" fill="%s" class="cur"/>\n'
              % (x + int(size * 6.05), y - int(size * 0.78), int(size * 0.42), int(size * 0.86), SIGNAL))
    return s


def hairline(x1, y, x2):
    return '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="1"/>\n' % (x1, y, x2, y, HAIR)


def placeholder(x, y, w, h, caption):
    """Striped image placeholder + L corner tick + mono caption."""
    return ('<rect x="%d" y="%d" width="%d" height="%d" fill="url(#stripe)" stroke="%s" stroke-width="1"/>\n'
            '<path d="M%d %d L%d %d L%d %d" fill="none" stroke="%s" stroke-width="2" opacity="0.85"/>\n'
            '<text class="meta" x="%d" y="%d" fill="%s">%s</text>\n'
            % (x, y, w, h, BORDER,
               x, y + h - 44, x, y + h, x + 44, y + h, SIGNAL,
               x + 12, y + 22, FAINT, caption))


def live(x, y):
    return ('<circle cx="%d" cy="%d" r="3.5" fill="%s"/>\n'
            '<text class="meta" x="%d" y="%d" fill="%s">live</text>\n'
            % (x, y - 4, SIGNAL, x + 12, y, TEXTMID))


def header():
    """780x340 so it pairs inline with the 380x340 operator.gif. A real
    <table> would work too, but GitHub's markdown CSS draws cell borders."""
    W, H = 780, 340
    G = 28
    s = head(W, H, "blackbrainpy - GENZ TECH", bar=True)
    s += wordmark(G, 46, 22)
    s += live(W - G - 42, 44)
    s += hairline(G, 64, W - G)
    s += '<text class="kick" x="%d" y="112">~/ github &#183; profile</text>\n' % G
    s += ('<text class="disp" x="%d" y="172" font-size="54">blackbrainpy'
          '<tspan fill="%s">.</tspan></text>\n' % (G, SIGNAL))
    s += ('<text class="dek" x="%d" y="212" font-size="16">building GENZ TECH &#8212; latest tech news, decoded.</text>\n' % G)
    s += ('<text class="dek" x="%d" y="236" font-size="16" fill="%s">acoustic wall scanner &#183; cost calculators &#183; a free dev-data API.</text>\n'
          % (G, TEXTLOW))
    s += hairline(G, 268, W - G)
    s += ('<text class="meta" x="%d" y="298">NEW YORK &#183; REMOTE &#183; FULL-STACK</text>\n' % G)
    # explicit x, not text-anchor="end": anchoring a multi-tspan run makes
    # the Signal "$" overlap the label in some renderers.
    s += ('<text class="mono" x="%d" y="298" font-size="12" font-weight="500" fill="%s">'
          '<tspan fill="%s">$ </tspan>genztech.blog</text>\n' % (W - G - 112, TEXTMID, SIGNAL))
    s += "</svg>\n"
    return s


def icon(kind, x, y, col):
    """Platform marks in a 16x16 box, monochrome per the brand's icon rule.
    The X mark is the real angular glyph (filled), not two crossed strokes -
    a plain cross reads as a close/dismiss button."""
    if kind == "x":
        # official X geometry on a 24u grid, scaled to the 16u box
        return ('<g transform="translate(%d,%d) scale(0.6667)" fill="%s" stroke="none">'
                '<path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817'
                'L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833'
                'L7.084 4.126H5.117z"/></g>\n' % (x, y, col))
    g = ('<g transform="translate(%d,%d)" fill="none" stroke="%s" stroke-width="1.5" '
         'stroke-linecap="round" stroke-linejoin="round">' % (x, y, col))
    if kind == "site":                     # globe
        g += ('<circle cx="8" cy="8" r="6.6"/>'
              '<ellipse cx="8" cy="8" rx="3" ry="6.6"/>'
              '<path d="M1.6 8 H14.4"/>')
    elif kind == "ig":                     # camera body + lens + flash
        g += ('<rect x="1.4" y="1.4" width="13.2" height="13.2" rx="4"/>'
              '<circle cx="8" cy="8" r="3.4"/>'
              '<circle cx="11.9" cy="4.1" r="0.9" fill="%s" stroke="none"/>' % col)
    elif kind == "tt":                     # eighth note
        g += ('<path d="M6.4 12.1 V2.6 c1.3 2 2.9 2.9 4.9 3.0"/>'
              '<circle cx="4.2" cy="12.2" r="2.5"/>')
    elif kind == "mail":                   # envelope
        g += ('<rect x="1.2" y="3.2" width="13.6" height="9.6" rx="1.5"/>'
              '<path d="M1.9 4.4 L8 9.2 L14.1 4.4"/>')
    return g + "</g>\n"


def chip(label, kind):
    """Bordered link chip, per the brand's topic-chip pattern (radius 3px,
    Border stroke). Each is its own SVG so the README can wrap it in <a> -
    markdown links would render in GitHub blue."""
    W = int(len(label) * 7.25) + 62
    H = 40
    s = head(W, H, label)
    s += ('<rect x="0.5" y="0.5" width="%d" height="%d" rx="3" fill="%s" stroke="%s" stroke-width="1"/>\n'
          % (W - 1, H - 1, PANEL, BORDER))
    s += icon(kind, 14, 12, SIGNAL)
    s += ('<text class="mono" x="40" y="25" font-size="12" font-weight="500" letter-spacing="0.06em" fill="%s">%s</text>\n'
          % (TEXTMID, label))
    s += "</svg>\n"
    return s


# Labels trimmed so all five fit one ~880px README line instead of orphaning
# the email chip on a second row. Email sits centre of the run.
# Filenames carry -v2: GitHub's camo proxy caches by URL, so overwriting in
# place keeps serving the old icon-less chips.
LINKS = [("genztech.blog", "site"),
         ("@genztechblog", "x"),
         ("info@genztech.blog", "mail"),
         ("instagram", "ig"),
         ("tiktok", "tt")]


def section(slug, cmd, right, num):
    W, H = 1200, 92
    G = 28
    s = head(W, H, cmd)
    s += ('<text class="sec" x="%d" y="52"><tspan fill="%s">$ </tspan>%s</text>\n' % (G, SIGNAL, cmd))
    s += ('<text class="meta" x="%d" y="52" text-anchor="end">%s</text>\n' % (W - G, right))
    s += hairline(G, 72, W - G)
    s += "</svg>\n"
    return s


def dossier():
    W, H = 1200, 356
    G = 28
    rows = [("handle", "blackbrainpy"),
            ("org", "GENZ TECH"),
            ("location", "New York &#183; remote"),
            ("focus", "tech journalism &#183; full-stack &#183; data tooling"),
            ("writing", "genztech.blog &#8212; daily tech news for Gen Z"),
            ("building", "acoustic wall scanner &#183; repair-cost calculators &#183; public dev API")]
    s = head(W, H, "whoami")
    s += ('<rect x="%d" y="28" width="%d" height="%d" fill="%s" stroke="%s" stroke-width="1" rx="5"/>\n'
          % (G, W - 2 * G, H - 56, PANEL, HAIR))
    s += '<text class="lab" x="%d" y="66" fill="%s">// operator</text>\n' % (G + 28, FAINT)
    for i, (k, v) in enumerate(rows):
        y = 104 + i * 30
        s += '<text class="meta" x="%d" y="%d">%s</text>\n' % (G + 28, y, k.upper())
        s += ('<text class="sans" x="%d" y="%d" font-size="15" fill="%s">%s</text>\n'
              % (G + 190, y, BODY, v))
    s += hairline(G + 28, 276, W - G - 28)
    s += ('<text class="mono" x="%d" y="308" font-size="13" fill="%s">'
          '<tspan fill="%s">$ </tspan>status: shipping</text>\n' % (G + 28, TEXTMID, SIGNAL))
    s += ('<rect x="%d" y="297" width="9" height="14" fill="%s" class="cur"/>\n' % (G + 232, SIGNAL))
    s += "</svg>\n"
    return s


STACK = [("python", "scrapers, data pipelines, the API build"),
         ("javascript", "site logic, interactive explainers"),
         ("html / css", "the genztech.blog front end"),
         ("node.js", "tooling and build steps"),
         ("git / github actions", "everything ships on a schedule"),
         ("json / rest", "the free public dev-data API")]


def stack():
    """Numbered terminal rows - Signal index, name, dek. Brand 'Latest' pattern."""
    W = 1200
    G = 28
    H = 40 + len(STACK) * 52 + 20
    s = head(W, H, "stack")
    for i, (name, note) in enumerate(STACK):
        y = 62 + i * 52
        s += '<text class="idx" x="%d" y="%d">%02d</text>\n' % (G, y, i + 1)
        s += ('<text class="mono" x="%d" y="%d" font-size="16" font-weight="600" fill="%s">%s</text>\n'
              % (G + 46, y, BONE, name))
        s += ('<text class="sans" x="%d" y="%d" font-size="14" fill="%s">%s</text>\n'
              % (G + 300, y, TEXTMID, note))
        s += hairline(G, y + 20, W - G)
    s += "</svg>\n"
    return s


def footer():
    W, H = 1200, 260
    G = 28
    s = head(W, H, "subscribe")
    s += ('<rect x="%d" y="24" width="%d" height="150" fill="%s" stroke="%s" stroke-width="1" rx="5"/>\n'
          % (G, W - 2 * G, PANEL, HAIR))
    s += '<text class="lab" x="%d" y="60" fill="%s">// newsletter</text>\n' % (G + 28, FAINT)
    s += ('<text class="sec" x="%d" y="98" font-size="30"><tspan fill="%s">$ </tspan>subscribe --weekly</text>\n'
          % (G + 28, SIGNAL))
    s += ('<text class="sans" x="%d" y="126" font-size="15" fill="%s">'
          'the tech that actually mattered this week. no hype, no filler.</text>\n' % (G + 28, TEXTMID))
    s += ('<rect x="%d" y="86" width="300" height="40" fill="none" stroke="%s" stroke-width="1" rx="3"/>\n'
          % (W - G - 340, BORDER))
    s += ('<text class="mono" x="%d" y="112" font-size="13" fill="%s">'
          '<tspan fill="%s">&#8594; </tspan>genztech.blog</text>\n' % (W - G - 322, FAINT, SIGNAL))
    s += ('<text class="meta" x="%d" y="152" fill="%s">// built on the internet &#183; ships daily</text>\n'
          % (G + 28, FAINT))
    s += hairline(G, 206, W - G)
    s += wordmark(G, 240, 16)
    s += ('<text class="meta" x="%d" y="240" text-anchor="end" fill="%s">'
          '&#169; 2026 GENZ TECH &#183; // status: all systems operational</text>\n' % (W - G, FAINT))
    s += "</svg>\n"
    return s


def write(name, body):
    with open(os.path.join(D, name), "wb") as fh:
        fh.write(body.encode("utf-8"))
    print("wrote %-22s %6d bytes" % (name, len(body.encode("utf-8"))))


if __name__ == "__main__":
    write("header.svg", header())
    write("dossier.svg", dossier())
    write("arsenal.svg", stack())
    write("footer.svg", footer())
    for label, slug in LINKS:
        write("link-%s-v2.svg" % slug, chip(label, slug))
    for slug, cmd, right, n in [
            ("stack", "ls ./stack", "6 modules", "01"),
            ("builds", "ls ./builds", "public repos", "02"),
            ("streams", "git log --stat", "rolling 12 months", "03"),
            ("ice", "cat ./contributions", "12h refresh", "04"),
            ("transmission", "curl ./transmission", "channel open", "05")]:
        write("sec-%s.svg" % slug, section(slug, cmd, right, n))
