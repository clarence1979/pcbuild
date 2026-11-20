from visuals import *
from content_a import L, Q, STD_PACK, SAFE_ESD, SAFE_PSU, SAFE_PWR

LESSONS = []

# ---------------------------------------------------------------- WEEK 7
LESSONS.append(L(19, 7, 1, "Graphics cards: what a GPU does and how it fits",
 ["Explain why games need a GPU and spreadsheets do not.", "Read a GPU's size, slot, power plug and VRAM from its spec.", "Tell which cards can run on the Dell 180 W PSU and which must wait for the ATX PSU."],
 ["A low-profile GPU and a full-size GPU to handle (on the mat)", "Wrist strap", "Ruler", "Spec sheets"],
 [("GPU", "Graphics processing unit: thousands of small cores for drawing pixels in parallel."), ("VRAM", "The GPU's own memory for textures and frames."), ("iGPU / dGPU", "Integrated (inside the CPU) vs dedicated (a card)."), ("Low profile", "A short-bracket card that fits a slim case like the SFF."), ("TBP / TGP", "The card's peak power in watts.")],
 dict(steps=["Strap on. Two cards on the mat: measure both (length, height, slot width).", "Guess which one could fit the Dell case. Why?"]),
 dict(min=14, html="""<p>A CPU has four big cores that do anything. A GPU has thousands of tiny cores that all do the same simple job at once: work out the colour of one pixel. A 1080p screen is two million pixels, sixty times a second. That is a parallel job, so a parallel chip wins.</p>
{F0}
<p><b>Example 1 — the iGPU.</b> The i5-7500 has Intel HD 630 built in. Fine for the desktop, video and old games. It uses system RAM as its VRAM, which is slow.</p>
<p><b>Example 2 — power.</b> A PCIe slot can supply 75 W. A card with no power plug (GTX 1650 LP, RX 6400) lives on that and will run on the Dell PSU. A card with an 8-pin plug needs the ATX PSU, so it waits for Week 9.</p>
<p><b>Example 3 — size.</b> A full-height card is 112 mm tall; the SFF case fits only 'low profile' (69 mm). Length matters too: the open frame has no limit, the SFF has about 170 mm.</p>""", figures=[gpu()]),
 dict(min=18, steps=["Measure each card: length, bracket height, number of slots it blocks. Write on the worksheet.",
      "Find the power plug (if any). 6-pin, 8-pin, or none? Write the watts from the spec sheet.",
      "Decide: 'runs now on Dell PSU' or 'waits for ATX PSU'. Justify with the 75 W rule.",
      "Find the VRAM amount and the output ports (HDMI, DisplayPort, DVI). Write them.",
      "On the booted PC, Windows: Task Manager → Performance → GPU 0. Linux: <code>lspci | grep -i vga</code>. Write what graphics the PC uses now.",
      "Rank the two cards and the iGPU from weakest to strongest. Say what evidence you used."]),
 dict(quiz=[Q("A card with an 8-pin power plug on the Dell 180 W PSU…", ["works fine", "must wait for the ATX PSU", "needs two SATA plugs", "runs at half speed"], 1, "No PCIe power leads on the Dell PSU; the slot alone gives 75 W."),
      Q("VRAM is…", ["the CPU's cache", "the graphics card's own memory", "a kind of SSD", "the fan"], 1, "Textures and frames live there."),
      Q("Why is a GPU better at drawing pixels than a CPU?", ["It is bigger", "Thousands of small cores work on pixels in parallel", "It has more cache", "It runs Windows"], 1, "Parallel job, parallel chip.")]),
 dict(steps=["Cards back in anti-static bags, teacher collects.", "Shut down."]),
 dict(key_ideas=["GPU = thousands of small cores drawing pixels in parallel; CPU = few big cores doing anything.", "Slot gives 75 W. No plug = runs on the Dell PSU now; 6/8-pin = ATX PSU in Week 9.", "Low profile (69 mm) fits the SFF; full height needs the open frame."],
      questions=[("Card A: length ___ height ___ slots ___ plug ___ watts ___ VRAM ___ ports ___", 2), ("Card B: same.", 2), ("Which can run on the Dell PSU and why?", 2), ("Explain iGPU vs dGPU to a Year 7.", 2)],
      exit="Pixels per second at 1080p 60 fps = 1920 × 1080 × 60 = ___ million."),
 callouts=[SAFE_ESD]))

LESSONS.append(L(20, 7, 2, "Install the graphics card and get a picture",
 ["Seat a card in the PCIe x16 slot with the latch and bracket screw.", "Move the monitor cable to the card and confirm output.", "Install or verify the driver."],
 ["Dell 7050 SFF", "Low-profile GPU (≤75 W, no plug) per bench, or full-size card for a lid-off bench test", "Wrist strap", "Phillips #2", "Monitor with HDMI/DP cable"],
 [("Latch", "The small lever at the end of the x16 slot that locks the card."), ("Bracket", "The metal plate on the card's edge that screws to the case."), ("Driver", "Software that lets the OS use the card's features."), ("Slot cover", "The blanking plate you remove to expose the slot opening.")],
 dict(min=4, steps=["Strap on, unplug, press the button, panel off.", "Teacher: cards without a power plug install now. Cards with a plug go in with the panel off for a bench test only, after Week 9's PSU."]),
 dict(min=8, html="""<p>Installing a card is four moves: remove the slot cover, line the card up with the x16 slot, press straight down until the latch clicks, fit the bracket screw. Then move the monitor cable to the card. The board sees a card in x16 and uses it instead of the iGPU.</p>
{F0}
<p><b>Example 1.</b> Monitor still plugged into the board's HDMI: black screen, because the board switched output to the card. Move the cable.</p>
<p><b>Example 2.</b> Card half-seated: the PC boots on the iGPU, the card is 'not detected'. Power off, press until the latch clicks.</p>
<p><b>Example 3.</b> Picture appears but at low resolution and jerky: the driver is missing. Install from the maker's site or the OS driver tool.</p>""", figures=[gpu()]),
 dict(min=26, steps=["Remove the slot cover(s) behind the x16 slot. Keep the screw.",
      "Open the slot latch. Line the card's gold edge with the slot and the bracket with the case opening.",
      ("Press straight down evenly on the top edge until the latch clicks. Check from the end: no gold showing.", "Full-size card on a bench test: support it with one hand; it will stick out of the case."),
      "Fit the bracket screw. If your card has a power plug AND you have the ATX PSU dry-run ready, connect 6+2 now; otherwise leave it for Week 9.",
      "Navigator check: latched, screwed, cables clear of the fan. Panel on (or lid-off bench test). Plug in.",
      "Move the monitor cable to the CARD's port. Power on. Expect the Dell logo on screen.",
      "Windows: Device Manager → Display adapters. Linux: <code>lspci | grep -i vga</code>. Is the card listed?",
      "Install the driver (Windows: maker's installer from the teacher's USB; Linux Mint: Driver Manager). Reboot and check resolution and refresh rate."]),
 dict(min=4, quiz=[Q("Black screen after the install. First check:", ["RAM", "Monitor cable is on the card, not the board", "PSU watts", "Driver"], 1, "Output moved to the card."),
      Q("The latch did not click. You…", ["power on anyway", "press down evenly until it does", "remove a screw", "use a different monitor"], 1, "Half-seated = not detected."),
      Q("A driver is…", ["a metal bracket", "software the OS uses to control the card", "a kind of cable", "a BIOS setting"], 1, "Without it you get basic, slow output.")]),
 dict(steps=STD_PACK),
 dict(key_ideas=["Slot cover off → latch open → press until click → bracket screw → monitor cable to the card.", "Black screen: cable on the wrong port. Not detected: reseat. Low-res/jerky: driver.", "No-plug cards run on the Dell PSU; plug cards wait for the ATX PSU."],
      questions=[("Card installed: model ___ detected? ___ driver version ___ resolution ___ Hz ___", 2), ("Write the install steps in order (6 steps).", 4), ("Three symptoms and their causes: black screen / not detected / low resolution.", 3)],
      exit="What did the latch feel like when it was properly seated?"),
 callouts=[SAFE_ESD, SAFE_PWR]))

LESSONS.append(L(21, 7, 3, "Benchmark: iGPU vs card, and what the numbers mean",
 ["Run a graphics benchmark and read FPS and temperature.", "Compare the iGPU with the card and explain the difference.", "Describe what limits frame rate: GPU, CPU or settings."],
 ["Dell 7050 with GPU", "Benchmark: Unigine Heaven (Windows) or glmark2 (Linux); a game if licensed", "GPU-Z / Task Manager / nvidia-smi", "Worksheet"],
 [("FPS", "Frames per second: how many pictures the GPU finishes each second."), ("Resolution", "Pixels across × down: 1920×1080 is 1080p."), ("Bottleneck", "The slowest part that holds the rest back."), ("Thermal throttling", "The GPU slowing itself down when hot.")],
 dict(steps=["Boot, log in, open the benchmark tool. Teacher sets the common settings so benches can be compared.", "Predict: how many times faster than the iGPU will your card be?"]),
 dict(min=8, html="""<p>A benchmark draws the same scene on every PC so numbers can be compared. FPS above 60 looks smooth; below 30 feels choppy. Watching the GPU temperature and load at the same time tells you whether the card is working hard (99% load) or waiting on the CPU (GPU load low, FPS low = CPU bottleneck).</p>
<p><b>Example 1.</b> HD 630 iGPU at 1080p: 8 FPS. GTX 1650: 60 FPS. Same scene, 7× faster.</p>
<p><b>Example 2.</b> Drop resolution to 720p: the iGPU doubles to 16 FPS. Fewer pixels per frame = less work.</p>
<p><b>Example 3.</b> A fast card with an old CPU: GPU load sits at 50%, FPS does not rise with lower settings. The CPU cannot feed it frames fast enough.</p>{F0}""", figures=[gpu()]),
 dict(min=27, steps=["Run 1: force the iGPU. Windows: plug the monitor into the board port and set the benchmark to use the Intel GPU (or temporarily remove the card). Record average FPS at 1080p.",
      "Run 2: the card at 1080p, same settings. Record average FPS, GPU temperature at the end, GPU load %.",
      "Run 3: the card at 720p. Record FPS. Did it rise? By how much?",
      "Run 4: highest quality preset at 1080p. Record FPS and temperature.",
      "Write the ratio: card FPS ÷ iGPU FPS.",
      "Watch GPU load during a run: near 100% means the GPU is the limit; much lower means the CPU is.",
      "Compare across benches. Which card won? Was the result in line with the spec sheets?"]),
 dict(quiz=[Q("60 FPS means…", ["60 pixels per second", "60 complete pictures per second", "60 GHz", "60 W"], 1, "Frames, not pixels."),
      Q("FPS rises a lot when you lower the resolution. The limit was…", ["the CPU", "the GPU", "the RAM", "the monitor"], 1, "Fewer pixels = less GPU work = more frames."),
      Q("GPU load is 45% and FPS is low. The limit is probably…", ["the GPU", "the CPU feeding it", "the PSU", "VRAM"], 1, "The GPU is waiting.")]),
 dict(steps=["Close the benchmark, return settings to normal, shut down.", "Worksheet in the folder."]),
 dict(key_ideas=["Benchmarks compare PCs on the same scene. 60 FPS smooth, 30 choppy.", "Resolution and quality settings change GPU work; GPU load tells you who is the bottleneck.", "Watch temperature: a hot card throttles and FPS falls over time."],
      questions=[("Run 1 iGPU ___ FPS. Run 2 card 1080p ___ FPS ___ °C ___ % load. Run 3 720p ___ FPS. Run 4 max ___ FPS ___ °C.", 2), ("Card ÷ iGPU = ___×. Was your prediction close?", 1), ("Explain 'bottleneck' with an example from today.", 3), ("Why do we keep the settings identical across benches?", 2)],
      exit="If you could change one part of this PC to get more FPS, which and why?"),
 callouts=[]))

# ---------------------------------------------------------------- WEEK 8
LESSONS.append(L(22, 8, 1, "Cases and cooling: airflow, standoffs and the open frame",
 ["Describe the path air takes through a case and why.", "Explain standoffs, I/O shields and why they exist.", "Compare a closed case with an open frame for our transplant."],
 ["The open-frame case kit (one per bench, or shared)", "A standard mATX case for comparison (teacher bench)", "Standoff kit, nylon washers", "Wrist strap"],
 [("Intake / exhaust", "Fans that pull cool air in / push warm air out."), ("Positive pressure", "Slightly more intake than exhaust so dust cannot creep in through gaps."), ("Standoff", "A brass post that holds the board above the metal tray."), ("Open frame", "A case with no sides: the board sits on rails in the open air."), ("I/O shield", "The thin plate that fits around the rear ports in a closed case.")],
 dict(steps=["Unbox the frame kit. Lay out every part on the mat and count against the parts list.", "Teacher shows the airflow figure."]),
 dict(min=12, html="""<p>A closed case is a wind tunnel. Front and bottom fans pull in cool air; rear and top fans push warm air out. The CPU and GPU coolers sit in that stream. Block it (dust, cables, a case against a wall) and temperatures climb.</p>
{F0}
<p><b>Example 1.</b> A PC pushed into a cupboard with the back against the wood: no exhaust path, CPU 95 °C. Pull it out 10 cm: 70 °C.</p>
<p><b>Example 2.</b> Intake fans without filters: in a year the heatsink fins are a felt blanket. Filters on intakes, positive pressure, clean every term.</p>
<p><b>Example 3.</b> Our open frame has no sides at all. Room air reaches everything, so a single CPU cooler is enough; the trade-off is dust, noise, and that nothing protects the board. That is why we use it on a bench, never on the floor.</p>
{F1}""", figures=[airflow(), standoff()]),
 dict(min=20, steps=["Identify on the frame: board rails or tray, PSU position, GPU bracket rail, the power-switch lead.",
      "Check: are the board mounts slotted rails or fixed holes? Slotted = can match Dell's pattern. Write which you have.",
      "Screw three standoffs into the rail by hand. Feel the thread. Unscrew them.",
      "Find the nylon washers. Explain to your partner what they are for (hint: standoff figure).",
      "Teacher bench: look at the mATX case's I/O shield cutout and PCIe slot openings. Why would a Dell board's ports not line up?",
      "Plan your frame's fan: where would one 120 mm fan go to blow across the CPU cooler? Mark it on the worksheet.",
      "Repack the kit exactly as it came, parts list ticked."]),
 dict(quiz=[Q("Standoffs exist to…", ["look nice", "keep the board's solder points off the metal tray", "add weight", "hold the fan"], 1, "Metal tray + solder = short circuit."),
      Q("Positive pressure means…", ["more exhaust than intake", "more intake than exhaust, so dust is pushed out of gaps", "no fans", "fans at full speed"], 1, "Air leaks out of the gaps instead of in."),
      Q("An open frame is a good home for the Dell board because…", ["it is cheaper", "no I/O shield or slot cutouts to match", "it is quieter", "it has better airflow than a case"], 1, "Nothing to line up except the standoffs.")]),
 dict(steps=["Kit repacked and labelled with your bench number.", "Strap off last."]),
 dict(key_ideas=["Front/bottom in, rear/top out. Keep the path clear. Filters on intakes, positive pressure.", "Standoffs lift the board off the metal; washers insulate screw heads; unused holes stay empty.", "Open frame: nothing to line up but the standoffs, but no protection — bench only."],
      questions=[("Draw the airflow through a tower case with three fans and label intake/exhaust.", 4), ("Your frame: slotted rails or fixed holes? What does that mean for the Dell board?", 2), ("Explain what happens if a board edge touches the metal frame at power-on.", 2), ("Two advantages and two disadvantages of an open frame.", 2)],
      exit="Where will your single fan go, and why?"),
 callouts=[SAFE_ESD]))

LESSONS.append(L(23, 8, 2, "The compatibility audit: will the Dell board fit, and what else do we need?",
 ["Measure the Dell board's mounting holes and compare with the frame.", "Identify every adapter the transplant needs and why.", "Decide which holes get standoffs and which get nothing."],
 ["Dell 7050 (board visible)", "Open frame", "Ruler / callipers", "Standoffs, washers", "Adapters: 24→6 power, 5-pin front panel (or Dell button module)", "Wrist strap"],
 [("Hole pattern", "Where the board's mounting holes are, measured from one corner."), ("Mismatch", "A board hole with no matching frame hole: leave it without a standoff."), ("Riser", "A short flexible PCIe extension used when a card's bracket does not line up."), ("Audit", "A checklist that proves every part will work together before you start.")],
 dict(min=4, steps=["Strap on, unplug, press the button, panel off.", "Teacher: 'Measure twice, build once. Today nobody moves a board.'"]),
 dict(min=10, html="""<p>Before a transplant, a technician proves fit on paper: hole positions, port positions, power plugs, button plug, card bracket. Every mismatch gets a plan: an adapter, a washer, an empty hole, a riser. Only then does the build start.</p>
{F0}
<p><b>Example 1.</b> Nine holes on the board; six line up with the frame's slotted rails. Six standoffs is enough support. The three odd holes get nothing: a standoff under a hole with no screw is fine, a standoff touching a solder pad is not.</p>
<p><b>Example 2.</b> The front USB block is soldered to the board edge. On an open frame it is reachable, so it still works; in a closed case it would be buried.</p>
<p><b>Example 3.</b> The GPU bracket sits 4 mm off the frame's bracket rail because the Dell slot is not where ATX expects. A short riser cable fixes it; or on an open frame, the card simply hangs in the slot supported by the latch, with no screw.</p>""", figures=[board_shapes()]),
 dict(min=24, steps=["Measure from the board's top-left corner to each mounting hole (x, y in mm). Write all of them on the audit sheet.",
      "Measure the frame's rail positions or fixed holes the same way. Mark each board hole as MATCH or NO MATCH.",
      "Count matches. Fewer than four? Call the teacher: you may need to shift rails.",
      "Check the power: does the 24→6 adapter say 3050/5050/7050? Does the ATX PSU have a 4-pin CPU plug? Tick.",
      "Check the button: adapter present, or Dell button module unscrewed and on its lead? Tick.",
      "Check the GPU: card length vs frame, bracket alignment plan (screw / riser / none). Tick.",
      "Check insulation: a nylon washer for every standoff screw; nothing metal near the rear USB housing. Tick.",
      "Sign the audit sheet. Both names. No signature, no build next week."]),
 dict(min=4, quiz=[Q("A board hole has no matching frame hole. You…", ["drill the board", "leave it: no standoff, no screw", "use a longer screw", "glue it"], 1, "Support from the matched holes is enough."),
      Q("The adapter must be labelled for…", ["any Dell", "3050/5050/7050", "ATX only", "laptops"], 1, "Other Dell generations use different plugs."),
      Q("Why is the audit signed before the build?", ["Tradition", "So every mismatch already has a plan and no one improvises at power-on", "For marks", "No reason"], 1, "Improvising with a live board is how boards die.")]),
 dict(steps=STD_PACK + ["Audit sheet in the bench folder."]),
 dict(key_ideas=["Measure every hole; mark MATCH / NO MATCH; four or more matches is enough; odd holes get nothing.", "Adapters: 24→6 (3050/5050/7050), 4-pin CPU standard, button adapter or Dell module, GPU riser if the bracket is off.", "Nylon washers everywhere; nothing metal near the board edge."],
      questions=[("Hole table: x, y for each board hole and MATCH/NO MATCH.", 5), ("Matches counted: ___. Enough?", 1), ("List every adapter/part the transplant needs, with its reason.", 4), ("What is the GPU bracket plan for your bench?", 1)],
      exit="One thing on the audit that surprised you."),
 callouts=[SAFE_ESD]))

LESSONS.append(L(24, 8, 3, "Transplant run-sheet: order of operations, labels and the before-photo",
 ["Write a step-by-step run-sheet for next week's three lessons.", "Label every cable and bag every screw group in advance.", "Take the 'before' photo set that you will rebuild from."],
 ["Dell 7050 (panel off)", "Frame kit, PSU, adapters, GPU, RAM, SSD laid out", "Labels, zip bags, marker", "Phone/camera", "Run-sheet template"],
 [("Run-sheet", "A numbered list of what happens, in order, with who does it."), ("Before-photo", "Pictures of every connection before you unplug anything."), ("Dependency", "A step that cannot happen until another is done (e.g. standoffs before board)."), ("Checkpoint", "A moment where the Navigator checks before you go on.")],
 dict(min=4, steps=["Strap on. Lay out every part for the build on the mat: frame, PSU, adapter, button adapter, GPU, RAM, SSD, fan.", "Teacher: next week is three 45-minute lessons. Each ends at a checkpoint."]),
 dict(min=8, html="""<p>Professional builds run from a sheet, not from memory. Lesson 25 strips the Dell. Lesson 26 mounts board, PSU, power and button on the frame. Lesson 27 fits RAM, SSD, GPU and fan, then first power-on. Each lesson ends at a checkpoint so a late bench is not a disaster.</p>
<p><b>Example 1 — dependencies.</b> Standoffs before board. Board before CPU cooler check. PSU mounted before the 24-pin is routed. Front-panel plug before the first power-on test, or there is no button to press.</p>
<p><b>Example 2 — labels.</b> 'MAIN', 'CPU', 'SATA-SSD', 'GPU', 'FAN', 'BTN'. A labelled lead goes on in seconds; an unlabelled one gets debated.</p>
<p><b>Example 3 — photos.</b> Overall inside shot, then one close-up per plug. If something does not boot in Lesson 27, you compare against the photos first.</p>{F0}""", figures=[anatomy()]),
 dict(min=26, steps=["Take the photo set: whole interior, then close-ups of the 6-pin, 4-pin, SATA, fan plug, front-panel plug, M.2.",
      "Label every PSU lead you will use and both adapters.",
      "Prepare bags: 'board screws', 'cooler', 'cage', 'frame screws', 'GPU/bracket', 'M.2'.",
      "Write the run-sheet with your partner. Lesson 25: strip (8–10 steps). Lesson 26: mount (8–10 steps). Lesson 27: fit and first power (8–10 steps). Mark the Navigator checkpoints.",
      "Mark on the sheet who is Driver for each lesson (swap each lesson).",
      "Read your sheet to another bench. They look for a missing dependency. Fix it.",
      "Teacher signs the run-sheet. Parts back in the kit box with your bench number."]),
 dict(min=4, quiz=[Q("Which must come first?", ["Board on frame, then standoffs", "Standoffs, then board", "GPU, then board", "Power on, then button"], 1, "You cannot mount a board on standoffs that are not there."),
      Q("The before-photos are for…", ["social media", "comparing against if the rebuild does not boot", "the teacher's records", "nothing"], 1, "Your own reference."),
      Q("A checkpoint is…", ["a break", "a moment the Navigator checks before continuing", "the end of the course", "a BIOS setting"], 1, "Catch mistakes while they are cheap.")]),
 dict(steps=["Kit box closed and labelled. Dell panel on, PC on the shelf.", "Run-sheet and photos (printed or on the shared drive) in the bench folder."]),
 dict(key_ideas=["Three lessons, three checkpoints: strip → mount → fit and power.", "Dependencies decide the order. Labels and bags make the order fast.", "Photos first, so a no-boot has something to compare against."],
      questions=[("Write your run-sheet: Lesson 25 (strip), Lesson 26 (mount), Lesson 27 (fit + power). Number every step and mark checkpoints.", 10), ("List the labels you made and the bags you prepared.", 2)],
      exit="Which step are you least sure about? Ask about it now, not next week."),
 callouts=[SAFE_ESD], parts=PARTS))

# ---------------------------------------------------------------- WEEK 9
LESSONS.append(L(25, 9, 1, "Rebuild 1 of 3: strip the Dell",
 ["Remove every component from the Dell case in the planned order.", "Keep every screw bagged and every part protected.", "Finish at the checkpoint: bare board out, parts on the mat."],
 ["Dell 7050 SFF", "Run-sheet, photos, bags, labels", "Wrist strap", "Phillips #2, spudger", "Anti-static bags for board, GPU, RAM, SSD"],
 [("Strip", "Remove everything from the case down to the empty chassis."), ("Board screws", "The screws holding the motherboard to the case; count them."), ("Rear I/O", "The ports on the back edge; on the Dell they are part of the board.")],
 dict(min=3, steps=["Strap on, unplug, press the button, panel off. Run-sheet open.", "Driver per the sheet. Navigator reads step 1."]),
 dict(min=4, html="""<p>Follow your sheet. The order below is the safe default if your sheet differs.</p>
<p>Keep the CPU and cooler ON the board. The board travels with them. Fewer moves on the socket = fewer risks.</p>{F0}""", figures=[anatomy(["cage", "ram", "m2", "pcie16", "pwr6", "pwr4", "fpanel"])]),
 dict(min=33, steps=["Photo-check: compare the inside with last week's photos. Anything different? Note it.",
      "Unplug the Dell PSU's 6-pin and 4-pin from the board. Unplug SATA data and power from the drive.",
      "Remove the GPU if fitted: bracket screw, latch, lift straight up. Into its bag.",
      "Remove the drive and caddy from the cage. SATA SSD into its bag.",
      "Remove the RAM: clips out, lift. Into the bag, label side up.",
      "Remove the M.2 SSD: screw to the magnetic tray, lift at 30°, into its bag.",
      "Unplug the front-panel plug and any fan plug from the board. Unscrew the Dell button module from the case if you are reusing it; keep it on its lead.",
      "Count and remove the board screws. All in the 'board screws' bag. Write the count on the bag.",
      "Lift the board straight up by its edges, cooler attached. Lay it on the anti-static bag on the mat, cooler up.",
      "Checkpoint: Navigator confirms: board on mat, 5 bags labelled, Dell case empty except PSU. Teacher signs."]),
 dict(min=3, quiz=[Q("Why does the cooler stay on the board during the strip?", ["It is glued", "Fewer moves on the socket means less risk", "It cannot come off", "The screws are lost"], 1, "Every CPU handling is a chance to bend a pin."),
      Q("The board is lifted…", ["by the cooler", "by its edges, straight up", "by the RAM slots", "with pliers"], 1, "Edges only; never by components.")]),
 dict(min=2, steps=["Board, bags and Dell case on the shelf together, bench number on everything.", "Strap off last; log 'stripped, checkpoint signed'."]),
 dict(key_ideas=["Order: photo-check → power plugs → GPU → drive → RAM → M.2 → front panel/fan → board screws → board out.", "Board moves with the cooler on. Lift by the edges. Count the screws.", "Checkpoint signed = you are ready for Lesson 26."],
      questions=[("Tick each strip step as you go (use the Do list). Board screws counted: ___", 1), ("What did you find different from the photos, if anything?", 2), ("Which step took longest and why?", 2)],
      exit="Checkpoint signed? Yes / No. If no, what is left?"),
 callouts=[SAFE_ESD, ("danger", "Lift the board by its edges only", "Never by the cooler, the slots or any cable. One hand each side, straight up.")]))

LESSONS.append(L(26, 9, 2, "Rebuild 2 of 3: mount the board, PSU, power and button on the frame",
 ["Fit standoffs in the matched holes and mount the board with washers.", "Mount the ATX PSU and connect the 24→6 adapter and 4-pin CPU plug.", "Connect the power button (adapter or Dell module) ready for the first test."],
 ["Open frame, standoffs, washers, frame screws", "Dell board (cooler on)", "ATX PSU + 24→6 adapter", "Button adapter or Dell button module", "Run-sheet, audit sheet", "Wrist strap, Phillips #2"],
 [("Matched hole", "A board hole with a frame hole/rail under it, from the audit."), ("Washer", "A nylon ring between the screw head and the board."), ("Snug", "Tight enough that nothing moves; not so tight the board bends.")],
 dict(min=3, steps=["Strap on, clip to the frame. Audit sheet beside the frame.", "Navigator reads the matched-hole list. Driver has standoffs in hand."]),
 dict(min=4, html="""<p>The board goes on standoffs only where the audit said MATCH. Every screw gets a nylon washer. Then the PSU is mounted so the 24-pin reaches the adapter without crossing the CPU cooler. Then the button, so Lesson 27 can test.</p>
<p>Keep the board's rear USB housing clear of any metal rail. That is the one that kills boards.</p>{F0}""", figures=[standoff()]),
 dict(min=33, steps=["Fit a standoff in every MATCHED position on the rail/tray. Finger-tight, then a quarter turn with pliers.",
      "Hold the board over the standoffs. Lower it straight down. Every standoff should show through a board hole; none under a solder area.",
      "Screw with a washer under each head, starting with two opposite corners, then the rest. Snug, not tight.",
      "Navigator torch check: board edges and the rear USB housing not touching any metal. Lift and add washers/spacers if they are.",
      "Mount the PSU in the frame's PSU position, fan facing open air. Four screws.",
      "Plug the 24-pin into the adapter (click). Plug the adapter's 6-pin into the board (click). Plug one 4-pin half into the CPU socket (click).",
      "Connect the button: adapter to the Dell 5-pin, frame switch to the adapter; OR Dell button module on its lead, fixed to the frame with a cable tie.",
      "Plug the CPU cooler fan into its header. Route the leads away from the fan.",
      "Checkpoint: Navigator confirms standoffs, washers, no metal contact, main + CPU power latched, button connected, fan plugged. Teacher signs."]),
 dict(min=3, quiz=[Q("A standoff sits under a part of the board with no hole. You…", ["leave it", "remove that standoff", "add a washer on top", "ignore it"], 1, "A standoff on a solder pad is a short."),
      Q("The 24-pin goes to…", ["the board", "the adapter", "the GPU", "the switch"], 1, "No 24-pin socket on the Dell board.")]),
 dict(min=2, steps=["Frame on the shelf, bags beside it, bench number visible.", "Log 'mounted, checkpoint signed'."]),
 dict(key_ideas=["Standoffs only in MATCHED holes; washer under every screw; snug not tight.", "Rear USB housing and board edges clear of all metal.", "24-pin → adapter → 6-pin; one 4-pin half to CPU; button connected; fan plugged."],
      questions=[("Standoffs fitted: ___. Screws used: ___. Washers used: ___.", 1), ("Describe the torch check and what you were looking for.", 2), ("How is your button connected?", 1), ("What is left for Lesson 27?", 2)],
      exit="Checkpoint signed? What would you do differently?"),
 callouts=[SAFE_ESD, SAFE_PSU, ("danger", "Still no mains lead", "Power stays in the box until Lesson 27's final checkpoint.")]))

LESSONS.append(L(27, 9, 3, "Rebuild 3 of 3: RAM, SSD, GPU, fan, cable management and first power-on",
 ["Fit RAM, M.2 SSD, SATA drive, GPU and case fan on the frame.", "Complete the pre-power checklist and perform the first power-on.", "Confirm POST, BIOS detection of every part, and boot."],
 ["Mounted frame from Lesson 26", "RAM, M.2 SSD, SATA SSD, GPU, 120 mm fan", "PSU leads, 6+2 PCIe lead, SATA power", "Monitor, keyboard, mains lead", "Wrist strap"],
 [("Pre-power checklist", "The list the Navigator reads before the mains lead goes in."), ("First power-on", "The moment of truth; done once, calmly, with the teacher present."), ("Detect", "Every part appears in the BIOS lists.")],
 dict(min=3, steps=["Strap on. Run-sheet to Lesson 27. Parts bags open on the mat.", "Teacher: 'No mains lead until I have seen the checklist.'"]),
 dict(min=3, html="""<p>Everything you have practised comes together: RAM pair in same-colour slots, M.2 at 30° then flat, SATA data + power, GPU latched and powered, fan plugged. Then the checklist. Then power.</p>{F0}""", figures=[boot_chain()]),
 dict(min=33, steps=["RAM: matched pair into the same-colour slots. Both clips click on both sticks.",
      "M.2: 30°, in, flat, screw snug.",
      "SATA SSD: mount in the frame's drive spot. SATA data to a board port, SATA power from the PSU.",
      "GPU: latch open, press until click, bracket screw or riser per your audit, 6+2 power plug if the card has one.",
      "Case fan: mount where you planned, blowing across the CPU cooler. Plug into the free fan header (or a PSU adapter).",
      "Cable management: Velcro the PSU leads, nothing near fans, nothing resting on the board.",
      "Pre-power checklist (Navigator reads, Driver touches each one): main latched · CPU 4-pin latched · RAM clips ×4 · M.2 screw · SATA data · SATA power · GPU latch · GPU power · CPU fan · case fan · button · no metal contact · no loose screws on the board.",
      "Teacher inspects and says 'go'. Mains lead in. PSU switch on. Monitor to the GPU. Press the button.",
      "Watch: fans spin, LED amber → white, Dell logo. Tap F2. Check: memory GB + Dual, both drives, GPU detected. Exit and boot to the OS.",
      "No POST? Mains off. Compare against photos and checklist. Reseat RAM, then GPU, then power plugs. Call the teacher."]),
 dict(min=3, quiz=[Q("Fans spin but there is no screen and the LED blinks amber 2,3. First action:", ["Replace the PSU", "Mains off, reseat the RAM", "Press the button again", "Reinstall Windows"], 1, "2,3 = memory/CPU/board; reseat RAM first."),
      Q("The pre-power checklist is read by…", ["the Driver silently", "the Navigator aloud while the Driver touches each item", "the teacher only", "nobody"], 1, "Two people, one list.")]),
 dict(min=3, steps=["If booted: shut down properly, PSU switch off, mains lead out, frame on the shelf.", "Log 'first power-on: POST OK / fault: …'. Checkpoint signed."]),
 dict(key_ideas=["Fit order: RAM → M.2 → SATA → GPU → fan → cable management → checklist → power.", "Checklist is read aloud and touched. Teacher says 'go'.", "No POST: mains off, photos, reseat RAM, GPU, power plugs, in that order."],
      questions=[("First power-on result: ___. LED sequence seen: ___. BIOS: RAM ___ GB ___ channel, drives ___, GPU ___.", 2), ("Which checklist item did you nearly miss?", 1), ("If it did not POST first time, what fixed it?", 2), ("Write a two-sentence build log for the class record.", 2)],
      exit="How does it feel to press the button on a machine you rebuilt?"),
 callouts=[SAFE_ESD, SAFE_PWR, SAFE_PSU]))

# ---------------------------------------------------------------- WEEK 10
LESSONS.append(L(28, 10, 1, "Troubleshooting method: six steps and a log",
 ["Use the six-step troubleshooting method on a described fault.", "Explain half-splitting and known-good swaps.", "Keep a fault log that another tech could follow."],
 ["Fault log sheets", "Three written case studies", "Whiteboard"],
 [("Theory", "Your best guess at the cause, written before you touch anything."), ("Half-split", "Remove half the parts to see which half holds the fault."), ("Known good", "A part you are certain works, used to swap-test."), ("Root cause", "The real reason, not the symptom.")],
 dict(steps=["No hardware today. Pairs get three case cards.", "Teacher: 'The expensive mistake is changing three things at once.'"]),
 dict(min=14, html="""<p>Technicians across the world use the same six steps. They stop you guessing.</p>
{F0}
<p><b>Case 1.</b> 'It turns on but no picture.' Identify: fans spin, LED white, monitor says no signal. Theory: monitor on the wrong port. Test: move the cable to the GPU. Picture. Fix: label the port. Document: 'cable on iGPU port after GPU install'.</p>
<p><b>Case 2.</b> 'Random restarts when gaming.' Theory 1: PSU overloaded. Test: PSU tester under load: fine. Theory 2: overheating. Test: temperature log shows 99 °C. Fix: re-paste. Verify: 72 °C, no restarts for a week.</p>
<p><b>Case 3.</b> 'Dead. Nothing at all.' Half-split: unplug everything but board, CPU, one RAM stick. Still dead → PSU or board. PSU BIST passes → board. Swap a known-good board → alive. Root cause: board.</p>""", figures=[method6()]),
 dict(min=18, steps=["Read case card A. Write step 1 (identify) as three facts you would gather.",
      "Write two theories, most likely first.",
      "Write the single test for theory 1 and what result would confirm or reject it.",
      "Do the same for cards B and C. Each card: facts, two theories, one test each.",
      "Swap sheets with another bench. Mark: did they change one thing at a time? Did they write the simplest theory first?",
      "Pick the best log from the class. Why is it the best?"]),
 dict(quiz=[Q("Step 2 is…", ["fix it", "form a theory", "write it down", "buy parts"], 1, "Identify, theory, test, plan, fix/verify, document."),
      Q("Half-splitting means…", ["cutting the case in half", "removing half the parts to narrow down which half has the fault", "doing half the job", "testing at half speed"], 1, "Binary search on hardware."),
      Q("You swap the RAM, the SSD and the PSU at once and it works. You have learned…", ["which part was faulty", "nothing certain about the cause", "it was the PSU", "it was the RAM"], 1, "Three changes, no conclusion.")]),
 dict(steps=["Logs in the folder. Case cards back."]),
 dict(key_ideas=["Identify → theory → test → plan → fix & verify → document.", "Simplest theory first. One change at a time. Known-good swaps. Half-split big mysteries.", "A log another tech can follow is part of the job."],
      questions=[("Case A: facts / theories / tests.", 4), ("Case B: facts / theories / tests.", 4), ("Case C: facts / theories / tests.", 4), ("In your own words: why 'one change at a time'?", 2)],
      exit="Which step do you think most people skip?"),
 callouts=[]))

LESSONS.append(L(29, 10, 2, "Reading the machine: Dell LED codes, the one beep and the no-POST ladder",
 ["Decode a Dell amber blink pattern using the table.", "Recognise the 1-3-2 memory beep.", "Follow the no-power / no-POST / no-boot ladder."],
 ["Dell LED simulator (on screen)", "Dell 7050 or rebuilt frame", "Dell code table (printed)"],
 [("No power", "Nothing happens: no fans, no LED."), ("No POST", "Power arrives but the self-test never finishes: fans spin, no screen."), ("No boot", "POST passes, then the OS fails to load."), ("Pattern 2,3", "Two amber blinks, pause, three blinks: memory/CPU/board.")],
 dict(steps=["Open the simulator. Teacher plays a pattern; everyone counts and writes it.", "Where does the fault live: power, POST or boot?"]),
 dict(min=12, html="""<p>Dell took the beeps away and put the diagnosis in the power button. It blinks amber in two groups: count the first group, pause, count the second. Look it up. Since 2012 the only beep left is 1-3-2, and it means memory.</p>
<p>Before the codes, sort the symptom into one of three rungs:</p>
<ol><li><b>No power</b>: no fans, no LED → wall, lead, PSU switch, PSU BIST, front-panel plug.</li>
<li><b>No POST</b>: fans and LED but no screen → read the blink code; RAM, GPU, CPU power, board.</li>
<li><b>No boot</b>: Dell logo appears, then an error or black screen → boot order, drive cable, OS.</li></ol>
<p><b>Example 1.</b> 2,3 after a RAM upgrade: reseat the sticks, try one at a time.</p>
<p><b>Example 2.</b> 3,2 after a GPU install: video. Reseat the card, check its power plug, try the iGPU.</p>
<p><b>Example 3.</b> 2,2: PSU or cabling. Dell BIST, then the 6-pin and 4-pin.</p>{F0}{F1}""", figures=[dell_led(), boot_chain()]),
 dict(min=20, steps=["Play five patterns from the simulator (partner chooses, you count). Write the code and the meaning for each.",
      "Play the 1-3-2 beep. Say what it means without looking.",
      "Sort these into no power / no POST / no boot: 'fans spin, no screen' · 'Dell logo then \"no bootable device\"' · 'nothing at all' · 'LED blinks 2,4' · 'Windows loads then freezes'.",
      "On your rebuilt frame: unplug the 4-pin CPU power, power on, observe (fans? LED? pattern?). Mains off, plug it back.",
      "Remove one RAM stick and reseat it half-way. Power on. Observe and write the pattern. Mains off, fix it, confirm POST.",
      "Write the ladder on your worksheet from memory."]),
 dict(quiz=[Q("LED blinks 3 then 3. Dell's table says…", ["coin cell", "no memory detected", "video", "storage"], 1, "3,3 = no memory detected on this series."),
      Q("The Dell logo appears, then 'No bootable device'. Rung?", ["No power", "No POST", "No boot", "Overheat"], 2, "POST passed; the boot device is the problem."),
      Q("The only beep code Dell still uses means…", ["CPU", "memory", "GPU", "PSU"], 1, "1-3-2 = memory.")]),
 dict(steps=STD_PACK),
 dict(key_ideas=["No power / no POST / no boot: sort first, then look up the code.", "Dell amber blink: count, pause, count. 2,x = board/PSU/RAM/CPU family; 3,x = PCI/video/memory/storage family.", "1-3-2 beep = memory. Reseat first."],
      questions=[("Five patterns from the simulator: code and meaning.", 3), ("Sort the five symptoms into the three rungs.", 3), ("What happened with the CPU power unplugged? With the half-seated RAM?", 2), ("Draw the ladder.", 3)],
      exit="Which pattern would you expect after a bad GPU install?"),
 callouts=[SAFE_ESD, SAFE_PWR]))

LESSONS.append(L(30, 10, 3, "Fault lab: planted faults, timed diagnosis",
 ["Diagnose and fix three planted hardware faults using the six steps.", "Log each fault with theory, test, result and fix.", "Hand a working PC to the next bench."],
 ["Rebuilt frames or Dell PCs with faults planted by the teacher", "Fault log sheets", "Known-good RAM, SATA cable, monitor cable", "Wrist strap"],
 [("Planted fault", "A deliberate, safe problem the teacher created for you to find."), ("Time to fix", "Minutes from first look to confirmed boot."), ("Hand-over", "Leaving the PC exactly as a customer would expect.")],
 dict(min=3, steps=["Benches rotate: you sit at a PC you did not build. Strap on. Log sheet ready.", "Teacher: 'Each PC has one fault. Three rounds. Log before you touch.'"]),
 dict(min=4, html="""<p>Possible plants (you will not be told which): RAM half-seated · SATA data unplugged · monitor on the iGPU port · GPU not latched · front-panel plug off · 4-pin CPU power off · boot order set to USB with no USB · coin cell out (clock reset) · fan unplugged (fan warning at POST).</p>
<p>Use the ladder: no power / no POST / no boot. Then the code. Then one change at a time.</p>{F0}""", figures=[method6()]),
 dict(min=33, steps=["Round 1 (10 min): observe without touching. Write: symptom, rung, LED pattern if any, theory 1, theory 2.",
      "Test theory 1 with one change. Log the result. Fixed? Verify with a full boot. Not fixed? Theory 2.",
      "Write the fix and the time taken. Teacher checks and plants the next fault while you rotate.",
      "Round 2 (10 min): new PC, same method.",
      "Round 3 (10 min): new PC, same method. This one may have the fault in the firmware settings rather than the hardware.",
      "Hand-over: boots to login, panel on, cables tidy, log signed."]),
 dict(min=3, quiz=[Q("Best first move on any fault:", ["Open the case", "Observe and sort into the ladder", "Replace the PSU", "Reinstall the OS"], 1, "Look before you touch."),
      Q("Your fix worked. Before you move on you…", ["celebrate", "verify with a full boot and log it", "unplug it", "plant a new fault"], 1, "Verify, document, hand over.")]),
 dict(min=2, steps=["Logs to the teacher. PCs on the shelf as found.", "Fastest and most complete logs are read out next lesson."]),
 dict(key_ideas=["Observe → sort (ladder) → code → theory → one change → verify → log.", "The common plants are seating and cables. Check those before anything expensive.", "Hand-over means the customer would not know anything was wrong."],
      questions=[("Round 1: symptom / rung / code / theories / test / fix / time.", 3), ("Round 2: same.", 3), ("Round 3: same.", 3), ("Which fault took longest? What would make it faster next time?", 2)],
      exit="Total faults fixed: ___. Hardest one: ___."),
 callouts=[SAFE_ESD, SAFE_PWR]))

# ---------------------------------------------------------------- WEEK 11
LESSONS.append(L(31, 11, 1, "Boot media and the install: USB, boot menu, partitions",
 ["Create a bootable USB installer.", "Boot from USB using the F12 menu and start an OS install.", "Choose the install target and partition layout correctly."],
 ["Rebuilt frame or Dell PC", "8 GB+ USB stick per bench", "Installer image: Linux Mint (default) or Windows (if the school's licence/IT allows)", "Rufus / balenaEtcher / Ventoy on the teacher PC"],
 [("ISO", "A single file that is an exact image of an install disc."), ("Bootable USB", "A stick prepared so the firmware can start it."), ("Install target", "The drive the OS will be written to; everything on it is erased."), ("Live session", "Linux running from the USB without installing, for testing.")],
 dict(steps=["Teacher explains the OS choice for this lab: the 7050's 7th-gen CPU is not on Windows 11's supported list and Windows 10 is out of support, so the lab default is Linux Mint; Windows benches follow the same steps with the Windows installer.", "Collect your USB stick."]),
 dict(min=10, html="""<p>An installer is just an operating system small enough to run from a USB stick. You write the ISO to the stick (not copy; write), boot the stick with F12, and the installer copies the real OS onto your SSD.</p>
{F0}
<p><b>Example 1.</b> Copying the ISO file onto the stick in Explorer: the stick will not boot. It must be written with Rufus/Etcher/Ventoy so the stick has a boot sector and the files laid out properly.</p>
<p><b>Example 2.</b> Picking the wrong install target erases the wrong drive. Identify by size and model: the 500 GB NVMe, not the 240 GB SATA with your data.</p>
<p><b>Example 3.</b> Secure Boot on + unsigned installer = 'invalid signature'. Turn Secure Boot off in F2 for the install if that happens.</p>""", figures=[partition()]),
 dict(min=24, steps=["Write the ISO to the USB (teacher PC): Rufus → select ISO → GPT/UEFI → Start. Or Etcher → Flash.",
      "Plug the stick into the bench PC. Power on, tap <kbd>F12</kbd>, choose the stick under UEFI boot.",
      "Linux: choose 'Start Linux Mint' then run the installer from the desktop. Windows: Next → Install now → skip the key for now (OEM licence is in the firmware).",
      "Language and keyboard: English (Australia).",
      "Install target: select the NVMe by size/model. Linux: 'Erase disk and install' (GPT, ext4). Windows: delete existing partitions on that disk only, select unallocated, Next.",
      "Set the hostname/computer name to your bench: PC-01 … PC-20. User: student. Password: given by the teacher.",
      "Let it copy. Write the elapsed minutes. When asked, remove the USB and restart.",
      "First boot to the desktop = checkpoint. Do not install anything else yet."]),
 dict(quiz=[Q("A bootable USB is made by…", ["copying the ISO onto the stick", "writing the ISO with Rufus/Etcher/Ventoy", "renaming the ISO", "zipping the ISO"], 1, "Writing lays down the boot structure."),
      Q("The install target is chosen by…", ["drive letter", "size and model", "colour", "alphabetical order"], 1, "Letters change; size and model do not."),
      Q("Why was Linux Mint chosen as the lab default?", ["It is prettier", "The 7th-gen CPU is unsupported by Windows 11 and Windows 10 is out of support", "It has more games", "It needs no RAM"], 1, "A supported OS on an isolated lab network.")]),
 dict(steps=["USB stick labelled and in the bench box. PC shut down."]),
 dict(key_ideas=["ISO → written to USB → F12 → installer → install target by size/model → hostname PC-xx.", "Everything on the target drive is erased. Check twice.", "Secure Boot off if the installer is refused; on again afterwards if the OS supports it."],
      questions=[("OS installed: ___. Install target: ___ (size ___). Hostname: ___. Time to copy: ___ min.", 2), ("Explain why copying an ISO is not the same as writing it.", 2), ("What is the risk at the 'install target' screen and how do you avoid it?", 2), ("Why does the Windows OEM licence not need a typed key on this Dell?", 1)],
      exit="Did you need to change any firmware setting? Which?"),
 callouts=[SAFE_PWR, ("", "Data loss warning", "The install erases the chosen drive completely. Only drives from the bench kit may be used. Never a personal USB with files on it.")]))

LESSONS.append(L(32, 11, 2, "First boot: drivers, updates, accounts and the lab image",
 ["Install drivers and updates on a fresh OS.", "Create the lab user accounts and check the hostname.", "Record the system information for the bench log."],
 ["Freshly installed PC", "Driver installers (Windows) or Driver Manager (Mint) on the teacher USB", "Bench log"],
 [("Driver", "Code that teaches the OS to use a specific piece of hardware."), ("Update", "Fixes and security patches from the OS maker."), ("Activation", "Proving the Windows licence; the Dell's key is stored in the firmware."), ("Image", "A saved copy of a finished install that can be put back quickly.")],
 dict(steps=["Boot to the desktop. Log in as student.", "Teacher: 'A fresh install is half done. Drivers and updates finish it.'"]),
 dict(min=8, html="""<p>Right after an install, the OS knows the basics. It may not know your graphics card's full features, your network card, or the latest security fixes. Drivers and updates fill those gaps. Then you set the names and accounts the lab expects, record the specs, and the PC is 'imaged'.</p>
<p><b>Example 1.</b> Screen stuck at 1024×768 and sluggish: the graphics driver is missing.</p>
<p><b>Example 2.</b> The network port shows 'cable unplugged' with a cable in: wrong or missing network driver.</p>
<p><b>Example 3.</b> Windows says 'not activated' after a clean install on an OEM Dell: usually clears once online; the key lives in the firmware.</p>{F0}""", figures=[terminal(["student@PC-01:~$ hostnamectl", "   Static hostname: PC-01", "  Operating System: Linux Mint 22.2", "            Kernel: Linux 6.14", "student@PC-01:~$ ip link", "2: enp0s31f6: <BROADCAST,MULTICAST> mtu 1500 state DOWN", "    link/ether 3c:7c:3f:11:aa:01"], "PC-01 — terminal")]),
 dict(min=27, steps=["Windows: Device Manager → any yellow triangles? Install the chipset, graphics and network drivers from the teacher USB. Mint: Administration → Driver Manager → apply recommended.",
      "Check the display: native resolution and 60 Hz or better.",
      "Run updates if the lab has internet; otherwise skip and note it in the log.",
      "Confirm the hostname: Windows <code>hostname</code>; Linux <code>hostnamectl</code>. It must be PC-xx matching your bench.",
      "Create a second local account called 'tech' with the password the teacher gives. This is the account you will use for networking.",
      "Record on the bench log: OS and version, CPU, RAM GB, drives, GPU, driver versions, MAC address of the network port (<code>ipconfig /all</code> or <code>ip link</code>).",
      "Set the time zone to Melbourne and check the clock.",
      "Teacher takes an image of one finished bench for the lab (demonstration): what is in it and why."]),
 dict(quiz=[Q("Yellow triangles in Device Manager mean…", ["the device is dangerous", "a driver is missing or broken", "the device is on fire", "nothing"], 1, "Install the right driver."),
      Q("The MAC address is found with…", ["ping", "ipconfig /all or ip link", "F2", "Disk Management"], 1, "It belongs to the network card."),
      Q("An image is…", ["a photo of the PC", "a saved copy of a finished install", "a wallpaper", "a driver"], 1, "Restore many PCs quickly from one image.")]),
 dict(steps=["Log complete and signed. Shut down."]),
 dict(key_ideas=["Fresh install → drivers → updates → hostname PC-xx → accounts → record specs and MAC.", "Missing driver symptoms: wrong resolution, 'cable unplugged', no sound.", "An image saves the finished state so a lab can be restored fast."],
      questions=[("Bench log: OS ___ CPU ___ RAM ___ drives ___ GPU ___ MAC ___", 2), ("Which drivers did you install and how did you know they were needed?", 2), ("Why does the lab want a 'tech' account separate from 'student'?", 2)],
      exit="Is your PC ready for the network? What is its hostname?"),
 callouts=[]))

LESSONS.append(L(33, 11, 3, "Software troubleshooting: boot problems, safe mode, disk health and backups",
 ["Diagnose a no-boot that is software, not hardware.", "Use safe mode / recovery and read SMART disk health.", "Explain the 3-2-1 backup rule."],
 ["Bench PC", "Teacher-planted software faults (boot order, disabled network, corrupted shortcut, full disk)", "CrystalDiskInfo (Windows) or GNOME Disks SMART (Linux)"],
 [("Safe mode", "Starting with only the basic drivers to see if an add-on is the problem."), ("SMART", "Self-monitoring data every drive keeps about its own health."), ("Boot order", "Firmware list of where to look for an OS."), ("3-2-1", "Three copies, two different media, one off-site.")],
 dict(steps=["Boot the PC. Teacher has planted one software fault per bench.", "Sort it: did POST pass? Then it is a software/boot problem."]),
 dict(min=12, html="""<p>When POST passes but the OS misbehaves, the fault is in firmware settings, the boot files, drivers, or the disk itself. The tools are: the firmware boot order, the OS recovery menu (safe mode), the event/system log, and the drive's own SMART report.</p>
<p><b>Example 1.</b> 'No bootable device': boot order points at an empty port, or the SATA data cable is out. Firmware first, then the cable.</p>
<p><b>Example 2.</b> PC boots, then crashes after a driver install: safe mode starts fine. Uninstall that driver.</p>
<p><b>Example 3.</b> Slow, with freezes; SMART shows 'Reallocated sectors: 240' and 'Caution'. The drive is dying. Back up today; replace it.</p>
<p>Backups: 3 copies, 2 kinds of media, 1 somewhere else. A copy on the same disk is not a backup.</p>{F0}""", figures=[boot_chain()]),
 dict(min=20, steps=["Find your planted fault. Log symptom and rung (it should be 'no boot' or 'boots but…').",
      "Theory 1: firmware. F2 → boot order and SATA mode. Fix if wrong.",
      "Theory 2: recovery. Windows: hold Shift + Restart → Troubleshoot → Startup Settings → Safe Mode. Mint: hold Shift at boot → Advanced → recovery mode.",
      "Theory 3: the disk. Run the SMART tool. Write: health status, power-on hours, reallocated sectors, temperature.",
      "Fix the fault, verify with two clean reboots, log it.",
      "Plan a backup for a family PC: list three copies, two media, one off-site. Cost in dollars?"]),
 dict(quiz=[Q("POST passes, then 'No bootable device'. First check:", ["RAM", "Firmware boot order, then the drive cable", "PSU", "Monitor"], 1, "Boot order is the cheapest fix."),
      Q("Safe mode helps because…", ["it is faster", "it loads only basic drivers, so an add-on driver can be ruled in or out", "it fixes RAM", "it reinstalls Windows"], 1, "Isolation by subtraction."),
      Q("3-2-1 is…", ["three drives in one PC", "three copies, two media, one off-site", "a BIOS version", "a beep code"], 1, "The rule that survives fire, theft and failure.")]),
 dict(steps=["Fault logs in. Shut down."]),
 dict(key_ideas=["POST passed → software/boot: firmware order → recovery/safe mode → logs → SMART.", "SMART warnings mean back up now, replace soon.", "3-2-1 backups. A second copy on the same disk is not a backup."],
      questions=[("Planted fault: symptom / theories / test / fix.", 3), ("SMART: status ___ hours ___ reallocated ___ temp ___", 1), ("Backup plan for a family PC with 300 GB of photos: three copies, two media, one off-site, cost.", 4)],
      exit="What is one thing on your own device that is not backed up?"),
 callouts=[]))

# ---------------------------------------------------------------- WEEK 12
LESSONS.append(L(34, 12, 1, "Networks: NICs, MAC addresses, switches and what a LAN is",
 ["Define LAN, NIC, MAC address and switch.", "Find your PC's MAC address and the switch's job.", "Explain the difference between a hub, a switch and a router."],
 ["Bench PC", "The lab switch (unplugged, to look at)", "A patch lead", "Worksheet"],
 [("LAN", "Local area network: devices in one place joined together."), ("NIC", "Network interface card: the Ethernet port and its chip."), ("MAC address", "A 48-bit hardware address burnt into every NIC, written as 12 hex characters."), ("Switch", "A box that learns which MAC is on which port and sends frames only where needed."), ("Router", "Joins different networks together, e.g. your LAN to the internet.")],
 dict(steps=["Boot. Teacher holds up the switch and a patch lead: 'This is the whole network we will build.'", "Guess: how does the switch know which port to send to?"]),
 dict(min=14, html="""<p>A LAN is computers in one room (or building) joined by cables to a switch. Each computer's network port is a <b>NIC</b> with a unique <b>MAC address</b>, like a serial number. Data goes in chunks called <b>frames</b>; each frame has a 'to' MAC and a 'from' MAC. The switch reads the 'from' on every frame and learns which port each MAC lives on. After that, it sends frames to the right port only.</p>
{F0}
<p><b>Example 1 — hub vs switch.</b> An old hub repeated every frame to every port, like shouting in a room. A switch is like passing a note to the right person.</p>
<p><b>Example 2 — router.</b> The switch joins PCs on one network. A router joins networks: your LAN to your ISP's network, and on to the internet. Our lab has no router: it is an island on purpose.</p>
<p><b>Example 3 — MAC.</b> <code>3C-7C-3F-11-AA-02</code>: the first half says who made the chip, the second half is the unit. Change the network card and the MAC changes with it.</p>""", figures=[lan()]),
 dict(min=18, steps=["Find your MAC: Windows <code>ipconfig /all</code> (look for 'Physical Address' under Ethernet). Linux <code>ip link</code> (the 'link/ether' line). Write it.",
      "Compare with your neighbour. Which half matches? That is the maker code.",
      "Look at the switch: count the ports, find the link lights, the power socket, the uplink port if any. Write the port count.",
      "Look at the patch lead: count the wires through the plug (8), find the clip, read the jacket text (Cat5e / Cat6).",
      "Draw the lab LAN: 20 PCs, one switch, teacher PC. Label one PC with your MAC.",
      "Write one sentence each: what a hub does, what a switch does, what a router does."]),
 dict(quiz=[Q("A MAC address is…", ["set by the user", "burnt into the NIC by the maker", "the same on every PC", "given by the switch"], 1, "Hardware address, unique."),
      Q("A switch sends a frame…", ["to every port", "only to the port where the destination MAC lives (once learned)", "to the router", "to the internet"], 1, "It learns from the 'from' addresses."),
      Q("Our lab has no router. That means…", ["no network at all", "PCs can talk to each other but not to other networks", "no MAC addresses", "no switch"], 1, "An island LAN.")]),
 dict(steps=["Worksheets in. Shut down. Switch stays unplugged until Week 15."]),
 dict(key_ideas=["LAN = devices in one place on a switch. NIC = the port + chip. MAC = its hardware address.", "Switch learns MAC→port and delivers frames to one port. Hub shouted to all. Router joins networks.", "Our lab is an island: switch only, no router, no internet."],
      questions=[("My MAC: ___. Maker half: ___. Neighbour's MAC: ___.", 1), ("Switch: ports ___. Lead: category ___, wires ___.", 1), ("Draw the lab LAN with labels.", 4), ("Hub / switch / router in one sentence each.", 3)],
      exit="Why does the switch need to 'learn' before it can be clever?"),
 callouts=[]))

LESSONS.append(L(35, 12, 2, "How data travels: frames, packets, ports and the four layers",
 ["Describe the four-layer model and what each layer adds.", "Explain the difference between a MAC address, an IP address and a port number.", "Trace a ping and a chat message through the layers."],
 ["Bench PC", "Envelopes and slips of paper (one set per bench)", "Worksheet"],
 [("Frame", "The Link-layer chunk: MAC to MAC, on one cable segment."), ("Packet", "The Internet-layer chunk: IP to IP, across networks."), ("Port number", "A number that says which program on the PC should get the data, e.g. 2323 for our chat."), ("Encapsulation", "Wrapping data in headers, layer by layer."), ("Protocol", "An agreed set of rules, e.g. TCP, IP, ICMP, Ethernet.")],
 dict(steps=["Boot. Each bench gets three envelopes of different sizes and a slip of paper.", "Write a short message on the slip. That is your 'data'."]),
 dict(min=14, html="""<p>Sending data is like posting a letter inside an envelope inside a parcel. Each layer adds its own label and only reads its own label at the other end.</p>
{F0}
<p><b>Example 1 — ping.</b> Ping is an ICMP message at the Internet layer. It has IP addresses but no port, because it is not for any program; the OS answers it directly.</p>
<p><b>Example 2 — our chat.</b> Your text (Application) → TCP adds ports 51000→2323 (Transport) → IP adds 192.168.10.11→.12 (Internet) → Ethernet adds the MACs (Link) → onto the cable. The server PC unwraps in reverse and hands the text to the program listening on 2323.</p>
<p><b>Example 3 — wrong layer, wrong fix.</b> 'Minecraft can't connect' but ping works: the Link and Internet layers are fine. Look at the Transport/Application layers: port, firewall, is the game actually hosting?</p>""", figures=[layers()]),
 dict(min=18, steps=["Put the slip in the small envelope. Write 'port 2323' on it. That is the Transport layer.",
      "Put that in the middle envelope. Write 'to 192.168.10.12 from 192.168.10.11'. Internet layer.",
      "Put that in the big envelope. Write the two MAC addresses. Link layer.",
      "Hand it to the 'switch' (another bench). They read ONLY the outer envelope and pass it to the right bench. Why don't they open it?",
      "The receiving bench unwraps in reverse and reads the message. Which envelope told them which program gets it?",
      "On your PC: <code>netstat -an</code> (Windows) or <code>ss -tln</code> (Linux). Find any line with 'LISTENING' / 'LISTEN' and a port number. That is a program waiting at a door.",
      "Write the three addresses for your PC in the right boxes: MAC (from last lesson), IP (next week), port (2323 for chat)."]),
 dict(quiz=[Q("Which layer adds port numbers?", ["Link", "Internet", "Transport", "Application"], 2, "TCP/UDP ports choose the program."),
      Q("Ping has no port because…", ["it is broken", "it is answered by the OS at the Internet layer, not by a program", "it uses MAC only", "ports are optional"], 1, "ICMP lives at the Internet layer."),
      Q("The switch reads…", ["the message", "the IP addresses", "only the MAC addresses on the outer frame", "the port"], 2, "Link layer only.")]),
 dict(steps=["Envelopes back in the kit. Shut down."]),
 dict(key_ideas=["Application → Transport (ports) → Internet (IP) → Link (MAC, cable). Receiver unwraps in reverse.", "MAC = which card, IP = which computer on which network, port = which program.", "Ping works but the app does not → look at ports/firewall/is it hosting."],
      questions=[("Label the four layers and what each adds.", 4), ("MAC vs IP vs port: one line each.", 3), ("Trace a chat message from PC-01 to PC-02 through the layers.", 4), ("Why does the switch not need IP addresses?", 2)],
      exit="Which layer would a bad cable break? Which would a wrong port number break?"),
 callouts=[]))

LESSONS.append(L(36, 12, 3, "Cables and standards: Cat5e/6, twisted pairs, RJ45 and the rules",
 ["Explain why Ethernet pairs are twisted and what Cat5e/Cat6 mean.", "State the 100 m rule and the difference between straight-through and crossover.", "State what students may and may not plug into (the ACMA registered-cabler rule)."],
 ["Cut lengths of Cat5e and Cat6 (strip 100 mm to show pairs)", "An RJ45 plug and a keystone jack", "Worksheet"],
 [("Twisted pair", "Two wires twisted together so interference affects both equally and cancels."), ("Cat5e / Cat6", "Cable categories: 5e does 1 Gb/s to 100 m; 6 does 10 Gb/s to 55 m."), ("RJ45 / 8P8C", "The 8-pin plug on the end of an Ethernet lead."), ("Patch lead", "A short cable with plugs on both ends; fine for anyone to make and use."), ("Registered cabler", "In Australia, the licensed person who may install fixed cabling in walls and ceilings.")],
 dict(steps=["Pass the stripped samples around. Count the pairs. Notice each pair's twist rate is different.", "Teacher: 'Next week you make one of these. Today you learn what you are making.'"]),
 dict(min=14, html="""<p>Inside an Ethernet cable are four pairs. Twisting makes noise hit both wires of a pair almost equally, and the receiver only cares about the difference, so the noise cancels. Different twist rates stop pairs interfering with each other. That is why, at the plug, you untwist as little as possible.</p>
{F0}
<p><b>Example 1 — categories.</b> Cat5e is enough for gigabit to 100 m: our whole lab. Cat6 has a plastic spline and tighter twists for 10 gigabit over short runs. Cat6 costs more and is stiffer; it is not 'faster' for us.</p>
<p><b>Example 2 — straight vs crossover.</b> A straight-through lead is T568B on both ends. A crossover (B one end, A the other) was for PC-to-PC without a switch. Modern NICs auto-detect (Auto-MDIX), so straight-through works everywhere now.</p>
<p><b>Example 3 — the law.</b> In Australia, cabling fixed in a building (wall sockets, ceiling runs, patch panels) must be done by an ACMA-registered cabler. Making and plugging in a patch lead is fine. In this lab you only ever plug into the lab switch and your own PCs, never the school's wall ports.</p>""", figures=[twist()]),
 dict(min=18, steps=["On the Cat6 sample find the plastic spline between the pairs. Is it in the Cat5e? Write the difference.",
      "Measure 50 mm of one pair and count the twists. Do another pair. Different?",
      "Read the jacket print: category, maker, maybe 'UTP' (unshielded). Write it.",
      "Look at the RJ45 plug: 8 gold pins, the clip, the bar that grips the jacket. Look at the keystone jack: where the wires are punched down.",
      "Write the rule: max ___ m for one Ethernet run. Our longest bench-to-switch lead will be about ___ m.",
      "Write, in your own words, what you may plug into in this lab and what you may not. Both partners sign it."]),
 dict(quiz=[Q("Why twist the pairs?", ["It looks neat", "Noise hits both wires equally and cancels at the receiver", "To make the cable stronger", "To colour-code it"], 1, "Differential signalling."),
      Q("A gigabit lab that never exceeds 30 m needs…", ["Cat6a at least", "Cat5e is enough", "fibre", "Cat3"], 1, "Cat5e carries 1 Gb/s to 100 m."),
      Q("Who may install a new wall socket at school?", ["Any student in this course", "An ACMA-registered cabler", "The teacher", "Anyone with a crimper"], 1, "Fixed cabling is licensed work in Australia; patch leads are not.")]),
 dict(steps=["Samples back in the kit. Signed rule sheet in the folder."]),
 dict(key_ideas=["Four twisted pairs; twisting cancels noise; untwist as little as possible at the plug.", "Cat5e: 1 Gb/s to 100 m (enough for us). Cat6: 10 Gb/s to 55 m. 100 m max per run.", "Straight-through = B both ends; modern NICs auto-cross. Fixed cabling = registered cabler only; patch leads are fine."],
      questions=[("Cat5e vs Cat6: two differences you can see.", 2), ("Twists per 50 mm: pair 1 ___ pair 2 ___. Why different?", 2), ("Explain the 100 m rule and why a 5 m patch lead at each end counts.", 2), ("What may you plug into in this lab? What may you not? Why?", 3)],
      exit="Which standard will you use on both ends next week?"),
 callouts=[("", "Lab cabling rule", "You only plug into the lab switch and the bench PCs. School wall ports and patch panels are off limits: fixed cabling in Australia is registered-cabler work.")]))
