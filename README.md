# ReBuild Lab — PC Building, Repair & Maintenance

Year 9/10 elective · 18 weeks · 54 lessons × 45 minutes · 20 students in pairs on ten Dell OptiPlex 7050 SFF benches.

**Start here:** [index.html](index.html) (course map) · [teacher-guide.html](teacher-guide.html) (answers, kit list, planted faults)

Every lesson page is a single standalone HTML file with no external dependencies. Each one carries a 45-minute segmented timer, animated SVG figures, tick-off step checklists, an instant-feedback quiz, and an embedded A4 worksheet PDF (button in the right column) that works offline from a `file://` URL.

## Course arc

| Weeks | Arc | Content |
|---|---|---|
| 1–6 | Know the machine | Safety/ESD, anatomy, teardown, CPU + thermals, RAM, storage, motherboard, firmware, PSU |
| 7–11 | Upgrade and transplant | GPU, cases, compatibility audit, three-lesson transplant into an open frame, troubleshooting, OS install |
| 12–18 | Connect and play | Cabling (T568B), IP/subnets, build the LAN, Python chat server over telnet, firewalls, LAN party, capstone |

## Rebuilding the pages

Source lives in `src/`. Requires Python 3 and Playwright with Chromium (used to render the worksheet PDFs).

```bash
cd src
pip install playwright && playwright install chromium
python build.py      # writes out/ with all 56 HTML files
```

Lesson content: `content_a.py` (1–18), `content_b.py` (19–36), `content_c.py` (37–54). Figures: `visuals.py`. Page chrome and print CSS: `template.py`.

## Lab network plan

192.168.10.0/24, no gateway, no DHCP. Teacher .1 on switch port 24; benches .11–.30 on ports 1–20; chat on TCP 2323; game on TCP 25565 (Minecraft Java) or UDP 30000 (Luanti).

© Plenty Valley Christian College Digital Technologies. Built with Digital Vector tooling.
