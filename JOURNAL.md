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

![image](/assets/recent_board_schematic.png)

![image](/assets/70errors.png)

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

Today I didn’t touch any traces, but focused on polishing the product around the PCB.
I finalized the first pass of the industrial enclosure and realized that my Edge Nexus shield and case can be reused with the **`NVIDIA Jetson Orin Nano Super Developer Kit`**, not just RK3588/Orange Pi. The official dev kit already includes a professional carrier board, so my role is to provide an industrial isolation layer and a rugged, EMI‑aware housing around it.

![image](Docs/assets/NVIDIA_JETSON_NANO.png)

I still need to refine mounting points, clearances and I/O cutouts to match the real Jetson dimensions, but the overall architecture (split data/power sides, standoffs at Z=35 mm, and fan tunnel) is compatible. Next step is to stylize the PCB silkscreen and enclosure and then add one more small, fully custom hardware module to increase the amount of hands‑on soldering and assembly in the project.

# 2026-03-08 to 09 - Front HMI Board: Routing & Design

> Today I completed the PCB routing for the Edge Nexus Front HMI module. To make it a realistic piece of industrial hardware, I went with a 70x20mm 'stick' form factor

A engineering thing here was trace width managment. Since the 4 WS2812B LEDs. I routed the 5V and GND with thicker traces in addition to routing the other NETs.

> I also poured a ground plane to improve EMI shielding and a little of silkscreen. This parts i did in **KiCad**, I'll study how this app works. _I think thats it..._

![image](Docs/assets/frontPCB.png)
## 2026-03-02 – Front HMI Schematic & Planning (3h)
Today I focused entirely on the Edge Nexus Front HMI board. This is the small 70×20 mm PCB that lives on the front of the enclosure and gives the Jetson Orin Nano a proper industrial‑style status interface.

I started by drafting the schematic in EasyEDA:

*   4× WS2812B addressable RGB LEDs connected in series for a vertical status bar.
*   A dedicated N‑channel MOSFET level shifter to convert the Jetson’s 3.3 V GPIO data to a clean 5 V WS2812B signal.
*   Local 0.1 µF decoupling capacitors near each LED, powered from the 5 V rail generated by the isolation shield.
*   A MODE / Emergency button wired between BTN_OUT and GND, plus a 2‑pin header so I can later swap to a big panel‑mount switch without changing the PCB.

The main engineering decision here was to treat this like a real industrial HMI, not just “a strip of LEDs on a breadboard”. The board has its own connector, power domain, and level shifting instead of relying on random breakout modules.

## 2026-03-03 – HMI PCB Layout & Trace Width Tuning (4h)
Today was all about routing and design rules for the HMI PCB.

I locked in a 70×20 mm stick form factor, added four M3 mounting holes, and aligned the WS2812B LEDs in a straight vertical line down the center of the board. The MODE button sits at the bottom so it’s easy to reach on the front panel.

On the electrical side I:

*   Set up explicit trace width rules:
    *   0.30 mm for 5 V and GND rails feeding the LEDs (up to ~240 mA worst case for 4× WS2812B).
    *   0.20 mm for logic signals (DATA line, BTN_OUT, MOSFET gate).
*   Routed the data “snake” from the level shifter into LED1 DIN, then daisy‑chained DOUT → DIN all the way to LED4.
*   Added a solid ground pour on both layers to lower impedance and simplify GND routing.

I ran DRC until I had zero clearance or unconnected‑net errors. It now looks and behaves like a shippable, JLC‑ready PCB, not a quick prototype.

## 2026-03-04 – Silkscreen, KiCad Export & Gerbers (3h)
This session was about giving the board a personality and preparing it for fabrication.

I exported the PCB from EasyEDA into KiCad to tweak the silkscreen and 3D visualization. On the front side I added:

*   Title: “EDGE NEXUS – FRONT HMI” at the top edge.
*   Label “MODE” around the push button.
*   My handle “@EngThi” along the board edge.

On the back I verified the 3D model: connector orientation, LED height and button footprint all line up correctly. With that confirmed, I exported:

*   Full Gerber set for the HMI PCB.
*   Drill file.
*   Position files (Pick & Place) for future assembly.

Even if I don’t immediately send this to JLCPCB, the project is now truly “fabrication‑ready”.

## 2026-03-05 – Enclosure Integration: Mounting, Cutouts & Airflow (5h)
Today I integrated the main isolation shield PCB and the Front HMI PCB into the 3D enclosure.

Steps in CAD:

*   Imported the STEP/OBJ of the Edge Nexus isolation shield and positioned it above where the Jetson Orin Nano dev kit will live.
*   Added standoffs and mounting bosses so the shield sits at a safe height above the dev‑kit components while preserving airflow.
*   Placed the Front HMI board behind the front face of the case and aligned:
    *   Four small circular holes for the WS2812B LEDs.
    *   One larger hole for the MODE button.
    *   Matching screw holes so the HMI can be fixed from behind with M3 bolts.

I also refined the side vents and internal clearances so the fan exhaust from the Jetson is not blocked by my shield. The result is an enclosure that doesn’t just hold the boards; it actually respects thermal and mechanical constraints.

## 2026-03-06 – Jetson GPIO + LED Status Script (Design & Stub) (3h)
I didn’t have the Jetson Orin Nano Super physically wired up yet, but I designed the software side so it’s clear how the hardware will be used.

I outlined a Python script (using Jetson.GPIO) that will:

*   Configure one GPIO pin as input for the MODE button (with internal pull‑up).
*   Configure another GPIO pin as the data line for the WS2812B chain.
*   Implement a simple state machine with modes like:
    *   IDLE – LEDs blue.
    *   PROCESSING – LEDs green, maybe with a simple animation.
    *   ERROR / EMERGENCY – LEDs red, blinking when the button is long‑pressed.

I wrote a stub version of this script with clear TODOs for the actual WS2812B driver (either a Python NeoPixel library or an external microcontroller). The important part is that the electrical contract between Jetson ↔ Shield ↔ HMI is fully documented and reflected in code.

## 2026-03-07 – Final Review & Submission Prep (2h)
Today I did a full pass across the entire Edge Nexus stack to check for inconsistencies before submission:

*   Re‑checked the isolation shield schematic and PCB:
    *   PC817 optocouplers correctly wired with separate dirty/clean grounds.
    *   LM2596 feedback network and capacitors sized for a stable 5 V rail.
*   40‑pin header aligned with the Jetson Orin Nano Super pinout.
*   Confirmed that the Front HMI board dimensions and mounting holes match the front‑panel CAD cutouts.

Cleaned up the repository structure:

*   hardware/isolation_shield/
*   hardware/front_hmi/
*   enclosure/
*   software/jetson_status_demo.py

Finally, I wrote the project description and devlogs explaining the journey: starting with generic ARM SoCs, hitting real limitations, then pivoting to NVIDIA Jetson for proper CUDA/TensorRT support, while building my own industrial isolation shield and HMI around it.

At this point, the project is in a place where I can confidently say: the hardware, enclosure and demo software design are complete – I’m ready to submit Edge Nexus. 🚀

