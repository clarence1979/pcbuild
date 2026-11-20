import base64, os, sys, json, html
from pathlib import Path
from playwright.sync_api import sync_playwright
import content_a, content_b, content_c
from template import lesson_page, print_page, CSS, esc

OUT = Path(__file__).resolve().parent / "out"; OUT.mkdir(exist_ok=True)
TMP = Path(__file__).resolve().parent / "tmp"; TMP.mkdir(exist_ok=True)
LESSONS = content_a.LESSONS + content_b.LESSONS + content_c.LESSONS
for L in LESSONS:
    L["file"] = f"L{L['n']:02d}_W{L['week']}L{L['lnum']}.html"

WEEKS = {
 1: "Safety and anatomy", 2: "The processor and its cooler", 3: "Memory", 4: "Storage", 5: "Motherboard and firmware", 6: "Power",
 7: "Graphics", 8: "Cases and the transplant plan", 9: "The transplant", 10: "Troubleshooting", 11: "Operating system", 12: "Networks: foundations",
 13: "Cable making and testing", 14: "IP addressing", 15: "Building the LAN", 16: "Sockets, chat and firewalls", 17: "LAN party and the wider network", 18: "Capstone and wrap-up"}

def make_pdfs():
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page()
        for L in LESSONS:
            htmlp = TMP / L["file"].replace(".html", "_print.html")
            htmlp.write_text(print_page(L), encoding="utf-8")
            pg.goto(htmlp.as_uri(), wait_until="load")
            pdfp = TMP / L["file"].replace(".html", ".pdf")
            pg.pdf(path=str(pdfp), format="A4", print_background=True, margin={"top": "0", "bottom": "0", "left": "0", "right": "0"}, prefer_css_page_size=True)
            L["pdf"] = pdfp
            print("pdf", L["n"], pdfp.stat().st_size // 1024, "KB")
        b.close()

def write_lessons():
    for i, L in enumerate(LESSONS):
        prev_l = LESSONS[i - 1]["file"] if i > 0 else None
        next_l = LESSONS[i + 1]["file"] if i < len(LESSONS) - 1 else None
        b64 = base64.b64encode(L["pdf"].read_bytes()).decode()
        (OUT / L["file"]).write_text(lesson_page(L, b64, (prev_l, next_l)), encoding="utf-8")
        print("html", L["file"], (OUT / L["file"]).stat().st_size // 1024, "KB")

INDEX_CSS = CSS + r"""
.hero{background:var(--ink);color:#fff;padding:40px 24px 30px}
.hero .in{max-width:1180px;margin:0 auto}
.hero h1{font-size:34px;margin:0 0 6px}.hero p{margin:4px 0;color:#CFEFD9;max-width:760px}
.arc{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;max-width:1180px;margin:-18px auto 0;padding:0 24px}
.arc div{background:#fff;border:1px solid var(--mid);border-radius:10px;padding:14px 16px;border-top:6px solid var(--c)}
.arc b{display:block;font-size:15px}.arc span{font-size:13.5px;color:var(--grey)}
.grid{max-width:1180px;margin:30px auto;padding:0 24px;display:grid;grid-template-columns:repeat(auto-fill,minmax(360px,1fr));gap:16px}
.wk{background:#fff;border:1px solid var(--mid);border-radius:10px;padding:14px 16px}
.wk h2{font-size:16px;margin:0 0 8px;display:flex;gap:10px;align-items:baseline}.wk h2 .n{font-family:var(--mono);color:var(--pcb);font-size:13px}
.wk a{display:block;padding:7px 10px;margin:4px 0;border-radius:6px;text-decoration:none;color:var(--ink);background:var(--paper);border:1px solid var(--light)}
.wk a:hover{border-color:var(--blue);background:#fff}.wk a small{display:block;color:var(--grey);font-size:12.5px}
.notes{max-width:1180px;margin:0 auto 50px;padding:0 24px}
.notes h2{font-size:18px}
.notes table.plain{font-size:14px}
"""

def write_index():
    arcs = [("Weeks 1–6", "Know the machine", "Every part of the Dell 7050: what it does, how to remove and refit it, how to test it.", "--seg-learn"),
            ("Weeks 7–11", "Upgrade and transplant", "GPU, PSU, open frame, the three-lesson rebuild, then troubleshooting and a fresh OS.", "--seg-do"),
            ("Weeks 12–18", "Connect and play", "Cables, IP, the lab LAN, a Python chat server, a LAN party, then the capstone.", "--seg-check")]
    arc_html = "".join(f'<div style="--c:var({c})"><b>{a} · {t}</b><span>{d}</span></div>' for a, t, d, c in arcs)
    weeks_html = ""
    for w in range(1, 19):
        items = [L for L in LESSONS if L["week"] == w]
        links = "".join(f'<a href="{L["file"]}">Lesson {L["lnum"]} · {esc(L["title"])}<small>{esc(L["outcomes"][0])}</small></a>' for L in items)
        weeks_html += f'<div class="wk"><h2><span class="n">Week {w}</span>{WEEKS[w]}</h2>{links}</div>'
    body = f"""<!doctype html><html lang="en-AU"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>ReBuild Lab — course map</title><style>{INDEX_CSS}</style></head><body>
<div class="hero"><div class="in"><h1>ReBuild Lab: PC Building, Repair &amp; Maintenance</h1>
<p>Year 9/10 elective · 18 weeks · 54 lessons of 45 minutes · 20 students in pairs on ten Dell OptiPlex 7050 SFF benches.</p>
<p>Each lesson page runs the 45 minutes on a timer, carries its own animated figures, and holds a printable A4 worksheet (the button in the right column).</p></div></div>
<div class="arc">{arc_html}</div>
<div class="grid">{weeks_html}</div>
<div class="notes"><h2>Lab address plan</h2><table class="plain"><tr><th>Item</th><th>Value</th></tr>
<tr><td>Network</td><td>192.168.10.0/24 (mask 255.255.255.0), no gateway, no DHCP, no DNS. Isolated switch only.</td></tr>
<tr><td>Teacher PC</td><td>192.168.10.1 on switch port 24</td></tr>
<tr><td>Benches 1–20</td><td>192.168.10.11 – 192.168.10.30, switch ports 1–20, hostnames PC-01 – PC-20</td></tr>
<tr><td>Chat server</td><td>TCP 2323 (Python, Weeks 16–17)</td></tr>
<tr><td>Game</td><td>Minecraft Java TCP 25565 if licensed; otherwise Luanti UDP 30000 (free, open source)</td></tr></table>
<p style="font-size:13px;color:var(--grey)">Teacher guide (answers, planted-fault lists, kit list, curriculum map): <a href="teacher-guide.html">teacher-guide.html</a></p></div>
<footer><span>ReBuild Lab · Plenty Valley Christian College · Digital Technologies</span><span>Victorian Curriculum 2.0 Digital Technologies 9–10: Digital Systems and Security</span></footer>
</body></html>"""
    (OUT / "index.html").write_text(body, encoding="utf-8")

def write_teacher_guide():
    rows = ""
    for L in LESSONS:
        answers = "<br>".join(f"Q{i+1}: {esc(q['o'][q['a']])}" for i, q in enumerate(L["check"]["quiz"]))
        rows += f'<tr><td>{L["n"]}</td><td>W{L["week"]} L{L["lnum"]}</td><td><a href="{L["file"]}">{esc(L["title"])}</a></td><td>{"<br>".join(esc(k) for k in L["kit"])}</td><td style="font-size:12.5px">{answers}</td></tr>'
    plants = """<h2>Planted faults (Lessons 30, 44, 52)</h2>
<table class="plain"><tr><th>Lesson</th><th>Fault</th><th>How to plant</th><th>Expected symptom</th><th>Rung / code</th></tr>
<tr><td>30</td><td>RAM half-seated</td><td>Open one clip, lift one end 2 mm</td><td>No POST, amber 2,3 or 3,3</td><td>No POST</td></tr>
<tr><td>30</td><td>SATA data unplugged</td><td>Pull the L-plug at the board end</td><td>POST OK, 'No bootable device'</td><td>No boot</td></tr>
<tr><td>30</td><td>Monitor on iGPU port</td><td>Move HDMI to the board after GPU install</td><td>Fans, white LED, no signal</td><td>No POST (apparent)</td></tr>
<tr><td>30</td><td>GPU not latched</td><td>Lift the card 3 mm, leave screw</td><td>Boots on iGPU if cable moved; else no signal</td><td>No POST / 3,2</td></tr>
<tr><td>30</td><td>Front-panel plug off</td><td>Unplug the 5-pin</td><td>Button does nothing</td><td>No power</td></tr>
<tr><td>30</td><td>4-pin CPU power off</td><td>Unplug the 4-pin</td><td>Fans may spin, no POST, 2,2 or 4,2 pattern depending on firmware</td><td>No POST</td></tr>
<tr><td>30</td><td>Boot order to USB</td><td>F2 → Boot Sequence → USB first, no USB</td><td>Delay then boots, or 'no bootable device' on some firmware</td><td>No boot</td></tr>
<tr><td>30</td><td>Coin cell out</td><td>Remove CR2032</td><td>Time-of-day error at POST</td><td>No boot (prompt)</td></tr>
<tr><td>30</td><td>Fan unplugged</td><td>Unplug CPU fan header</td><td>'Alert! CPU fan failure' at POST</td><td>POST message</td></tr>
<tr><td>44</td><td>Lead unplugged at switch</td><td>Pull the switch end</td><td>Link light off</td><td>Rung 1</td></tr>
<tr><td>44</td><td>Open wire lead</td><td>Substitute a known-bad lead</td><td>Link light off, or 100 Mb only</td><td>Rung 1</td></tr>
<tr><td>44</td><td>Wrong mask /16</td><td>Set 255.255.0.0</td><td>Self pings OK; neighbour OK (still 'local'); fault invisible until off-lab</td><td>Rung 5 (discussion)</td></tr>
<tr><td>44</td><td>Wrong mask /25</td><td>Set 255.255.255.128 on a bench ≥.11 pinging a bench &lt;.128 … choose addresses either side of .128</td><td>Neighbour 'unreachable'</td><td>Rung 5</td></tr>
<tr><td>44</td><td>Wrong third octet</td><td>192.168.11.x</td><td>Self OK, neighbour unreachable</td><td>Rung 5</td></tr>
<tr><td>44</td><td>Duplicate IP</td><td>Give two benches .17</td><td>Intermittent timeouts; arp -a MAC flips</td><td>Rung 5 (sneaky)</td></tr>
<tr><td>44</td><td>Firewall blocks ICMP</td><td>Disable the Echo-In rule / ufw deny icmp</td><td>Others cannot ping this PC; it can ping out</td><td>Rung 5</td></tr>
<tr><td>44</td><td>IPv4 disabled</td><td>Untick IPv4 on the adapter</td><td>ip a shows no inet; 127.0.0.1 may still work</td><td>Rung 2</td></tr>
<tr><td>44</td><td>Switch port moved</td><td>Plug into an unlabelled port</td><td>Works, but port plan wrong</td><td>Documentation</td></tr>
<tr><td>52</td><td>One hardware + one network fault from the lists above, per bench</td><td>Mix; avoid repeating a bench's earlier fault</td><td></td><td></td></tr></table>"""
    kit = """<h2>Consolidated kit list (10 benches)</h2>
<table class="plain"><tr><th>Item</th><th>Qty</th><th>Notes</th></tr>
<tr><td>Dell OptiPlex 7050 SFF</td><td>10 (+2 spare)</td><td>i5-7500 or similar, 8 GB, 256 GB. Service tags recorded Week 1.</td></tr>
<tr><td>Anti-static wrist straps + mats</td><td>12</td><td>Check the 1 MΩ resistor with a meter each term.</td></tr>
<tr><td>Phillips #2 magnetic, #0/#1, spudger, torch, flush cutters</td><td>10 sets</td><td></td></tr>
<tr><td>Isopropyl 70%+, lint-free wipes, thermal paste</td><td>Class</td><td>Week 2</td></tr>
<tr><td>DDR4-2400 8 GB sticks (matched pairs)</td><td>10 pairs (+2 known-bad for Week 3)</td><td>Dell 7050 supports 2400; faster sticks downclock.</td></tr>
<tr><td>NVMe M.2 2280 SSD 500 GB</td><td>10</td><td>M-key; the board's slot supports NVMe and SATA M.2.</td></tr>
<tr><td>2.5-inch SATA SSD 240 GB + SATA cable + Dell caddy</td><td>10</td><td></td></tr>
<tr><td>Low-profile GPU ≤75 W, no power plug (e.g. GTX 1650 LP, RX 6400)</td><td>10</td><td>Runs on the Dell PSU; fits the SFF case.</td></tr>
<tr><td>Full-size GPU with 8-pin (optional, for Week 9+ benches)</td><td>2–4</td><td>Needs the ATX PSU.</td></tr>
<tr><td>ATX PSU 550 W 80 Plus Bronze+</td><td>10</td><td>Must include 4+4 CPU and 6+2 PCIe leads.</td></tr>
<tr><td>24-pin → 6-pin adapter for OptiPlex 3050/5050/7050</td><td>10</td><td>Not a passive cable: buy the one made for this series (e.g. Moddiy).</td></tr>
<tr><td>Dell 5-pin front-panel adapter</td><td>10</td><td>Or reuse the Dell button module on its own lead.</td></tr>
<tr><td>Open-frame test bench case with slotted rails/adjustable standoffs</td><td>10</td><td>Verify slotted mounting before purchase; fixed ATX-hole trays will not fit the Dell pattern.</td></tr>
<tr><td>Brass standoffs, nylon washers, PCIe riser (short)</td><td>10 kits + 4 risers</td><td></td></tr>
<tr><td>120 mm case fan + fan header adapter</td><td>10</td><td></td></tr>
<tr><td>PSU tester</td><td>2</td><td>Teacher bench; Week 6.</td></tr>
<tr><td>CR2032 cells</td><td>20</td><td>Week 5.</td></tr>
<tr><td>Cat5e UTP (305 m box), RJ45 plugs (200+), boots, crimp tool with stripper, cable tester</td><td>10 crimp kits, 5 testers</td><td>Weeks 13–15. Expect 3–4 plugs per student lead.</td></tr>
<tr><td>Gigabit switch, 24-port, unmanaged</td><td>1</td><td>Isolated; never uplinked to the school network.</td></tr>
<tr><td>USB sticks 8 GB+ (MemTest86, Linux Mint ISO, drivers)</td><td>12</td><td></td></tr>
<tr><td>Spare monitor, keyboard, mouse, mains leads</td><td>3 sets</td><td></td></tr></table>"""
    cur = """<h2>Curriculum alignment</h2>
<p>Victorian Curriculum 2.0, Digital Technologies Levels 9 and 10, Digital Systems and Security strand: students <i>explain how hardware specifications affect performance and select appropriate hardware for particular tasks and workloads</i> (Weeks 2–7, 17) and <i>investigate how hardware and software manage, control and secure access to data in networked digital systems</i> (Weeks 11–18). Processes and production skills are addressed through the iterative build, test and document cycle in every lesson. Where the school maps to the Australian Curriculum v9, the equivalent descriptors are AC9TDI10K01 (hardware and performance) and AC9TDI10K02/P14 (networked systems and security).</p>
<p>Industry framing: the course mirrors CompTIA A+ Core 1 domains 1–3 (hardware, networking, troubleshooting) at an introductory level; this is for context only and is not a certification course.</p>"""
    body = f"""<!doctype html><html lang="en-AU"><head><meta charset="utf-8"><title>ReBuild Lab — teacher guide</title><style>{INDEX_CSS}</style></head><body>
<div class="hero"><div class="in"><h1>ReBuild Lab — teacher guide</h1><p>Lesson answers, kit, planted faults, address plan and curriculum notes. Not for student distribution.</p></div></div>
<div class="notes">
<h2>How the lesson pages work</h2>
<p>Every page is a single standalone HTML file with no external dependencies; copy the folder to each bench PC or host it on the intranet. The sticky header runs a 45-minute timer with a segmented timeline (Start / Learn / Do / Check / Pack down). Step checklists persist per browser via localStorage. Quizzes give instant feedback. The right-hand "Open the printable worksheet" button opens the embedded A4 PDF in a new tab (and "download the PDF" saves it); the PDF is base64 inside the file, so it works offline from a file:// URL. Figures are inline SVG with CSS/SMIL animation and respect prefers-reduced-motion.</p>
<p>Driver/Navigator roles swap every lesson. The Navigator reads steps aloud and owns the pre-power check; you say "go" before any mains lead is connected.</p>
<h2>Operating system note</h2>
<p>The OptiPlex 7050's 7th-generation Intel CPU is not on Microsoft's Windows 11 supported-processor list and Windows 10 reached end of support in October 2025, so the lessons default to Linux Mint for the fresh install (Week 11). Windows steps are given in parallel wherever a command differs. If the school prefers Windows 11 via an unsupported-hardware install, the hardware lessons are unchanged; the Week 16 Python code runs on either.</p>
<h2>Safety summary</h2>
<ul class="plain"><li>Unplug, press the button, strap on, open — every lesson, same order. Strap clipped to bare metal.</li><li>Never open a PSU. The paperclip start is a teacher demonstration only; students use the PSU tester or Dell BIST.</li><li>Isopropyl: small amounts, capped, no mains at the bench while in use.</li><li>Crimp tool and cutters: safety glasses, cut away from the hand.</li><li>Cabling: patch leads only, lab switch only. Fixed cabling is ACMA registered-cabler work.</li><li>Wireshark (Week 16) is teacher-run on the isolated lab network only.</li></ul>
{cur}
{kit}
{plants}
<h2>Lesson index with kit and quiz answers</h2>
<table class="plain"><tr><th>#</th><th>Wk/L</th><th>Title</th><th>Kit</th><th>Check answers</th></tr>{rows}</table>
</div></body></html>"""
    (OUT / "teacher-guide.html").write_text(body, encoding="utf-8")

if __name__ == "__main__":
    make_pdfs()
    write_lessons()
    write_index()
    write_teacher_guide()
    print("done", len(list(OUT.glob("*.html"))), "html files")
