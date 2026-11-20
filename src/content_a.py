from visuals import *

def L(n, week, lnum, title, outcomes, kit, vocab, start, learn, do, check, pack, print_, callouts=None, parts=None):
    d = dict(n=n, week=week, lnum=lnum, title=title, outcomes=outcomes, kit=kit, vocab=vocab, start=start, learn=learn, do=do, check=check, pack=pack, print=print_, callouts=callouts or [], parts=parts or {})
    for k, dflt in (("start", 5), ("learn", 12), ("do", 20), ("check", 5), ("pack", 3)):
        d[k].setdefault("min", dflt)
    assert sum(d[k]["min"] for k in ("start", "learn", "do", "check", "pack")) == 45, f"Lesson {n} does not add to 45"
    return d

STD_PACK = ["Power off, unplug the mains lead, then touch the chassis before anything else.", "Screws back in the bench tray; nothing loose inside the case.", "Side panel on, PC back on the shelf label-out, cables coiled.", "Navigator ticks the bench card; Driver signs the log."]
SAFE_ESD = ("", "Before you touch anything inside", "Wrist strap on and clipped to bare metal on the case. PC unplugged from the wall. Hold boards by the edges.")
SAFE_PSU = ("danger", "Never open a power supply", "The capacitors inside can hold a dangerous charge for days after it is unplugged. Nothing in this course needs the PSU lid off.")
SAFE_PWR = ("", "Power-on rule", "Nobody plugs in or presses the power button until the Navigator has checked every connector and the teacher has said 'go'.")

Q = lambda q, o, a, why: dict(q=q, o=o, a=a, why=why)

LESSONS = []

# ---------------------------------------------------------------- WEEK 1
LESSONS.append(L(1, 1, 1, "Welcome to the bench: what we will build, and how we stay safe",
 ["Explain what the course builds over 18 weeks (upgrade, transplant, LAN).", "List the three safety rules that apply every lesson.", "Put on a wrist strap correctly and name the main bench tools."],
 ["One Dell OptiPlex 7050 SFF per pair", "Anti-static wrist strap + mat", "#2 Phillips screwdriver (magnetic tip)", "Parts tray", "Bench log sheet"],
 [("ESD", "Electrostatic discharge: a tiny spark from your body that can damage chips."), ("Chassis", "The metal frame/case of the computer."), ("SFF", "Small form factor: Dell's compact case design."), ("Navigator / Driver", "Bench roles: one reads and checks, one does.")],
 dict(min=6, steps=["Sit in pairs at a bench. Decide who is Driver first (they swap next lesson).", "Teacher shows the course map: upgrade the Dell → move it into an open-frame case → build a LAN and play across it.", "Write your bench number on the log sheet."]),
 dict(min=12, html="""<p>Every PC you will touch this year is the same model: a <b>Dell OptiPlex 7050 small form factor</b>. That is good news. Learn one machine deeply and you can work on any of them.</p>
<p>Three rules apply every single lesson:</p>
<ol><li><b>Unplug before you open.</b> Power off, pull the mains lead, then press the power button once to drain the last of the charge.</li>
<li><b>Strap on before you touch.</b> Your body can carry thousands of volts of static. You will not feel it; a RAM chip will.</li>
<li><b>Check before you power on.</b> The Navigator reads every connector, then calls the teacher. Only then does anyone press the button.</li></ol>
{F0}
<p><b>Example 1.</b> Jess walks across the carpet in sneakers, sits down and picks up a stick of RAM. Nothing happens that she can see. The RAM fails two weeks later. ESD damage is often invisible and delayed.</p>
<p><b>Example 2.</b> Sam straps on, clips to the painted part of the case, and feels safe. Paint is an insulator: the strap is not doing anything. Clip to <i>bare metal</i> — a screw head or the unpainted chassis edge.</p>
<p><b>Example 3.</b> Ali is not sure a cable is plugged in all the way, powers on anyway, and the fan jams. "Not sure" always means stop and ask.</p>""", figures=[esd()]),
 dict(min=19, steps=[("Put on the strap: snug on the wrist, metal plate against skin, clip on bare metal of the case.", "Navigator checks the clip is on unpainted metal."),
      "Unplug the PC. Press the power button once. Count to five.",
      "Find the side-panel release (rear latch on the 7050). Slide the panel off and lay it flat on the mat.",
      "Look, do not touch yet: find the big silver box (PSU), the fan on the processor, and the four thin slots (RAM).",
      "Tool roll: pick up the Phillips #2, the spudger and the flashlight. Name each to your partner.",
      "Refit the side panel. Make sure the latch clicks.",
      "Fill in the first line of the bench log: date, names, 'opened and closed, no changes'."]),
 dict(min=5, quiz=[Q("Why do you press the power button after unplugging?", ["To turn the fans on", "To drain leftover charge from the board", "To reset the BIOS", "It does nothing"], 1, "Capacitors keep a little charge; pressing the button uses it up so the board is truly dead."),
      Q("Where must the wrist-strap clip go?", ["Any part of the case", "Bare, unpainted metal", "The plastic front", "The power cable"], 1, "Paint and plastic are insulators. The strap only works through a metal path."),
      Q("You are not sure if a plug is fully in. What now?", ["Power on and see", "Push harder", "Stop, ask the Navigator or teacher", "Pull it out and leave it"], 2, "'Not sure' means stop. A loose plug can arc or jam a fan.")]),
 dict(min=3, steps=STD_PACK),
 dict(key_ideas=["Unplug → press the button → strap on → open. Every lesson, same order.", "ESD damage is invisible and delayed, so you follow the rule even when nothing 'happens'.", "The Navigator checks every connector before power-on."],
      questions=[("List the three safety rules in the order you do them.", 3), ("Explain why clipping the strap onto a painted panel does not protect the PC.", 2), ("Name three tools in the bench roll and what each is for.", 3), ("What does SFF stand for and why does it matter for upgrades later?", 2)],
      exit="One thing you are looking forward to building, and one thing you want to be careful about."),
 callouts=[SAFE_ESD, SAFE_PSU]))

LESSONS.append(L(2, 1, 2, "Anatomy tour: every part inside the Dell and what it does",
 ["Point to and name 12 parts inside the 7050.", "Say in one sentence what each part does.", "Explain why Dell's board shape will matter later."],
 ["Dell 7050 SFF per pair", "Wrist strap", "Torch", "Sticky labels + marker", "Worksheet"],
 [("Motherboard", "The big board everything plugs into."), ("CPU", "Central processing unit: the processor."), ("RAM", "Random access memory: fast, temporary working memory."), ("PSU", "Power supply unit."), ("Header", "A row of pins on the board that a small plug fits onto."), ("Chipset", "A chip that manages traffic between the CPU and slower parts.")],
 dict(steps=["Driver/Navigator swap. Strap on, unplug, press the button, open the side panel.", "Teacher puts the labelled map on the big screen. Match it to the real thing in front of you."]),
 dict(min=14, html="""<p>Think of the board as a city. The <b>CPU</b> is the brain in the middle. <b>RAM</b> is its desk: fast, but cleared when the power goes. The <b>SSD</b> is the filing cabinet: slower, but it remembers. The <b>PSU</b> is the power station. The <b>chipset</b> is the traffic cop for everything slower than RAM. Cables and slots are the roads.</p>
{F0}
<p><b>Example 1.</b> You open a photo. It is read from the SSD (cabinet) into RAM (desk) so the CPU (brain) can work on it fast.</p>
<p><b>Example 2.</b> You add more RAM. The desk gets bigger, so more things can be open at once. The brain does not get faster.</p>
<p><b>Example 3.</b> A Dell board is an odd shape with the front USB ports soldered on and a tiny 6-pin power plug. That is why, in Week 9, we need adapters to move it into a normal case.</p>""", figures=[anatomy()]),
 dict(min=18, steps=["Open the panel. Using the torch, find each part on the on-screen map, in this order: PSU, drive cage, CPU cooler, RAM slots, M.2 slot, PCIe x16, SATA ports, 6-pin power, 4-pin CPU power, front-panel plug, coin cell, chipset heatsink.",
      "Write a sticky label for each and place it next to (not on) the part. Do not stick labels onto chips or slots.",
      "Navigator quizzes Driver: point at random, name it, say what it does. Then swap.",
      ("Count the RAM slots and the number of sticks fitted. Write it on the worksheet.", "Most units have 1 or 2 of 4 slots used."),
      "Find the service tag sticker on the case and copy it to the worksheet. Dell's website uses it to look up this exact PC.",
      "Remove all labels and refit the panel."]),
 dict(quiz=[Q("Which part keeps your files when the power is off?", ["RAM", "CPU", "SSD / hard drive", "Chipset"], 2, "RAM is wiped at power-off; storage (SSD/HDD) is permanent."),
      Q("The small plug near the CPU with a '4' on our map carries…", ["USB", "12 V just for the CPU", "video", "network"], 1, "The 4-pin feeds 12 V to the CPU's voltage regulators."),
      Q("Why does Dell's board shape matter for Week 9?", ["It is too heavy", "Its holes and ports do not match standard cases", "It has no RAM", "It cannot run Windows"], 1, "Proprietary shape = adapters and an open frame instead of a normal case.")]),
 dict(steps=STD_PACK),
 dict(key_ideas=["CPU = brain, RAM = desk, SSD = filing cabinet, PSU = power station, chipset = traffic cop.", "A header is just a row of pins; a slot is a long connector for a card or module.", "Dell's board is a custom shape with a 6-pin power plug and a 5-pin button plug."],
      questions=[("Label the twelve parts on the diagram (teacher will hand out the blank map) and write one job each.", 6), ("RAM slots: how many in total, how many used, how many empty?", 1), ("Service tag:", 1), ("Which two parts are not standard on this Dell and will need adapters later?", 2)],
      exit="Which part surprised you most and why?"),
 callouts=[SAFE_ESD], parts=PARTS))

LESSONS.append(L(3, 1, 3, "Teardown level 1: out, in, and it still boots",
 ["Remove and refit the drive cage and a RAM module safely.", "Use the bag-and-tag method for screws.", "Run the power-on check and confirm the PC still POSTs."],
 ["Dell 7050 SFF", "Wrist strap", "Phillips #2", "Zip bags + marker", "Monitor, keyboard, mains lead"],
 [("POST", "Power-on self-test: the checks the PC runs before loading the operating system."), ("Reseat", "Take a part out and put it back in cleanly."), ("Bag and tag", "Each group of screws goes in its own labelled bag.")],
 dict(min=4, steps=["Strap on, unplug, press the button, open the panel.", "Teacher demonstrates the drive-cage swing-up and the RAM clips once on the big screen."]),
 dict(min=8, html="""<p>Taking a PC apart is easy. Putting it back so it works is the skill. Three habits make it reliable:</p>
<ul><li><b>One bag per part.</b> Screws from the drive cage go in a bag marked 'cage'. Never a loose pile.</li>
<li><b>Photo before you pull.</b> One phone photo of the cables before any plug comes out.</li>
<li><b>The POST check.</b> After every rebuild: plug in, power on, watch for the Dell logo and the LED going solid white. No screen = stop and look again.</li></ul>
{F0}
<p><b>Example.</b> The drive cage on the 7050 has a blue latch; it hinges up rather than lifting out. RAM clips open outward; the stick lifts straight up. Nothing in this lesson needs force.</p>""", figures=[boot_chain()]),
 dict(min=25, steps=["Photo the inside. Then unclip the drive cage latch and swing the cage up. Notice the SATA data and power plugs on the drive.",
      "Unplug the SATA data cable from the drive (press the small latch, pull straight). Plug it back in. Feel the click.",
      "Swing the cage back down until it latches.",
      "Press both clips on one RAM slot outward. Lift the stick straight up. Hold it by the edges only.",
      ("Look at the notch position. Put it back the same way: line up the notch, press both ends down evenly until both clips snap closed.", "If it needs real force, the notch is the wrong way round."),
      "Navigator check: cage latched, RAM clips closed, SATA plugged, nothing left in the case.",
      "Panel on. Plug in monitor, keyboard, mains. Power on. Watch the LED: amber blink → solid white → Dell logo.",
      "If it boots to the login screen, write 'POST OK' in the log. If not, unplug and recheck the RAM first."]),
 dict(min=5, quiz=[Q("A RAM stick will not go in without real force. What is wrong?", ["Wrong slot colour", "Notch is the wrong way round", "Clips are too tight", "The stick is too big"], 1, "The notch is off-centre so it fits one way only. Flip it."),
      Q("The power LED stays blinking amber and nothing appears on screen. This is a…", ["no-boot problem (software)", "no-POST problem (hardware)", "monitor problem only", "normal start"], 1, "No POST = the hardware did not pass its self-test. Go back inside."),
      Q("Why one bag per part?", ["It looks tidy", "Different screws have different threads and lengths", "The teacher said so", "So you can lose them together"], 1, "A long screw in the wrong hole can crack a board.")]),
 dict(steps=STD_PACK),
 dict(key_ideas=["Photo before you pull. One bag of screws per part. POST check after every rebuild.", "RAM: clips out, lift straight up; notch decides the direction; press both ends until both clips click.", "LED amber-blink → solid white → logo is a healthy start."],
      questions=[("Write the eight steps of today's teardown and rebuild in order.", 5), ("What are the three LED stages of a healthy start?", 2), ("Your PC shows no screen after a rebuild. Write the first three things you check.", 3)],
      exit="Did your PC POST first time? If not, what fixed it?"),
 callouts=[SAFE_ESD, SAFE_PWR]))

# ---------------------------------------------------------------- WEEK 2
LESSONS.append(L(4, 2, 1, "How a CPU works: fetch, decode, execute",
 ["Describe the fetch-decode-execute cycle.", "Explain cores, clock speed and cache in plain words.", "Read the specifications of the CPU in your bench PC."],
 ["Dell 7050 (booted)", "CPU-Z (Windows) or a terminal with lscpu (Linux)", "Worksheet"],
 [("Core", "One complete processing unit inside the CPU; four cores can run four jobs at once."), ("Clock speed", "How many steps per second, measured in GHz (billions)."), ("Cache", "A small, very fast memory inside the CPU."), ("Thread", "One stream of instructions."), ("TDP", "Thermal design power: how much heat (in watts) the cooler must remove.")],
 dict(steps=["Boot the PC while the teacher talks. No panel off today.", "Guess: how many instructions per second does your i5 run? Write the guess down."]),
 dict(min=14, html="""<p>A CPU does only one thing: it repeats a tiny loop, billions of times a second.</p>
<ol><li><b>Fetch</b> the next instruction from RAM.</li><li><b>Decode</b> it: what is it asking for?</li><li><b>Execute</b> it: add, compare, move, jump.</li></ol>
{F0}
<p><b>Example 1 — clock speed.</b> 3.4 GHz means 3.4 billion ticks a second. Roughly one small step per tick. A 4.0 GHz chip is not twice as fast as a 2.0 GHz one from a different generation, but inside one family, faster ticks = faster work.</p>
<p><b>Example 2 — cores.</b> Four cores are four of these loops running at the same time. A game that only uses one core will not speed up with eight cores; a video export that uses all of them will.</p>
<p><b>Example 3 — cache.</b> RAM is far away (in CPU time, a trip across town). Cache is a notepad on the desk. The CPU keeps the most-used data there so it rarely waits. More cache = fewer waits.</p>
<p>Your bench PC: <b>Intel Core i5-7500</b> — 4 cores, 4 threads, 3.4 GHz base / 3.8 GHz boost, 6 MB cache, 65 W TDP, socket LGA1151. Some units may carry an i3 or i7; check yours.</p>""", figures=[fde()]),
 dict(min=18, steps=["Windows: open CPU-Z (teacher's USB) → CPU tab. Linux: open a terminal and type <code>lscpu</code>.",
      "Write on the worksheet: model name, cores, threads, base clock, max clock, L3 cache size.",
      "Open Task Manager (Ctrl+Shift+Esc) → Performance → CPU, or <code>htop</code> on Linux. Count the core graphs.",
      "Open five browser tabs playing video at once. Watch the core graphs. Which cores are busy? Write one sentence.",
      ("Find the TDP for your model on the spec sheet. That number is the heat your cooler removes next lesson.", "65 W for the i5-7500; 35 W for 'T' models."),
      "Compare with your neighbour's bench: same CPU? If not, whose is faster and why?"]),
 dict(quiz=[Q("Which happens first in the cycle?", ["Execute", "Decode", "Fetch", "Store"], 2, "Fetch the instruction from RAM, then decode, then execute."),
      Q("A program uses one core only. Adding four more cores will…", ["double its speed", "make no difference to it", "slow it down", "crash it"], 1, "Single-threaded work cannot be split across cores."),
      Q("Cache is…", ["a bigger kind of RAM on the board", "small fast memory inside the CPU", "storage for files", "the fan controller"], 1, "Cache sits inside the CPU to avoid slow trips to RAM.")]),
 dict(steps=["Close programs, shut down properly, keyboard squared up, chairs in."]),
 dict(key_ideas=["Fetch → decode → execute, repeated billions of times a second.", "GHz = ticks per second; cores = parallel loops; cache = fast notepad inside the CPU.", "TDP (watts) is the heat the cooler must remove."],
      questions=[("Fill in your CPU: model, cores, threads, base GHz, boost GHz, cache, TDP.", 3), ("Explain the fetch-decode-execute cycle using the 'brain and desk' idea.", 3), ("A friend says 'more cores always = faster'. Give one example where that is true and one where it is false.", 3), ("Why does the CPU have cache if there is RAM?", 2)],
      exit="Instructions per second: your guess vs the real number (cores × GHz, roughly)."),
 callouts=[]))

LESSONS.append(L(5, 2, 2, "Sockets and coolers: taking the heat off the processor",
 ["Identify the LGA1151 socket, its lever and the alignment triangle.", "Remove the cooler, clean old paste safely, and inspect the CPU without touching the pins.", "Explain how thermal paste works."],
 ["Dell 7050 SFF", "Wrist strap", "Phillips #2", "Isopropyl alcohol (70%+) and lint-free wipes", "Thermal paste (one tube per bench)", "Parts tray"],
 [("LGA", "Land grid array: the pins are in the socket, the chip has flat pads."), ("Heat spreader", "The metal lid on top of the CPU."), ("Thermal paste", "A grey compound that fills gaps between CPU and cooler so heat can cross."), ("Heatsink", "The finned metal block that spreads heat into the air.")],
 dict(min=4, steps=["Strap on, unplug, press the button, panel off.", "Teacher shows a CPU removal on the demo unit under the camera. Students do not remove the CPU today; you remove the cooler."]),
 dict(min=10, html="""<p>A 65 W processor is a 65 W heater the size of a postage stamp. Without a cooler it reaches 100 °C in seconds and shuts itself down.</p>
{F0}
<p><b>Example 1 — the socket.</b> On LGA1151 the 1151 spring pins live in the socket. One bent pin can kill the board. That is why the chip is lowered straight down with the triangle matched, and the lever does the clamping, not your thumb.</p>
<p><b>Example 2 — paste.</b> Two metal surfaces look flat but are rough under a microscope. Air in those gaps is an insulator. Paste pushes the air out. A pea-sized dot in the centre is enough; the cooler's pressure spreads it.</p>
<p><b>Example 3 — too much.</b> Half a tube squeezes out the sides, onto the socket, and makes a mess that is hard to clean. More is worse, not better.</p>""", figures=[socket_cooler()]),
 dict(min=24, steps=["Photo the cooler and its fan plug. Unplug the fan (press the latch, pull up).",
      "Loosen the four cooler screws half a turn each in an X pattern, then all the way. Keep them in the 'cooler' bag.",
      ("Twist the cooler gently side to side to break the paste seal, then lift straight up.", "Do not lever it. If the CPU comes up stuck to the cooler, stop and call the teacher."),
      "Look at the CPU lid. Do not touch the socket, do not lift the lever.",
      "Put two drops of isopropyl on a wipe. Clean the CPU lid and the cooler base until the metal is bright. Dry with a fresh wipe.",
      "Read the text on the CPU lid: model and batch. Write the model on the worksheet.",
      "Navigator confirms: CPU clean, cooler base clean, nothing on the socket. Leave the cooler OFF — next lesson we re-paste and refit.",
      "Cover the open socket area with a clean sheet of paper. Panel loosely on. Label the PC 'NO COOLER — DO NOT POWER'."]),
 dict(min=4, quiz=[Q("On an LGA socket, where are the pins?", ["On the CPU", "In the socket", "On the cooler", "There are none"], 1, "Land grid array: pins in the socket, pads on the chip."),
      Q("How much paste goes on?", ["Cover the whole lid thickly", "A pea-sized dot in the centre", "None, metal touches metal", "A line down each edge"], 1, "The cooler's pressure spreads a pea-sized dot into a thin layer."),
      Q("The cooler comes up with the CPU stuck to it. You should…", ["Pull them apart quickly", "Stop and call the teacher", "Put it back and power on", "Bend the lever"], 1, "The chip must go back straight with the triangle aligned, with the lever open. Teacher supervises.")]),
 dict(steps=["Isopropyl capped and back on the shelf, wipes binned, 'no cooler' label on, screws bagged.", "Strap off last, after the panel is on."]),
 dict(key_ideas=["LGA1151: pins in the socket; triangle on the chip matches the triangle on the socket; the lever clamps it.", "Paste fills microscopic air gaps. Pea-sized dot, centre, let the cooler spread it.", "Loosen and tighten cooler screws in an X pattern, a little at a time."],
      questions=[("Label the socket diagram: lever, load plate, alignment triangle, pins.", 3), ("Why can a single bent pin stop the PC working?", 2), ("Describe cleaning old paste: what you use and what 'clean' looks like.", 2), ("CPU model printed on your lid:", 1)],
      exit="What is the X pattern for, and what could happen if you tightened one corner fully first?"),
 callouts=[SAFE_ESD, ("danger", "Isopropyl alcohol", "Flammable and irritating. Small amounts on a wipe only, cap the bottle, no mains power at the bench while it is out.")]))

LESSONS.append(L(6, 2, 3, "Thermals lab: re-paste, refit, measure the difference",
 ["Apply thermal paste and refit the cooler in the X pattern.", "Measure CPU temperature at idle and under load.", "Explain why temperatures and fan speed rise together."],
 ["Dell 7050 (cooler off from last lesson)", "Thermal paste", "Wrist strap", "HWMonitor / Core Temp (Windows) or lm-sensors (Linux)", "Stress tool: CPU-Z bench, Prime95 or <code>stress</code>"],
 [("Idle", "Doing nothing much: desktop open, no programs working."), ("Load", "Working hard: all cores busy."), ("Throttling", "The CPU slowing itself down to stay below its safe temperature (about 100 °C)."), ("PWM fan", "A fan whose speed the board controls with a 4-pin plug.")],
 dict(min=4, steps=["Strap on. Check the 'no cooler' label is yours and the socket is still clean.", "Teacher shows the pea method once on the demo unit."]),
 dict(min=6, html="""<p>Heat moves: CPU → paste → heatsink → air. The fan replaces warm air with cool. The board watches the temperature and spins the fan faster as it rises. If the cooler is loose or the paste is missing, the first link breaks and the CPU hits 100 °C and throttles.</p>
<p><b>Numbers to expect on a 7050:</b> idle 30–45 °C; full load 60–80 °C with a healthy cooler. Over 90 °C under load means something is wrong.</p>
<p><b>Example.</b> Two identical PCs: one re-pasted properly, one with the cooler screws left loose. Under load the first sits at 70 °C; the second races to 98 °C and the clock drops from 3.6 GHz to 2.0 GHz. Same chip, half the speed.</p>""", figures=[socket_cooler()]),
 dict(min=28, steps=["Pea-sized dot of paste in the centre of the CPU lid. Do not spread it.",
      "Lower the cooler straight down. Start all four screws by hand two turns each.",
      "Tighten in an X pattern: a few turns on one, then the diagonal, then the other two. Repeat until snug (not strained).",
      "Plug the fan back in. The plug is keyed; it fits one way.",
      "Navigator check: four screws, fan plugged, nothing left inside. Panel on. Plug in. Power on. POST check.",
      "Open the temperature tool. Write the idle temperature after 2 minutes.",
      "Start the stress test for 3 minutes. Write the temperature every minute and the fan speed (RPM) if shown.",
      "Stop the test. Watch the temperature fall. Write how long it takes to get back near idle.",
      "Compare with another bench. Any PC over 90 °C under load goes on the 'check cooler' list."]),
 dict(min=4, quiz=[Q("Under load the CPU shows 99 °C and the clock drops. This is…", ["normal", "throttling: the cooler is not doing its job", "a RAM problem", "a virus"], 1, "The CPU protects itself by slowing down. Check paste and cooler seating."),
      Q("Why tighten in an X pattern?", ["It is faster", "Even pressure so the paste spreads evenly and the chip is not tilted", "To avoid losing screws", "No reason"], 1, "Uneven pressure leaves a wedge-shaped gap on one side."),
      Q("A 4-pin fan plug lets the board…", ["turn the fan off only", "control fan speed (PWM)", "charge the battery", "nothing extra"], 1, "The fourth wire carries the speed signal.")]),
 dict(steps=STD_PACK),
 dict(key_ideas=["Heat path: CPU → paste → heatsink → air. Break any link and the CPU throttles near 100 °C.", "Pea-sized dot, cooler straight down, X pattern, fan plugged.", "Healthy 7050: idle 30–45 °C, load 60–80 °C."],
      questions=[("Record: idle temp ___, load temp at 1 min ___, 2 min ___, 3 min ___, fan RPM ___.", 2), ("Sketch the heat path from CPU to room air and label each stage.", 3), ("Explain what throttling is and why the CPU does it.", 2), ("Two PCs: 70 °C and 98 °C under load. List three possible causes for the hot one.", 3)],
      exit="Your load temperature compared with the class range. Healthy, borderline or needs work?"),
 callouts=[SAFE_ESD, SAFE_PWR]))

# ---------------------------------------------------------------- WEEK 3
LESSONS.append(L(7, 3, 1, "Memory: what RAM is, what the numbers mean",
 ["Explain why RAM is fast but forgets.", "Read a DDR4 label: capacity, speed, DIMM type.", "Describe single vs dual channel."],
 ["A DDR4 DIMM per pair (handled on the mat)", "A DDR3 or SO-DIMM sample for comparison", "Wrist strap", "Worksheet"],
 [("DIMM", "Dual in-line memory module: the stick that goes in a desktop."), ("SO-DIMM", "The short laptop version. Does not fit a desktop slot."), ("DDR4", "The generation. DDR3, DDR4 and DDR5 all have different notches and do not mix."), ("MT/s", "Mega-transfers per second: the speed on the label, e.g. 2400."), ("Dual channel", "Two sticks working as a pair so data moves on two lanes at once.")],
 dict(steps=["Strap on. Each pair gets one DDR4 stick on the mat and one 'odd one out' sample.", "Look at both. Without touching the gold edge, list every difference you can see."]),
 dict(min=14, html="""<p>RAM is the CPU's desk. It holds whatever is open right now. It is about 100 times faster than an SSD, but it only works while powered: cut the power and the desk is wiped. That is why you 'save' to the SSD.</p>
{F0}
<p><b>Reading a label.</b> <code>8GB 1Rx8 PC4-2400T-UA</code> means 8 GB capacity, single rank, DDR4, 2400 MT/s, unbuffered (desktop). Simpler labels say <code>DDR4-2400 8GB UDIMM</code>.</p>
<p><b>Example 1 — capacity.</b> 8 GB runs Windows and a browser. 16 GB is comfortable for games and editing. 32 GB is for heavy work. More than you use is wasted money.</p>
<p><b>Example 2 — speed.</b> The i5-7500 runs memory at 2400 MT/s. Put in 3200 sticks and they slow down to 2400. Nothing breaks; you just paid for speed you cannot use.</p>
<p><b>Example 3 — mixing.</b> Two different 8 GB sticks usually work, but at the slower speed. A DDR3 stick will not even go in: the notch is in a different place.</p>""", figures=[dimm()]),
 dict(min=16, steps=["Holding the stick by its edges, read the label. Write capacity, type (DDR3/DDR4), speed and whether it is a DIMM or SO-DIMM.",
      "Count the chips on it. Are there chips on both sides (dual rank) or one (single rank)?",
      "Compare notches: your DDR4 stick vs the sample. Line them up on the mat. Different generation = different notch position.",
      "Boot your bench PC. Windows: Task Manager → Performance → Memory. Linux: <code>free -h</code> and <code>sudo dmidecode -t memory</code>. Write total GB, speed and slots used.",
      "From last week's slot count: how much more RAM could this PC take? (Max 4 × 16 GB.)",
      "Write the upgrade you would buy for this PC and why (capacity, speed, number of sticks)."]),
 dict(quiz=[Q("You install DDR4-3200 in the 7050. It will run at…", ["3200", "2400 (the CPU's limit)", "1600", "It will not boot"], 1, "The memory controller in the i5-7500 tops out at 2400."),
      Q("Why can't a DDR3 stick go into a DDR4 slot?", ["It is too long", "The notch is in a different place", "It is the wrong colour", "It needs a screw"], 1, "Each generation keys the notch differently on purpose."),
      Q("Dual channel needs…", ["one big stick", "two sticks in a matched pair of slots", "four sticks of different sizes", "a special cable"], 1, "Matched pair, paired slots, two lanes of data.")]),
 dict(steps=["Sticks back in their anti-static bags, flat on the mat, teacher collects.", "Shut down."]),
 dict(key_ideas=["RAM is fast, temporary working memory; storage is slower and permanent.", "Label: capacity (GB), generation (DDR4), speed (MT/s), DIMM vs SO-DIMM.", "This PC: DDR4-2400, 4 slots, 64 GB max; dual channel needs a matched pair in paired slots."],
      questions=[("Your stick's label says:", 1), ("Decode it: capacity ___ generation ___ speed ___ type ___", 2), ("Your PC right now: total RAM ___ speed ___ slots used ___ of 4", 1), ("Explain dual channel using the 'two lanes' idea.", 2), ("Which upgrade would you buy for this PC and why?", 3)],
      exit="One thing RAM does and one thing it cannot do."),
 callouts=[SAFE_ESD]))

LESSONS.append(L(8, 3, 2, "Install RAM: pairs, slots and the BIOS check",
 ["Install two DIMMs in the correct paired slots.", "Confirm the capacity and 'dual' channel mode in the BIOS.", "Reseat a stick that is not detected."],
 ["Dell 7050 SFF", "RAM upgrade kit (2 matched sticks per bench, rotate if short)", "Wrist strap", "Monitor/keyboard"],
 [("BIOS / UEFI", "The firmware menu you reach with F2 at start-up."), ("Paired slots", "The two slots that form one channel; on Dell boards they share a clip colour."), ("Detected", "The board can see the stick during POST.")],
 dict(min=4, steps=["Strap on, unplug, press the button, panel off.", "Navigator reads the kit label: it must say DDR4 and a speed of 2400 or higher."]),
 dict(min=8, html="""<p>Installing RAM has three parts: the right slots, a firm press, and a check. Dell colour-codes the clips. A matched pair goes in the two slots whose clips share a colour. Then the BIOS tells you whether it is running in dual-channel mode.</p>
{F0}
<p><b>Example 1.</b> Both new sticks in slots 1 and 2 (different colours): the PC boots, shows 16 GB, but 'Single' channel. Half the bandwidth.</p>
<p><b>Example 2.</b> One stick only half-clicked: the PC shows 8 GB instead of 16, or does not POST at all. The fix is always reseat first.</p>
<p><b>Example 3.</b> Keeping the old 4 GB stick plus two new 8 GB sticks: it works (20 GB total), but the odd stick may force single-channel. Simpler is better: a matched pair.</p>""", figures=[dimm()]),
 dict(min=24, steps=["Remove the existing sticks (clips out, lift straight up). Lay them on the mat, label side up.",
      "Identify the two same-colour slots. Open their clips.",
      ("Line up the notch of stick 1. Press firmly on both ends at once until both clips snap. Repeat for stick 2.", "It takes a definite push. If one clip did not close, the stick is not in."),
      "Navigator check: both clips closed on both sticks, old sticks safely on the mat, nothing in the case.",
      "Panel on, plug in, power on and tap <kbd>F2</kbd> for BIOS Setup.",
      "Find System Information → Memory. Write: installed GB, speed, channel mode (should read 'Dual').",
      "Exit BIOS, boot, confirm the OS shows the same total.",
      "Fault drill: power off, unplug, open the panel, pull ONE stick half out, power on. What happens? Write it down. Then reseat it properly and confirm POST."]),
 dict(min=4, quiz=[Q("Where does a matched pair go on this board?", ["Any two slots", "The two slots whose clips share a colour", "Slots 1 and 2 always", "Only slot 4"], 1, "Same-colour clips = same channel pair on Dell boards."),
      Q("BIOS shows 16 GB but 'Single' channel. Most likely…", ["the sticks are faulty", "the sticks are in the wrong pair of slots", "the CPU is too slow", "the cable is loose"], 1, "Right amount detected, wrong slots."),
      Q("The PC will not POST after a RAM change. First thing to do:", ["Buy new RAM", "Reseat both sticks", "Update Windows", "Replace the PSU"], 1, "Reseat first. It fixes most RAM 'faults'.")]),
 dict(steps=["Old sticks into labelled anti-static bags, teacher collects.", "Pack down as usual; log 'RAM upgraded to __ GB'."]),
 dict(key_ideas=["Matched pair → same-colour slots → press both ends until both clips click.", "F2 at start-up opens the BIOS. Memory page shows GB, speed and channel mode.", "Not detected or no POST? Reseat first."],
      questions=[("Before: ___ GB in ___ slots.  After: ___ GB, speed ___, channel mode ___.", 2), ("Describe exactly how you know a stick is seated.", 2), ("Fault drill result: what did the PC do with a half-seated stick?", 2), ("Why is a matched pair better than three mismatched sticks?", 2)],
      exit="Did your BIOS say 'Dual'? If not, what did you change?"),
 callouts=[SAFE_ESD, SAFE_PWR]))

LESSONS.append(L(9, 3, 3, "Memory faults: testing RAM and reading the signs",
 ["Run a memory test and read its result.", "Recognise the symptoms of bad or unseated RAM.", "Use the Dell LED patterns for memory problems."],
 ["Dell 7050", "MemTest86 bootable USB (one per bench) or Windows Memory Diagnostic", "Wrist strap"],
 [("MemTest86", "A program that boots from USB and writes patterns to every byte of RAM to find errors."), ("Blue screen (BSOD)", "Windows crash screen; random ones often point to RAM."), ("Diagnostic LED", "The Dell power button blinks a two-number amber pattern to say what failed.")],
 dict(steps=["Boot the PC. While it starts, teacher lists the symptoms of bad RAM on the board: random crashes, freezes, files that corrupt, no POST.", "Strap on if you will open the case later."]),
 dict(min=10, html="""<p>RAM faults are sneaky. A stick can be mostly fine but have a few bad cells. The PC works until a program lands on those cells, then crashes for 'no reason'. A memory test writes patterns to every cell and reads them back, over and over.</p>
{F0}
<p><b>Example 1.</b> A laptop blue-screens once a day with a different error each time. MemTest finds 14 errors in pass 1. New RAM, problem gone.</p>
<p><b>Example 2.</b> A desktop will not POST and the Dell light blinks 2, then 3 (or 3, then 3). Nothing to test yet: that pattern means the board cannot see any working memory. Reseat, then try one stick at a time.</p>
<p><b>Example 3.</b> Memory test passes but the PC still crashes. The fault is somewhere else: overheating, storage, drivers. A pass tells you what it is <i>not</i>.</p>""", figures=[boot_chain()]),
 dict(min=22, steps=["Plug in the test USB. Power on and tap <kbd>F12</kbd> for the one-time boot menu. Choose the USB stick.",
      "Let the test run. Write the total RAM it sees and the speed.",
      "After 5–8 minutes (one partial pass is enough today), write the error count. Zero is a pass.",
      "Power off. Open the case (strap on). Swap the two sticks' positions. Run the test again for 3 minutes. Still zero? Good: the slots are fine too.",
      "Teacher's 'mystery stick' round: one bench gets a known-bad stick. Everyone predicts the result, then that bench tests it.",
      "Close up, remove the USB, boot normally. Confirm the OS still sees the full amount."]),
 dict(quiz=[Q("MemTest shows 0 errors but the PC still crashes. The RAM is…", ["definitely faulty", "probably fine; look elsewhere", "too fast", "too slow"], 1, "A pass rules RAM out as the likely cause."),
      Q("Dell LED blinks 2 then 7 at start-up. Dell's table says…", ["coin cell", "memory failure", "video", "CPU"], 1, "2,7 = memory failures on the 2012–2020 series. Reseat, then swap."),
      Q("Best first move for a suspected RAM fault:", ["Reinstall Windows", "Reseat the sticks, then test one at a time", "Replace the PSU", "Ignore it"], 1, "Cheap, fast, and fixes most of them.")]),
 dict(steps=STD_PACK),
 dict(key_ideas=["Symptoms of bad RAM: random crashes, freezes, corruption, no POST.", "MemTest86 from USB (F12 boot menu). Zero errors = pass. Swap sticks between slots to test the slots too.", "Dell LED 2,3 / 3,3 = no memory seen; 2,7 / 3,5 / 3,7 = memory failure or wrong config. Reseat first."],
      questions=[("MemTest result: RAM seen ___, speed ___, errors ___ after ___ minutes.", 1), ("List four symptoms that make you suspect RAM.", 2), ("Write the test order you would use for a PC with one stick in each of two slots that keeps crashing.", 4), ("What does a passing memory test tell you, and what does it not tell you?", 2)],
      exit="What pattern did the mystery stick produce, and what fixed it?"),
 callouts=[SAFE_ESD]))

# ---------------------------------------------------------------- WEEK 4
LESSONS.append(L(10, 4, 1, "Storage: hard drives, SATA SSDs and NVMe",
 ["Compare HDD, SATA SSD and NVMe on speed, moving parts and price.", "Identify M.2 keying and the 2280 size.", "Explain why the OS belongs on the fastest drive."],
 ["One HDD (opened demo unit), one 2.5-inch SSD, one M.2 NVMe per bench", "Wrist strap", "Ruler"],
 [("HDD", "Hard disk drive: spinning magnetic platters and a moving arm."), ("SSD", "Solid state drive: flash memory chips, no moving parts."), ("NVMe", "The fast protocol SSDs use over PCIe lanes."), ("M.2", "The small stick-shaped slot; 2280 = 22 mm wide, 80 mm long."), ("TBW", "Terabytes written: how much an SSD can write in its life.")],
 dict(steps=["Strap on. Pass the three drives around the bench on the mat.", "Guess the order from slowest to fastest. Write it down before we measure."]),
 dict(min=14, html="""<p>Three generations of storage are still sold today. A <b>hard drive</b> stores bits as magnetism on spinning discs; the arm has to physically move to find data. A <b>SATA SSD</b> stores bits in flash chips with no motion, but talks over the old SATA cable (about 550 MB/s max). An <b>NVMe SSD</b> uses the same flash but plugs straight into PCIe lanes, so it can move several gigabytes a second.</p>
{F0}
<p><b>Example 1 — boot time.</b> Windows on HDD: 60–90 s. On SATA SSD: 15 s. On NVMe: 10 s. The jump from HDD to any SSD is the one you feel most.</p>
<p><b>Example 2 — capacity per dollar.</b> HDDs are still the cheapest per terabyte, so big video archives often stay on HDD.</p>
<p><b>Example 3 — keying.</b> An M.2 slot with an 'M key' notch takes NVMe (and on this board, SATA M.2 too). A 'B+M' key SATA-only stick fits an M-key slot physically but may not work in an NVMe-only slot. Read the spec, not just the shape.</p>""", figures=[storage()]),
 dict(min=16, steps=["Look inside the opened demo HDD: find the platter, the arm and the read head. Spin the platter gently with a gloved finger. Never do this to a working drive.",
      "Measure the M.2 stick: width and length in mm. Write the size code (2280, 2242…).",
      "Find the notch on the M.2 stick. One notch near the edge = M key. Two notches = B+M.",
      "Read the label: capacity, NVMe or SATA, PCIe generation if shown.",
      "On the booted PC: Windows → <code>Task Manager → Performance → Disk</code> or Linux → <code>lsblk -d -o NAME,MODEL,SIZE,ROTA</code>. ROTA 1 = spinning. Write what your PC has now.",
      "Rank the three drives slowest → fastest with the figure's numbers. Compare with your guess."]),
 dict(quiz=[Q("Which drive has moving parts?", ["HDD", "SATA SSD", "NVMe", "All of them"], 0, "Only the hard drive spins and seeks."),
      Q("The main speed limit of a SATA SSD is…", ["the flash chips", "the SATA cable/interface (~550 MB/s)", "the fan", "the OS"], 1, "SATA was designed for spinning disks."),
      Q("2280 means…", ["22 GB, 80 ms", "22 mm wide, 80 mm long", "2280 MB/s", "year 2280"], 1, "Width then length in millimetres.")]),
 dict(steps=["Drives back in anti-static bags; demo HDD to the teacher.", "Shut down."]),
 dict(key_ideas=["HDD: magnetic, spinning, cheap per TB, slow. SATA SSD: flash, ~550 MB/s. NVMe: flash over PCIe, 3000+ MB/s.", "M.2 2280 = 22 × 80 mm; M key = NVMe; this board's slot takes NVMe or SATA M.2.", "Put the operating system on the fastest drive; keep big archives on cheap, big drives."],
      questions=[("Complete the table: drive / moving parts? / typical read MB/s / best use.", 4), ("Your PC's current drive: model ___ size ___ spinning or solid state?", 1), ("Why is HDD → SSD the upgrade people notice most?", 2), ("What could go wrong if you buy an M.2 SATA stick for a board that only supports NVMe in that slot?", 2)],
      exit="Which upgrade would you give a slow family PC first, RAM or SSD? Why?"),
 callouts=[SAFE_ESD]))

LESSONS.append(L(11, 4, 2, "Install an NVMe SSD and cable a SATA drive",
 ["Fit an M.2 NVMe SSD into the 2280 slot with the retaining screw.", "Connect SATA data and power to a 2.5-inch drive.", "Confirm both drives appear in the BIOS."],
 ["Dell 7050 SFF", "NVMe SSD per bench (rotate kits if needed)", "2.5-inch SATA SSD + SATA cable + Dell drive caddy", "Tiny Phillips (#1 or #0) for the M.2 screw", "Wrist strap", "Magnetic parts tray"],
 [("Retaining screw", "The single tiny screw holding down the M.2 stick."), ("Standoff", "The raised threaded post the M.2 screw goes into."), ("SATA data cable", "The thin 7-pin L-shaped cable; data only."), ("SATA power", "The wider 15-pin flat plug from the PSU.")],
 dict(min=4, steps=["Strap on, unplug, press the button, panel off.", "Check the M.2 screw is in the standoff on your board before you start. If it is missing, ask for one now."]),
 dict(min=8, html="""<p>Two installs today, both low-force. The M.2 stick slides in at an angle and is pinned flat with one screw. The SATA drive sits in a caddy and gets two cables: thin L-shaped data to the board, wider flat power from the PSU.</p>
{F0}
<p><b>Example 1.</b> Pressing the M.2 flat before it is fully in the slot: the gold fingers are only half in, the screw goes in, and the drive is never detected. Push in first, then press down.</p>
<p><b>Example 2.</b> The M.2 screw is tiny and the tray is not magnetic; it rolls under the PSU. Use the magnetic tray and the small driver, nothing else.</p>
<p><b>Example 3.</b> SATA data plugged in, power forgotten: the BIOS sees nothing. Two cables, always.</p>""", figures=[storage()]),
 dict(min=24, steps=["Unscrew the M.2 retaining screw and put it in the magnetic tray.",
      ("Hold the NVMe stick by the edges. Line up the notch. Slide it into the slot at about 30° until the gold fingers disappear.", "It should go in smoothly. Do not force it."),
      "Press the far end down onto the standoff. Fit the screw: snug, not tight.",
      "Fit the 2.5-inch SSD into the Dell caddy. Swing up the drive cage and clip the caddy in.",
      "Plug SATA data: L-shape matches the port; press until it clicks. Other end to a SATA port on the board (note which number).",
      "Plug SATA power from the PSU lead: L-shape, firm push.",
      "Navigator check: M.2 screw in, both SATA cables seated, cage latched. Panel on, plug in, power on, <kbd>F2</kbd>.",
      "BIOS → System Information → Drives (or Boot/Storage). Write which drives appear and on which port. Both there? Done. One missing? Power off and reseat it."]),
 dict(min=4, quiz=[Q("The M.2 drive is screwed down but not detected. Most likely…", ["the screw is too tight", "it was pressed flat before it was fully in the slot", "the OS is missing", "the SATA cable is loose"], 1, "Half-inserted fingers = no contact. Remove, re-insert at 30°, then press down."),
      Q("A SATA drive needs…", ["one cable: data", "two cables: data and power", "three cables", "no cables, it is M.2"], 1, "Data from the board, power from the PSU."),
      Q("The L-shaped plug will not go in. You should…", ["push harder", "flip it: the L matches the port one way only", "use a different drive", "bend the pins"], 1, "The L-shape keys the orientation.")]),
 dict(steps=STD_PACK),
 dict(key_ideas=["M.2: notch aligned, in at ~30°, fingers fully in, press flat, one screw snug.", "SATA drive: caddy → data (L-shaped, to board) → power (flat, from PSU).", "F2 → BIOS → drives list is the proof. Missing drive = reseat."],
      questions=[("Drives in the BIOS after the install: ___ (port ___), ___ (port ___).", 2), ("Describe the M.2 install in four steps.", 4), ("Why does the BIOS, not Windows, tell you the install worked?", 2), ("Which single mistake makes an M.2 'dead on arrival' most often?", 1)],
      exit="How many cables does each drive type need? M.2 ___ SATA ___"),
 callouts=[SAFE_ESD, SAFE_PWR]))

LESSONS.append(L(12, 4, 3, "Disks in the operating system: partition, format, benchmark",
 ["Initialise a new disk with GPT and create a formatted partition.", "Explain partitions, file systems and what formatting really does.", "Benchmark the old drive against the new SSD."],
 ["Dell 7050 with the new drives installed", "Windows (Disk Management, CrystalDiskMark) or Linux Mint (Disks / GParted)", "Worksheet"],
 [("Partition", "A section of a disk the OS treats as a separate drive."), ("GPT / MBR", "Two ways to write the partition table; GPT is the modern one used with UEFI."), ("File system", "The index that turns raw space into folders and files: NTFS, exFAT, ext4."), ("Format", "Writing a new empty file system onto a partition.")],
 dict(steps=["Boot the PC. New drives are blank: they do not show as a letter yet. That is expected.", "Teacher shows the partition figure on screen."]),
 dict(min=10, html="""<p>A blank drive is like a notebook with no page numbers or contents page. <b>Initialising</b> chooses the table style (GPT). <b>Partitioning</b> draws the sections. <b>Formatting</b> writes the empty contents page (the file system). Only then can the OS put files on it.</p>
{F0}
<p><b>Example 1.</b> A 1 TB drive split into OS (200 GB) and Data (800 GB). Reinstalling Windows wipes the OS partition and leaves Data alone.</p>
<p><b>Example 2.</b> A USB stick formatted exFAT works on Windows, Mac and Linux. NTFS is best for Windows system drives; ext4 for Linux.</p>
<p><b>Example 3.</b> 'Quick format' takes seconds because it only rewrites the contents page. The old files are still physically there until overwritten, which is why recovery tools exist and why you wipe a drive properly before giving a PC away.</p>""", figures=[partition()]),
 dict(min=22, steps=["Windows: right-click Start → Disk Management. Linux: Menu → Disks. Find the new drive by its size.",
      "Windows: if asked, Initialize Disk → GPT. Linux: Format disk → GPT.",
      "Create one partition using all the space. Windows: New Simple Volume → NTFS, label it DATA. Linux: + → ext4, name DATA.",
      "Check it appears in File Explorer / Files. Copy a folder of photos onto it as a test.",
      "Benchmark the OLD drive: Windows → CrystalDiskMark (1 GB, 1 pass). Linux → Disks → ⋮ → Benchmark (read-only). Write sequential read and write MB/s.",
      "Benchmark the NEW drive the same way. Write the numbers.",
      "Calculate: how many times faster is the new drive for sequential read?",
      "Do the same for the SATA SSD if your bench has one. Rank all three."]),
 dict(quiz=[Q("GPT is…", ["a file system", "a modern partition table used with UEFI", "a type of cable", "a benchmark"], 1, "GPT describes where partitions are; NTFS/ext4 live inside a partition."),
      Q("After a quick format, the old files are…", ["gone forever", "still physically on the disk until overwritten", "moved to the cloud", "compressed"], 1, "Only the index was rewritten."),
      Q("Best file system for a Windows system drive:", ["exFAT", "ext4", "NTFS", "FAT16"], 2, "NTFS supports permissions, large files and journaling.")]),
 dict(steps=["Delete the test photos, close tools, shut down."]),
 dict(key_ideas=["Initialise (GPT) → partition → format (file system) → the drive gets a letter / mount point.", "NTFS for Windows, ext4 for Linux, exFAT for sticks shared between both.", "Formatting rewrites the index, not the data; wipe properly before giving a drive away."],
      questions=[("Benchmark: old drive read ___ write ___; new NVMe read ___ write ___; SATA SSD read ___ write ___.", 2), ("New drive is ___ times faster for sequential read (show working).", 2), ("Explain initialise, partition and format using the notebook idea.", 3), ("Why can a 'deleted' file sometimes be recovered?", 2)],
      exit="Which file system did you choose and why?"),
 callouts=[]))

# ---------------------------------------------------------------- WEEK 5
LESSONS.append(L(13, 5, 1, "The motherboard map: chipset, slots, headers and form factors",
 ["Trace how the CPU, chipset and slots connect.", "Name the standard board sizes and explain why Dell's is not one of them.", "Find every header on the 7050 board."],
 ["Dell 7050 SFF (panel off)", "Wrist strap", "Torch", "Ruler or tape measure", "Printed blank board map"],
 [("Chipset", "Intel Q270 here: links the CPU to USB, SATA, network and extra PCIe lanes."), ("PCIe lane", "One two-way data path; x16 = 16 lanes."), ("ATX / micro-ATX / mini-ITX", "Standard board sizes: 305×244, 244×244, 170×170 mm."), ("I/O shield", "The metal plate around the rear ports on a standard case.")],
 dict(steps=["Strap on, unplug, press the button, panel off. Lay the blank map beside the PC.", "Teacher: 'Everything fast talks to the CPU directly; everything else goes through the chipset.'"]),
 dict(min=14, html="""<p>Two chips run the board. The <b>CPU</b> talks directly to RAM and to the x16 graphics slot, because those need the most speed. The <b>chipset</b> (under the small heatsink) handles the rest: USB, SATA, the network port, the M.2 slot and the x4 slot. Between CPU and chipset runs a fast link called DMI.</p>
{F0}
<p><b>Example 1 — lanes.</b> A graphics card in the x16 slot gets 16 lanes straight to the CPU. The NVMe drive gets 4 lanes via the chipset. Both are PCIe; the difference is width.</p>
<p><b>Example 2 — form factors.</b> Standard sizes mean any ATX board fits any ATX case: same screw holes, same I/O cutout, same slot positions. Dell drew its own shape so the board only fits a Dell case. Cheaper for Dell; harder for us.</p>
<p><b>Example 3 — headers.</b> A header is a row of pins. The front-panel header takes the power button; the fan header takes a fan; a USB header takes the front USB cable. On this Dell, the front USB is soldered on, so there is no USB header to find.</p>
{F1}""", figures=[board_shapes(), anatomy(["chipset", "pcie16", "pcie4", "m2", "fpanel"])]),
 dict(min=16, steps=["Measure the board: longest edge and widest edge in mm. Compare with the ATX/mATX/ITX sizes in the Words list.",
      "Count and mark every mounting hole on your blank map. Measure between two holes and write the distance.",
      "Find and label on the map: chipset heatsink, x16 slot, x4 slot, M.2, SATA ports, 6-pin power, 4-pin CPU power, front-panel plug, fan header(s), coin cell.",
      "Trace with your finger: CPU → x16 slot. CPU → RAM. Chipset → SATA. Say which is a 'direct' link and which goes through the chipset.",
      "Write one upgrade that would need the x4 slot (hint: a second NVMe adapter or a 2.5 Gb network card).",
      "Panel on (no changes made)."]),
 dict(quiz=[Q("Which two parts talk to the CPU directly?", ["USB and SATA", "RAM and the x16 slot", "Network and audio", "Coin cell and fan"], 1, "Speed-critical parts get direct lanes."),
      Q("A micro-ATX board measures…", ["305 × 244 mm", "244 × 244 mm", "170 × 170 mm", "22 × 80 mm"], 1, "mATX is square-ish at 244 mm; ATX is longer; ITX is tiny."),
      Q("Why does the Dell board not fit a normal case?", ["It is too thick", "Hole pattern, port positions and power plug are all custom", "It has no chipset", "It is made of plastic"], 1, "Proprietary design.")]),
 dict(steps=STD_PACK),
 dict(key_ideas=["CPU ↔ RAM and x16 directly; everything else via the chipset over DMI.", "Standard sizes (ATX 305×244, mATX 244×244, ITX 170×170) share holes and I/O cutouts; Dell's does not.", "Headers are pin rows: front panel, fans, USB. On this Dell the front USB is soldered on."],
      questions=[("Board measurements: ___ × ___ mm. Closest standard size: ___. Does it match exactly?", 2), ("Mounting holes counted: ___. Distance between two holes you measured: ___ mm.", 1), ("Draw the CPU–chipset diagram and attach: RAM, x16, x4, M.2, SATA, USB.", 4), ("Explain 'lanes' using a road picture.", 2)],
      exit="Name one thing the chipset handles and one thing the CPU handles directly."),
 callouts=[SAFE_ESD], parts=PARTS))

LESSONS.append(L(14, 5, 2, "Firmware: BIOS/UEFI, POST and the boot order",
 ["Explain what firmware does before the OS starts.", "Navigate the Dell BIOS: F2 setup, F12 boot menu, boot order, Secure Boot, SATA mode.", "Swap the coin cell and explain what is lost."],
 ["Dell 7050 (booting)", "Keyboard", "Wrist strap", "A spare CR2032"],
 [("Firmware", "Software stored on a chip on the board; runs before any disk is read."), ("UEFI", "The modern firmware standard; BIOS is the old name people still use."), ("Boot order", "The list of devices the firmware tries, in order, to find an OS."), ("Secure Boot", "A UEFI check that only signed bootloaders run."), ("CMOS / NVRAM", "Where settings and the clock are kept; the coin cell powers the clock.")],
 dict(steps=["Power on and tap <kbd>F2</kbd> repeatedly until the Dell setup screen appears. Do not change anything yet.", "Teacher runs through the boot chain figure on screen."]),
 dict(min=12, html="""<p>When you press the button, there is no Windows yet. A small program on a chip (the firmware) wakes the CPU, counts the RAM, finds the graphics output, checks the keyboard and then looks down its <b>boot order</b> for a drive or USB stick that contains an operating system. That whole process is the <b>POST</b>. Only after that does the OS load.</p>
{F0}
<p><b>Example 1.</b> You plug a MemTest USB in and nothing happens. The boot order still says 'SSD first'. Use <kbd>F12</kbd> for a one-time choice, or move USB up in the order.</p>
<p><b>Example 2.</b> The clock resets to 2017 every start and a message says 'Time-of-day not set'. The coin cell is flat. Replace it, set the clock, done.</p>
<p><b>Example 3.</b> A Linux USB will not boot with Secure Boot on because its bootloader is not signed with a key the firmware trusts. Turn Secure Boot off for the install, or use a distribution that is signed.</p>""", figures=[boot_chain()]),
 dict(min=20, steps=["In Setup, find and write down: BIOS version, service tag, boot mode (UEFI or Legacy), Secure Boot state, SATA operation mode (AHCI or RAID).",
      "Find Boot Sequence. Write the current order. Do not save changes.",
      "Exit without saving. Power on again and tap <kbd>F12</kbd>. Note the one-time boot menu lists each drive and USB.",
      "Power off, unplug, press the button, strap on, panel off.",
      ("Use a plastic spudger to release the coin cell clip and lift the cell out. Note which side faces up (+ up).", "Count to 30. You have just cleared the settings."),
      "Fit the spare cell + side up. Panel on, power on. Expect a 'time/date' warning: press F2, set the clock, save.",
      "Confirm the boot order you wrote earlier is back to default. Compare with your notes."]),
 dict(quiz=[Q("The firmware's job is to…", ["run Windows", "test the hardware and find something to boot", "draw the desktop", "store your files"], 1, "POST then boot order."),
      Q("F12 at start-up gives you…", ["a one-time boot menu", "the desktop", "a factory reset", "nothing"], 0, "F2 = settings, F12 = pick a boot device this once."),
      Q("Removing the coin cell for 30 seconds…", ["wipes the SSD", "resets firmware settings and the clock", "upgrades the BIOS", "kills the RAM"], 1, "That is also the classic 'clear CMOS' fix for a bad setting.")]),
 dict(steps=STD_PACK),
 dict(key_ideas=["Firmware (UEFI/BIOS) runs first: POST, then boot order, then hands over to the OS.", "F2 = setup, F12 = one-time boot menu on Dell.", "Coin cell keeps the clock and settings; pulling it resets them (clear CMOS)."],
      questions=[("BIOS version ___ boot mode ___ Secure Boot ___ SATA mode ___ boot order 1. ___ 2. ___ 3. ___", 2), ("Explain POST in your own words.", 2), ("Why would you turn Secure Boot off, and why would you turn it back on afterwards?", 2), ("What happened after the coin cell was out for 30 seconds?", 2)],
      exit="One situation where F12 is the right key, and one where F2 is."),
 callouts=[SAFE_ESD, SAFE_PWR]))

LESSONS.append(L(15, 5, 3, "Front panel and the Dell problem: buttons, LEDs and adapters",
 ["Read a standard front-panel header pinout.", "Explain why the Dell 5-pin plug needs an adapter or the original button module.", "Plan the front-panel wiring for the Week 9 transplant."],
 ["Dell 7050 SFF (panel off)", "A standard case front-panel cable set (sample)", "Dell 5-pin front-panel adapter (sample) or the Dell button module", "Wrist strap", "Torch"],
 [("Front-panel header", "The pin block for power button, reset, power LED, drive LED."), ("Polarity", "Which way round + and − go; matters for LEDs, not switches."), ("Momentary switch", "A button that only connects while pressed; the board does the rest.")],
 dict(min=4, steps=["Strap on, unplug, press the button, panel off.", "Teacher holds up a standard case's front-panel cable bundle: PWR SW, RESET SW, PWR LED, HDD LED."]),
 dict(min=12, html="""<p>A power button is just a momentary switch: press it and two pins touch for a moment. The board sees that and starts the PSU. Standard boards put those pins in a 2×5 block. Dell runs the button, LED and front USB through its own plugs instead.</p>
{F0}
<p><b>Example 1.</b> A standard case: the 'PWR SW' two-pin plug goes on the PWR SW pins, either way round. The 'PWR LED' plug must go + to +, or the light never comes on (nothing breaks, it just stays dark).</p>
<p><b>Example 2.</b> Our transplant: the open frame comes with a standard two-pin switch. The Dell board wants its 5-pin plug. Either we use a Dell-to-standard adapter, or we unscrew Dell's own button module from the SFF case and run it on its original cable.</p>
<p><b>Example 3.</b> The 'screwdriver start': with no button at all, a tech briefly touches the two PWR SW pins with a screwdriver tip. It works because a switch is just a short. We will not need it, but you should know what it means.</p>""", figures=[fpanel()]),
 dict(min=20, steps=["Follow the cable from the Dell power button: where does its plug land on the board? Photo it. Count the pins.",
      "Unplug it (note the key) and plug it back in. Feel the single orientation.",
      "On the sample standard header, place the PWR SW, PWR LED and HDD LED plugs correctly using the diagram. Navigator checks polarity on the LEDs.",
      "Examine the adapter (or Dell button module). Match each wire from the Dell side to the standard side. Draw it.",
      "Find the Dell button module in the case front: how is it held in? Could it be moved to the open frame on its cable? Write yes/no and why.",
      "Fill in the 'front panel' line of the transplant parts list: adapter or original module."]),
 dict(min=4, quiz=[Q("A power switch plug is connected backwards. Result:", ["The PC will not turn on", "Works fine: switches have no polarity", "The LED breaks", "The PSU is damaged"], 1, "A switch just connects two pins."),
      Q("The power LED stays dark after a build. Likely cause:", ["Dead PSU", "LED plug reversed", "No RAM", "Wrong case"], 1, "LEDs only pass current one way."),
      Q("Why does the Dell board need special treatment for the button?", ["It has no button", "It uses a 5-pin plug instead of the standard 2×5 header", "It needs 12 V", "It uses a wireless button"], 1, "Proprietary plug → adapter or reuse Dell's own module.")]),
 dict(steps=STD_PACK),
 dict(key_ideas=["Power button = momentary switch; polarity does not matter for switches, it does for LEDs.", "Standard header: 2×5 block with PWR SW, RESET, PWR LED, HDD LED.", "Dell 7050: a keyed 5-pin plug. Transplant options: adapter, or reuse Dell's own button module on its cable."],
      questions=[("Draw the standard 2×5 header with labels.", 4), ("Dell front-panel plug: pins ___, keyed? ___", 1), ("Explain how a screwdriver can 'press' the power button.", 2), ("Your transplant plan for the button: adapter or Dell module? Why?", 2)],
      exit="Switch vs LED: which cares about + and −?"),
 callouts=[SAFE_ESD]))

# ---------------------------------------------------------------- WEEK 6
LESSONS.append(L(16, 6, 1, "Power supplies: volts, watts, rails and connectors",
 ["Explain what a PSU does and name its three main rails.", "Identify every ATX connector by shape and pin count.", "Describe why the Dell PSU cannot be reused for the upgrade."],
 ["An ATX PSU (unplugged, lid on) per bench", "The Dell 180 W PSU in the bench PC for comparison", "Printed connector sheet"],
 [("Rail", "One of the PSU's output voltages: 3.3 V, 5 V or 12 V."), ("Watt", "Power = volts × amps. A 550 W PSU can deliver up to 550 W total."), ("80 Plus", "An efficiency rating: Bronze, Gold, Platinum."), ("PS_ON", "The green wire; the board pulls it low to switch the PSU on."), ("PWR_OK", "The grey wire; the PSU says 'voltages are stable' so the CPU can start.")],
 dict(steps=["No panel off today. Each bench has an ATX PSU to handle with the lid ON.", "Teacher: 'A PSU is the one part in this room that can hurt you after it is unplugged.'"]),
 dict(min=14, html="""<p>The wall gives 230 V AC. Chips want 1–12 V DC. The PSU converts, filters and splits that into three <b>rails</b>: 12 V (CPU, GPU, fans, motors), 5 V (USB, drives, logic) and 3.3 V (some chips). Each cable carries a mix of these plus ground.</p>
{F0}
<p><b>Example 1 — watts.</b> Our upgraded build: CPU 65 W + board 25 W + GPU 130 W + drives and fans 20 W = 240 W at full tilt. Add 30% headroom = 312 W. A 450–550 W PSU is plenty; the Dell 180 W is not.</p>
<p><b>Example 2 — connectors.</b> 24-pin main, 4+4 (8-pin) CPU, 6+2 PCIe for graphics, flat 15-pin SATA power. All keyed; none fit the wrong socket.</p>
<p><b>Example 3 — Dell.</b> The 7050 board has no 24-pin socket: it uses a 6-pin main plug plus the 4-pin CPU plug. A 24-to-6 adapter made for the 3050/5050/7050 solves it. The 4-pin CPU plug is standard.</p>""", figures=[psu()]),
 dict(min=16, steps=["Read the ATX PSU label. Write: total watts, 12 V amps, 80 Plus rating, form factor (ATX / SFX).",
      "Calculate 12 V rail watts: volts × amps. Is it close to the total? (It should be: 12 V does the heavy lifting.)",
      "Lay out every cable. Count the pins on each plug and match it to the connector sheet.",
      "Find the green PS_ON wire and the grey PWR_OK wire in the 24-pin plug. Point them out to your partner.",
      "Compare with the Dell PSU in the bench PC: its label watts, its plugs (6-pin + 4-pin), its shape.",
      "Write one sentence: why can't the Dell PSU power a graphics card with an 8-pin plug?"]),
 dict(quiz=[Q("Which rail powers the CPU and GPU?", ["3.3 V", "5 V", "12 V", "230 V"], 2, "12 V carries most of the power."),
      Q("A 550 W PSU in a 300 W build…", ["wastes 250 W", "is fine: it only delivers what is asked", "will blow up", "needs a bigger case"], 1, "Headroom is good; the PSU is not 'always on full'."),
      Q("The 7050 board's main power plug is…", ["24-pin", "20-pin", "6-pin (Dell)", "8-pin"], 2, "That is why we need the 24→6 adapter.")]),
 dict(steps=["Cables coiled, PSU back in its box, label up.", "Connector sheet in the folder."]),
 dict(key_ideas=["PSU: 230 V AC → 12 V / 5 V / 3.3 V DC rails. Watts = volts × amps.", "Connectors: 24-pin main, 4+4 CPU, 6+2 PCIe, SATA power; all keyed.", "Dell 7050 uses a 6-pin main plug: 24→6 adapter for the transplant. The 180 W unit cannot feed a plug-in GPU."],
      questions=[("Your ATX PSU: watts ___, 12 V amps ___ (= ___ W), rating ___, form factor ___.", 2), ("Match each connector to its job: 24-pin, 4+4, 6+2, SATA.", 2), ("Explain PS_ON and PWR_OK in one sentence each.", 2), ("Why does the transplant need a new PSU and an adapter?", 2)],
      exit="Volts × amps = watts. Check: 12 V × 40 A = ___ W"),
 callouts=[SAFE_PSU]))

LESSONS.append(L(17, 6, 2, "Power budget: size the PSU, then test it",
 ["Add up a build's power draw and choose a PSU with headroom.", "Run the Dell PSU's built-in self-test (BIST).", "Watch the teacher test an ATX PSU with a tester and explain each reading."],
 ["Dell 7050 SFF", "ATX PSU + PSU tester (teacher bench)", "Power-budget worksheet", "Calculator"],
 [("Headroom", "Spare capacity above the expected peak, usually 25–30%."), ("BIST", "Built-in self-test: the small button and LED on the back of a Dell PSU."), ("PSU tester", "A box that fakes the motherboard so the PSU turns on and shows each rail's voltage."), ("Peak draw", "The most the build will pull with everything busy.")],
 dict(steps=["Boot the PC. Open the budget tool below while the teacher explains headroom.", "Guess your upgraded build's peak draw in watts before you add it up."]),
 dict(min=12, html="""<p>Sizing a PSU is arithmetic. List every part, write its peak watts, add them, then add about 30% so the PSU is not running flat out (quieter, cooler, longer life). Round up to a size that exists.</p>
<p><b>Example 1.</b> i5-7500 (65) + board and RAM (25) + NVMe (7) + two fans (6) + GTX 1650 (75) = 178 W. ×1.3 = 231 W. A 450 W unit is already generous.</p>
<p><b>Example 2.</b> Same build with an RTX 3060 (170 W): 273 W ×1.3 = 355 W. Choose 550 W.</p>
<p><b>Example 3.</b> A budget '600 W' no-name unit with a 12 V rail rated 20 A can only really deliver 240 W where it matters. Read the 12 V line, not the big number on the box.</p>
<p>Try it: change the parts and watch the gauge.</p>{F0}""", figures=[power_budget()]),
 dict(min=22, steps=["Use the budget tool for YOUR planned upgrade (the GPU your bench will get). Write the peak, the 30% figure and the PSU you would buy.",
      "Dell PSU self-test: PC plugged in but off. Find the small button and LED on the back of the PSU. Press and hold: LED lights = PSU can make power. Write the result.",
      "Teacher bench: watch the ATX PSU tester. Write the readings for +12 V, +5 V, +3.3 V and PG (power good) delay in ms.",
      "Rule: a rail more than 5% off (12 V outside 11.4–12.6 V) fails. Mark each reading pass/fail.",
      "Teacher demonstrates the paperclip start on a spare PSU (PS_ON to ground) and explains why the tester is the safer habit.",
      "Discuss: a PC that randomly restarts under game load. PSU too small, or bad RAM? What test separates them?"]),
 dict(quiz=[Q("Why add 30% headroom?", ["To make the box look bigger", "So the PSU runs cooler, quieter and lasts longer with room for spikes", "PSUs lose 30% a year", "No reason"], 1, "A PSU at 60–70% load is in its happy zone."),
      Q("+12 V reads 11.1 V on the tester. Verdict:", ["Pass", "Fail: more than 5% low", "Needs more cable", "Perfect"], 1, "Anything outside 11.4–12.6 is a fail."),
      Q("The Dell BIST LED lights. This means…", ["the whole PC is fine", "the PSU can make power; the board might still be the problem", "the RAM is good", "nothing"], 1, "BIST tests the supply only.")]),
 dict(steps=["Tester to the teacher. Worksheets in the folder. Shut down."]),
 dict(key_ideas=["Peak watts of every part, add them, ×1.3, round up to a real size.", "Read the 12 V amps, not the box number.", "Dell BIST: button on the PSU, LED = supply OK. ATX tester: each rail within 5%, PG delay 100–500 ms."],
      questions=[("Your build: parts and watts ___ total ___ ×1.3 = ___ → PSU chosen ___", 3), ("Tester readings: 12 V ___ 5 V ___ 3.3 V ___ PG ___ ms. Pass/fail each.", 2), ("A 'random restarts under load' PC: which test tells PSU apart from RAM?", 2), ("Why is the tester a better habit than the paperclip trick?", 2)],
      exit="Your guess vs the calculated peak draw: how far off were you?"),
 callouts=[SAFE_PSU, ("danger", "Paperclip start is teacher-only", "It is a demonstration of what PS_ON does. Students use the PSU tester or the Dell BIST button.")]))

LESSONS.append(L(18, 6, 3, "Cabling the ATX PSU: dry run with the 24→6 adapter",
 ["Route and connect every PSU cable on the bench without power.", "Fit the 24-to-6 pin Dell adapter and the 4-pin CPU plug.", "Produce a labelled cable plan for the transplant."],
 ["Dell 7050 board (in the case, panel off)", "ATX PSU (NOT plugged into the wall)", "24-to-6 pin Dell 3050/5050/7050 adapter", "Cable ties / Velcro", "Labels", "Wrist strap"],
 [("Adapter", "A short lead that changes one plug type into another, here 24-pin ATX to Dell 6-pin."), ("Keyed", "Shaped so it fits one way only."), ("Dry run", "Doing the job with no power so mistakes cost nothing."), ("Strain relief", "Routing so the cable's weight does not pull on the plug.")],
 dict(min=4, steps=["Strap on. Confirm the ATX PSU's mains lead is NOT attached and its switch is off.", "Lay the PSU beside the open Dell. Nothing is being mounted today."]),
 dict(min=8, html="""<p>Today is rehearsal. Every plug goes on, every route is chosen, nothing is powered. In Week 9 you will do this for real inside the frame, fast, because you have already done it once.</p>
{F0}
<p><b>Example 1.</b> The adapter: ATX 24-pin goes into the adapter's socket; the adapter's 6-pin goes into the Dell board. The 24-pin latch must click. The 6-pin is keyed and clicks too.</p>
<p><b>Example 2.</b> The 4+4 CPU plug: you only need one half (4 pins) for this board. The halves are keyed; the shape of the pin housings matches the socket.</p>
<p><b>Example 3.</b> Route cables so nothing crosses the CPU fan and the PCIe slot stays clear for the graphics card. Tie off the unused leads; a loose SATA plug touching the board can short it.</p>""", figures=[psu()]),
 dict(min=25, steps=["Unplug the Dell PSU's 6-pin and 4-pin plugs from the board (press latch, pull straight). Photo first.",
      "Plug the ATX 24-pin into the adapter. Listen for the latch. Plug the adapter's 6-pin into the board.",
      "Plug one 4-pin half of the CPU lead into the 4-pin socket near the CPU. Check the latch side.",
      "Plug a SATA power lead to the 2.5-inch drive. Lay out (do not connect) a PCIe 6+2 lead where the GPU will sit.",
      "Route: cables away from the fan, under the drive cage line, PCIe slot clear. Velcro the unused leads together.",
      "Label every plug with tape: 'MAIN', 'CPU', 'SATA', 'GPU'.",
      "Navigator check with the torch: every plug latched, nothing touching the board that should not.",
      "Draw the cable plan on the worksheet. Then undo everything, refit the Dell PSU plugs, and photo-check against the first photo."]),
 dict(min=5, quiz=[Q("The 24-pin plug goes into…", ["the Dell board directly", "the adapter, whose 6-pin goes to the board", "the GPU", "the SATA drive"], 1, "No 24-pin socket on the Dell."),
      Q("For the CPU power on this board you use…", ["both halves of the 4+4", "one 4-pin half", "a PCIe plug", "a SATA plug"], 1, "The 4-pin socket takes one keyed half."),
      Q("Why tie off unused PSU leads?", ["It looks neat", "A loose plug touching the board can short it", "They get hot", "The teacher likes it"], 1, "Safety first, tidiness second.")]),
 dict(steps=["Dell plugs back in and checked against the photo. Adapter back in its bag.", "Pack down as usual; log 'PSU dry run complete'."]),
 dict(key_ideas=["24-pin → adapter → 6-pin board; one 4-pin half for the CPU; SATA power to the drive; 6+2 ready for the GPU.", "Everything keyed and latched. Routed away from fans. Unused leads tied.", "Dry run now = fast, calm build in Week 9."],
      questions=[("Draw your cable plan: PSU → adapter → board, CPU plug, SATA, GPU.", 5), ("Which plugs have a latch you must hear click?", 1), ("Name two routing rules you followed.", 2), ("What would happen if the 6-pin were only half in at power-on?", 2)],
      exit="How long did the dry run take? Target for Week 9: half that."),
 callouts=[SAFE_ESD, SAFE_PSU, ("danger", "No mains lead on the ATX PSU today", "The dry run is unpowered. The mains lead stays in the box.")]))
