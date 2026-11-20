from visuals import *
from content_a import L, Q, STD_PACK, SAFE_ESD, SAFE_PSU, SAFE_PWR

LESSONS = []
SAFE_CRIMP = ("", "Crimp tool and cutters", "The crimp tool's blade and the flush cutters are sharp. Cut away from your hand, keep the tool closed on the bench, and never crimp a plug with a finger inside the jaws.")
SAFE_CABLE = ("", "Lab cabling rule", "Patch leads go between bench PCs and the lab switch only. Never into a school wall port or patch panel.")

CHAT_SERVER = '''import socket, threading

HOST = "0.0.0.0"      # listen on every network card
PORT = 2323           # our chat door (telnet's usual door is 23, this avoids needing admin)
clients = {}          # socket -> name

def broadcast(text, sender=None):
    for c in list(clients):
        if c is not sender:
            try:
                c.sendall((text + "\\r\\n").encode())
            except OSError:
                clients.pop(c, None)

def handle(conn, addr):
    conn.sendall(b"Name? ")
    name = conn.recv(64).decode(errors="ignore").strip() or str(addr[0])
    clients[conn] = name
    broadcast(f"*** {name} joined from {addr[0]}")
    while True:
        data = conn.recv(1024)
        if not data:
            break
        line = data.decode(errors="ignore").strip()
        if line.lower() == "/quit":
            break
        if line:
            broadcast(f"<{name}> {line}", sender=conn)
    broadcast(f"*** {name} left")
    clients.pop(conn, None)
    conn.close()

srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
srv.bind((HOST, PORT))
srv.listen()
print(f"Chat server listening on port {PORT}. Ctrl+C to stop.")
while True:
    conn, addr = srv.accept()
    threading.Thread(target=handle, args=(conn, addr), daemon=True).start()
'''

CHAT_CLIENT = '''import socket, threading, sys

SERVER = sys.argv[1] if len(sys.argv) > 1 else "192.168.10.11"
PORT = 2323

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SERVER, PORT))

def listen():
    while True:
        data = s.recv(1024)
        if not data:
            print("Disconnected."); break
        print(data.decode(errors="ignore"), end="")

threading.Thread(target=listen, daemon=True).start()
while True:
    line = input()
    s.sendall((line + "\\n").encode())
    if line.strip().lower() == "/quit":
        break
'''

# ---------------------------------------------------------------- WEEK 13
LESSONS.append(L(37, 13, 1, "The T568B pinout: colours, order and why both ends match",
 ["Recite the T568B wire order from memory.", "Hold an RJ45 plug the right way and identify pin 1.", "Explain which pins carry data at 100 Mb/s and 1 Gb/s."],
 ["Cut 300 mm lengths of Cat5e (two per pair)", "RJ45 plugs (a handful to examine, not crimp yet)", "Pinout card", "Stripper"],
 [("T568B", "The wiring standard we use: white-orange, orange, white-green, blue, white-blue, green, white-brown, brown."), ("T568A", "The other standard; same wires, orange and green pairs swapped."), ("Pin 1", "The leftmost pin when the clip is down and the gold pins face you."), ("Straight-through", "Same standard on both ends; what every lab lead is.")],
 dict(steps=["Collect two cut lengths and the pinout card.", "Teacher reads the B order aloud; the class says it back twice."]),
 dict(min=14, html="""<p>Eight wires, one correct order. T568B is the common standard in Australia and the one we use on both ends. Memorise it as four pairs: <b>orange, green, blue, brown</b>, with the striped (white) wire of each pair first, except that the blue pair sits in the middle and splits the green pair.</p>
{F0}
<p><b>Example 1 — 100 Mb/s.</b> Fast Ethernet uses only pins 1,2 (send) and 3,6 (receive). The blue and brown pairs are spare. That is why a cable with a broken blue wire can still 'work' at 100 Mb/s and then fail at gigabit.</p>
<p><b>Example 2 — 1 Gb/s.</b> Gigabit uses all four pairs, in both directions at once. All eight wires must be right.</p>
<p><b>Example 3 — A on one end, B on the other.</b> That is a crossover cable. Old gear needed it to connect PC to PC. Modern NICs swap automatically, so the cable works, but anyone testing it would call it a miswire. Both ends B, always.</p>""", figures=[pinout()]),
 dict(min=18, steps=["Strip 25 mm of jacket from one cut length. Fan out the four pairs. Name each pair by colour.",
      "Untwist and lay the eight wires flat on the pinout card in B order. Check with your partner, then swap and check theirs.",
      "Hold an empty RJ45 plug clip-down, pins toward you. Point to pin 1 and pin 8. Flip it: which side is the clip now?",
      "Say the B order out loud without the card. Partner checks. Three times each.",
      "On the card, write which pins are used at 100 Mb/s and which at 1 Gb/s.",
      "Lay the eight wires in A order next to the B set. Circle the two pairs that moved."]),
 dict(quiz=[Q("In T568B, pin 1 is…", ["blue", "white-orange", "green", "brown"], 1, "White-orange, then orange."),
      Q("Which pair splits the green pair in B?", ["orange", "brown", "blue", "none"], 2, "Blue sits on pins 4 and 5, between white-green (3) and green (6)."),
      Q("Gigabit Ethernet uses…", ["pins 1,2,3,6 only", "all eight wires", "pins 4,5 only", "the clip"], 1, "All four pairs, both directions.")]),
 dict(steps=["Wires and plugs back in the kit box. Card in the folder."]),
 dict(key_ideas=["T568B: white-orange, orange, white-green, blue, white-blue, green, white-brown, brown.", "Clip down, pins facing you: pin 1 on the left.", "100 Mb/s uses 1,2,3,6; gigabit uses all eight. Both ends B = straight-through."],
      questions=[("Write the B order 1–8 from memory.", 2), ("Write the A order 1–8 and circle what changed.", 2), ("Why can a cable with a broken blue wire work at 100 Mb/s but not at 1 Gb/s?", 2), ("Describe how to find pin 1 on a plug.", 1)],
      exit="Say the B order to the teacher on the way out."),
 callouts=[SAFE_CRIMP]))

LESSONS.append(L(38, 13, 2, "Make a patch lead: strip, order, trim, insert, crimp",
 ["Terminate one end of a Cat5e cable to T568B.", "Check the termination through the plug before and after crimping.", "Terminate the second end and tug-test the lead."],
 ["2 m Cat5e per pair (plus spare)", "RJ45 plugs (at least 6 per pair: you will waste some)", "Crimp tool with stripper and cutter", "Flush cutters", "Pinout card", "Safety glasses"],
 [("Strain relief", "The bar in the plug that clamps the jacket so pulling the cable does not pull the wires."), ("Insulation displacement", "How the gold pins cut through the wire's insulation when crimped."), ("Tug test", "A firm pull on the cable after crimping; nothing should move."), ("Boot", "Optional rubber cover that protects the clip; it goes on BEFORE the plug.")],
 dict(min=4, steps=["Safety glasses on. Tools laid out: crimper, cutters, card, plugs, cable.", "Teacher does one end under the camera, narrating the six steps."]),
 dict(min=8, html="""<p>Six steps, same every time. Rushing step 3 (order) or step 5 (insert all the way) causes almost every failed cable. Click through the steps below before you start, then follow them at the bench.</p>
{F0}
<p><b>Example 1.</b> Wires cut at a slant: pins 1 and 2 reach the end of the plug, pins 7 and 8 stop short. The tester shows 7 and 8 open. Cut off, start again.</p>
<p><b>Example 2.</b> Jacket not under the strain-relief bar: the lead works on the bench, then fails the first time someone trips on it.</p>
<p><b>Example 3.</b> Untwisted 40 mm back to make the order easier: the lead passes a basic tester but drops gigabit link randomly (crosstalk). Keep the twist within 13 mm.</p>""", figures=[crimp()]),
 dict(min=26, steps=["Slide a boot onto the cable if using one (open end toward the end you are terminating).",
      "Strip 25 mm of jacket. Check no wire is nicked. If copper shows anywhere, cut and re-strip.",
      "Untwist only as far as needed. Straighten and order the wires in B. Say the order aloud. Press flat.",
      "Trim all eight straight across at 13 mm from the jacket.",
      "Clip down, pin 1 left. Push the wires in until every one touches the end AND the jacket is under the bar. Look through the clear plastic: eight wire ends, all at the front.",
      "Navigator check before the crimp: order through the plastic, jacket under the bar.",
      "Crimp until the tool clicks through. Tug test.",
      "Second end: repeat steps 1–7. Then hold both plugs side by side, clips down: the colours should match left to right.",
      "Label the lead with your bench number and 'B/B'. Keep it: you test it next lesson and use it in Week 15."]),
 dict(min=4, quiz=[Q("The wires must reach…", ["half-way into the plug", "the very end of the plug, all eight", "just past the bar", "anywhere"], 1, "Short wires = open pins."),
      Q("The jacket must sit…", ["outside the plug", "under the strain-relief bar", "in the clip", "nowhere special"], 1, "Otherwise a tug pulls the wires out of the pins."),
      Q("You untwisted 40 mm to make ordering easy. Result at gigabit:", ["works perfectly", "random drop-outs from crosstalk", "faster", "nothing"], 1, "Keep twists within 13 mm.")]),
 dict(steps=["Wire offcuts in the bin, tools closed and in the box, lead labelled and in the bench folder.", "Glasses back on the rack."]),
 dict(key_ideas=["Strip 25 mm → order B → trim 13 mm straight → insert to the end, jacket under the bar → crimp → tug test.", "Check through the plastic BEFORE crimping; after is too late.", "Both ends B; plugs side by side show matching colours."],
      questions=[("Number of plugs used today: ___. Reasons for any wasted: ___", 2), ("Describe what you look for through the clear plastic before crimping.", 2), ("Why does a slanted cut cause open pins?", 2), ("Explain the strain-relief bar to someone who has never seen a plug.", 2)],
      exit="Your lead is labelled and in the folder: Yes / No."),
 callouts=[SAFE_CRIMP, SAFE_CABLE], ))
LESSONS[-1]["do"]["print_html"] = "<h2>The six steps</h2>" + crimp_print()

LESSONS.append(L(39, 13, 3, "Test, diagnose, fix: the LAN tester and what each light means",
 ["Use a cable tester to pass or fail a patch lead.", "Read open, short, miswire and split-pair results from the lights.", "Re-terminate a failed end and retest."],
 ["Your patch lead from last lesson", "LAN cable tester (master + remote) per two benches", "Crimp kit, spare plugs", "A teacher-made 'mystery' lead per bench"],
 [("Open", "A wire not connected at one end: that number never lights at the remote."), ("Short", "Two wires touching: two lights at once."), ("Miswire", "Wrong order: the remote lights in a different sequence."), ("Split pair", "Right pins, wrong pairing (e.g. 3 and 5 swapped): passes a basic tester, fails at speed."), ("Continuity", "An unbroken electrical path.")],
 dict(steps=["Pair up with the next bench to share a tester. Teacher shows the sequence: master sends on 1→8, remote should light 1→8.", "Try the simulator first: pick each fault and watch."]),
 dict(min=10, html="""<p>A basic tester sends a pulse down each wire in turn. The remote unit lights the pin it arrives on. A good straight-through lead lights 1,2,3,4,5,6,7,8 in order on both units. Anything else tells you what went wrong and, usually, which end.</p>
{F0}
<p><b>Example 1 — open.</b> Master lights 4, remote shows nothing for 4. Wire 4 did not reach its pin on one end. Look at both plugs; the short wire is visible through the plastic.</p>
<p><b>Example 2 — miswire.</b> Master 2, remote 3; master 3, remote 2. Green and orange swapped on one end. Cut that end off.</p>
<p><b>Example 3 — split pair.</b> Everything lights 1→8 in order, but you used white-blue on pin 3 and white-green on pin 5. The tester cannot tell. The cable links but drops out at gigabit. Only a visual check or a certifier catches it, so the Navigator check before crimping matters.</p>""", figures=[tester()]),
 dict(min=20, steps=["Test your own lead. Write the sequence for both units. Pass?",
      "If it failed: identify the fault type (open/short/miswire) and the end. Cut that plug off, re-terminate, retest. Log plugs used.",
      "Test the teacher's mystery lead. Write the fault type. Open both plugs' plastic to the light and find the cause by eye.",
      "Swap mystery leads with another bench and repeat.",
      "Visual split-pair check on your own lead: pins 3 and 6 must be the SAME colour family (both green). Pins 4 and 5 both blue. Write pass/fail.",
      "Final: lead passes tester AND visual check → write 'TESTED' on the label with the date."]),
 dict(quiz=[Q("Remote never lights 7. Fault:", ["short", "open on wire 7", "miswire", "split pair"], 1, "No arrival = no path."),
      Q("Two remote lights come on together. Fault:", ["open", "short", "miswire", "good"], 1, "Two wires touching."),
      Q("A basic tester passes a lead that drops out at gigabit. Likely:", ["open", "split pair", "too long", "wrong colour boot"], 1, "Right pins, wrong pairing; the tester cannot see it.")]),
 dict(steps=["Testers off (battery!) and back in their boxes. Leads in folders.", "Offcuts binned, tools closed."]),
 dict(key_ideas=["Good lead: 1→8 in order on both units.", "Open = missing light; short = two lights; miswire = wrong order; split pair = passes but fails at speed.", "Fix = cut the bad end, re-terminate, retest. Visual pair check catches splits."],
      questions=[("Your lead: master sequence ___ remote sequence ___ result ___", 1), ("Mystery lead 1: fault type ___ cause seen ___. Mystery lead 2: ___", 2), ("Why can a basic tester miss a split pair?", 2), ("A lead passes at the bench but fails after a week in use. Two likely causes?", 2)],
      exit="Plugs used across both lessons: ___. Target for a technician: 2 per lead."),
 callouts=[SAFE_CRIMP, SAFE_CABLE]))

# ---------------------------------------------------------------- WEEK 14
LESSONS.append(L(40, 14, 1, "IP addresses: dotted decimal, binary and the private ranges",
 ["Convert an octet between decimal and binary.", "Explain why an IP address is four numbers from 0 to 255.", "Name the private address ranges and why we use 192.168.10.x."],
 ["Bench PC", "Binary place-value card (128 64 32 16 8 4 2 1)", "Worksheet"],
 [("IPv4 address", "A 32-bit number written as four decimal octets, e.g. 192.168.10.11."), ("Octet", "One of the four 8-bit groups; 0–255."), ("Private range", "Addresses reserved for inside networks: 10.x.x.x, 172.16–31.x.x, 192.168.x.x."), ("Binary", "Base 2: each digit is 0 or 1 and each place is worth double the one to its right.")],
 dict(steps=["Boot. Open the bit calculator below.", "Teacher: 'A MAC is who you are. An IP is where you are. Today, where.'"]),
 dict(min=14, html="""<p>Computers address each other with 32-bit numbers. Humans cannot read 32 bits, so we chop them into four groups of eight (octets) and write each as a decimal 0–255. 192.168.10.11 is just a friendly way of writing 11000000.10101000.00001010.00001011.</p>
{F0}
<p><b>Example 1 — converting.</b> 192 = 128 + 64 = 11000000. 10 = 8 + 2 = 00001010. 255 = all eight bits on. 256 is impossible: eight bits only reach 255.</p>
<p><b>Example 2 — private ranges.</b> Addresses starting 10., 172.16–31., or 192.168. are never used on the public internet. Every home and school reuses them. Our lab uses 192.168.10.0/24: 192.168.10.1 to .254 available, .11–.30 for benches.</p>
<p><b>Example 3 — special ones.</b> 127.0.0.1 is 'myself' (loopback). x.x.x.0 is the network's name and x.x.x.255 is 'everyone' (broadcast); you never give those to a PC.</p>""", figures=[ipbits()]),
 dict(min=18, steps=["Convert to binary on paper using the place-value card: 192, 168, 10, 11. Check each in the calculator.",
      "Convert to decimal: 11000000, 00010000, 11111111, 00000001.",
      "Write your bench's lab address: 192.168.10.(10 + bench number). Bench 7 = 192.168.10.17.",
      "In the calculator, put your address in A and your neighbour's in B with mask /24. Are you on the same network? Now try B = 192.168.11.12. Same?",
      "List the three private ranges and one reason each is useful.",
      "Find what your PC has NOW: <code>ipconfig</code> or <code>ip a</code>. Probably 169.254.x.x or nothing: no network yet. Write it down."]),
 dict(quiz=[Q("An octet can be at most…", ["99", "255", "256", "1024"], 1, "Eight bits: 2^8 − 1 = 255."),
      Q("192.168.10.0 is…", ["a PC's address", "the network's own name; never given to a PC", "the router", "a broadcast"], 1, ".0 names the network; .255 is broadcast."),
      Q("127.0.0.1 is…", ["the switch", "the teacher's PC", "'myself' (loopback)", "the internet"], 2, "Pinging it tests your own TCP/IP stack.")]),
 dict(steps=["Worksheet in. Shut down."]),
 dict(key_ideas=["IPv4 = 32 bits = four octets 0–255. Place values 128 64 32 16 8 4 2 1.", "Private ranges: 10/8, 172.16/12, 192.168/16. Lab: 192.168.10.x, benches .11–.30.", "127.0.0.1 = me; .0 = the network; .255 = everyone."],
      questions=[("192 = ___ binary. 168 = ___. 10 = ___. 11 = ___.", 2), ("11000000 = ___. 00010000 = ___. 11111111 = ___.", 1), ("Your lab address: 192.168.10.___. Why that number?", 1), ("Name the three private ranges.", 2), ("What does your PC show right now and why?", 2)],
      exit="Say your lab IP and your MAC. Which one could change if you swapped the network card?"),
 callouts=[]))

LESSONS.append(L(41, 14, 2, "Subnet masks: who is on my network, and who needs a router",
 ["Explain what a /24 subnet mask does.", "Work out whether two addresses are on the same network.", "Explain why the lab needs no gateway and what a gateway is for."],
 ["Bench PC", "Bit calculator", "Worksheet"],
 [("Subnet mask", "A pattern of 1s then 0s that says which part of the address is the network and which is the host."), ("/24", "CIDR notation: the first 24 bits are the network; same as 255.255.255.0."), ("Host", "The part of the address that identifies one PC within the network."), ("Default gateway", "The router's address: where packets go when the destination is on a different network.")],
 dict(steps=["Open the bit calculator. Set A = your lab address, B = 192.168.10.1, mask /24.", "Teacher: 'The mask draws a line through the address. Left of the line: the street. Right: the house number.'"]),
 dict(min=14, html="""<p>A PC decides for itself whether another address is 'local'. It ANDs its own address with the mask to get its network, does the same to the destination, and compares. Same network → talk directly through the switch (ARP for the MAC, send). Different → hand the packet to the default gateway, a router. No router in our lab means different networks simply cannot talk. That is the whole point of an isolated lab.</p>
{F0}
<p><b>Example 1.</b> 192.168.10.11 /24 and 192.168.10.42 /24: first 24 bits match (192.168.10). Same network.</p>
<p><b>Example 2.</b> 192.168.10.11 /24 and 192.168.11.11 /24: third octet differs. Different network. No gateway → 'Destination unreachable'.</p>
<p><b>Example 3.</b> 192.168.10.11 /16 and 192.168.11.11 /16: now only 16 bits are the network, so both are in 192.168.x.x. Same network. The mask, not the numbers, decides.</p>""", figures=[ipbits()]),
 dict(min=18, steps=["In the calculator, keep A = your address. Try B = 192.168.10.200, 192.168.20.11, 10.0.0.5, each at /24. Write same/different for each.",
      "Change the mask to /16 and repeat the three. What changed and why?",
      "Change the mask to /25 with B = 192.168.10.200. Same or different? Work out where the line falls (hint: 128).",
      "Write 255.255.255.0 in binary. Count the 1s. That is why it is /24.",
      "Write the lab network plan on the worksheet: network 192.168.10.0/24, mask 255.255.255.0, benches .11–.30, teacher .1, gateway: none.",
      "Explain in two sentences what would happen if bench 5 typed 192.168.11.15 by mistake."]),
 dict(quiz=[Q("255.255.255.0 is the same as…", ["/8", "/16", "/24", "/32"], 2, "24 ones then 8 zeros."),
      Q("Two /24 addresses with a different third octet are…", ["the same network", "different networks; they need a router", "both broadcast", "invalid"], 1, "The network part differs."),
      Q("Our lab has no default gateway because…", ["it is broken", "all PCs are on one network and there is nowhere else to go", "gateways cost money", "Linux does not need one"], 1, "Isolated single network.")]),
 dict(steps=["Worksheet in. Shut down."]),
 dict(key_ideas=["Mask = 1s for the network part, 0s for the host part. /24 = 255.255.255.0.", "Same network after ANDing → direct via the switch; different → needs a router (gateway).", "Lab: 192.168.10.0/24, benches .11–.30, teacher .1, no gateway."],
      questions=[("A = your address. B = .200 /24 ___, 192.168.20.11 /24 ___, 10.0.0.5 /24 ___. At /16: ___ ___ ___.", 2), ("/25 with B = .200: same or different? Show the AND.", 3), ("Why is a mistyped third octet worse than a mistyped fourth octet?", 2), ("What is a default gateway and why don't we have one?", 2)],
      exit="In one line: how does a PC decide 'local or not'?"),
 callouts=[]))

LESSONS.append(L(42, 14, 3, "Static IP, link lights and the first ping",
 ["Set a static IP address and mask on Windows and Linux.", "Read the NIC link light and the switch port light.", "Ping yourself, then confirm the address with ipconfig / ip a."],
 ["Bench PC", "Lab switch (powered on today)", "Your tested patch lead", "Address plan"],
 [("Static IP", "An address you type in, which never changes."), ("DHCP", "A service that hands out addresses automatically; we have none, so we go static."), ("Link light", "The LED on the NIC and switch port: lit = cable and both ends are electrically talking."), ("Loopback", "127.0.0.1: the address that means 'this PC'.")],
 dict(steps=["Switch on, patch lead from your NIC to the port with your bench number.", "Watch the link light. On? Good: Link layer works. Off? Reseat both ends; swap the lead if still dark."]),
 dict(min=10, html="""<p>Without a router or DHCP server, nothing will give your PC an address. You set it yourself: address 192.168.10.(10 + bench), mask 255.255.255.0, gateway empty. Then you prove each layer from the bottom: link light (cable), <code>ip a</code> (address set), <code>ping 127.0.0.1</code> (stack works), <code>ping</code> your own address (NIC works).</p>
{F0}
<p><b>Example 1.</b> Link light off: it is never the IP settings. Cable, port, or NIC.</p>
<p><b>Example 2.</b> Link light on, <code>ping 127.0.0.1</code> fails: the OS's TCP/IP stack is broken or the firewall is blocking even itself. Rare; reboot first.</p>
<p><b>Example 3.</b> Everything local passes but a neighbour does not answer: that is next lesson. Stop at your own address today.</p>""", figures=[ladder()]),
 dict(min=22, steps=["Windows: Settings → Network → Ethernet → IP assignment → Edit → Manual → IPv4 on → address, mask 255.255.255.0 (or prefix 24), gateway blank → Save. Linux Mint: Network icon → Wired Settings → ⚙ → IPv4 → Manual → address, netmask, no gateway → Apply, then toggle the connection off and on.",
      "Confirm: Windows <code>ipconfig</code>; Linux <code>ip a</code>. Your address and /24 should appear. Write what you see.",
      "<code>ping 127.0.0.1</code> (Windows: 4 replies; Linux: Ctrl+C after 4). Write the result.",
      "Ping your own lab address. Write the result and the time in ms.",
      "Look at the switch port light for your bench: colour / blink. Write it. Unplug the lead: what happens to it?",
      "Fault drill: set the mask to 255.255.0.0 by mistake, save, run <code>ipconfig</code>/<code>ip a</code>. Does the PC complain? Why not? Put it back to /24.",
      "Second fault drill: type 192.168.10.(10 + bench) but with a typo in the third octet. Save. Ping yourself: still works! Why is that dangerous? Fix it."]),
 dict(quiz=[Q("No link light. The first thing to check is…", ["the IP address", "the cable and both plugs", "the subnet mask", "the firewall"], 1, "Link light is layer 1/2: physical."),
      Q("ping 127.0.0.1 tests…", ["the cable", "the switch", "your own TCP/IP stack", "the neighbour"], 2, "It never leaves the PC."),
      Q("Why do we type the address instead of getting one automatically?", ["Typing is faster", "There is no DHCP server on our island LAN", "Linux cannot do DHCP", "The switch forbids it"], 1, "No router/DHCP = static.")]),
 dict(steps=["Leave the static IP set; it is used for the rest of the course.", "Lead unplugged from the switch and coiled in the folder. Shut down."]),
 dict(key_ideas=["Static: address 192.168.10.(10+bench), mask 255.255.255.0, no gateway.", "Bottom-up: link light → ip a → ping 127.0.0.1 → ping myself.", "A wrong mask or third octet does not stop local pings; it shows up when you try to reach others."],
      questions=[("ipconfig / ip a shows: ___ /___. Ping 127.0.0.1: ___. Ping self: ___ ms.", 1), ("Switch port light: lit? colour? what happened when unplugged?", 1), ("Write the Windows OR Linux steps to set a static IP (5 steps).", 4), ("Why did the typo drills still let you ping yourself?", 2)],
      exit="Which rung of the ladder did you get to today?"),
 callouts=[SAFE_CABLE]))

# ---------------------------------------------------------------- WEEK 15
LESSONS.append(L(43, 15, 1, "Build the lab LAN: cable every bench, ping every neighbour",
 ["Connect 20 PCs to the switch with a documented port plan.", "Ping neighbours and read ARP to prove MAC-to-IP mapping.", "Fix the firewall rule that blocks incoming ping."],
 ["All bench PCs", "Lab switch", "Tested patch leads", "Port plan sheet", "Marker and port labels"],
 [("Port plan", "A table: switch port → bench → IP → MAC."), ("ARP", "Address Resolution Protocol: 'who has this IP? tell me your MAC'."), ("ICMP", "The protocol ping uses: echo request and echo reply."), ("Firewall", "Software on each PC that blocks unwanted incoming traffic; by default it often blocks ping.")],
 dict(min=4, steps=["Lead into the port with your bench number. Confirm the link light.", "Teacher's PC on port 24 with 192.168.10.1."]),
 dict(min=8, html="""<p>Twenty PCs, one switch, one network. Each PC already has its address. Now they find each other. When you ping .12, your PC first broadcasts an ARP request ('who has 192.168.10.12?'). PC-02 replies with its MAC. The switch learns both ports. Then the ping travels directly. Watch it happen below, then do it for real.</p>
{F0}
<p><b>Example 1.</b> Ping a neighbour: 'Request timed out' on all four. Their link light is on and their address is right. Their firewall is dropping ICMP. Allow it (Windows: enable 'File and Printer Sharing (Echo Request – ICMPv4-In)'; Mint: ufw allow from 192.168.10.0/24, or ufw is off by default).</p>
<p><b>Example 2.</b> 'Destination host unreachable' from your OWN address: the destination is on a different network or does not exist; ARP got no reply.</p>
<p><b>Example 3.</b> <code>arp -a</code> shows the neighbour's IP next to a MAC that matches their label. That is the proof the two layers are linked.</p>""", figures=[arp()]),
 dict(min=26, steps=["Fill your row of the port plan: port, bench, IP, MAC, hostname.",
      "Ping the teacher: <code>ping 192.168.10.1</code>. Write the result.",
      "Ping your left and right neighbours. Write results. Timed out? Ask them to allow ICMP through their firewall (steps above). Retest.",
      "<code>arp -a</code> (Windows) or <code>ip neigh</code> (Linux). Find your neighbours' IPs and MACs. Compare the MACs with the labels on their PCs.",
      "Ping 192.168.10.255 (broadcast) and watch who answers (Linux answers by default; Windows usually does not). Discuss why broadcast is useful and risky.",
      "Chain test: ping every bench from 11 to 30 with <code>ping -n 1</code> (Windows) / <code>ping -c 1</code> (Linux). Mark each on the port plan: OK / no reply. Report the no-reply ones to the teacher.",
      "Write the finished port plan on the whiteboard. Every bench reachable = class checkpoint."]),
 dict(min=4, quiz=[Q("ARP's question is…", ["what is your IP?", "who has this IP? tell me your MAC", "are you alive?", "what port?"], 1, "IP → MAC resolution."),
      Q("'Request timed out' but link lights are on and addresses are right. Most likely:", ["bad cable", "the other PC's firewall drops ping", "wrong MAC", "switch is broken"], 1, "ICMP blocked by default on many systems."),
      Q("The switch learns MACs from…", ["the port plan", "the 'from' address of frames it sees", "the teacher", "DHCP"], 1, "Source MAC learning.")]),
 dict(min=3, steps=["Leave leads connected for the rest of the week. Switch stays on.", "Port plan photographed and in the folder. Shut down."]),
 dict(key_ideas=["Port plan: port → bench → IP → MAC → hostname. Keep it current.", "Ping → ARP first (IP→MAC) → switch learns → reply. arp -a / ip neigh shows the mapping.", "Timed out with everything else right = the far end's firewall. Allow ICMP from the lab subnet only."],
      questions=[("Port plan row: port ___ bench ___ IP ___ MAC ___ host ___", 1), ("Ping teacher ___ left ___ right ___. What did you change if any failed?", 2), ("arp -a: two neighbours' IP → MAC pairs.", 2), ("Chain test: benches with no reply ___ and why.", 2), ("Explain 'timed out' vs 'destination host unreachable'.", 2)],
      exit="Is every bench reachable? Which rung is the class on?"),
 callouts=[SAFE_CABLE]))

LESSONS.append(L(44, 15, 2, "Network troubleshooting: the bottom-up ladder on planted faults",
 ["Apply the bottom-up ladder to find a network fault in under five minutes.", "Use ping, ipconfig/ip a, arp, and the link light as evidence.", "Log each fault with the rung it failed on."],
 ["Lab LAN with teacher-planted faults", "Fault log sheets", "Spare tested lead"],
 [("Bottom-up", "Start at the cable and work up: link, address, loopback, self, neighbour, application."), ("Duplicate IP", "Two PCs with the same address; both get intermittent failures."), ("APIPA", "169.254.x.x: the address a PC gives itself when it expected DHCP and got nothing.")],
 dict(min=3, steps=["Rotate benches. Each PC has one planted network fault. Log sheet ready.", "Teacher: 'Do not touch a setting until you have named the rung.'"]),
 dict(min=6, html="""<p>Possible plants: lead unplugged at the switch · lead with an open wire · wrong mask (/16 or /25) · wrong third octet · duplicate IP with another bench · firewall blocking ICMP · IPv4 disabled on the adapter · switch port moved. Each one fails at a specific rung. Find the rung, then the cause.</p>
{F0}
<p><b>Example.</b> Rung 1 OK (light on). Rung 2: <code>ip a</code> shows 169.254.7.3. The PC is waiting for DHCP: the static setting was removed. Fix the setting; everything above comes back.</p>""", figures=[ladder()]),
 dict(min=28, steps=["Round 1 (9 min): climb the ladder, writing the result of each rung. Stop at the first failure. Name the rung and two possible causes.",
      "Test one cause with one change. Log it. Verify by climbing the rest of the ladder to a neighbour ping.",
      "Round 2 (9 min): new PC, same method.",
      "Round 3 (9 min): new PC. This one is sneaky: it may pass everything and still fail sometimes (duplicate IP). Ping repeatedly; look for mixed replies/timeouts; check <code>arp -a</code> for a MAC that changes.",
      "Hand-over: neighbour ping passes, settings correct, log signed."]),
 dict(min=5, quiz=[Q("169.254.x.x means…", ["a hacker", "the PC gave itself an address because no DHCP answered; the static setting is missing", "the switch assigned it", "all is well"], 1, "APIPA = 'I got nothing'."),
      Q("Intermittent replies and a MAC that changes in arp -a =", ["bad cable", "duplicate IP", "wrong mask", "firewall"], 1, "Two PCs answering for one address."),
      Q("Where does a wrong subnet mask show up on the ladder?", ["rung 1 (link)", "rung 3 (loopback)", "rung 5 (neighbour)", "never"], 2, "Local pings pass; the neighbour is judged 'not local'.")]),
 dict(min=3, steps=["Logs in. Leads stay connected. Shut down."]),
 dict(key_ideas=["Ladder: link light → address → 127.0.0.1 → self → neighbour → application.", "APIPA 169.254 = no static address set. Changing MAC in arp = duplicate IP. Neighbour fails but self passes = mask/octet/firewall.", "Name the rung before touching anything; one change at a time."],
      questions=[("Round 1: rung failed ___ cause ___ fix ___ time ___", 2), ("Round 2: same.", 2), ("Round 3: same.", 2), ("Write the ladder from memory with one tool per rung.", 3)],
      exit="Which plant was hardest and why?"),
 callouts=[SAFE_CABLE]))

LESSONS.append(L(45, 15, 3, "Ports, sockets and telnet: talking to a program by its door number",
 ["Explain what a port and a socket are.", "Install a telnet client and connect to a listening port.", "Read a connection refused / timed out error and say which layer failed."],
 ["Lab LAN", "Telnet client (Windows: Turn Windows features on → Telnet Client; Mint: <code>sudo apt install telnet</code> or use <code>nc</code>)", "Teacher's PC running a netcat listener on 2323"],
 [("Port", "A 16-bit number (0–65535) that picks which program on a PC gets the data."), ("Socket", "One end of a connection: IP address + port."), ("Listening", "A program waiting on a port for connections."), ("Telnet", "A very old, plain-text way to open a TCP connection to a port and type into it."), ("Connection refused", "The PC answered, but nothing is listening on that port.")],
 dict(steps=["Boot. Teacher starts <code>nc -l -p 2323</code> (or <code>ncat -l 2323</code>) on 192.168.10.1 and shows the empty, waiting terminal.", "Guess: what happens when the first student connects?"]),
 dict(min=12, html="""<p>An IP address gets you to the right PC. A port gets you to the right program on it. Web servers listen on 80 and 443, Minecraft on 25565, our chat on 2323. Telnet is the simplest client there is: it opens a TCP connection to an IP and port and sends whatever you type.</p>
{F0}
<p><b>Example 1.</b> <code>telnet 192.168.10.1 2323</code> → 'Connected'. Type 'hello' → it appears on the teacher's screen. The teacher types back → it appears on yours. That is a raw TCP socket, with nothing in between.</p>
<p><b>Example 2.</b> <code>telnet 192.168.10.1 2324</code> → 'Connection refused'. The PC is there (Internet layer fine) but no program is on door 2324 (Transport layer: no listener).</p>
<p><b>Example 3.</b> <code>telnet 192.168.10.99 2323</code> → hangs, then 'timed out'. Nobody answered at all: wrong IP, or a firewall silently dropping. Different error, different layer.</p>{F1}""", figures=[sockets(), terminal(["C:\\> telnet 192.168.10.1 2323", "Connecting to 192.168.10.1...", "hello from bench 4", "teacher: welcome, bench 4", "", "C:\\> telnet 192.168.10.1 2324", "Connecting to 192.168.10.1...Could not open connection to the host, on port 2324: Connect failed"], "PC-04 — command prompt")]),
 dict(min=20, steps=["Install the telnet client (Windows: Settings → Optional features / 'Turn Windows features on or off' → Telnet Client; Mint: <code>sudo apt install telnet</code>, or use <code>nc</code>).",
      "<code>telnet 192.168.10.1 2323</code>. Type your bench number and a greeting. Watch the teacher's screen.",
      "Close with Ctrl+] then <code>quit</code> (Windows) or Ctrl+C.",
      "Try port 2324. Write the exact error. Which layer?",
      "Try 192.168.10.99 port 2323. Write the error. Which layer?",
      "Start your own listener: Windows <code>ncat -l 2323</code> (from the teacher USB) or Mint <code>nc -l -p 2323</code>. Ask a neighbour to telnet to you. Type to each other.",
      "<code>netstat -an | findstr 2323</code> (Windows) or <code>ss -tn | grep 2323</code> (Linux) while connected. Find the line: your IP:2323 ↔ their IP:random port. That is the socket pair."]),
 dict(quiz=[Q("A socket is…", ["a wall plug", "IP address + port, one end of a connection", "a cable", "a MAC"], 1, "Both ends have one."),
      Q("'Connection refused' means…", ["wrong cable", "the PC answered but nothing listens on that port", "the IP does not exist", "the firewall dropped it"], 1, "Internet layer fine, no listener at the Transport layer."),
      Q("'Timed out' means…", ["nothing answered at all: wrong IP or silent firewall", "the port is busy", "the program crashed", "the cable is too long"], 0, "No reply, not even a refusal.")]),
 dict(steps=["Listeners stopped (Ctrl+C). Leads stay connected. Shut down."]),
 dict(key_ideas=["IP = which PC, port = which program. Socket = IP + port.", "telnet IP port opens a raw TCP connection. nc -l port listens.", "Refused = PC there, no listener. Timed out = no answer at all (IP/firewall)."],
      questions=[("Telnet to .1:2323 result ___. To .1:2324 error ___ layer ___. To .99:2323 error ___ layer ___.", 3), ("Your own listener: who connected? What did netstat/ss show for the socket pair?", 2), ("Explain port numbers using the 'door number' idea.", 2), ("Why does Minecraft need both an IP and a port?", 2)],
      exit="Say one port number and what lives on it."),
 callouts=[SAFE_CABLE]))

# ---------------------------------------------------------------- WEEK 16
LESSONS.append(L(46, 16, 1, "Write a chat server in Python: sockets, bind, listen, accept",
 ["Explain what each socket call does: socket, bind, listen, accept, recv, send.", "Run the chat server and connect to it with telnet from another bench.", "Read the server's output to see who connected."],
 ["Bench PC with Python 3", "chat_server.py (typed or from the teacher USB)", "Telnet / nc", "Lab LAN"],
 [("bind", "Attach the socket to an address and port."), ("listen", "Open the door: accept connections."), ("accept", "Wait for a knock; returns a new socket for that one client."), ("recv / send", "Read from and write to a connected socket."), ("Thread", "A separate line of execution so one slow client does not block the others.")],
 dict(steps=["Boot. Open a text editor and a terminal side by side.", "Teacher: 'Last week you used a tool that listens. Today you write one.'"]),
 dict(min=14, html="""<p>A server is a loop: make a socket, bind it to a port, listen, then accept clients forever. Each accepted client gets its own socket and its own thread so twenty students can type at once. Every line a client sends is broadcast to everyone else. That is the whole program.</p>
{F0}
<p><b>Example 1 — bind to 0.0.0.0.</b> That means 'every network card on this PC'. Binding to 127.0.0.1 would only allow connections from the same PC.</p>
<p><b>Example 2 — port 2323, not 23.</b> Real telnet lives on 23, but ports below 1024 need admin rights on Linux. 2323 is free and needs nothing special.</p>
<p><b>Example 3 — the firewall again.</b> The server runs, a neighbour gets 'timed out'. Allow TCP 2323 in from 192.168.10.0/24 on the server PC. Only that port, only from the lab.</p>
<pre><code>{CODE}</code></pre>""".replace("{CODE}", CHAT_SERVER.replace("<", "&lt;").replace(">", "&gt;")), figures=[sockets()]),
 dict(min=18, steps=["Save the server code as <code>chat_server.py</code>. Read it top to bottom with your partner; write one line of explanation beside each socket call.",
      "Run it: <code>python chat_server.py</code> (Windows) / <code>python3 chat_server.py</code> (Mint). It should print 'listening on port 2323'.",
      "From the same PC, open a second terminal: <code>telnet 127.0.0.1 2323</code>. Give a name, type a line. Nothing echoes back (there is no one else yet) but the server stays alive.",
      "Ask a neighbour to telnet to YOUR lab IP, port 2323. If they time out, allow TCP 2323 in your firewall (Windows: Defender Firewall → Inbound rule → Port 2323; Mint: <code>sudo ufw allow from 192.168.10.0/24 to any port 2323</code>) and retry.",
      "Chat across the two benches. Watch the server's terminal: it prints joins and leaves.",
      "Stop the server with Ctrl+C. Start it again. Reconnect. (SO_REUSEADDR is why the port is free immediately.)",
      "Change PORT to 2424, restart, and tell your neighbour. Does the old port still work? Why not?"]),
 dict(quiz=[Q("bind((\"0.0.0.0\", 2323)) means…", ["connect to 0.0.0.0", "listen on port 2323 on every network card", "block all traffic", "use port 0"], 1, "0.0.0.0 = all interfaces."),
      Q("Why one thread per client?", ["Threads are fun", "So a slow or idle client does not stop the others being served", "Python requires it", "To use more RAM"], 1, "accept() and recv() block; threads keep the loop free."),
      Q("The server runs but neighbours time out. Fix:", ["change the IP", "allow TCP 2323 inbound in the firewall", "reinstall Python", "use port 23"], 1, "The OS firewall drops unknown inbound ports.")]),
 dict(steps=["Servers stopped. Code saved in the bench folder on the PC. Shut down."]),
 dict(key_ideas=["socket → bind(0.0.0.0, 2323) → listen → accept loop → one thread per client → recv/broadcast.", "Ports under 1024 need admin on Linux; 2323 does not.", "A listener nobody can reach = firewall. Allow one port from the lab subnet only."],
      questions=[("One line beside each: socket(), bind(), listen(), accept(), recv(), sendall().", 6), ("Who connected to your server? What did the server print?", 1), ("What did you change to fix a timed-out neighbour?", 2), ("Why does changing PORT break the old connection?", 1)],
      exit="In one sentence: what does accept() give you?"),
 callouts=[("", "Python note", "Type the code exactly, including indentation. A wrong indent is the most common 'bug'. If the teacher's USB has the file, use it and read it rather than retyping.")]))
LESSONS[-1]["do"]["print_html"] = "<h2>chat_server.py</h2><pre>" + CHAT_SERVER.replace("<", "&lt;").replace(">", "&gt;") + "</pre>"

LESSONS.append(L(47, 16, 2, "Write the chat client, run a class-wide chat, and read the traffic",
 ["Write a socket client that sends and receives at the same time.", "Join a 20-PC chat on one server and observe the server's load.", "Explain why the chat is readable by anyone on the wire (no encryption)."],
 ["Lab LAN", "chat_client.py", "One server bench chosen by the class", "Wireshark on the teacher PC (demonstration only)"],
 [("Client", "The program that connects out to a server."), ("connect", "The client's call that knocks on the server's door."), ("Plain text", "Data sent as readable characters, not encrypted; anyone capturing the wire can read it."), ("Packet capture", "Recording every frame on a port to look inside them.")],
 dict(steps=["Class picks one server bench. That bench starts chat_server.py and announces its IP.", "Everyone else opens the client code."]),
 dict(min=10, html="""<p>Telnet works, but your own client is better: it listens for incoming lines in one thread and sends your typing in another. Then the class joins one server. With twenty clients, the server's single accept loop and twenty threads are all busy; watch its terminal.</p>
<pre><code>{CODE}</code></pre>
<p><b>Example 1.</b> Run with the server's IP as an argument: <code>python chat_client.py 192.168.10.14</code>. 'Name?' appears. Type your name, then chat.</p>
<p><b>Example 2.</b> Someone types <code>/quit</code>: the server broadcasts '*** name left' and closes that socket. The other nineteen are untouched.</p>
<p><b>Example 3.</b> The teacher captures port 2323 traffic with Wireshark and projects it. Every message is readable in the packet bytes. Nothing you type here is private. This is why real chat apps use TLS.</p>""".replace("{CODE}", CHAT_CLIENT.replace("<", "&lt;").replace(">", "&gt;")), figures=[]),
 dict(min=22, steps=["Save the client as <code>chat_client.py</code>. Beside each line, write what it does (connect, the listening thread, the input loop).",
      "Run it against the class server. Name = your bench. Say hello. Everyone should see everyone.",
      "Count: how many clients does the server bench's terminal say joined? Does it match the room?",
      "Try sending twenty lines fast. Did anything lag? Ask the server bench what their CPU graph shows.",
      "Teacher demo: Wireshark filter <code>tcp.port == 2323</code>. Find your own message in a packet. Write the source port your client used.",
      "Type <code>/quit</code>. Reconnect with a different name. What did everyone see?",
      "Discussion: name two things you would add to make this a 'real' chat (hint: login, encryption, message history)."]),
 dict(min=5, quiz=[Q("The client needs two threads because…", ["Python is slow", "it must listen for incoming lines while waiting for your typing", "the server has two ports", "telnet does"], 1, "input() blocks; so does recv()."),
      Q("Your client's own port number is…", ["2323", "a random free port chosen by the OS", "23", "80"], 1, "Only the server's port is fixed."),
      Q("Wireshark showed your message in plain text because…", ["Wireshark decrypts everything", "the chat sends unencrypted bytes", "the teacher has your password", "port 2323 is special"], 1, "No TLS = readable on the wire.")]),
 dict(steps=["Clients closed with /quit, server stopped. Shut down."]),
 dict(key_ideas=["Client: connect(ip, port) → one thread recv/print → main loop input/send.", "Server port is fixed (2323); each client's port is random.", "Plain TCP is readable by anyone capturing the wire. Real apps add TLS."],
      questions=[("Annotate the client: connect / listen thread / input loop.", 4), ("Clients joined per the server terminal: ___. Lag with fast typing? CPU on the server?", 2), ("Your client's source port in Wireshark: ___. Why is it not 2323?", 2), ("Two features a real chat app adds and why.", 2)],
      exit="Would you type a password into this chat? Why not?"),
 callouts=[("", "Lab-only tool", "Wireshark is run by the teacher on the isolated lab network only. Capturing traffic on any network you do not own or have permission for is illegal.")]))
LESSONS[-1]["do"]["print_html"] = "<h2>chat_client.py</h2><pre>" + CHAT_CLIENT.replace("<", "&lt;").replace(">", "&gt;") + "</pre>"

LESSONS.append(L(48, 16, 3, "Firewalls and services: open exactly one door",
 ["Explain what a host firewall does and why the default is 'block inbound'.", "Add and remove a rule for a single port from the lab subnet only.", "Prove the rule with telnet from a neighbour before and after."],
 ["Lab LAN", "chat_server.py", "Windows Defender Firewall / ufw on Mint", "Telnet"],
 [("Inbound rule", "Permission for traffic arriving at this PC on a port."), ("Scope", "Which source addresses a rule applies to; ours is 192.168.10.0/24 only."), ("Service", "A program that listens and waits: a server."), ("Least privilege", "Open only what is needed, to only who needs it, for only as long as needed.")],
 dict(steps=["Boot. Start chat_server.py. Ask a neighbour to telnet to you. Note whether it works right now (your rule from Week 16 may still exist).", "Teacher: 'Every open port is a door. A tech opens one, labels it, and closes it when done.'"]),
 dict(min=12, html="""<p>A host firewall is a list of rules checked against every incoming packet. The default on every modern OS is: outbound allowed, inbound blocked unless a rule says otherwise. That is why your server was unreachable until you added a rule. Good rules are narrow: one port, one protocol, one source range.</p>
{F0}
<p><b>Example 1 — too wide.</b> 'Allow all inbound' makes the chat work and also exposes file sharing, remote desktop and anything else listening. Wrong.</p>
<p><b>Example 2 — right size.</b> 'Allow TCP 2323 inbound from 192.168.10.0/24'. The chat works; nothing else changes; a device from any other network is still blocked.</p>
<p><b>Example 3 — cleanup.</b> At the end of the course, delete the rule. A door you forgot is a door someone else finds.</p>""", figures=[firewall()]),
 dict(min=20, steps=["Delete any 2323 rule you made earlier (Windows: Defender Firewall → Advanced → Inbound Rules → delete; Mint: <code>sudo ufw status numbered</code>, <code>sudo ufw delete N</code>). Neighbour telnets: expect timed out.",
      "Add the narrow rule. Windows: Inbound Rules → New → Port → TCP 2323 → Allow → Scope: remote IP 192.168.10.0/24 → name 'ReBuild chat 2323'. Mint: <code>sudo ufw enable</code> then <code>sudo ufw allow from 192.168.10.0/24 to any port 2323 proto tcp</code>.",
      "Neighbour telnets: expect connected. Write the before/after.",
      "Ask the neighbour to try port 2324: still refused (no listener) — the firewall was never the issue there. Explain the difference to each other.",
      "Mint only: <code>sudo ufw status verbose</code>. Windows: <code>netsh advfirewall firewall show rule name=\"ReBuild chat 2323\"</code>. Copy the key line into the worksheet.",
      "Discuss with the bench: which ports will the LAN party need next week? (Minecraft Java: TCP 25565. Luanti: UDP 30000.) Write the rule you will add."]),
 dict(quiz=[Q("The firewall default is…", ["allow everything", "outbound allowed, inbound blocked unless a rule allows it", "block everything", "allow inbound only"], 1, "That is why servers need a rule and clients do not."),
      Q("The best rule for our chat:", ["allow all inbound", "allow TCP 2323 from 192.168.10.0/24", "disable the firewall", "allow port 23"], 1, "One port, one protocol, lab subnet only."),
      Q("Neighbour gets 'refused' on 2324 even with the firewall open. Because…", ["the rule is wrong", "nothing is listening on 2324", "the cable is bad", "ufw is off"], 1, "Refused = reached the PC, no listener.")]),
 dict(steps=["Leave the 2323 rule for now; it is removed in Week 18.", "Server stopped. Shut down."]),
 dict(key_ideas=["Host firewall: inbound blocked by default; add narrow rules (port + protocol + source range).", "Timed out = firewall/IP; refused = no listener. Different problems.", "Least privilege: open one door, label it, close it at the end."],
      questions=[("Before the rule: ___. After: ___. Port 2324 with the rule: ___ and why.", 3), ("Write your rule exactly (port, protocol, scope, name).", 2), ("Why is 'allow all inbound' a bad fix even on an isolated lab?", 2), ("Which port(s) does next week's game need and what rule will you add?", 2)],
      exit="Define least privilege in one line."),
 callouts=[]))

# ---------------------------------------------------------------- WEEK 17
LESSONS.append(L(49, 17, 1, "LAN party setup: host a game server and connect every bench",
 ["Host a multiplayer game server on one bench and join from the others over the LAN.", "Open the right port with a scoped rule.", "Diagnose a join failure with the ladder."],
 ["Lab LAN", "Game: Minecraft Java Edition (if the school holds licences) or Luanti (free, open source) installed on every bench", "The port plan"],
 [("Game server", "A program that holds the world; players connect to it."), ("Direct connect", "Joining by typing IP:port instead of using a server list."), ("Luanti", "A free, open-source voxel game (formerly Minetest) that runs on these PCs with no licence; UDP port 30000."), ("UDP", "A transport protocol with no connection setup; games use it for speed.")],
 dict(min=4, steps=["Teacher announces the game for the lab (Minecraft Java if licensed; otherwise Luanti) and the host bench.", "Everyone checks their lead and link light."]),
 dict(min=8, html="""<p>A LAN game is the chat server with graphics. One PC hosts (listens on a port); the rest connect to its IP and port. Minecraft Java hosts on TCP 25565 by default; Luanti hosts on UDP 30000. The host PC needs an inbound rule for that port from the lab subnet. Everything else is the ladder you already know.</p>
<p><b>Example 1 — Minecraft Java.</b> Host: Open to LAN from a single-player world (it prints a random port) or run the dedicated server (25565). Others: Multiplayer → Direct Connect → <code>192.168.10.14:25565</code>.</p>
<p><b>Example 2 — Luanti.</b> Host: Start Game → Host Server tick → port 30000. Others: Join Game → address <code>192.168.10.14</code>, port 30000.</p>
<p><b>Example 3 — 'can't connect'.</b> Ping the host: OK? Then telnet to 25565 (TCP): refused = server not running; timed out = firewall. For UDP you cannot telnet; check the host's rule and that the game says 'listening'.</p>{F0}""", figures=[sockets()]),
 dict(min=25, steps=["Host bench: start the server. Note the port it prints. Add the inbound rule (TCP 25565 or UDP 30000, scope 192.168.10.0/24).",
      "Host bench: <code>netstat -an | findstr 25565</code> or <code>ss -ulpn | grep 30000</code>. Confirm LISTENING / UNCONN on the port.",
      "Every other bench: direct connect to host IP:port. Write 'joined' or the error.",
      "Failed to join? Ladder: link light → ping host → (TCP games) telnet host port → read the error → fix the one thing it points to.",
      "Once in: everyone meets at spawn. Teacher checks the host's player list matches the room.",
      "Host bench: watch CPU and network graphs with 19 players. Write the numbers.",
      "Rotate: a second bench hosts for 5 minutes. Does the first host's rule help the new host? Why not?"]),
 dict(min=5, quiz=[Q("Minecraft Java listens on…", ["UDP 30000", "TCP 25565", "TCP 2323", "port 80"], 1, "Default server port."),
      Q("Why can't you telnet to a Luanti server to test it?", ["It is too fast", "It uses UDP, and telnet only does TCP", "It is encrypted", "It needs a password"], 1, "Different transport protocol."),
      Q("A new host bench needs…", ["nothing: the old rule covers it", "its own inbound rule on its own firewall", "a router", "a new switch"], 1, "Rules live on the host PC.")]),
 dict(min=3, steps=["Game closed properly (host saves the world). Rules left in place for Lesson 50.", "Shut down."]),
 dict(key_ideas=["Host listens (TCP 25565 Minecraft Java / UDP 30000 Luanti) + inbound rule from the lab subnet; others direct-connect to IP:port.", "Join failure = ladder: link → ping → telnet (TCP) → error → one fix.", "Each host needs its own rule; a rule lives on the PC it protects."],
      questions=[("Game ___ host IP ___ port ___ protocol ___. Your join result: ___", 1), ("If you failed to join: rung ___ error ___ fix ___", 2), ("Host bench: CPU ___ % network ___ with ___ players.", 1), ("Explain why Luanti cannot be tested with telnet but Minecraft can.", 2)],
      exit="What is the one setting the host had to change that a client did not?"),
 callouts=[("", "Licensing", "Minecraft Java needs a licence per account; use it only if the school holds them. Luanti is free and open source and runs well on these PCs. Either way: no internet, no public servers, lab subnet only.")]))

LESSONS.append(L(50, 17, 2, "LAN party: play, measure, and see the network under load",
 ["Play a 20-player LAN session and keep it running.", "Measure latency, bandwidth and host load during play.", "Relate what you see to frames, packets and ports."],
 ["Lab LAN", "Game server from last lesson", "ping, Task Manager / htop, switch port lights"],
 [("Latency", "Round-trip time, shown by ping in ms; lower is better."), ("Bandwidth", "How much data per second the link carries; a gigabit lab has far more than a game needs."), ("Tick", "The server's update heartbeat (Minecraft: 20 per second)."), ("Lag", "What players feel when latency rises or the server falls behind its ticks.")],
 dict(min=3, steps=["Host bench starts the server. Everyone joins. Teacher gives a 20-minute build or race challenge in-game.", "Measurement roles: two benches keep ping running to the host in a second window; one watches the host's graphs."]),
 dict(min=4, html="""<p>This is the reward and the experiment. While you play, the network carries a packet per player many times a second. Ping to the host should sit around 1 ms on a wired gigabit LAN. If the host's CPU hits 100% or its tick rate drops, everyone lags, no matter how good the cables are.</p>
<p><b>Example.</b> Twenty players exploding TNT at once: the host's CPU spikes, ticks fall behind, and ping is still 1 ms. The network was never the problem; the server was.</p>""", figures=[]),
 dict(min=30, steps=["Play. Keep the host's terminal visible on the host bench.",
      "Measuring bench A: <code>ping -t 192.168.10.host</code> (Windows) or <code>ping host</code> (Linux) in a window. Every 5 minutes write the typical ms and the worst ms.",
      "Measuring bench B: unplug and replug its own lead once (teacher's signal). What happened to that player in-game? How long to recover?",
      "Host watcher: write CPU %, RAM used, and network Mb/s at 5, 10, 15, 20 minutes.",
      "Everyone at 15 minutes: do something expensive in-game together (teacher's call). Watchers note what changed.",
      "At 20 minutes: host saves and stops the server. Everyone back to the desktop."]),
 dict(min=5, quiz=[Q("Ping stays at 1 ms but the game lags. The cause is probably…", ["the cables", "the host PC falling behind its ticks", "the switch", "the subnet mask"], 1, "Network fine; server overloaded."),
      Q("A gigabit LAN is…", ["barely enough for 20 players", "far more than a game needs; bandwidth is not the limit", "too fast for games", "only for video"], 1, "Games use kilobits per player, not megabits."),
      Q("A player's lead is unplugged for 3 seconds. The server…", ["crashes", "times that player out after a while; others continue", "kicks everyone", "needs a restart"], 1, "Sockets are per client.")]),
 dict(min=3, steps=["World saved by the host and copied to the teacher USB. Shut down."]),
 dict(key_ideas=["Wired gigabit LAN: ~1 ms ping; bandwidth is never the game's limit.", "Lag with low ping = the host is the bottleneck (CPU/ticks).", "Each player is a socket; one dropped link affects one player."],
      questions=[("Ping log: typical ___ ms worst ___ ms. Host: CPU ___ RAM ___ network ___ at 5/10/15/20 min.", 2), ("What happened when bench B unplugged? Recovery time?", 2), ("Explain 'lag with 1 ms ping' using the tick idea.", 2), ("Which part of your PC would you upgrade to be a better host: CPU, RAM, GPU or NIC? Why?", 2)],
      exit="Best moment of the session, and one thing you measured."),
 callouts=[]))

LESSONS.append(L(51, 17, 3, "From LAN to WAN: routers, DHCP, DNS and why the lab is an island",
 ["Explain what a router, DHCP and DNS add to a network.", "Describe what would be needed to connect the lab to the internet, and why we do not.", "Trace a web request from a home PC to a website through the layers."],
 ["Bench PC (no changes)", "Whiteboard", "Worksheet"],
 [("Router", "Forwards packets between networks using IP addresses; the default gateway."), ("DHCP", "Hands out IP, mask, gateway and DNS automatically."), ("DNS", "Turns names (school.vic.edu.au) into IP addresses."), ("NAT", "Lets many private addresses share one public one."), ("WAN", "Wide area network: the links between LANs, including the internet.")],
 dict(steps=["Boot. Teacher draws the lab on the board: 20 PCs, switch. Then draws a home: PCs, Wi-Fi, a router, the internet.", "What does the home have that the lab does not? List on the board."]),
 dict(min=16, html="""<p>Our lab stops at the switch. A real network adds three services. A <b>router</b> connects the LAN to other networks and is every PC's default gateway. <b>DHCP</b> (usually running on the router) hands out addresses so nobody types them. <b>DNS</b> turns names into addresses so nobody remembers numbers. <b>NAT</b> on the router lets all your private 192.168 addresses share the one public address your ISP gave you.</p>
{F0}
<p><b>Example 1 — a web page at home.</b> You type a name → DNS gives an IP → your PC sees it is not local → sends to the gateway → router NATs it out → reply comes back → router maps it back to your PC. Four services you never see.</p>
<p><b>Example 2 — why the lab is an island.</b> No gateway means nothing can leave or arrive. That is deliberate: no updates mid-lesson, no outside traffic, no risk to the school network from student-built machines and open ports. The cybersecurity elective runs the same way.</p>
<p><b>Example 3 — adding internet properly.</b> You would need a router with NAT, DHCP (or keep static), DNS forwarding, a firewall policy, and permission from the school's IT. That is a project, not a cable.</p>""", figures=[layers()]),
 dict(min=18, steps=["Draw the lab network and the home network side by side. Label switch, router, DHCP, DNS, NAT, gateway where they exist.",
      "Write what <code>ipconfig /all</code> / <code>ip a</code> + <code>cat /etc/resolv.conf</code> would show at home that it does not show here (gateway, DNS server, DHCP lease).",
      "Trace: 'bench 4 opens a web page at home'. Number the steps through DNS, gateway, NAT and back.",
      "Role play: one student is DHCP. Three 'new PCs' join; DHCP hands each an address, mask, gateway and DNS on a card. One PC refuses DHCP and types its own: what conflict could occur?",
      "List three reasons the lab is kept isolated. Which one matters most to the school's IT team?",
      "Write what you would need, in order, to connect this lab to the internet safely."]),
 dict(quiz=[Q("DHCP gives a PC…", ["a MAC", "IP, mask, gateway and DNS", "a hostname", "a game"], 1, "The four settings we typed by hand."),
      Q("DNS turns…", ["IPs into MACs", "names into IP addresses", "packets into frames", "ports into IPs"], 1, "Name resolution."),
      Q("The lab is an island because…", ["we forgot the router", "it is deliberate: no outside traffic, no risk to the school network", "switches cannot route", "DNS is broken"], 1, "Isolation is the design.")]),
 dict(steps=["Worksheet in. Shut down."]),
 dict(key_ideas=["Router = gateway between networks; DHCP = automatic addresses; DNS = names to IPs; NAT = share one public IP.", "A home network has all four; the lab has none, on purpose.", "Connecting the lab would need a router, NAT, DNS, a firewall policy and IT's permission."],
      questions=[("Two diagrams: lab vs home, fully labelled.", 5), ("Trace a web page request in numbered steps.", 4), ("Three reasons the lab is isolated.", 2), ("What breaks if two PCs ignore DHCP and type the same address?", 1)],
      exit="If the lab had a router at .1, what one line would you add to every PC's network settings?"),
 callouts=[]))

# ---------------------------------------------------------------- WEEK 18
LESSONS.append(L(52, 18, 1, "Capstone 1: full fault diagnosis under time",
 ["Diagnose and repair two unknown faults (one hardware, one network) on a PC you did not build.", "Use the six steps and the ladder with a written log.", "Hand over a working PC to the assessor."],
 ["Rebuilt frames with two planted faults each", "Fault log sheets", "Known-good parts and lead", "Wrist strap, tools, tester"],
 [("Assessment", "Your work is judged against the rubric on the worksheet."), ("Hand-over", "PC boots, joins the LAN, pings the teacher, and the log is complete."), ("Time-box", "A fixed time per fault; stop and write what you would do next if you run out.")],
 dict(min=3, steps=["Rotate to an assigned bench. Strap on. Log sheet and rubric out.", "Teacher: 'Two faults. One inside, one on the network. 35 minutes. Log as you go.'"]),
 dict(min=2, html="""<p>Everything from the course in one session. Observe before you touch. Name the rung. One change at a time. Verify. Write it down.</p>{F0}""", figures=[method6()]),
 dict(min=35, steps=["Fault A (hardware, 17 min): observe → sort (no power / no POST / no boot) → LED code → theory → one change → verify with a full boot → log.",
      "Fault B (network, 17 min): observe → ladder from the link light up → name the failing rung → theory → one change → verify with a ping to 192.168.10.1 and a telnet to a listener → log.",
      "Hand-over (1 min): panel/frame tidy, cables managed, log signed by both partners, teacher verifies boot + ping."]),
 dict(min=3, quiz=[Q("You ran out of time on fault B. The log should end with…", ["nothing", "the rung reached, the theory, and the next test you would run", "a guess", "'fixed'"], 1, "A clear hand-over point is worth marks."),
      Q("You changed two things and it works. The log says…", ["fixed by X", "fixed; cause unclear because two changes were made at once; retest each", "nothing", "it was the cable"], 1, "Honest logs are technician logs.")]),
 dict(min=2, steps=["Logs and rubric sheets to the teacher. PC left working.", "Strap off last."]),
 dict(key_ideas=["Hardware: ladder of no power / no POST / no boot, then the Dell code.", "Network: link → address → loopback → self → neighbour → application.", "A good log beats a lucky fix."],
      questions=[("Fault A log: symptom / rung / code / theories / test / fix / verify / time.", 4), ("Fault B log: symptom / rung / tool output / theories / test / fix / verify / time.", 4), ("Self-assessment against the rubric below: circle your level per row and say why.", 3)],
      exit="One thing you did better than in Week 10."),
 callouts=[SAFE_ESD, SAFE_PWR]))
LESSONS[-1]["do"]["print_html"] = rubric_table([
    ("Safety", "Strap or unplug missed", "Reminded once", "All rules kept", "Kept and coached partner"),
    ("Method", "Random changes", "Some theory, several changes", "One change at a time, verified", "Simplest theory first, half-split used, verified"),
    ("Diagnosis", "Fault not found", "One of two found", "Both found", "Both found with cause explained"),
    ("Log", "Missing", "Partial", "Complete and readable", "Another tech could repeat it"),
    ("Hand-over", "Not working", "Works, untidy", "Works, tidy, signed", "Works, tidy, signed, customer-ready")])

LESSONS.append(L(53, 18, 2, "Capstone 2: the technician's hand-over document and a 3-minute demo",
 ["Write a one-page hand-over for your rebuilt PC: parts, settings, IP, known issues.", "Demonstrate one skill from the course to a Year 8 audience in three minutes.", "Give peer feedback using the rubric."],
 ["Your rebuilt frame", "Hand-over template", "Timer", "Rubric"],
 [("Hand-over document", "What a customer or next technician needs: what was done, what is in it, how it is set up, what to watch."), ("Known issue", "A problem you know about but did not fix, written down honestly."), ("Demo", "Showing a skill clearly enough that someone new could copy it.")],
 dict(min=3, steps=["Boot your rebuilt PC. Open the hand-over template.", "Teacher: 'A PC without paperwork is a mystery for the next person.'"]),
 dict(min=5, html="""<p>Professional work ends in writing. The hand-over says what the machine is, what you did to it, how it is configured, and what is still wrong. The demo proves you can teach a skill, which is the best test of understanding it.</p>
<p><b>Example hand-over, abridged.</b> Bench 4 · Dell OptiPlex 7050 SFF board in open frame · i5-7500, 16 GB DDR4-2400 (2×8, dual), 500 GB NVMe (OS), 240 GB SATA (data), GTX 1650 LP, 550 W ATX via 24→6 adapter, Dell button on original lead · Linux Mint 22, hostname PC-04, user student/tech, static 192.168.10.14/24, no gateway, firewall rule TCP 2323 from lab subnet · Known issue: case fan header 2 dead, fan on PSU adapter · Temps: 38 idle / 71 load.</p>""", figures=[]),
 dict(min=30, steps=["Fill the hand-over: hardware list with exact specs (from BIOS and OS, not memory), OS and accounts, network settings, firewall rules, temperatures, known issues, date, names.",
      "Print it (or export PDF) and tape it inside the frame or to the shelf label.",
      "Choose one skill: crimping, RAM install, reading a Dell code, setting a static IP, or the firewall rule. Plan a 3-minute demo with a 'do this, not this' moment.",
      "Demo to another bench playing Year 8s. They score you on the rubric: clear steps, safety mentioned, one mistake shown and avoided, within time.",
      "Swap and score theirs.",
      "Teacher picks three demos for the showcase next lesson."]),
 dict(min=4, quiz=[Q("A hand-over must include known issues because…", ["it looks thorough", "the next person needs the truth to work safely and quickly", "marks", "it is longer"], 1, "Honesty is part of the job."),
      Q("Specs in the hand-over come from…", ["memory", "the BIOS and OS tools, checked today", "the box", "a guess"], 1, "Verified, not remembered.")]),
 dict(min=3, steps=["Hand-over attached to the PC. Rubric sheets to the teacher. Shut down."]),
 dict(key_ideas=["Hand-over: hardware (verified), OS/accounts, network, firewall, temps, known issues, date, names.", "A demo is the best test of understanding: steps, safety, a 'not this' moment.", "Written honestly, a known issue is a feature, not a failure."],
      questions=[("Complete the hand-over on the back of this sheet (use the headings).", 10), ("Demo score received: ___ /4. One piece of feedback you got.", 2)],
      exit="Which skill would you be most confident teaching a Year 8?"),
 callouts=[]))

LESSONS.append(L(54, 18, 3, "Wrap-up: showcase, decommission the lab, what comes next",
 ["Present a showcase demo to the class.", "Decommission the lab correctly: remove firewall rules, document, pack the kit.", "Map what you learned to real jobs and next-step courses."],
 ["All PCs", "Kit boxes, labels", "Course reflection sheet"],
 [("Decommission", "Returning equipment to a safe, documented, ready-for-next-time state."), ("Inventory", "A list of every item and where it is."), ("Pathway", "Where this learning leads: certificates, courses, jobs.")],
 dict(min=10, steps=["Three showcase demos (3 min each) from last lesson. Class applauds and asks one question each.", "Teacher: 'Techs leave a room better than they found it.'"]),
 dict(min=5, html="""<p>You started with a locked-down office PC and ended with a machine you rebuilt, networked, programmed and played on. Today we close it down properly, because the next cohort starts in Term 3 and they deserve the same clean start you had.</p>
<p><b>Where this goes.</b> CompTIA A+ covers almost exactly this course (hardware, troubleshooting, networking basics); Network+ goes deeper on Weeks 12–17. VCE Applied Computing and the Cybersecurity elective build on the same bench habits. Jobs that start here: IT support technician, field technician, network technician, systems administrator.</p>""", figures=[]),
 dict(min=22, steps=["Remove the chat and game firewall rules you added. Confirm with <code>ufw status</code> / the Inbound Rules list.",
      "Return network settings to the lab default (static IP stays; it is the lab image).",
      "Shut down. Unplug mains. Strap on. Visual check of the frame: nothing loose, cables tied, hand-over attached.",
      "Inventory the kit box against the parts list from Week 8. Note anything missing or damaged on the sheet.",
      "Coil and label your patch lead; it goes in the kit, tested.",
      "Reflection sheet: three things you can now do that you could not in Week 1; one thing you would change about the course; one job or course you might look at.",
      "Benches checked off by the teacher. Shelf labelled with bench number and 'READY'."]),
 dict(min=5, quiz=[Q("Why remove the firewall rules at the end?", ["They slow the PC", "An open door you forgot is a risk for the next user", "The teacher said so", "They expire anyway"], 1, "Least privilege includes cleanup."),
      Q("Which certification matches this course most closely?", ["CCIE", "CompTIA A+", "AWS Architect", "Adobe Certified"], 1, "A+ = hardware, troubleshooting, networking basics."),
      Q("A tech leaves the lab…", ["as they found it", "better than they found it, documented", "quickly", "with the tools"], 1, "Decommission is part of the job.")]),
 dict(min=3, steps=["Reflection sheets in. Kit boxes shelved. Chairs in.", "Thank your bench partner."]),
 dict(key_ideas=["Decommission: rules removed, settings documented, hardware checked, kit inventoried, shelf labelled.", "This course ≈ CompTIA A+; Weeks 12–17 lead toward Network+.", "Three things you can do now; one thing to change; one next step."],
      questions=[("Rules removed: ___. Inventory: missing/damaged ___.", 1), ("Three things you can do now that you could not in Week 1.", 3), ("One thing you would change about the course.", 2), ("One job or course you might look at next, and why.", 2)],
      exit="Shake hands with your partner. Say the T568B order one last time."),
 callouts=[SAFE_ESD]))
