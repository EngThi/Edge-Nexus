## 2026-02-27 Day 1

**Focus:** Schematic design and initial PCB laypout in EasyEDA
![image](Docs/assets/Schematic.png)

## What I worked on

**Opto-isolation input stage**
Designed a 4-channel galvanic isolationfront-end using PC817 optocouplers and screw terminals. Each channels uses calculated input resistors `(470 Ω for 5V sensors)`and 10KΩ pull-ups on the 3.3 V side to protect the SoC GPIOs from dirty, salvaged sensors.

![image](Docs/assets/PCBSchematic.png)

**Connector strategys:**
Chose a 40-pin header footprint compatible with common ARM SoMs (Orange PI/Raspberry Pi style). This keeps the design flexible: the same shield can leter be used with other boards or systems without changing the isolation circuitry.

### Time spent **Approx:** 5 hours (schematic, part selection, calculations, and first placement pass)

### Notes
- Today's work establishes the eletrical safety layer for future experiments with ARM-based edge AI (initially targeting an RK3588 SoC/ some SoM in this type). 


## 2026-02-28 to 2026-03-02 - Days 2 to 4

**Focus:** Component placement, fighting the Hybrid-Router, manual trace optimization, and fixing severe DRC errors to achieve true galvanic isolation.

### The challenge
I quickly learned that Auto-Routers are completely blind to the concept of **Galvanic Isolation**. When I tried to reach an hybrid routing, the sftware ignored my carefully planned "no-man's-land" and threw traces staight through the optocoupler barrier, defeating the entire purpose of the board... me to cloned the archive of PCB to try working from a point that was advanced, but I ended up getting lost an causing, errors, problems.

![image](Docs/assets/recent_board_schematic.png)

![image](Docs/assets/70errors.png)

I had to completely unroute the board and do everything mannualy. This turned into a grueling 3-day process of trial, error, and learning EDA quirks.

### Technical progress
- **Feb 28 (Day 2) - Placement & Power Loops:** Organized the board into three zones. Manually routed the LM2596 buck converter using 1mm traces to handle up to 3A and reduce indutance on the 5V rail.
- **Mar 1 (Day 3) - The ground plane Trap and almost finalizing routing:** Spent hours fighting over 70 DRC errors. The main issue was `Copper Area`pours failing to reach the optocouplers ground pins due to tight clearences around the 10KΩ pull-up resistors.
- **Mar 2 (Day 4) - DRC Victory:** Reset the EDA clearence rules (I changed them without knowing exactly what they meant) to `0.254mm`. Manually routed the `GND` lines first, then appliedthe copper pours to the outer edges. This created a perfect physical gap under the optocouplers, achieving 0 DRC errors. Exported the `.STEP`3D model.
![image](Docs/assets/3Dcopper.png)

![image](Docs/assets/3DSchematic.png)

### Time Spent **Approx:** 12,5 - 13 hours

### Notes & Next steps 
- This was the hardest phase yet (software auto-routers don't understand physical isolation requiremnts... I didn't configured it that way, but I think it would cause some problems aniway).
- Now I'll i port the `3D file`into **OnShape** to begin the mechanical enclousure design, focusing on thermal dissipation for high-performance SoCs (I think it must be that).

## 2026-03-03 to 2026-03-06 - Basically the enclousure, Cyberdeck vibe

**Focus:** Mechanical CAD design, thermal managment for AI processors and EMI mitigation.

### Transition to mechanical engineering 
With the `Edge Nexus`PCB fully routed, next I create a physical environment that could handle the heat and connectivity of an Edge AI and domestic multi-service brain. Primarily targeting a SoC like RK3588 that would later develop a complete component/board for this use, but later studying and remembering that **`professional systems use NVIDIA chips`**, I think this will be the ideal solution.

I imported the `.STEP`file to OnShape and designed a modular, cyberdeck-style split chassis.


![image](Docs/assets/developing_the_enclosure.png)

![image](Docs/assets/complete_render_enclousure.png)

_I also had to fiz the Mounting Holes in the PCB in EasyEDA. Later when I export all the docs from the site I'll update the things here_

# 2026-03-07 - Design polish & NVIDIA pivot

Today I didn't touch any traces, but focused on polishing the product around the PCB.
I finalized the first pass of the industrial enclosure and realized that my Edge Nexus shield and case can be reused with the **`NVIDIA Jetson Orin Nano Super Developer Kit`**, not just RK3588/Orange Pi. The official dev kit already includes a professional carrier board, so my role is to provide an industrial isolation layer and a rugged, EMI‑aware housing around it.

![image](Docs/assets/NVIDIA_JETSON_NANO.png)

I still need to refine mounting points, clearances and I/O cutouts to match the real Jetson dimensions, but the overall architecture (split data/power sides, standoffs at Z=35 mm, and fan tunnel) is compatible. Next step is to stylize the PCB silkscreen and enclosure and then add one more small, fully custom hardware module to increase the amount of hands‑on soldering and assembly in the project.

# 2026-03-08 to 09 - Front HMI Board: Routing & Design

> Today I completed the PCB routing for the Edge Nexus Front HMI module. To make it a realistic piece of industrial hardware, I went with a 70x20mm 'stick' form factor
- The routing was a good exercise in thinking about current. The LEDs and signals with thinner traces.

A engineering thing here was trace width managment. Since the 4 WS2812B LEDs. I routed the 5V and GND with thicker traces in addition to routing the other NETs. The board ended up at **70x200 mm**.  This form factor fits all things if the system need. 

> I also poured a ground plane to improve EMI shielding and a little of silkscreen. This parts i did in **KiCad**, I'll study how this app works. _I think thats it..._

![image](Docs/assets/frontPCB.png)

### Time spent ~11h

### 2026-03-10 to 16 - Enclousure Integration
All CAD this week. Imported STEP files of both boards into OnShape and positioned everything: isolation shield stacked above the Jetson via the 40-pin header, Front HMI mounted behind the front face panel with M3 bolts.

 For the front panel I dropped the rctangular window idea- went with **individual cutouts** instead: 4 small holes alligned to the LED centrs + 1 larger hole for the button. I think it looks like industrial/server equipment. Also had to work around the Jetson's fan exhaust path, refining side vents and standoff heights to keep airflow clear.

 ![image](Docs/assets/HMIboard.png)

### Time spent: ~15h

# 2026-03-16 & 17 - Cleanup & Submission Prep

Cleaned up the repo structure, wrote (but not versioned) `jetson_status_demo.py`using `Jetson.GPIO` - reads the MODE button and cycles LED states: blue (idle), green (processing), red blinking (emergency). Hardware stub for now, but the state machine and eletrical interface are fully documented.

**Edge Nexus V1 is ready to submit.** 🚀

### Time spent: ~5h

---

## 2026-03-18 to 22 — The Great Pivot (15h)
- Scrapped the Jetson shield idea. Felt like "buying a computer" instead of hardware engineering. 
- Decision: Build a standalone Industrial Controller using ESP32-S3 (WeAct Studio).
- Re-did schematic:
    - Added RS-485 (SP3485) for Modbus.
    - Added 2x Relays for load switching.
    - Added sensors: INA219 (power), SHT41 (env), DS3231 (RTC).
    - Kept PC817 isolation stage from V1.
- Started 100x80mm layout. 

## 2026-03-23 to 27 — Routing & 3D (12h)
- Fixed layout: Blocked screw terminals with the ESP32 module in the first pass. Moved all connectors to board edges.
- CR2032 battery holder routed under the ESP32 module to save space. 
- Enforced 1.5mm air gap between Dirty and Clean ground planes. 
- 3D Model check: Moved SD slot to fix Z-axis collision with the ESP32 body.
- Exported Gerbers, BOM, and PickPlace.

![image](Docs/assets/pcb_routing_view.png)
![image](Docs/assets/main_shield_3d_render.png)

## 2026-03-28 to 30 — Final Submission Prep (8h)
- Updated OnShape enclosure for the new board dimensions and relay heights.
- Verified BOM links and part pricing.
- Final repo cleanup.

**Timelapses:**
- [new parts & searching](https://lapse.hackclub.com/timelapse/lmfT6dZKEx6h)
- [more working to submit](https://lapse.hackclub.com/timelapse/3QgjKu2FWrUs)
- [making the pivot](https://lapse.hackclub.com/timelapse/ZSAejujQKgtY)

**Edge Nexus V2 — submitted. 🚀**
