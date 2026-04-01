## 2026-02-27 — Day 1

**Focus:** Schematic design and initial PCB layout in EasyEDA

![image](Docs/assets/Schematic.png)

## What I worked on

**Opto-isolation input stage**  
Designed a 4-channel galvanic isolation front-end using PC817 optocouplers and screw terminals. Each channel uses calculated input resistors `(470 Ω for 5V sensors)` and 10 kΩ pull-ups on the 3.3 V side to protect the SoC GPIOs from dirty, salvaged sensors.

![image](Docs/assets/PCBSchematic.png)

**Connector strategy:**  
Chose a 40-pin header footprint compatible with common ARM SoMs (Orange Pi / Raspberry Pi style). This keeps the design flexible: the same shield can later be used with other boards or systems without changing the isolation circuitry.

### Time spent — **~5h** (schematic, part selection, calculations, first placement pass)

### Notes
- Today's work establishes the electrical safety layer for future experiments with ARM-based edge AI (initially targeting an RK3588 SoC).

---

## 2026-02-28 to 2026-03-02 — Days 2 to 4

**Focus:** Component placement, fighting the Hybrid Router, manual trace optimization, and fixing severe DRC errors to achieve true galvanic isolation.

### The challenge
I quickly learned that auto-routers are completely blind to the concept of **galvanic isolation**. When I tried hybrid routing, the software ignored my carefully planned "no-man's-land" and threw traces straight through the optocoupler barrier, defeating the entire purpose of the board. I cloned the PCB archive to try working from a more advanced checkpoint, but ended up introducing new errors instead.

![image](Docs/assets/recent_board_schematic.png)

![image](Docs/assets/70errors.png)

I had to completely unroute the board and do everything manually. This turned into a grueling 3-day process of trial, error, and learning EDA quirks.

### Technical progress
- **Feb 28 (Day 2) — Placement & Power Loops:** Organized the board into three zones. Manually routed the LM2596 buck converter using 1 mm traces to handle up to 3 A and reduce inductance on the 5 V rail.
- **Mar 1 (Day 3) — The Ground Plane Trap:** Spent hours fighting over 70 DRC errors. The main issue was copper area pours failing to reach the optocoupler ground pins due to tight clearances around the 10 kΩ pull-up resistors.
- **Mar 2 (Day 4) — DRC Victory:** Reset the EDA clearance rules to `0.254 mm`. Manually routed the `GND` lines first, then applied copper pours to the outer edges. This created a perfect physical gap under the optocouplers, achieving 0 DRC errors. Exported the `.STEP` 3D model.

![image](Docs/assets/3Dcopper.png)

![image](Docs/assets/3DSchematic.png)

### Time spent — **~12.5h**

### Notes
- This was the hardest phase yet. Auto-routers don't understand physical isolation requirements — even with correct configuration, the gap would likely have been violated.
- Next step: import the 3D file into **OnShape** to begin the mechanical enclosure design, focusing on thermal dissipation.

---

## 2026-03-03 to 2026-03-06 — Enclosure & Cyberdeck Vibe

**Focus:** Mechanical CAD design, thermal management for AI processors, and EMI mitigation.

### Transition to mechanical engineering
With the Edge Nexus PCB fully routed, the next step was creating a physical environment that could handle the heat and connectivity of an edge AI brain. I imported the `.STEP` file into OnShape and designed a modular, cyberdeck-style split chassis.

![image](Docs/assets/developing_the_enclosure.png)

![image](Docs/assets/complete_render_enclousure.png)

_Also had to fix the mounting holes in the PCB in EasyEDA during this phase._

---

## 2026-03-07 — Design Polish & NVIDIA Pivot

Finalized the first pass of the industrial enclosure and realized the Edge Nexus shield and case could be reused with the **NVIDIA Jetson Orin Nano Super Developer Kit**, not just RK3588/Orange Pi. The official dev kit already includes a professional carrier board, so my role here is to provide an industrial isolation layer and a rugged, EMI-aware housing around it.

![image](Docs/assets/NVIDIA_JETSON_NANO.png)

Still needed to refine mounting points, clearances, and I/O cutouts to match the real Jetson dimensions, but the overall architecture (split data/power sides, standoffs at Z=35 mm, and fan tunnel) was compatible.

---

## 2026-03-08 to 09 — Front HMI Board: Routing & Design

Completed the PCB routing for the Edge Nexus Front HMI module. Went with a 70×20 mm "stick" form factor to fit alongside the main board inside the enclosure.

Trace width management was a real engineering exercise here. The 4× WS2812B LEDs share a 5 V rail, so I routed power and GND with thicker traces while keeping signal lines thinner. Poured a ground plane to improve EMI shielding. This part was done in **KiCad**.

![image](Docs/assets/frontPCB.png)

### Time spent — **~11h**

---

## 2026-03-10 to 16 — Enclosure Integration

All CAD this week. Imported STEP files of both boards into OnShape and positioned everything: isolation shield stacked above the Jetson via the 40-pin header, Front HMI mounted behind the front face panel with M3 bolts.

For the front panel I dropped the rectangular window idea and went with individual cutouts: 4 small holes aligned to the LED centers + 1 larger hole for the button. It looks like industrial/server equipment. Also had to work around the Jetson's fan exhaust path, refining side vents and standoff heights to keep airflow clear.

![image](Docs/assets/HMIboard.png)

### Time spent — **~15h**

---

## 2026-03-16 & 17 — Cleanup & V1 Submission Prep

Cleaned up the repo structure. Wrote `jetson_status_demo.py` using `Jetson.GPIO` — reads the MODE button and cycles LED states: blue (idle), green (processing), red blinking (emergency). Hardware stub, but the state machine and electrical interface are fully documented.

**Edge Nexus V1 ready for initial submission.** 

### Time spent — **~5h**

---

## 2026-03-18 to 22 — The Great Pivot

Scrapped the Jetson shield architecture. Using a $249 NVIDIA board as a dependency felt like "buying a computer" rather than doing hardware engineering. The point of Blueprint is to build something, not to wrap something expensive.

**Decision: standalone Industrial Controller using ESP32-S3 (WeAct Studio).**

Re-did the schematic from scratch:
- Added **RS-485 (SP3485)** for Modbus RTU communication.
- Added **2× 5 V relays** for physical load switching.
- Added sensors: **INA219** (power monitor), **SHT41** (temp/humidity), **DS3231** (RTC with battery backup).
- Kept the **PC817 isolation stage** from V1 — that part was solid.
- Started fresh 100×80 mm layout.

### Time spent — **~15h**

---

## 2026-03-23 to 27 — Routing & 3D

- Fixed layout: screw terminals were blocked by the ESP32 module footprint in the first pass. Moved all connectors to board edges.
- CR2032 battery holder routed under the ESP32 module to save space.
- Enforced 1.5 mm air gap between dirty and clean ground planes.
- 3D model check: moved SD slot to fix Z-axis collision with the ESP32 body.
- Exported Gerbers, BOM, and PickPlace.

![image](Docs/assets/pcb_routing_view.png)
![image](Docs/assets/main_shield_3d_render.png)

### Time spent — **~12h**

---

## 2026-03-28 to 30 — Final Submission Prep

Updated OnShape enclosure for the new board dimensions and relay heights. Verified BOM links and part pricing. Replaced V1 Jetson firmware stub with a proper **MicroPython firmware** (`software/main.py`) for the ESP32-S3 — reads SHT41 temperature/humidity, INA219 bus voltage, isolated digital inputs, and broadcasts telemetry over RS-485 every 5 seconds. Final repo cleanup.

**Timelapses:**
- [new parts & searching](https://lapse.hackclub.com/timelapse/lmfT6dZKEx6h)
- [more working to submit](https://lapse.hackclub.com/timelapse/3QgjKu2FWrUs)
- [making the pivot](https://lapse.hackclub.com/timelapse/ZSAejujQKgtY)

**Edge Nexus V2 — submitted. 🚀**

### Time spent — **~8h**
