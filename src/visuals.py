# visuals.py — SVG / HTML figure builders. Each SVG carries its own <style> for animation so it is self-contained.
import math

INK = "#1F2630"; PCB = "#1E6E52"; PCBD = "#145039"; GOLD = "#C8902A"; BLUE = "#2457C5"; AMBER = "#E8A317"
RED = "#C0392B"; GREY = "#8A9099"; WHITE = "#FFFFFF"; MID = "#C9CED6"; SLATE = "#3A4350"; GREEN = "#2E9E5B"
F = "font-family:'Segoe UI',Roboto,Helvetica,Arial,sans-serif;"
M = "font-family:Consolas,'DejaVu Sans Mono',Menlo,monospace;"

def svg(w, h, body, style="", cls=""):
    return (f'<svg class="fig {cls}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" role="img">'
            f'<style>{style}</style>{body}</svg>')

def t(x, y, s, size=13, fill=INK, anchor="start", weight=400, mono=False, extra=""):
    fam = M if mono else F
    return (f'<text x="{x}" y="{y}" style="{fam}font-size:{size}px;font-weight:{weight};{extra}" '
            f'fill="{fill}" text-anchor="{anchor}">{s}</text>')

def rect(x, y, w, h, fill, rx=3, stroke="none", sw=1, extra=""):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" {extra}/>'

def line(x1, y1, x2, y2, stroke=INK, sw=1.5, extra=""):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}" {extra}/>'

def arrow_def(id_="arr", color=INK):
    return (f'<defs><marker id="{id_}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
            f'<path d="M0 0 L10 5 L0 10 z" fill="{color}"/></marker></defs>')

# ------------------------------------------------------------------ anatomy
PARTS = {
 "psu": ["Power supply (180 W)", "Turns 240 V AC from the wall into the low DC voltages the parts use. Dell's is a special shape with a 6-pin plug, not the usual 24-pin."],
 "cage": ["Drive cage", "Holds the 2.5-inch / 3.5-inch drive and the slim optical drive. Swings up on this model."],
 "cooler": ["CPU cooler (blower)", "A heatsink plus fan sitting on the processor. Without it the CPU overheats in seconds."],
 "cpu": ["CPU in its socket", "The processor (Intel Core i5-7500 or similar) sits under the cooler in an LGA1151 socket."],
 "ram": ["RAM slots (4 x DDR4)", "Four DIMM slots. Modules go in matching pairs for dual-channel. Max 64 GB."],
 "pcie16": ["PCIe x16 slot", "The long slot for a graphics card. Low-profile cards only in this small case."],
 "pcie4": ["PCIe x4 slot", "A shorter slot for small expansion cards (network, capture, extra M.2)."],
 "m2": ["M.2 2280 slot", "Takes a stick-shaped SSD (SATA or NVMe). Held by one tiny screw."],
 "sata": ["SATA ports", "Data ports for 2.5-inch / 3.5-inch drives and the optical drive. Power comes from the PSU, not here."],
 "pwr6": ["6-pin main power", "Dell's small main power plug from the PSU. An adapter converts a standard 24-pin lead to this."],
 "pwr4": ["4-pin CPU power", "A second 12 V feed just for the processor."],
 "fpanel": ["Front-panel header", "Power button, LEDs and front USB. Dell uses a 5-pin plug here instead of the usual 2x5 pin block."],
 "cmos": ["Coin cell (CR2032)", "Keeps the clock and settings alive when the PC is unplugged."],
 "chipset": ["Chipset (Intel Q270)", "The traffic controller that connects USB, SATA, network and slower PCIe to the CPU."],
 "io": ["Rear ports", "DisplayPort, HDMI, USB, network, audio. Built onto the board."],
}

def anatomy(hl=()):
    hl = set(hl)
    def cls(k): return f'part{" hl" if k in hl else ""}'
    b = []
    b.append(rect(20, 20, 720, 390, "#F3F4F0", 10, MID, 2))
    b.append(t(32, 42, "Dell OptiPlex 7050 SFF — side panel off, lying flat", 13, GREY))
    b.append(f'<g class="{cls("psu")}" data-part="psu">' + rect(40, 60, 150, 110, SLATE, 6) + rect(52, 72, 60, 86, "#2B333E", 4) +
             f'<circle cx="82" cy="115" r="26" fill="none" stroke="{GREY}" stroke-width="3"/>' + t(125, 110, "PSU", 14, WHITE, "start", 700) + t(125, 128, "180 W", 12, MID) + '</g>')
    b.append(f'<g class="{cls("cage")}" data-part="cage">' + rect(40, 190, 150, 200, "#C8CCD2", 6) + rect(52, 205, 126, 70, "#AEB4BC", 4) +
             rect(52, 285, 126, 40, "#AEB4BC", 4) + rect(52, 335, 126, 40, "#AEB4BC", 4) + t(115, 245, "2.5\" / 3.5\" drive", 12, INK, "middle") +
             t(115, 310, "Optical (slim)", 11, INK, "middle") + t(115, 360, "Drive cage", 12, INK, "middle", 700) + '</g>')
    b.append(rect(210, 60, 510, 330, PCB, 8, PCBD, 2))
    b.append(t(222, 80, "Motherboard (Dell proprietary shape)", 12, "#CFEFD9"))
    b.append(f'<g class="{cls("io")}" data-part="io">' + rect(696, 90, 22, 220, "#2B333E", 3) + t(707, 200, "REAR PORTS", 9, WHITE, "middle", 700, extra="writing-mode:tb;") + '</g>')
    b.append(f'<g class="{cls("cpu")}" data-part="cpu">' + rect(560, 130, 70, 70, "#BFC6CF", 4, GOLD, 2) + t(595, 170, "CPU", 12, INK, "middle", 700) + '</g>')
    b.append(f'<g class="{cls("cooler")}" data-part="cooler">' + rect(540, 110, 110, 110, "none", 8, "#9AA3AE", 3, extra='stroke-dasharray="6 4"') +
             f'<circle cx="595" cy="165" r="48" fill="none" stroke="#9AA3AE" stroke-width="2" opacity=".7"/>' + t(595, 240, "cooler sits here", 10, "#CFEFD9", "middle") + '</g>')
    ram = ""
    for i in range(4):
        x = 420 + i * 22
        ram += rect(x, 100, 12, 150, "#111" if i % 2 == 0 else "#EEE", 2, "#000", .5)
    b.append(f'<g class="{cls("ram")}" data-part="ram">' + ram + t(463, 268, "DIMM 1-4", 11, "#CFEFD9", "middle") + '</g>')
    b.append(f'<g class="{cls("pcie16")}" data-part="pcie16">' + rect(230, 300, 260, 14, "#1B1B1B", 2) + t(230, 330, "PCIe x16", 11, "#CFEFD9") + '</g>')
    b.append(f'<g class="{cls("pcie4")}" data-part="pcie4">' + rect(230, 345, 110, 12, "#1B1B1B", 2) + t(230, 373, "PCIe x4", 11, "#CFEFD9") + '</g>')
    b.append(f'<g class="{cls("m2")}" data-part="m2">' + rect(250, 110, 150, 22, "#2F6B2F", 3, GOLD, 1) + rect(250, 110, 10, 22, GOLD, 1) +
             f'<circle cx="394" cy="121" r="4" fill="{GOLD}"/>' + t(325, 150, "M.2 2280", 11, "#CFEFD9", "middle") + '</g>')
    sata = "".join(rect(250 + i * 30, 180, 22, 12, "#1B1B1B", 2) for i in range(3))
    b.append(f'<g class="{cls("sata")}" data-part="sata">' + sata + t(283, 210, "SATA x3", 11, "#CFEFD9", "middle") + '</g>')
    b.append(f'<g class="{cls("pwr6")}" data-part="pwr6">' + rect(520, 270, 36, 24, WHITE, 3, INK, 1) + t(538, 286, "6", 11, INK, "middle", 700) + t(538, 312, "main pwr", 10, "#CFEFD9", "middle") + '</g>')
    b.append(f'<g class="{cls("pwr4")}" data-part="pwr4">' + rect(660, 100, 26, 24, WHITE, 3, INK, 1) + t(673, 116, "4", 11, INK, "middle", 700) + t(673, 140, "CPU pwr", 10, "#CFEFD9", "middle") + '</g>')
    b.append(f'<g class="{cls("fpanel")}" data-part="fpanel">' + rect(230, 230, 34, 14, WHITE, 2, INK, 1) + t(247, 262, "front panel", 10, "#CFEFD9", "middle") + '</g>')
    b.append(f'<g class="{cls("cmos")}" data-part="cmos">' + f'<circle cx="610" cy="330" r="16" fill="#D8D8D8" stroke="{GREY}"/>' + t(610, 334, "CR2032", 7, INK, "middle") + t(610, 362, "coin cell", 10, "#CFEFD9", "middle") + '</g>')
    b.append(f'<g class="{cls("chipset")}" data-part="chipset">' + rect(520, 180, 44, 44, "#2B2B2B", 4) + t(542, 206, "Q270", 9, WHITE, "middle") + t(542, 244, "chipset", 10, "#CFEFD9", "middle") + '</g>')
    style = (".part{cursor:pointer}.part.hl rect,.part.hl circle{stroke:#FFD166;stroke-width:3;animation:glow 1.4s ease-in-out infinite}"
             "@keyframes glow{0%,100%{stroke-opacity:1}50%{stroke-opacity:.25}}.part:hover rect:first-of-type{stroke:#FFD166;stroke-width:2.5}")
    return svg(760, 430, "".join(b), style, "anatomy")

# ------------------------------------------------------------------ ESD
def esd():
    b = [arrow_def("arrB", BLUE)]
    for i, (title, strap) in enumerate([("Without a strap", False), ("With a wrist strap", True)]):
        ox = i * 380
        b.append(rect(ox + 20, 20, 340, 300, "#F3F4F0", 10, MID, 2))
        b.append(t(ox + 40, 48, title, 15, INK, weight=700))
        b.append(rect(ox + 30, 290, 320, 20, "#B48A5C", 2)); b.append(t(ox + 190, 304, "carpet + rubber soles = charge builds up", 10, WHITE, "middle"))
        px = ox + 90
        b.append(f'<circle cx="{px}" cy="110" r="18" fill="#F1C27D"/>' + line(px, 128, px, 215, INK, 4) + line(px, 215, px - 18, 285, INK, 4) + line(px, 215, px + 18, 285, INK, 4))
        b.append(line(px, 150, px + 60, 175, INK, 4))
        for k in range(6):
            cx = px - 30 + (k * 13) % 60; cy = 100 + (k * 37) % 150
            b.append(t(cx, cy, "+", 14, RED if not strap else GREY, "middle", 700, extra=f"animation:drift 2s {k*.3}s ease-in-out infinite"))
        b.append(rect(ox + 190, 150, 150, 130, SLATE, 6)); b.append(rect(ox + 250, 170, 12, 90, "#111", 2)); b.append(t(ox + 265, 215, "RAM", 11, WHITE))
        b.append(t(ox + 265, 165, "PC (unplugged)", 10, MID))
        if not strap:
            b.append(f'<path class="zap" d="M{px+60} 175 L{px+80} 190 L{px+70} 198 L{px+95} 212" fill="none" stroke="{AMBER}" stroke-width="4" stroke-linejoin="round"/>')
            b.append(t(ox + 190, 125, "a 2,000 V spark you cannot feel", 12, RED, weight=700))
            b.append(t(ox + 190, 140, "can quietly kill a chip", 12, RED))
        else:
            b.append(f'<path d="M{px+55} 172 C {px+70} 240, {px+120} 250, {px+190} 262" fill="none" stroke="{BLUE}" stroke-width="3" stroke-dasharray="8 6" class="flow"/>')
            b.append(f'<circle cx="{px+55}" cy="172" r="7" fill="{BLUE}"/>')
            b.append(t(ox + 190, 125, "charge drains slowly to the case", 12, BLUE, weight=700))
            b.append(t(ox + 190, 140, "through the 1 MΩ resistor in the strap", 12, BLUE))
    style = ("@keyframes drift{0%,100%{transform:translateY(0)}50%{transform:translateY(-6px)}}"
             ".zap{animation:zap 1.2s steps(2) infinite}@keyframes zap{0%,45%{opacity:0}50%,100%{opacity:1}}"
             ".flow{animation:dash 1.5s linear infinite}@keyframes dash{to{stroke-dashoffset:-28}}")
    return svg(760, 340, "".join(b), style)

# ------------------------------------------------------------------ fetch-decode-execute
def fde():
    b = [arrow_def("arr", INK)]
    b.append(rect(30, 40, 170, 250, "#2B333E", 8)); b.append(t(115, 65, "RAM", 15, WHITE, "middle", 700))
    prog = ["LOAD  A, 7", "LOAD  B, 5", "ADD   A, B", "STORE A → 200", "JUMP  0"]
    for i, s in enumerate(prog):
        b.append(rect(45, 80 + i * 38, 140, 30, "#3D4756", 4)); b.append(t(52, 100 + i * 38, f"{i*2:02d}  {s}", 11, "#E8ECF1", mono=True))
    b.append(rect(260, 40, 470, 250, PCB, 10, PCBD, 2)); b.append(t(495, 65, "CPU", 15, WHITE, "middle", 700))
    b.append(rect(280, 85, 130, 90, "#CFEFD9", 6)); b.append(t(345, 110, "Control unit", 13, INK, "middle", 700)); b.append(t(345, 130, "reads the", 11, INK, "middle")); b.append(t(345, 146, "instruction &", 11, INK, "middle")); b.append(t(345, 162, "decides what to do", 11, INK, "middle"))
    b.append(rect(430, 85, 130, 90, "#FFE9B8", 6)); b.append(t(495, 110, "ALU", 13, INK, "middle", 700)); b.append(t(495, 132, "does the maths", 11, INK, "middle")); b.append(t(495, 150, "+ − × ÷ compare", 12, INK, "middle", mono=True))
    b.append(rect(580, 85, 130, 90, "#DCE6FB", 6)); b.append(t(645, 110, "Registers", 13, INK, "middle", 700)); b.append(t(645, 132, "PC = 04", 11, INK, "middle", mono=True)); b.append(t(645, 150, "A = 7   B = 5", 11, INK, "middle", mono=True)); b.append(t(645, 166, "tiny, super-fast", 10, GREY, "middle"))
    b.append(rect(280, 195, 430, 80, "#E9ECEF", 6)); b.append(t(300, 220, "Cache: a small, fast copy of recently used RAM so the CPU rarely waits", 11, INK))
    b.append(t(300, 240, "Clock: 3.4 GHz = 3.4 billion ticks per second; one step per tick (roughly)", 11, INK))
    b.append(t(300, 260, "Cores: 4 cores = 4 of these loops running at once", 11, INK))
    b.append(f'<circle r="9" fill="{AMBER}" stroke="{INK}" stroke-width="2"><animateMotion dur="4.5s" repeatCount="indefinite" path="M 185 171 L 300 130 L 495 130 L 645 130 L 645 60 L 185 60 Z"/></circle>')
    b.append(t(380, 310, "FETCH", 13, INK, "middle", 700, extra="animation:ph 4.5s linear infinite;animation-delay:0s"))
    b.append(t(495, 310, "DECODE", 13, INK, "middle", 700, extra="animation:ph 4.5s linear infinite;animation-delay:-3s"))
    b.append(t(610, 310, "EXECUTE", 13, INK, "middle", 700, extra="animation:ph 4.5s linear infinite;animation-delay:-1.5s"))
    b.append(t(495, 335, "The loop repeats billions of times a second", 11, GREY, "middle"))
    style = "@keyframes ph{0%,30%{fill:#C8902A}31%,100%{fill:#8A9099}}"
    return svg(760, 350, "".join(b), style)

# ------------------------------------------------------------------ socket + cooler
def socket_cooler():
    b = []
    b.append(rect(20, 20, 350, 300, "#F3F4F0", 10, MID, 2)); b.append(t(40, 48, "LGA1151 socket (pins are in the board, not the chip)", 12, INK, weight=700))
    b.append(rect(80, 80, 180, 180, "#BFC6CF", 4, GREY, 2))
    for r in range(12):
        for c in range(12):
            b.append(f'<circle cx="{95+c*13.6:.1f}" cy="{95+r*13.6:.1f}" r="2" fill="{GOLD}"/>')
    b.append(f'<path d="M80 80 L100 80 L80 100 Z" fill="{AMBER}"/>'); b.append(t(105, 76, "▲ triangle matches the corner of the CPU", 10, INK))
    b.append(f'<g style="transform-origin:280px 240px;animation:lever 4s ease-in-out infinite">' + line(280, 240, 280, 110, INK, 5) + f'<circle cx="280" cy="240" r="6" fill="{INK}"/>' + '</g>')
    b.append(t(300, 250, "load lever", 10, INK)); b.append(t(40, 290, "Never touch the pins. Hold the CPU by its edges. Lower it straight down.", 11, RED))
    b.append(rect(390, 20, 350, 300, "#F3F4F0", 10, MID, 2)); b.append(t(410, 48, "Thermal paste + cooler", 12, INK, weight=700))
    b.append(rect(450, 230, 160, 30, "#D9DDE2", 3, GREY)); b.append(t(530, 250, "CPU heat spreader", 10, INK, "middle"))
    b.append(f'<ellipse cx="530" cy="228" rx="9" ry="5" fill="{GREY}" class="pea"/>'); b.append(t(620, 215, "pea-sized dot", 10, INK)); b.append(t(620, 230, "in the centre", 10, INK))
    b.append(f'<g class="sink">' + rect(440, 120, 180, 100, "#AEB4BC", 4) + "".join(line(455 + i * 15, 120, 455 + i * 15, 220, "#8A9099", 2) for i in range(11)) + rect(440, 80, 180, 40, "#8A9099", 4) + t(530, 105, "FAN", 12, WHITE, "middle", 700) + '</g>')
    for i in range(4):
        b.append(f'<path d="M{470+i*40} 75 q 6 -10 0 -20 q -6 -10 0 -20" fill="none" stroke="{RED}" stroke-width="2" style="animation:heat 2s {i*.4}s ease-in infinite" opacity=".7"/>')
    b.append(t(410, 290, "Paste fills microscopic gaps so heat crosses into the metal. Too much = mess, not better.", 10, INK))
    style = ("@keyframes lever{0%,40%{transform:rotate(0)}60%,100%{transform:rotate(-70deg)}}"
             ".sink{animation:press 4s ease-in-out infinite}@keyframes press{0%,40%{transform:translateY(-30px)}60%,100%{transform:translateY(0)}}"
             ".pea{animation:spread 4s ease-in-out infinite}@keyframes spread{0%,40%{rx:9}60%,100%{rx:70}}"
             "@keyframes heat{0%{opacity:0;transform:translateY(10px)}50%{opacity:.8}100%{opacity:0;transform:translateY(-20px)}}")
    return svg(760, 340, "".join(b), style)

# ------------------------------------------------------------------ DIMM
def dimm():
    b = []
    b.append(t(30, 30, "Installing a DDR4 DIMM: line up the notch, press both ends, clips snap closed", 13, INK, weight=700))
    for i in range(4):
        x = 60 + i * 150
        pair = "A" if i % 2 == 0 else "B"
        col = "#111" if i % 2 == 0 else "#EEE"
        b.append(rect(x, 230, 120, 18, col, 2, INK, .5))
        b.append(rect(x + 52, 230, 8, 18, PCB, 1))
        b.append(t(x + 60, 270, f"DIMM {i+1}  (pair {pair})", 11, INK, "middle"))
        b.append(f'<rect x="{x-10}" y="222" width="10" height="26" rx="2" fill="{GREY}" style="transform-origin:{x-5}px 248px" class="clipL"/>')
        b.append(f'<rect x="{x+120}" y="222" width="10" height="26" rx="2" fill="{GREY}" style="transform-origin:{x+125}px 248px" class="clipR"/>')
    mod = rect(60, 60, 120, 40, PCB, 2, PCBD, 1) + "".join(rect(66 + k * 14, 66, 10, 16, "#111", 1) for k in range(8)) + rect(60, 100, 120, 8, GOLD, 1) + rect(112, 100, 8, 8, PCB, 0)
    b.append(f'<g class="mod">{mod}' + t(120, 56, "notch is off-centre: it only fits one way", 10, INK, "middle") + '</g>')
    b.append(rect(420, 60, 310, 130, "#F3F4F0", 8, MID, 1.5))
    b.append(t(435, 85, "Dual channel = two lanes to the CPU", 12, INK, weight=700))
    b.append(t(435, 105, "Put a matched pair in the two slots with the", 11, INK)); b.append(t(435, 121, "same-colour clips (pair A or pair B).", 11, INK))
    b.append(t(435, 143, "One stick works, but data moves on one lane.", 11, INK)); b.append(t(435, 159, "Check BIOS: Memory → 'Dual' channel mode.", 11, INK))
    b.append(t(435, 179, "This board: DDR4-2400, max 4 × 16 GB = 64 GB", 11, BLUE, mono=True))
    style = (".mod{animation:drop 5s ease-in-out infinite}@keyframes drop{0%,15%{transform:translateY(0)}45%,100%{transform:translateY(122px)}}"
             ".clipL{animation:cl 5s ease-in-out infinite}.clipR{animation:cr 5s ease-in-out infinite}"
             "@keyframes cl{0%,40%{transform:rotate(-35deg)}55%,100%{transform:rotate(0)}}@keyframes cr{0%,40%{transform:rotate(35deg)}55%,100%{transform:rotate(0)}}")
    return svg(760, 290, "".join(b), style)

# ------------------------------------------------------------------ storage
def storage():
    b = []
    rows = [("HDD (spinning disk, SATA)", 150, "#8A9099"), ("SATA SSD (2.5-inch)", 550, BLUE), ("NVMe SSD (M.2, PCIe 3.0 x4)", 3500, PCB)]
    b.append(t(30, 30, "How fast can each one read a file? (typical, MB per second)", 13, INK, weight=700))
    for i, (name, spd, col) in enumerate(rows):
        y = 55 + i * 55
        b.append(t(30, y + 18, name, 12, INK))
        w = 40 + (spd / 3500) * 420
        b.append(f'<rect x="250" y="{y}" width="{w:.0f}" height="26" rx="4" fill="{col}" class="bar" style="animation-duration:{0.6 + spd/1200:.1f}s"/>')
        b.append(t(258 + w, y + 18, f"{spd} MB/s", 12, INK, mono=True))
    b.append(t(30, 232, "A 4 GB game update: HDD ≈ 27 s, SATA SSD ≈ 7 s, NVMe ≈ 1.2 s (if nothing else slows it)", 11, GREY))
    b.append(rect(30, 255, 700, 80, "#F3F4F0", 8, MID, 1.5))
    b.append(t(45, 278, "M.2 install: slide in at about 30°, then press flat and fit the single screw", 12, INK, weight=700))
    b.append(rect(60, 300, 16, 20, "#1B1B1B", 2)); b.append(t(68, 332, "slot", 9, INK, "middle"))
    b.append(f'<g class="m2stick" style="transform-origin:76px 310px">' + rect(76, 304, 140, 12, "#2F6B2F", 2, GOLD, 1) + rect(76, 304, 12, 12, GOLD, 1) + f'<circle cx="212" cy="310" r="5" fill="none" stroke="{GOLD}" stroke-width="2"/>' + '</g>')
    b.append(rect(236, 300, 20, 20, "#D9DDE2", 3, GREY)); b.append(t(246, 332, "standoff + screw", 9, INK, "middle"))
    b.append(t(300, 300, "M key notch = NVMe or SATA (this board takes both)", 11, INK)); b.append(t(300, 318, "2280 = 22 mm wide, 80 mm long", 11, INK, mono=True))
    style = (".bar{transform-origin:250px 0;animation:grow 2.5s ease-out infinite alternate}@keyframes grow{from{transform:scaleX(.05)}to{transform:scaleX(1)}}"
             ".m2stick{animation:m2 4s ease-in-out infinite}@keyframes m2{0%,30%{transform:rotate(-30deg) translateX(-30px)}60%,100%{transform:rotate(0) translateX(0)}}")
    return svg(760, 345, "".join(b), style)

# ------------------------------------------------------------------ boot chain
def boot_chain():
    steps = [("Power button", "PSU gets PS_ON"), ("PWR_OK", "voltages stable"), ("UEFI firmware", "runs from a chip"), ("POST", "tests CPU, RAM, GPU, keyboard"), ("Boot device", "reads EFI partition"), ("Bootloader → OS", "Windows / Linux loads")]
    b = [arrow_def("arr", INK)]
    for i, (a, c) in enumerate(steps):
        x = 30 + i * 120
        b.append(rect(x, 60, 108, 70, "#F3F4F0", 8, MID, 1.5))
        b.append(t(x + 54, 88, a, 12, INK, "middle", 700)); b.append(t(x + 54, 108, c, 9.5, GREY, "middle"))
        if i < 5: b.append(line(x + 108, 95, x + 120, 95, INK, 2, 'marker-end="url(#arr)"'))
    b.append(f'<circle r="8" fill="{AMBER}" stroke="{INK}" stroke-width="2"><animateMotion dur="6s" repeatCount="indefinite" path="M 84 140 L 684 140"/></circle>')
    b.append(t(30, 185, "Dell power LED while this happens:", 12, INK, weight=700))
    leds = [("blinking amber", AMBER, "power arriving"), ("solid amber", "#E07B00", "PWR_OK, CPU starting"), ("solid white", "#F2F2F2", "firmware running — normal")]
    for i, (n, c, d) in enumerate(leds):
        x = 300 + i * 150
        b.append(f'<circle cx="{x}" cy="181" r="8" fill="{c}" stroke="{INK}"/>' + t(x + 14, 178, n, 10, INK) + t(x + 14, 191, d, 9, GREY))
    b.append(t(30, 215, "If it stops before the screen lights up, that is a 'no POST' problem: hardware. If Windows/Linux then fails, that is a 'no boot' problem: disk or software.", 10.5, INK))
    return svg(760, 230, "".join(b))

# ------------------------------------------------------------------ front panel
def fpanel():
    b = []
    b.append(t(30, 28, "Standard 2×5 front-panel header (most boards)", 13, INK, weight=700))
    labels = [("PWR LED +", "#2E9E5B"), ("PWR LED −", "#2E9E5B"), ("PWR SW", BLUE), ("PWR SW", BLUE), ("—", GREY), ("HDD LED +", AMBER), ("HDD LED −", AMBER), ("RESET", RED), ("RESET", RED), ("", "none")]
    for i, (lab, col) in enumerate(labels):
        r, c = i // 5, i % 5
        x, y = 60 + c * 60, 60 + r * 60
        if col != "none": b.append(rect(x, y, 28, 28, col, 4))
        b.append(t(x + 14, y + 45, lab, 9, INK, "middle"))
    b.append(t(30, 200, "A case's power switch is just two wires on 'PWR SW'. Polarity does not matter for switches; it does for LEDs.", 10.5, INK))
    b.append(t(410, 28, "Dell 7050: one 5-pin plug does the job", 13, INK, weight=700))
    b.append(rect(430, 60, 26, 110, WHITE, 3, INK, 1.2))
    for i in range(5): b.append(f'<circle cx="443" cy="{72+i*22}" r="4" fill="{GOLD}"/>')
    b.append(t(465, 118, "Dell power button + LED (keyed, fits one way)", 10.5, INK))
    b.append(rect(560, 150, 170, 40, "#FFF3D6", 6, AMBER, 1.5)); b.append(t(645, 168, "Adapter: Dell 5-pin ⇄ standard", 10, INK, "middle", 700)); b.append(t(645, 182, "or re-use Dell's own button module", 9.5, INK, "middle"))
    b.append(f'<path d="M456 115 C 500 115, 520 170, 560 170" fill="none" stroke="{AMBER}" stroke-width="2.5" stroke-dasharray="6 5" class="flow"/>')
    style = ".flow{animation:dash 1.2s linear infinite}@keyframes dash{to{stroke-dashoffset:-22}}"
    return svg(760, 215, "".join(b), style)

# ------------------------------------------------------------------ PSU
ATX24 = ["#F28C28", "#F28C28", "#111", "#C0392B", "#111", "#C0392B", "#111", "#8A9099", "#8E44AD", "#F1C40F", "#F1C40F", "#F28C28",
         "#F28C28", "#2457C5", "#111", "#2E9E5B", "#111", "#111", "#111", "#EEE", "#C0392B", "#C0392B", "#C0392B", "#111"]
def psu():
    b = []
    b.append(rect(20, 20, 200, 130, SLATE, 8)); b.append(t(120, 45, "ATX power supply", 13, WHITE, "middle", 700))
    b.append(f'<circle cx="80" cy="100" r="34" fill="none" stroke="{GREY}" stroke-width="4"/>'); b.append(t(150, 92, "230 V AC in", 10, MID, "middle")); b.append(t(150, 108, "3.3 / 5 / 12 V DC out", 10, MID, "middle"))
    b.append(t(250, 40, "24-pin main", 12, INK, weight=700))
    for i, c in enumerate(ATX24):
        r, col = i // 12, i % 12
        b.append(rect(250 + col * 18, 50 + r * 18, 15, 15, c, 2, "#555", .5))
    b.append(t(250, 100, "orange 3.3 V · red 5 V · yellow 12 V · black ground · green PS_ON · grey PWR_OK · purple 5 V standby", 9.5, INK))
    b.append(t(250, 130, "8-pin (4+4) CPU", 12, INK, weight=700))
    for i in range(8): b.append(rect(250 + (i % 4) * 18, 140 + (i // 4) * 18, 15, 15, "#F1C40F" if i < 4 else "#111", 2, "#555", .5))
    b.append(t(360, 130, "6+2 pin PCIe (GPU)", 12, INK, weight=700))
    for i in range(8): b.append(rect(360 + (i % 4) * 18, 140 + (i // 4) * 18, 15, 15, "#F1C40F" if i % 4 < 3 else "#111", 2, "#555", .5))
    b.append(t(500, 130, "SATA power (15-pin flat)", 12, INK, weight=700)); b.append(rect(500, 140, 120, 14, "#111", 2))
    for i, c in enumerate(["#F28C28", "#111", "#C0392B", "#111", "#F1C40F"]): b.append(rect(504 + i * 23, 143, 20, 8, c, 1))
    b.append(rect(480, 20, 260, 95, "#FFF3D6", 8, AMBER, 1.5)); b.append(t(610, 42, "Dell 7050 board wants a 6-pin main plug", 11.5, INK, "middle", 700))
    for i in range(6): b.append(rect(560 + (i % 3) * 18, 52 + (i // 3) * 18, 15, 15, "#F1C40F" if i < 3 else "#111", 2, "#555", .5))
    b.append(t(610, 103, "use a 24-pin → 6-pin adapter made for 3050/5050/7050", 9.5, INK, "middle"))
    b.append(f'<path d="M470 60 C 500 60, 520 60, 555 60" fill="none" stroke="{AMBER}" stroke-width="2.5" stroke-dasharray="6 5" class="flow"/>')
    b.append(rect(20, 170, 720, 60, "#F3F4F0", 8, MID, 1.5))
    b.append(t(35, 192, "Rails: a PSU is really three supplies in one box. 12 V does the heavy lifting (CPU, GPU, fans). 5 V and 3.3 V feed drives, USB and logic.", 10.5, INK))
    b.append(t(35, 212, "80 Plus Bronze/Gold = how little is wasted as heat. A 550 W Gold unit pulling 300 W wastes about 30 W; a cheap unit wastes far more.", 10.5, INK))
    style = ".flow{animation:dash 1.2s linear infinite}@keyframes dash{to{stroke-dashoffset:-22}}"
    return svg(760, 245, "".join(b), style)

def power_budget():
    return '''<div class="pb" data-visual="power_budget">
<div class="pb-grid">
 <div class="pb-list">
  <label><input type="checkbox" checked disabled data-w="65"> CPU Intel Core i5-7500 <b>65 W</b></label>
  <label><input type="checkbox" checked disabled data-w="25"> Motherboard + 4 RAM sticks <b>25 W</b></label>
  <label><input type="checkbox" checked data-w="7"> NVMe SSD <b>7 W</b></label>
  <label><input type="checkbox" data-w="5"> SATA SSD <b>5 W</b></label>
  <label><input type="checkbox" data-w="10"> 3.5-inch HDD <b>10 W</b></label>
  <label><input type="checkbox" data-w="6"> 2 case fans <b>6 W</b></label>
  <label><input type="checkbox" data-w="10"> USB devices + RGB <b>10 W</b></label>
  <label>Graphics card <select data-gpu>
   <option value="0">none (iGPU) 0 W</option><option value="75">GTX 1650 LP 75 W (no plug)</option><option value="115">RTX 4060 115 W (8-pin)</option>
   <option value="130">RTX 3050 130 W (8-pin)</option><option value="132">RX 6600 132 W (8-pin)</option><option value="170">RTX 3060 170 W (8-pin)</option></select></label>
  <label>Power supply <select data-psu>
   <option value="180">Dell stock 180 W</option><option value="450">450 W ATX</option><option value="550" selected>550 W ATX</option><option value="650">650 W ATX</option></select></label>
 </div>
 <div class="pb-gauge"><svg viewBox="0 0 220 150"><path d="M20 130 A90 90 0 0 1 200 130" fill="none" stroke="#E9ECEF" stroke-width="22"/>
  <path class="pb-arc" d="M20 130 A90 90 0 0 1 200 130" fill="none" stroke="#2E9E5B" stroke-width="22" stroke-dasharray="283" stroke-dashoffset="283"/>
  <text x="110" y="100" text-anchor="middle" class="pb-total" style="font-size:28px;font-weight:700">0 W</text>
  <text x="110" y="122" text-anchor="middle" class="pb-note" style="font-size:11px">peak draw with 30% headroom</text></svg>
  <p class="pb-verdict"></p></div>
</div></div>'''

# ------------------------------------------------------------------ GPU
def gpu():
    b = []
    b.append(t(30, 28, "Graphics card into PCIe x16: bracket at the rear, press until the latch clicks, one screw", 13, INK, weight=700))
    b.append(rect(60, 230, 300, 14, "#1B1B1B", 2)); b.append(rect(355, 226, 14, 22, GREY, 2, extra='class="latch" style="transform-origin:362px 248px"'))
    b.append(t(210, 265, "PCIe x16 slot (16 lanes = 16 tiny two-way roads)", 11, INK, "middle"))
    card = rect(60, 100, 300, 120, PCB, 6, PCBD, 1.5) + rect(70, 110, 120, 60, "#2B2B2B", 4) + t(130, 145, "GPU chip", 11, WHITE, "middle") + "".join(rect(200 + k * 34, 110, 28, 22, "#111", 2) for k in range(4)) + t(268, 150, "VRAM", 10, "#CFEFD9", "middle") + \
           rect(60, 220, 300, 10, GOLD, 1) + rect(40, 95, 20, 135, "#8A9099", 2) + f'<circle cx="50" cy="104" r="4" fill="{WHITE}"/>' + t(50, 250, "bracket", 9, INK, "middle") + rect(290, 92, 46, 12, "#111", 2) + t(313, 86, "8-pin power", 9, INK, "middle")
    b.append(f'<g class="card">{card}</g>')
    b.append(rect(400, 50, 340, 200, "#F3F4F0", 8, MID, 1.5)); b.append(t(570, 75, "What a GPU does 60+ times a second", 12, INK, "middle", 700))
    b.append(f'<polygon points="430,160 470,110 510,160" fill="none" stroke="{BLUE}" stroke-width="2"/>' + t(470, 185, "1. triangles (vertices)", 9.5, INK, "middle"))
    for r in range(5):
        for c in range(5):
            on = (r + c) % 2 == 0
            b.append(f'<rect x="{545+c*12}" y="{110+r*12}" width="10" height="10" fill="{BLUE if on else "#DCE6FB"}" class="px" style="animation-delay:{(r*5+c)*.05}s"/>')
    b.append(t(575, 185, "2. fill pixels (raster)", 9.5, INK, "middle"))
    b.append('<defs><linearGradient id="g1" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#9BB7F0"/><stop offset="1" stop-color="#143A8C"/></linearGradient></defs>')
    b.append(f'<rect x="640" y="108" width="60" height="60" rx="4" fill="url(#g1)"/>')
    b.append(t(670, 185, "3. shade & light", 9.5, INK, "middle")); b.append(t(570, 215, "Thousands of small cores do this in parallel; a CPU has 4 big ones.", 9.5, GREY, "middle")); b.append(t(570, 235, "That is why games need a GPU and spreadsheets do not.", 9.5, GREY, "middle"))
    style = (".card{animation:ins 4s ease-in-out infinite}@keyframes ins{0%,30%{transform:translateY(-60px)}60%,100%{transform:translateY(0)}}"
             ".latch{animation:lt 4s ease-in-out infinite}@keyframes lt{0%,45%{transform:rotate(40deg)}65%,100%{transform:rotate(0)}}"
             ".px{animation:pxa 2s ease-in-out infinite alternate}@keyframes pxa{from{opacity:.2}to{opacity:1}}")
    return svg(760, 275, "".join(b), style)

# ------------------------------------------------------------------ airflow
def airflow():
    b = []
    b.append(rect(80, 40, 520, 260, "#F3F4F0", 10, MID, 2)); b.append(t(340, 30, "Case seen from the side: cool air in at the front/bottom, warm air out the back/top", 12, INK, "middle", 700))
    for (x, y, lab) in [(80, 150, "intake"), (600, 100, "exhaust"), (340, 40, "top exhaust")]:
        b.append(f'<circle cx="{x}" cy="{y}" r="26" fill="{WHITE}" stroke="{INK}" stroke-width="2"/>')
        b.append(f'<g style="transform-origin:{x}px {y}px;animation:spin 1.2s linear infinite">' + "".join(f'<ellipse cx="{x}" cy="{y-14}" rx="5" ry="13" fill="{GREY}" transform="rotate({k*72} {x} {y})"/>' for k in range(5)) + '</g>')
        b.append(t(x, y + 42 if y < 150 else y - 34, lab, 10, INK, "middle"))
    b.append(rect(250, 120, 180, 90, "#AEB4BC", 6)); b.append(t(340, 170, "CPU cooler", 11, INK, "middle")); b.append(rect(300, 230, 200, 30, PCB, 4)); b.append(t(400, 250, "graphics card", 11, WHITE, "middle"))
    b.append(rect(90, 50, 110, 60, SLATE, 4)); b.append(t(145, 85, "PSU (own fan)", 10, WHITE, "middle"))
    paths = ["M 60 150 C 200 150, 260 200, 330 170 C 420 130, 500 110, 640 100", "M 60 170 C 180 200, 300 260, 400 230 C 480 210, 560 130, 640 100", "M 60 140 C 200 120, 300 110, 340 90 C 345 70, 340 50, 340 10"]
    for pi, p in enumerate(paths):
        for k in range(6):
            b.append(f'<circle r="4" fill="{BLUE if pi!=2 else RED}" opacity=".8"><animateMotion dur="{3+pi*.4}s" begin="{-(k*.5)}s" repeatCount="indefinite" path="{p}"/></circle>')
    b.append(t(340, 322, "Dust filters on intakes. Positive pressure (slightly more intake than exhaust) keeps dust out of the gaps.", 10.5, GREY, "middle"))
    style = "@keyframes spin{to{transform:rotate(360deg)}}"
    return svg(760, 335, "".join(b), style)

# ------------------------------------------------------------------ standoffs
def standoff():
    b = []
    b.append(t(30, 28, "Why standoffs and washers matter on a transplant", 13, INK, weight=700))
    for i, (title, bad) in enumerate([("Correct: brass standoffs, nylon washers, nothing else touches", False), ("Wrong: board edge or port touches the metal frame", True)]):
        oy = 50 + i * 120
        b.append(rect(40, oy + 60, 680, 14, "#9AA3AE", 2)); b.append(t(60, oy + 90, "metal tray / frame rails", 10, GREY))
        b.append(rect(90, oy + 20, 520, 12, PCB, 2, PCBD, 1))
        for x in (140, 320, 520):
            b.append(rect(x, oy + 32, 12, 28, GOLD, 2)); b.append(rect(x - 4, oy + 16, 20, 5, "#EEE", 1, GREY, .5))
        b.append(t(150, oy + 15, title, 11, INK, weight=700))
        if bad:
            b.append(rect(606, oy + 10, 30, 22, "#2B333E", 2)); b.append(line(621, oy + 32, 621, oy + 60, "#2B333E", 6))
            b.append(f'<path d="M600 {oy+40} l8 -8 l-6 10 l10 -4 l-8 12" fill="none" stroke="{RED}" stroke-width="3" class="zap"/>')
            b.append(t(400, oy + 50, "USB housing on the frame → short → dead board", 10.5, RED))
        else:
            b.append(t(400, oy + 50, "washer under each screw head; unused holes left open", 10.5, GREEN))
    style = ".zap{animation:zap .8s steps(2) infinite}@keyframes zap{0%,45%{opacity:0}50%,100%{opacity:1}}"
    return svg(760, 300, "".join(b), style)

# ------------------------------------------------------------------ six-step method
def method6():
    steps = ["Identify the problem", "Form a theory", "Test the theory", "Plan the fix", "Fix it & verify", "Write it down"]
    b = [arrow_def("arr", INK)]
    cx, cy, R = 300, 165, 115
    for i, s in enumerate(steps):
        a = -math.pi / 2 + i * 2 * math.pi / 6
        x, y = cx + R * math.cos(a), cy + R * math.sin(a)
        b.append(f'<g class="st" style="animation-delay:{i*1.2}s">' + f'<circle cx="{x:.0f}" cy="{y:.0f}" r="34" fill="#F3F4F0" stroke="{INK}" stroke-width="1.5"/>' + t(f"{x:.0f}", f"{y-4:.0f}", str(i + 1), 14, INK, "middle", 700) + t(f"{x:.0f}", f"{y+12:.0f}", s, 8.5, INK, "middle") + '</g>')
        a2 = a + 2 * math.pi / 6
        x1, y1 = cx + R * math.cos(a + .32), cy + R * math.sin(a + .32); x2, y2 = cx + R * math.cos(a2 - .32), cy + R * math.sin(a2 - .32)
        b.append(f'<path d="M{x1:.0f} {y1:.0f} A{R} {R} 0 0 1 {x2:.0f} {y2:.0f}" fill="none" stroke="{GREY}" stroke-width="1.5" marker-end="url(#arr)"/>')
    b.append(rect(440, 50, 300, 230, "#F3F4F0", 8, MID, 1.5))
    tips = ["Ask: what changed? what exactly happens? when?", "Simplest theory first (cable, seating, power).", "Change ONE thing, then re-test. Keep a log.", "If the theory fails, go back to step 2.", "Half-split: remove half the parts, test, repeat.", "'Known good' part swap beats guessing."]
    b.append(t(455, 75, "Habits of a good tech", 12, INK, weight=700))
    for i, s in enumerate(tips): b.append(t(455, 100 + i * 28, "• " + s, 10.5, INK))
    style = ".st circle{animation:hl 7.2s linear infinite}@keyframes hl{0%,16%{fill:#FFE9B8;stroke-width:3}17%,100%{fill:#F3F4F0;stroke-width:1.5}}"
    return svg(760, 300, "".join(b), style)

# ------------------------------------------------------------------ Dell LED simulator
DELL_CODES = [("2,1", "Bad motherboard"), ("2,2", "Motherboard, PSU or PSU cabling"), ("2,3", "Motherboard, memory or CPU"), ("2,4", "Coin-cell battery"), ("2,5", "BIOS checksum (recovery mode)"), ("2,6", "Processor"),
              ("2,7", "Memory failure"), ("3,1", "PCI device or video"), ("3,2", "Video subsystem"), ("3,3", "No memory detected"), ("3,4", "Storage subsystem"), ("3,5", "Memory configuration / incompatible"), ("3,6", "System board"), ("3,7", "Memory incompatible / invalid config")]
def dell_led():
    opts = "".join(f'<option value="{c}">{c} — {d}</option>' for c, d in DELL_CODES)
    return f'''<div class="ledsim" data-visual="dell_led">
<div class="ledsim-row"><div class="ledsim-btn"><div class="ledsim-led"></div><span>power button</span></div>
<div class="ledsim-ctl"><label>Pattern <select data-code>{opts}</select></label><button type="button" data-play>Play pattern</button><button type="button" data-beep>Play 1-3-2 beep</button><p class="ledsim-read"></p></div></div>
<p class="ledsim-note">Count the amber blinks: a group, a short pause, a second group, then a long pause. Write it as "first,second". Table: Dell OptiPlex 2012–2020 series (7050 included). Since 2012 the only beep code left is 1-3-2 = memory.</p></div>'''

# ------------------------------------------------------------------ LAN topology
def lan(frames=True):
    b = []
    sw_x, sw_y = 380, 60
    b.append(rect(sw_x - 120, sw_y, 240, 50, SLATE, 6)); b.append(t(sw_x, sw_y + 20, "24-port switch", 12, WHITE, "middle", 700))
    for i in range(8): b.append(rect(sw_x - 105 + i * 27, sw_y + 30, 18, 12, "#111", 2, GREY, .5))
    pcs = [("PC-01", "192.168.10.11", "3C-7C-3F-11-AA-01"), ("PC-02", "192.168.10.12", "3C-7C-3F-11-AA-02"), ("PC-03", "192.168.10.13", "3C-7C-3F-11-AA-03"), ("PC-04", "192.168.10.14", "3C-7C-3F-11-AA-04")]
    for i, (n, ip, mac) in enumerate(pcs):
        x = 70 + i * 185
        b.append(line(x + 45, 190, sw_x - 95 + i * 54, sw_y + 50, BLUE, 2.5))
        b.append(rect(x, 190, 90, 70, "#F3F4F0", 6, INK, 1.5)); b.append(rect(x + 15, 200, 60, 36, "#2B333E", 3)); b.append(t(x + 45, 253, n, 11, INK, "middle", 700))
        b.append(t(x + 45, 278, ip, 10, BLUE, "middle", mono=True)); b.append(t(x + 45, 292, mac, 8.5, GREY, "middle", mono=True))
    if frames:
        b.append(f'<rect width="26" height="12" rx="2" fill="{AMBER}" stroke="{INK}"><animateMotion dur="3s" repeatCount="indefinite" path="M 115 190 L {sw_x-95} {sw_y+50} L {sw_x-95+108} {sw_y+50} L 485 190"/></rect>')
        b.append(t(380, 150, "a frame from PC-01 to PC-03: the switch sends it out ONE port, the right one", 10.5, INK, "middle"))
    b.append(t(380, 325, "Every network card has a MAC address burnt in at the factory (hardware). An IP address is assigned later (software). Both are needed.", 10, GREY, "middle"))
    return svg(760, 335, "".join(b))

# ------------------------------------------------------------------ layers
def layers():
    b = []
    lay = [("Application", "the message: 'hi'", "#DCE6FB"), ("Transport (TCP/UDP)", "+ port numbers 2323 → 51000", "#FFE9B8"), ("Internet (IP)", "+ IP addresses 192.168.10.11 → .12", "#CFEFD9"), ("Link (Ethernet)", "+ MAC addresses, onto the cable", "#E9ECEF")]
    for i, (n, d, c) in enumerate(lay):
        y = 40 + i * 62
        b.append(f'<g class="lay" style="animation-delay:{i*.8}s">' + rect(40, y, 420, 50, c, 6, INK, 1) + t(55, y + 22, n, 12, INK, weight=700) + t(55, y + 40, d, 10.5, INK) + '</g>')
    b.append(rect(500, 40, 230, 236, "#F3F4F0", 8, MID, 1.5)); b.append(t(615, 65, "Like posting a letter", 12, INK, "middle", 700))
    for i, s in enumerate(["the note (data)", "the room number (port)", "the street address (IP)", "the truck + depot label (MAC)"]):
        b.append(t(515, 95 + i * 28, f"{i+1}. {s}", 10.5, INK))
    b.append(t(515, 225, "Each layer only reads its own", 10, GREY)); b.append(t(515, 240, "header. The receiver unwraps", 10, GREY)); b.append(t(515, 255, "in reverse order.", 10, GREY))
    b.append(t(40, 305, "Ping uses ICMP at the Internet layer (no port). Telnet and Minecraft use TCP ports. Wrong IP = letter never arrives; wrong port = no one answers the door.", 10, INK))
    style = ".lay{animation:wrap 4s ease-in-out infinite}@keyframes wrap{0%{opacity:0;transform:translateX(-20px)}20%,70%{opacity:1;transform:translateX(0)}100%{opacity:0}}"
    return svg(760, 320, "".join(b), style)

# ------------------------------------------------------------------ pinout
WIRES_B = [("white/orange", "#F28C28", True), ("orange", "#F28C28", False), ("white/green", "#27AE60", True), ("blue", "#2E86DE", False), ("white/blue", "#2E86DE", True), ("green", "#27AE60", False), ("white/brown", "#8B5A2B", True), ("brown", "#8B5A2B", False)]
WIRES_A = [WIRES_B[2], WIRES_B[5], WIRES_B[0], WIRES_B[3], WIRES_B[4], WIRES_B[1], WIRES_B[6], WIRES_B[7]]
def pinout():
    def wires(ws, oy, label):
        out = [t(30, oy - 10, label, 13, INK, weight=700)]
        for i, (n, c, striped) in enumerate(ws):
            x = 60 + i * 72
            out.append(f'<g class="wire" style="animation-delay:{i*.15}s">')
            out.append(rect(x, oy, 22, 70, c if not striped else WHITE, 3, c, 2 if striped else 0))
            if striped:
                for k in range(4): out.append(rect(x + 2, oy + 6 + k * 16, 18, 6, c, 1))
            out.append(t(x + 11, oy + 90, str(i + 1), 12, INK, "middle", 700)); out.append(t(x + 11, oy + 104, n, 9, INK, "middle")); out.append('</g>')
        return "".join(out)
    b = []
    b.append(t(30, 28, "Hold the plug with the clip DOWN and the gold pins facing you. Pin 1 is on the LEFT.", 11.5, GREY))
    b.append(wires(WIRES_B, 60, "T568B (the one we use on both ends)"))
    b.append(wires(WIRES_A, 210, "T568A (same wires, pairs 2 and 3 swapped)"))
    b.append(rect(630, 45, 110, 130, "#DCE6FB", 10, BLUE, 1.5)); b.append(t(685, 70, "RJ45 plug", 11, INK, "middle", 700))
    b.append(rect(655, 85, 60, 40, "#9BB7F0", 3, INK, 1)); b.append("".join(rect(659 + k * 7, 86, 4, 18, GOLD, 1) for k in range(8))); b.append(rect(670, 125, 30, 10, "#6B8FD6", 2)); b.append(t(685, 155, "clip underneath", 9.5, INK, "middle"))
    b.append(t(30, 340, "Memory trick for B: 'Orange-white, Orange, Green-white, Blue, Blue-white, Green, Brown-white, Brown' — the blue pair sits in the middle and splits the green pair.", 10.5, INK))
    style = ".wire{animation:slide 3s ease-out infinite}@keyframes slide{0%{transform:translateY(-14px);opacity:0}25%,100%{transform:translateY(0);opacity:1}}"
    return svg(760, 355, "".join(b), style)

# ------------------------------------------------------------------ crimp stepper
CRIMP = [("Strip", "Score the outer jacket about 25 mm from the end with the stripper, twist, and slide it off. Check: no nick on any coloured wire. If you see copper, cut and start again."),
         ("Untwist & straighten", "Fan out the four pairs. Untwist each pair only as far as you must (keep twists within 13 mm of the plug). Straighten each wire between finger and thumb."),
         ("Order", "Arrange left to right: white-orange, orange, white-green, blue, white-blue, green, white-brown, brown. Say it out loud. Press the wires flat and tight together."),
         ("Trim", "Cut all eight wires straight across so they are the same length, about 13 mm from the jacket. A slanted cut means some wires will not reach the pins."),
         ("Insert", "Clip down, pin 1 on the left. Slide all eight wires in until every one touches the end of the plug AND the jacket sits under the strain-relief bar. Look through the plastic to check."),
         ("Crimp", "Put the plug fully into the tool and squeeze until it clicks through. The gold pins bite the wires and the bar grips the jacket. Tug test: pull firmly; nothing should move.")]
def crimp_pic(i):
    b = []
    y = 60
    if i == 0:
        b.append(rect(20, y, 200, 24, "#1F2630", 10)); b.append(rect(220, y + 2, 120, 20, "#9AA3AE", 2)); b.append(rect(230, y - 25, 6, 70, RED, 1)); b.append(t(233, y + 68, "25 mm", 11, INK, "middle"))
    elif i == 1:
        b.append(rect(20, y, 160, 24, "#1F2630", 10))
        for k, c in enumerate(["#F28C28", "#27AE60", "#2E86DE", "#8B5A2B"]):
            b.append(f'<path d="M180 {y+12} C 220 {y+12-30+k*20}, 260 {y+12-30+k*20}, 320 {y-30+k*22}" fill="none" stroke="{c}" stroke-width="5"/>')
    elif i == 2:
        b.append(rect(20, y, 120, 24, "#1F2630", 10))
        for k, (n, c, s) in enumerate(WIRES_B):
            b.append(rect(140, y - 20 + k * 7, 180, 5, c if not s else "#FFF", 1, c, 1.5 if s else 0))
    elif i == 3:
        b.append(rect(20, y, 120, 24, "#1F2630", 10))
        for k, (n, c, s) in enumerate(WIRES_B): b.append(rect(140, y - 20 + k * 7, 100, 5, c if not s else "#FFF", 1, c, 1.5 if s else 0))
        b.append(line(240, y - 30, 240, y + 40, RED, 3, 'stroke-dasharray="6 4"')); b.append(t(250, y + 50, "13 mm — straight cut", 11, INK))
    elif i == 4:
        b.append(rect(20, y, 120, 24, "#1F2630", 10)); b.append(rect(140, y - 8, 120, 40, "#C9D9F7", 4, INK, 1))
        for k, (n, c, s) in enumerate(WIRES_B): b.append(rect(140, y - 4 + k * 4, 110, 3, c, 0))
        b.append(rect(250, y - 4, 8, 32, GOLD, 1)); b.append(t(200, y + 55, "all wires to the END; jacket under the bar", 11, INK, "middle"))
    else:
        b.append(rect(140, y - 8, 120, 40, "#C9D9F7", 4, INK, 1)); b.append(rect(120, y - 30, 160, 20, "#8A9099", 4)); b.append(rect(120, y + 34, 160, 20, "#8A9099", 4)); b.append(t(200, y + 72, "squeeze until it clicks, then tug test", 11, INK, "middle"))
    return svg(360, 140, "".join(b))

def crimp():
    tabs = "".join(f'<button type="button" data-step="{i}" {"class=on" if i == 0 else ""}>{i+1}. {n}</button>' for i, (n, _) in enumerate(CRIMP))
    panels = "".join(f'<div class="crimp-p" data-p="{i}" {"" if i == 0 else "hidden"}><div class="crimp-pic">{crimp_pic(i)}</div><p>{d}</p></div>' for i, (n, d) in enumerate(CRIMP))
    return f'<div class="crimp" data-visual="crimp"><div class="crimp-tabs">{tabs}</div>{panels}</div>'

def crimp_print():
    return "".join(f"<p><b>{i+1}. {n}.</b> {d}</p>" for i, (n, d) in enumerate(CRIMP))

# ------------------------------------------------------------------ LAN tester
def tester():
    def unit(label):
        leds = "".join(f'<div class="led" data-led="{k+1}"><i></i>{k+1}</div>' for k in range(8))
        return f'<div class="tester-unit"><div class="tester-name">{label}</div><div class="leds">{leds}<div class="led" data-led="G"><i></i>G</div></div></div>'
    return f'''<div class="tester" data-visual="tester">
<div class="tester-ctl"><label>Cable condition <select data-mode><option value="good">Good cable (straight-through)</option><option value="open">Open wire on pin 4</option><option value="cross">Wires 2 and 3 swapped (miswire)</option><option value="split">Split pair (3 and 5 swapped)</option><option value="short">Short between 1 and 2</option></select></label><button type="button" data-run>Test</button></div>
<div class="tester-units">{unit("Master")}{unit("Remote")}</div><p class="tester-read"></p></div>'''

# ------------------------------------------------------------------ IP bits
def ipbits():
    return '''<div class="ipb" data-visual="ipbits">
<div class="ipb-row"><label>Address A <input data-ipa value="192.168.10.11" maxlength="15"></label><label>Address B <input data-ipb value="192.168.10.42" maxlength="15"></label><label>Mask /<input data-cidr type="number" min="8" max="30" value="24" style="width:3.5em"></label></div>
<div class="ipb-bits" data-bitsa></div><div class="ipb-bits" data-bitsb></div><div class="ipb-bits ipb-mask" data-bitsm></div>
<p class="ipb-read"></p></div>'''

# ------------------------------------------------------------------ ARP + ping
def arp():
    b = []
    b.append(rect(40, 150, 100, 70, "#F3F4F0", 6, INK, 1.5)); b.append(t(90, 190, "PC-01", 12, INK, "middle", 700)); b.append(t(90, 240, ".11", 11, BLUE, "middle", mono=True))
    b.append(rect(620, 150, 100, 70, "#F3F4F0", 6, INK, 1.5)); b.append(t(670, 190, "PC-02", 12, INK, "middle", 700)); b.append(t(670, 240, ".12", 11, BLUE, "middle", mono=True))
    b.append(rect(300, 160, 160, 50, SLATE, 6)); b.append(t(380, 190, "switch", 12, WHITE, "middle", 700))
    b.append(line(140, 185, 300, 185, BLUE, 2.5)); b.append(line(460, 185, 620, 185, BLUE, 2.5))
    b.append(rect(300, 230, 160, 90, "#F3F4F0", 6, MID, 1.5)); b.append(t(380, 250, "switch MAC table", 10.5, INK, "middle", 700))
    b.append(t(315, 272, "port 1 → ...AA-01", 10, INK, mono=True, extra="animation:ap 8s linear infinite")); b.append(t(315, 292, "port 2 → ...AA-02", 10, INK, mono=True, extra="animation:ap2 8s linear infinite"))
    msgs = [("1  ARP: who has 192.168.10.12? (broadcast)", "M 140 170 L 300 170", 0, AMBER), ("2  ARP reply: .12 is at ...AA-02", "M 620 200 L 140 200", 2.5, GREEN), ("3  ping (ICMP echo) to ...AA-02", "M 140 170 L 620 170", 4.5, BLUE), ("4  ping reply", "M 620 200 L 140 200", 6.2, BLUE)]
    for i, (lab, p, d, c) in enumerate(msgs):
        b.append(f'<rect width="22" height="12" rx="2" fill="{c}" stroke="{INK}"><animateMotion dur="8s" begin="{-d}s" repeatCount="indefinite" path="{p}" keyPoints="0;1;1" keyTimes="0;0.2;1" calcMode="linear"/></rect>')
        b.append(t(40, 40 + i * 20, lab, 11, c, weight=700))
    b.append(t(40, 125, "Try it: ping a neighbour, then type  arp -a  (Windows) or  ip neigh  (Linux). Their MAC is now in your table.", 10.5, INK))
    style = "@keyframes ap{0%,5%{opacity:0}10%,100%{opacity:1}}@keyframes ap2{0%,30%{opacity:0}35%,100%{opacity:1}}"
    return svg(760, 330, "".join(b), style)

# ------------------------------------------------------------------ terminal
def terminal(lines, title="Terminal"):
    import html as _h
    rows = "".join(f'<div class="tl" style="animation-delay:{i*.5}s">{_h.escape(l)}</div>' for i, l in enumerate(lines))
    return f'<div class="term"><div class="term-bar">{title}</div><div class="term-body">{rows}</div></div>'

# ------------------------------------------------------------------ ladder
def ladder():
    steps = [("Link light on?", "cable, port, NIC"), ("Do I have an IP?", "ipconfig / ip a"), ("ping 127.0.0.1", "my own TCP/IP stack works"), ("ping my own IP", "my network card works"), ("ping my neighbour", "cable + switch + their firewall"), ("open the app", "port, firewall, server running")]
    b = []
    for i, (q, d) in enumerate(steps):
        y = 280 - i * 46
        b.append(f'<g class="rung" style="animation-delay:{i*.9}s">' + rect(60, y, 300, 38, "#F3F4F0", 6, INK, 1.2) + t(75, y + 24, f"{i+1}. {q}", 12, INK, weight=700) + t(380, y + 24, d, 11, GREY) + f'<text x="345" y="{y+26}" class="tick" font-size="18" fill="{GREEN}">✓</text></g>')
    b.append(t(60, 25, "Work from the bottom up. The first rung that fails is where the fault is.", 12, INK, weight=700))
    style = ".tick{opacity:0;animation:tk 6s linear infinite}@keyframes tk{0%,10%{opacity:0}15%,100%{opacity:1}}"
    return svg(760, 335, "".join(b), style)

# ------------------------------------------------------------------ twisted pair
def twist():
    b = []
    b.append(t(30, 28, "Why the wires are twisted", 13, INK, weight=700))
    p1 = " ".join(f"{40+x*6},{100+22*math.sin(x/4):.1f}" for x in range(0, 100))
    p2 = " ".join(f"{40+x*6},{100+22*math.sin(x/4+3.14):.1f}" for x in range(0, 100))
    b.append(f'<polyline points="{p1}" fill="none" stroke="#F28C28" stroke-width="5"/>')
    b.append(f'<polyline points="{p2}" fill="none" stroke="#FFF" stroke-width="5" stroke-dasharray="8 4"/>')
    b.append(f'<polyline points="{p2}" fill="none" stroke="#F28C28" stroke-width="5" stroke-dasharray="4 8"/>')
    b.append(arrow_def("arrR", RED))
    for x in (120, 300, 480):
        b.append(f'<path d="M{x} 40 l0 25" stroke="{RED}" stroke-width="2.5" marker-end="url(#arrR)"/>'); b.append(t(x, 35, "noise", 9, RED, "middle"))
    b.append(t(30, 160, "Interference (from a motor, a power lead, a phone) hits BOTH wires of a pair almost equally.", 11, INK)); b.append(t(30, 178, "The receiver only looks at the DIFFERENCE between the two wires, so the noise cancels out.", 11, INK))
    b.append(t(30, 196, "Each pair has a different twist rate so pairs don't talk to each other (crosstalk). Untwist too much at the plug and you throw this away.", 11, INK))
    b.append(rect(30, 215, 700, 70, "#F3F4F0", 8, MID, 1.5)); b.append(t(45, 238, "Cat5e: 1 Gb/s to 100 m.   Cat6: 1 Gb/s to 100 m, 10 Gb/s to 55 m.   Cat6a: 10 Gb/s to 100 m.", 11, INK, mono=True)); b.append(t(45, 262, "100 m is the Ethernet limit for one cable run, including patch leads at both ends.", 11, INK))
    return svg(760, 295, "".join(b))

# ------------------------------------------------------------------ partitions
def partition():
    b = []
    b.append(t(30, 28, "One SSD, several partitions (GPT layout used by UEFI)", 13, INK, weight=700))
    parts = [("EFI System", 100, "#FFE9B8", "~100 MB: boot files"), ("Recovery", 60, "#E9ECEF", "~600 MB"), ("OS", 380, "#DCE6FB", "C: / root — programs + system"), ("Data", 160, "#CFEFD9", "D: / home — your files")]
    x = 30
    for n, w, c, d in parts:
        b.append(rect(x, 50, w, 50, c, 4, INK, 1)); b.append(t(x + w / 2, 80, n, 11, INK, "middle", 700)); b.append(t(x + w / 2, 120, d, 9, GREY, "middle")); x += w
    b.append(t(30, 155, "Initialise (GPT) → create a partition → format (NTFS for Windows, ext4 for Linux) → it gets a letter / mount point.", 10.5, INK))
    b.append(t(30, 173, "Formatting erases the table of contents, not every byte: deleted files can often be recovered. A full wipe overwrites everything.", 10.5, INK))
    return svg(760, 185, "".join(b))

# ------------------------------------------------------------------ board shapes
def board_shapes():
    b = []
    b.append(t(30, 28, "Why the Dell board does not drop into a normal case", 13, INK, weight=700))
    b.append(rect(40, 50, 244, 305, "#E9ECEF", 4, INK, 1.2)); b.append(t(162, 70, "ATX 305 × 244 mm", 11, INK, "middle"))
    holes = [(53, 63), (162, 63), (271, 63), (53, 200), (162, 200), (271, 200), (53, 330), (162, 330), (271, 330), (105, 342)]
    for hx, hy in holes: b.append(f'<circle cx="{hx}" cy="{hy}" r="4" fill="{WHITE}" stroke="{INK}"/>')
    b.append(rect(40, 56, 14, 120, "#2B333E", 2)); b.append(t(47, 190, "I/O", 8, INK, "middle"))
    b.append(t(162, 375, "standard hole pattern, I/O shield, slot positions", 9.5, GREY, "middle"))
    b.append(f'<path d="M340 50 L560 50 L560 120 L600 120 L600 330 L340 330 Z" fill="{PCB}" stroke="{PCBD}" stroke-width="1.5"/>'); b.append(t(470, 70, "Dell 7050 (odd shape)", 11, WHITE, "middle"))
    for hx, hy in [(352, 62), (470, 62), (548, 62), (352, 200), (470, 215), (588, 205), (352, 318), (470, 318), (588, 318)]: b.append(f'<circle cx="{hx}" cy="{hy}" r="4" fill="{WHITE}" stroke="{INK}"/>')
    b.append(rect(345, 150, 50, 20, "#2B333E", 2)); b.append(t(370, 185, "front USB", 8.5, "#CFEFD9", "middle")); b.append(t(370, 196, "soldered on", 8.5, "#CFEFD9", "middle"))
    b.append(t(470, 352, "holes don't all match · front ports fixed · 6-pin power · 5-pin button", 9.5, GREY, "middle"))
    b.append(rect(620, 50, 120, 280, "#FFF3D6", 8, AMBER, 1.5)); b.append(t(680, 75, "Our answer:", 11, INK, "middle", 700))
    for i, s in enumerate(["open-frame case", "slotted rails /", "movable standoffs", "nylon washers", "24→6 pin adapter", "ATX PSU", "Dell button or", "5-pin adapter", "GPU riser if", "bracket misaligns"]): b.append(t(680, 100 + i * 20, s, 10, INK, "middle"))
    return svg(760, 385, "".join(b))

# ------------------------------------------------------------------ sockets / client-server
def sockets():
    b = [arrow_def("arr", INK)]
    b.append(rect(40, 60, 220, 200, "#F3F4F0", 8, INK, 1.5)); b.append(t(150, 85, "Server  PC-01  (.11)", 12, INK, "middle", 700))
    b.append(rect(60, 100, 180, 40, "#CFEFD9", 6)); b.append(t(150, 118, "socket()  bind(2323)", 11, INK, "middle", mono=True)); b.append(t(150, 133, "listen()  — door is open", 10, INK, "middle", mono=True))
    b.append(rect(60, 150, 180, 40, "#FFE9B8", 6)); b.append(t(150, 168, "accept()  — waits", 11, INK, "middle", mono=True)); b.append(t(150, 183, "for a knock", 10, INK, "middle", mono=True))
    b.append(rect(60, 200, 180, 40, "#DCE6FB", 6)); b.append(t(150, 218, "recv() / send()", 11, INK, "middle", mono=True)); b.append(t(150, 233, "talk on the new socket", 10, INK, "middle", mono=True))
    b.append(rect(500, 60, 220, 200, "#F3F4F0", 8, INK, 1.5)); b.append(t(610, 85, "Client  PC-02  (.12)", 12, INK, "middle", 700))
    b.append(rect(520, 100, 180, 40, "#CFEFD9", 6)); b.append(t(610, 118, "socket()", 11, INK, "middle", mono=True)); b.append(t(610, 133, "pick any free port, e.g. 51000", 10, INK, "middle", mono=True))
    b.append(rect(520, 150, 180, 40, "#FFE9B8", 6)); b.append(t(610, 168, "connect(.11, 2323)", 11, INK, "middle", mono=True)); b.append(t(610, 183, "the knock", 10, INK, "middle", mono=True))
    b.append(rect(520, 200, 180, 40, "#DCE6FB", 6)); b.append(t(610, 218, "send() / recv()", 11, INK, "middle", mono=True)); b.append(t(610, 233, "talk", 10, INK, "middle", mono=True))
    b.append(f'<path d="M500 170 L260 170" stroke="{AMBER}" stroke-width="2.5" marker-end="url(#arr)" class="knock"/>'); b.append(t(380, 162, "SYN: can I come in?", 10, INK, "middle"))
    b.append(f'<path d="M260 215 L500 215" stroke="{BLUE}" stroke-width="2.5" marker-end="url(#arr)" class="talk"/>'); b.append(t(380, 208, "'hi from PC-01'", 10, INK, "middle", mono=True))
    b.append(f'<path d="M500 230 L260 230" stroke="{BLUE}" stroke-width="2.5" marker-end="url(#arr)" class="talk2"/>')
    b.append(t(380, 290, "A socket = IP address + port. The server's door number is fixed (2323). The client's is temporary. Both sides can send once connected.", 10.5, INK, "middle"))
    style = ".knock{stroke-dasharray:240;animation:kn 4s linear infinite}@keyframes kn{0%{stroke-dashoffset:240}30%,100%{stroke-dashoffset:0}}.talk{stroke-dasharray:240;animation:kn 4s 1.2s linear infinite}.talk2{stroke-dasharray:240;animation:kn 4s 2.2s linear infinite}"
    return svg(760, 305, "".join(b), style)

# ------------------------------------------------------------------ firewall
def firewall():
    b = []
    b.append(rect(40, 60, 200, 180, "#F3F4F0", 8, INK, 1.5)); b.append(t(140, 85, "PC-02 wants to connect", 12, INK, "middle", 700)); b.append(t(140, 110, "to .11 : 2323", 12, BLUE, "middle", mono=True))
    b.append(rect(300, 40, 60, 220, "#8A5A2B", 6)); b.append(t(330, 150, "FIREWALL", 11, WHITE, "middle", 700, extra="writing-mode:tb;"))
    b.append(rect(300, 130, 60, 40, "#2E9E5B", 4, extra='class="gate"')); b.append(t(330, 182, "rule: allow", 9, INK, "middle")); b.append(t(330, 194, "TCP 2323 in", 9, INK, "middle"))
    b.append(rect(420, 60, 300, 180, "#F3F4F0", 8, INK, 1.5)); b.append(t(570, 85, "PC-01 (server)", 12, INK, "middle", 700))
    b.append(rect(440, 110, 120, 36, "#CFEFD9", 6)); b.append(t(500, 132, "2323 chat: open", 10, INK, "middle", mono=True))
    b.append(rect(440, 160, 120, 36, "#FDECEA", 6)); b.append(t(500, 182, "445 SMB: blocked", 10, INK, "middle", mono=True))
    b.append(rect(580, 110, 120, 36, "#CFEFD9", 6)); b.append(t(640, 132, "25565 Minecraft", 10, INK, "middle", mono=True))
    b.append(rect(580, 160, 120, 36, "#FDECEA", 6)); b.append(t(640, 182, "everything else", 10, INK, "middle", mono=True))
    b.append(f'<rect width="20" height="12" rx="2" fill="{BLUE}" stroke="{INK}"><animateMotion dur="3s" repeatCount="indefinite" path="M 240 150 L 440 150"/></rect>')
    b.append(f'<rect width="20" height="12" rx="2" fill="{RED}" stroke="{INK}"><animateMotion dur="3s" begin="1.5s" repeatCount="indefinite" path="M 240 210 L 300 210" keyPoints="0;1;1" keyTimes="0;0.4;1" calcMode="linear"/></rect>')
    b.append(t(380, 285, "A firewall is a list of rules. Default: block incoming. You add one rule per door you mean to open, and nothing else.", 10.5, INK, "middle"))
    return svg(760, 300, "".join(b))

# ------------------------------------------------------------------ rubric
def rubric_table(rows):
    head = "<tr><th>Criterion</th><th>Not yet</th><th>Developing</th><th>Competent</th><th>Technician</th></tr>"
    body = "".join(f"<tr><td><b>{r[0]}</b></td><td>{r[1]}</td><td>{r[2]}</td><td>{r[3]}</td><td>{r[4]}</td></tr>" for r in rows)
    return f'<table class="rubric">{head}{body}</table>'
