## 2026-02-27 Day 1

**Focus:** Schematic design and initial PCB laypout in EasyEDA
![image](assets/Schematic.png)

## What I worked on

**Opto-isolation input stage**
Designed a 4-channel galvanic isolationfront-end using PC817 optocouplers and screw terminals. Each channels uses calculated input resistors `(470 Ω for 5V sensors)`and 10KΩ pull-ups on the 3.3 V side to protect the SoC GPIOs from dirty, salvaged sensors.

![image](assets/PCBSchematic.png)

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
![image](assets/3Dcopper.png)

![image](assets/3DSchematic.png)

### Time Spent **Approx:** 12,5 - 13 hours

### Notes & Next steps 
- This was the hardest phase yet (software auto-routers don't understand physical isolation requiremnts... I didn't configured it that way, but I think it would cause some problems aniway).
- Now I'll i port the `3D file`into **OnShape** to begin the mechanical enclousure design, focusing on thermal dissipation for high-performance SoCs (I think it must be that).

## 2026-03-03 to 2026-03-06 - Basically the enclousure, Cyberdeck vibe

**Focus:** Mechanical CAD design, thermal managment for AI processors and EMI mitigation.

### Transition to mechanical engineering 
With the `Edge Nexus`PCB fully routed, next I create a physical environment that could handle the heat and connectivity of an Edge AI and domestic multi-service brain. Primarily targeting a SoC like RK3588 that would later develop a complete component/board for this use, but later studying and remembering that **`professional systems use NVIDIA chips`**, I think this will be the ideal solution.

I imported the `.STEP`file to OnShape and designed a modular, cyberdeck-style split chassis.


![image](assets/developing_the_enclosure.png)

![image](assets/complete_render_enclousure.png)