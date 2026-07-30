# -*- coding: utf-8 -*-
import os
D = os.path.dirname(os.path.abspath(__file__))
SVG = {}

SVG["header.svg"] = u'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 340" width="1200" height="340" role="img" aria-label="BLACKBRAINPY - GENZ TECH">
<defs>
<style>
.ttl{font-family:'Arial Black','Helvetica Neue',Impact,sans-serif;font-weight:900;font-size:104px;letter-spacing:2px}
.mono{font-family:'Consolas','SF Mono','DejaVu Sans Mono',monospace}
@keyframes slice1{0%,86%,100%{transform:translate(0,0)}87%{transform:translate(-18px,0)}89%{transform:translate(11px,0)}90%{transform:translate(0,0)}}
@keyframes slice2{0%,72%,100%{transform:translate(0,0)}74%{transform:translate(14px,0)}76%{transform:translate(-9px,0)}78%{transform:translate(0,0)}}
@keyframes slice3{0%,40%,100%{transform:translate(0,0)}42%{transform:translate(-22px,0)}44%{transform:translate(6px,0)}46%{transform:translate(0,0)}}
@keyframes flick{0%,90%,100%{opacity:1}92%{opacity:.35}94%{opacity:1}96%{opacity:.7}}
@keyframes blip{0%,49%{opacity:1}50%,100%{opacity:.15}}
@keyframes sweep{0%{transform:translate(0,-40px)}100%{transform:translate(0,380px)}}
@keyframes bar{0%{width:0}100%{width:186px}}
.g1{animation:slice1 7s infinite steps(1)}
.g2{animation:slice2 7s infinite steps(1)}
.g3{animation:slice3 7s infinite steps(1)}
.fl{animation:flick 6s infinite}
.bl{animation:blip 1.1s infinite steps(1)}
.sw{animation:sweep 5.5s linear infinite}
.bx{animation:bar 3s ease-out infinite alternate}
</style>
<pattern id="hz" width="30" height="30" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">
<rect width="30" height="30" fill="#0a0a0c"/><rect width="15" height="30" fill="#FCEE0A"/>
</pattern>
<pattern id="sl" width="3" height="3" patternUnits="userSpaceOnUse">
<rect width="3" height="1.4" fill="#000" opacity="0.5"/>
</pattern>
<pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
<path d="M40 0H0V40" fill="none" stroke="#FCEE0A" stroke-width="0.5" opacity="0.10"/>
</pattern>
<clipPath id="c1"><rect x="0" y="118" width="1200" height="26"/></clipPath>
<clipPath id="c2"><rect x="0" y="158" width="1200" height="20"/></clipPath>
<clipPath id="c3"><rect x="0" y="192" width="1200" height="24"/></clipPath>
<filter id="grain"><feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="3" seed="9"/>
<feColorMatrix type="saturate" values="0"/><feComponentTransfer><feFuncA type="linear" slope="0.10"/></feComponentTransfer></filter>
<linearGradient id="fade" x1="0" y1="0" x2="1" y2="0">
<stop offset="0" stop-color="#FCEE0A" stop-opacity="0"/><stop offset="0.5" stop-color="#FCEE0A" stop-opacity="1"/><stop offset="1" stop-color="#FCEE0A" stop-opacity="0"/>
</linearGradient>
</defs>
<rect width="1200" height="340" fill="#08070a"/>
<rect width="1200" height="340" fill="url(#grid)"/>
<rect x="0" y="0" width="1200" height="12" fill="url(#hz)"/>
<rect x="0" y="328" width="1200" height="12" fill="url(#hz)"/>
<g class="mono" fill="#FCEE0A" opacity="0.55" font-size="11" letter-spacing="3">
<text x="42" y="46">SYS.LINK // ESTABLISHED</text>
<text x="42" y="64" opacity="0.6">NODE 291556072 . SECTOR NYC . REL 2.0.77</text>
</g>
<circle cx="34" cy="42" r="4" fill="#FF003C" class="bl"/>
<g class="mono" fill="#FCEE0A" opacity="0.5" font-size="11" letter-spacing="3" text-anchor="end">
<text x="1158" y="46">STATUS . SHIPPING</text>
<text x="1158" y="64" opacity="0.6">UPTIME 100% . PING 4ms</text>
</g>
<g transform="translate(42,290)" class="mono">
<text x="0" y="0" font-size="11" fill="#FCEE0A" opacity="0.5" letter-spacing="3">NEURAL LOAD</text>
<rect x="0" y="8" width="186" height="6" fill="#FCEE0A" opacity="0.15"/>
<rect x="0" y="8" height="6" fill="#FCEE0A" class="bx"/>
</g>
<g transform="translate(1158,296)" class="mono" text-anchor="end">
<text x="0" y="0" font-size="11" fill="#FF003C" opacity="0.7" letter-spacing="3">CYBERPSYCHOSIS: NOMINAL</text>
</g>
<g class="fl">
<text class="ttl" x="60" y="212" fill="#00E5FF" opacity="0.9" transform="translate(-5,0)">BLACKBRAINPY</text>
<text class="ttl" x="60" y="212" fill="#FF003C" opacity="0.9" transform="translate(5,0)">BLACKBRAINPY</text>
<text class="ttl" x="60" y="212" fill="#FCEE0A">BLACKBRAINPY</text>
</g>
<g clip-path="url(#c1)" class="g1"><text class="ttl" x="60" y="212" fill="#FF003C" opacity="0.95">BLACKBRAINPY</text></g>
<g clip-path="url(#c2)" class="g2"><text class="ttl" x="60" y="212" fill="#00E5FF" opacity="0.95">BLACKBRAINPY</text></g>
<g clip-path="url(#c3)" class="g3"><text class="ttl" x="60" y="212" fill="#FCEE0A">BLACKBRAINPY</text></g>
<rect x="60" y="228" width="880" height="2" fill="url(#fade)" opacity="0.7"/>
<g class="mono" transform="translate(62,258)">
<text x="0" y="0" font-size="15" fill="#FCEE0A" letter-spacing="5" opacity="0.95">GENZ TECH</text>
<text x="122" y="0" font-size="15" fill="#FF003C" letter-spacing="5" opacity="0.9">//</text>
<text x="152" y="0" font-size="15" fill="#e8e6df" letter-spacing="3" opacity="0.8">DAILY TECH NEWS FOR GEN Z</text>
<text x="418" y="0" font-size="15" fill="#FF003C" letter-spacing="5" opacity="0.9">//</text>
<text x="448" y="0" font-size="15" fill="#FCEE0A" letter-spacing="3" opacity="0.95">genztech.blog</text>
</g>
<g transform="translate(1012,112)" class="mono" fill="#FCEE0A" opacity="0.28" font-size="26" letter-spacing="6">
<text x="0" y="0">サイバー</text><text x="0" y="34">パンク</text><text x="0" y="68">エッジ</text><text x="0" y="102">ランナーズ</text>
</g>
<g stroke="#FCEE0A" stroke-width="2.5" fill="none" opacity="0.9">
<path d="M28 92 L28 78 L52 78"/><path d="M1172 92 L1172 78 L1148 78"/>
<path d="M28 274 L28 288 L52 288"/><path d="M1172 274 L1172 288 L1148 288"/>
</g>
<rect x="0" y="0" width="1200" height="4" fill="#00E5FF" opacity="0.25" class="sw"/>
<rect width="1200" height="340" fill="url(#sl)" opacity="0.55"/>
<rect width="1200" height="340" filter="url(#grain)" opacity="0.6"/>
</svg>
'''

BARS = [("PYTHON",92),("JAVASCRIPT",88),("HTML / CSS",90),("NODE.JS",78),
        ("GIT",85),("GH ACTIONS",72),("VERCEL",70),("JSON / REST",82),("MARKDOWN",95)]

def arsenal():
    kf, cls, cells = [], [], []
    for i,(name,pct) in enumerate(BARS,1):
        w = round(240*pct/100.0)
        kf.append("@keyframes w%d{0%%{width:0}100%%{width:%dpx}}" % (i,w))
        cls.append(".b%d{animation:w%d %.1fs ease-out forwards}" % (i,i,1.7+i*0.1))
        x = 60 + (i-1)%3*390
        y = 72 + ((i-1)//3)*95
        cells.append(
            '<g transform="translate(%d,%d)">\n'
            '<text class="n" x="0" y="0">%s</text>\n'
            '<rect x="0" y="10" width="240" height="7" fill="#FCEE0A" opacity="0.14"/>\n'
            '<rect x="0" y="10" height="7" fill="#FCEE0A" class="b%d"/>\n'
            '<text class="m" x="252" y="17" fill="#FCEE0A" opacity="0.6">%d</text>\n</g>'
            % (x,y,name,i,pct))
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 330" width="1200" height="330" role="img" aria-label="Arsenal">\n'
        '<defs>\n<style>\n'
        ".n{font-family:'Arial Black','Helvetica Neue',Impact,sans-serif;font-weight:900;font-size:16px;letter-spacing:2px;fill:#FCEE0A}\n"
        ".m{font-family:'Consolas','SF Mono','DejaVu Sans Mono',monospace;font-size:11px;letter-spacing:2px}\n"
        + "\n".join(kf) + "\n@keyframes bl{0%,49%{opacity:1}50%,100%{opacity:.12}}\n"
        + "\n".join(cls) + "\n.bk{animation:bl 1.2s infinite steps(1)}\n</style>\n"
        '<pattern id="gr" width="40" height="40" patternUnits="userSpaceOnUse">'
        '<path d="M40 0H0V40" fill="none" stroke="#FCEE0A" stroke-width="0.5" opacity="0.08"/></pattern>\n'
        '<pattern id="sc" width="3" height="3" patternUnits="userSpaceOnUse"><rect width="3" height="1.4" fill="#000" opacity="0.45"/></pattern>\n'
        '</defs>\n<rect width="1200" height="330" fill="#08070a"/>\n<rect width="1200" height="330" fill="url(#gr)"/>\n'
        '<rect x="40" y="26" width="3" height="278" fill="#FCEE0A" opacity="0.5"/>\n'
        '<text class="m" x="60" y="34" fill="#FCEE0A" opacity="0.45">MODULE SCAN // 9 SUBSYSTEMS DETECTED</text>\n'
        '<circle cx="1152" cy="30" r="3.5" fill="#FF003C" class="bk"/>\n'
        '<text class="m" x="1140" y="34" fill="#FCEE0A" opacity="0.45" text-anchor="end">LIVE</text>\n'
        + "\n".join(cells) +
        '\n<g stroke="#FCEE0A" stroke-width="2" fill="none" opacity="0.8">'
        '<path d="M1160 20 L1176 20 L1176 36"/><path d="M1160 310 L1176 310 L1176 294"/></g>\n'
        '<rect width="1200" height="330" fill="url(#sc)" opacity="0.5"/>\n</svg>\n')

SVG["arsenal.svg"] = arsenal()

SVG["dossier.svg"] = u'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 330" width="1200" height="330" role="img" aria-label="Operator dossier">
<defs>
<style>
.lb{font-family:'Consolas','SF Mono','DejaVu Sans Mono',monospace;font-size:11px;letter-spacing:3px;fill:#FCEE0A;opacity:.55}
.vl{font-family:'Arial Black','Helvetica Neue',Impact,sans-serif;font-weight:900;font-size:17px;letter-spacing:1px;fill:#EDEAE0}
.sm{font-family:'Consolas','SF Mono','DejaVu Sans Mono',monospace;font-size:13px;fill:#EDEAE0;opacity:.75}
.tg{font-family:'Arial Black','Helvetica Neue',Impact,sans-serif;font-weight:900;font-size:13px;letter-spacing:3px;fill:#08070a}
@keyframes bl{0%,49%{opacity:1}50%,100%{opacity:.12}}
@keyframes sw{0%{transform:translate(0,0)}100%{transform:translate(0,220px)}}
@keyframes st{0%{width:0}100%{width:300px}}
.bk{animation:bl 1.2s infinite steps(1)}
.scn{animation:sw 3.4s linear infinite}
.stt{animation:st 2.8s ease-out forwards}
</style>
<pattern id="gr2" width="40" height="40" patternUnits="userSpaceOnUse">
<path d="M40 0H0V40" fill="none" stroke="#FCEE0A" stroke-width="0.5" opacity="0.08"/></pattern>
<pattern id="sc2" width="3" height="3" patternUnits="userSpaceOnUse"><rect width="3" height="1.4" fill="#000" opacity="0.45"/></pattern>
<pattern id="bc" width="22" height="34" patternUnits="userSpaceOnUse">
<rect x="0" y="0" width="2" height="34" fill="#FCEE0A"/><rect x="4" y="0" width="1" height="34" fill="#FCEE0A"/>
<rect x="7" y="0" width="3" height="34" fill="#FCEE0A"/><rect x="12" y="0" width="1" height="34" fill="#FCEE0A"/>
<rect x="15" y="0" width="2" height="34" fill="#FCEE0A"/><rect x="19" y="0" width="1" height="34" fill="#FCEE0A"/></pattern>
<clipPath id="pf"><rect x="60" y="52" width="200" height="220"/></clipPath>
</defs>
<rect width="1200" height="330" fill="#08070a"/>
<rect width="1200" height="330" fill="url(#gr2)"/>
<g clip-path="url(#pf)">
<rect x="60" y="52" width="200" height="220" fill="#100e14"/>
<g stroke="#FCEE0A" stroke-width="1" opacity="0.35" fill="none">
<circle cx="160" cy="130" r="46"/><circle cx="160" cy="130" r="30"/>
<path d="M160 60 L160 200 M90 130 L230 130"/>
</g>
<text x="160" y="228" class="lb" text-anchor="middle" style="opacity:.7">NO VISUAL ON FILE</text>
<text x="160" y="246" class="lb" text-anchor="middle" style="opacity:.4">REF 291556072</text>
<rect x="60" y="52" width="200" height="3" fill="#00E5FF" opacity="0.5" class="scn"/>
</g>
<rect x="60" y="52" width="200" height="220" fill="none" stroke="#FCEE0A" stroke-width="2" opacity="0.85"/>
<g stroke="#FF003C" stroke-width="3" fill="none">
<path d="M60 76 L60 52 L84 52"/><path d="M236 272 L260 272 L260 248"/>
</g>
<rect x="60" y="284" width="200" height="24" fill="#FCEE0A"/>
<text class="tg" x="160" y="301" text-anchor="middle">OPERATOR ID</text>
<g transform="translate(320,0)">
<text class="lb" x="0" y="66">HANDLE</text><text class="vl" x="150" y="68">blackbrainpy</text>
<text class="lb" x="0" y="104">ORG</text><text class="vl" x="150" y="106">GENZ TECH</text>
<text class="lb" x="0" y="142">SECTOR</text><text class="vl" x="150" y="144">NEW YORK // REMOTE</text>
<text class="lb" x="0" y="180">CLASS</text><text class="vl" x="150" y="182">NETRUNNER . FULL-STACK</text>
<text class="lb" x="0" y="218">MAIN QUEST</text><text class="sm" x="150" y="220">genztech.blog - daily tech news for Gen Z</text>
<text class="lb" x="0" y="248">SIDE QUESTS</text><text class="sm" x="150" y="250">acoustic wall scanner (tap-mapper)</text>
<text class="sm" x="150" y="270">home repair cost calculators . free public dev API</text>
<line x1="0" y1="80" x2="780" y2="80" stroke="#FCEE0A" stroke-width="1" opacity="0.12"/>
<line x1="0" y1="118" x2="780" y2="118" stroke="#FCEE0A" stroke-width="1" opacity="0.12"/>
<line x1="0" y1="156" x2="780" y2="156" stroke="#FCEE0A" stroke-width="1" opacity="0.12"/>
<line x1="0" y1="194" x2="780" y2="194" stroke="#FCEE0A" stroke-width="1" opacity="0.12"/>
<text class="lb" x="0" y="298">STATUS</text>
<rect x="150" y="288" width="300" height="8" fill="#FCEE0A" opacity="0.14"/>
<rect x="150" y="288" height="8" fill="#FCEE0A" class="stt"/>
<text class="lb" x="466" y="298" style="opacity:.9">SHIPPING</text>
<circle cx="566" cy="294" r="4" fill="#FF003C" class="bk"/>
</g>
<rect x="1096" y="52" width="66" height="34" fill="url(#bc)" opacity="0.8"/>
<text class="lb" x="1162" y="100" text-anchor="end">SCAN VALID</text>
<g stroke="#FCEE0A" stroke-width="2" fill="none" opacity="0.8">
<path d="M1160 24 L1176 24 L1176 40"/><path d="M1160 310 L1176 310 L1176 294"/>
</g>
<rect width="1200" height="330" fill="url(#sc2)" opacity="0.5"/>
</svg>
'''

SVG["footer.svg"] = u'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 200" width="1200" height="200" role="img" aria-label="Stay jacked in">
<defs>
<style>
.f{font-family:'Arial Black','Helvetica Neue',Impact,sans-serif;font-weight:900;font-size:58px;letter-spacing:4px}
.m2{font-family:'Consolas','SF Mono','DejaVu Sans Mono',monospace;font-size:11px;letter-spacing:3px}
@keyframes gl{0%,88%,100%{transform:translate(0,0)}89%{transform:translate(-14px,0)}91%{transform:translate(8px,0)}92%{transform:translate(0,0)}}
@keyframes fk{0%,92%,100%{opacity:1}93%{opacity:.3}95%{opacity:1}}
@keyframes bl2{0%,49%{opacity:1}50%,100%{opacity:.1}}
.gg{animation:gl 6s infinite steps(1)}
.ff{animation:fk 5s infinite}
.b2{animation:bl2 1.4s infinite steps(1)}
</style>
<pattern id="hz2" width="30" height="30" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">
<rect width="30" height="30" fill="#0a0a0c"/><rect width="15" height="30" fill="#FCEE0A"/></pattern>
<pattern id="sc3" width="3" height="3" patternUnits="userSpaceOnUse"><rect width="3" height="1.4" fill="#000" opacity="0.5"/></pattern>
<clipPath id="fc"><rect x="0" y="88" width="1200" height="18"/></clipPath>
<linearGradient id="fd2" x1="0" y1="0" x2="1" y2="0">
<stop offset="0" stop-color="#FCEE0A" stop-opacity="0"/><stop offset="0.5" stop-color="#FCEE0A" stop-opacity="0.8"/><stop offset="1" stop-color="#FCEE0A" stop-opacity="0"/></linearGradient>
</defs>
<rect width="1200" height="200" fill="#08070a"/>
<rect x="0" y="0" width="1200" height="12" fill="url(#hz2)"/>
<rect x="0" y="188" width="1200" height="12" fill="url(#hz2)"/>
<g class="ff" text-anchor="middle">
<text class="f" x="600" y="112" fill="#00E5FF" opacity="0.85" transform="translate(-4,0)">STAY JACKED IN.</text>
<text class="f" x="600" y="112" fill="#FF003C" opacity="0.85" transform="translate(4,0)">STAY JACKED IN.</text>
<text class="f" x="600" y="112" fill="#FCEE0A">STAY JACKED IN.</text>
</g>
<g clip-path="url(#fc)" class="gg" text-anchor="middle">
<text class="f" x="600" y="112" fill="#FF003C">STAY JACKED IN.</text>
</g>
<rect x="200" y="130" width="800" height="2" fill="url(#fd2)"/>
<text class="m2" x="600" y="158" fill="#FCEE0A" opacity="0.5" text-anchor="middle">genztech.blog . @genztechblog . github.com/blackbrainpy</text>
<circle cx="34" cy="36" r="4" fill="#FF003C" class="b2"/>
<text class="m2" x="50" y="40" fill="#FCEE0A" opacity="0.45">CONNECTION TERMINATED</text>
<text class="m2" x="1166" y="40" fill="#FCEE0A" opacity="0.45" text-anchor="end">EOF // 0x7F</text>
<rect width="1200" height="200" fill="url(#sc3)" opacity="0.5"/>
</svg>
'''

for name, body in SVG.items():
    p = os.path.join(D, name)
    with open(p, "wb") as fh:
        fh.write(body.encode("utf-8"))
    print("wrote %-16s %6d bytes" % (name, len(body.encode("utf-8"))))
