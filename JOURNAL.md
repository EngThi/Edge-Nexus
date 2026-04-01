## 2026-02-27 Day 1

Focus: Schematic design and initial PCB layout in EasyEDA.
![image](Docs/assets/Schematic.png)

What I worked on:
Designed a 4-channel galvanic isolation front-end using PC817 optocouplers and screw terminals. Each channel uses calculated input resistors (470 ohms for 5V sensors) and 10k pull-ups on the 3.3V side to protect the GPIOs from noisy sensors.

![image](Docs/assets/PCBSchematic.png)

Connector strategy:
Used a 40-pin header compatible with standard ARM boards. This makes the shield flexible for different systems.

Time spent: ~5 hours

Notes:
Basic safety layer is done. This will be the base for the AI pipeline experiments.

## 2026-02-28 to 2026-03-02 - Days 2 to 4

Focus: Component placement, manual routing, and fixing DRC errors.

The challenge:
The EasyEDA auto-router doesn't understand galvanic isolation. It tried to route traces right through the isolation barrier. I had to delete everything and start over manually.

![image](Docs/assets/recent_board_schematic.png)
![image](Docs/assets/70errors.png)

Technical progress:
- Feb 28: Zone organization. Routed the LM2596 buck converter with 1mm traces to handle 3A.
- Mar 1: Ground plane issues. Copper pours weren't reaching pins because of tight clearances around resistors. Had over 70 DRC errors.
- Mar 2: Reset clearance rules to 0.254mm. Manually routed GND lines first. Achieved 0 DRC errors.

![image](Docs/assets/3Dcopper.png)
![image](Docs/assets/3DSchematic.png)

Time Spent: ~13 hours

## 2026-03-03 to 2026-03-06 - Enclosure Design

Focus: CAD, thermals, and mechanical fit.

I imported the PCB step file into OnShape to design the chassis. Wanted a modular, industrial look.

![image](Docs/assets/developing_the_enclosure.png)
![image](Docs/assets/complete_render_enclousure.png)

Had to go back to EasyEDA to fix some mounting hole positions that didn't line up in the CAD.

# 2026-03-07 - Design Polish and NVIDIA Pivot

Realized that the isolation shield and case could work with the Jetson Orin Nano Dev Kit. The Jetson has better CUDA support for what I want to do. I need to adjust the I/O cutouts and mounting points for the Jetson dimensions.

![image](Docs/assets/NVIDIA_JETSON_NANO.png)

# 2026-03-08 to 09 - Front HMI Board

Routed the Front HMI module. 70x20mm stick form factor.
Used 4x WS2812B LEDs. Managed trace widths for power (5V/GND) and thinner lines for signals.

![image](Docs/assets/frontPCB.png)

Time spent: ~11h

# 2026-03-10 to 16 - Enclosure Integration

Positioned the isolation shield above the Jetson. HMI is mounted behind the front panel with M3 bolts.
Changed the front panel from a large window to individual cutouts for LEDs and the button. Looks more professional. Had to check airflow for the Jetson fan.

![image](Docs/assets/HMIboard.png)

Time spent: ~15h

# 2026-03-16 and 17 - Cleanup

Repo structure cleanup. Wrote a test script for the status LEDs using Jetson.GPIO. V1 is basically done.

Time spent: ~5h

## 2026-03-18 to 22 - The Great Pivot (V2)

Decided to drop the Jetson shield idea. It felt like I was just building an accessory for a computer I didn't design. I want to do real hardware engineering. 
The new plan is a standalone industrial controller using an ESP32-S3 (WeAct Studio).

What changed:
- Removed the 40-pin header.
- Added RS-485 (SP3485) for Modbus comms.
- Added 2 relays for load switching.
- Added INA219 (power), SHT41 (env), and DS3231 (RTC).
- Kept the PC817 isolation stage from V1.

Routing was a nightmare. Component count doubled but I wanted to keep the board small (100x80mm).

Lessons learned:
- Move all connectors to the edges. I couldn't reach the terminals with a screwdriver in the first layout because the ESP32 was in the way.
- Hidden battery: Put the CR2032 holder under the ESP32 module to save space.
- Maintained 1.5mm gap for isolation.

![image](Docs/assets/pcb_routing_view.png)
![image](Docs/assets/main_shield_3d_render.png)

Time spent: ~15h

## 2026-03-23 to 29 and until 04-01 - Final Tweaks

- Fixed a collision between the SD slot and the ESP32 in the 3D model.
- Updated silkscreen labels.
- Generated Gerbers and BOM.
- Adjusted the OnShape enclosure for the new board size.

Timelapses:
- [New parts and searching](https://lapse.hackclub.com/timelapse/lmfT6dZKEx6h)
- [Working to submit](https://lapse.hackclub.com/timelapse/3QgjKu2FWrUs)
- [Making the pivot](https://lapse.hackclub.com/timelapse/ZSAejujQKgtY)

Edge Nexus V2 is ready.

Time spent: ~12h
