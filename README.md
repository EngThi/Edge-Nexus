# 🛰️ Edge Nexus

**A custom industrial isolation shield for edge AI pipelines**

Edge Nexus is a carrier board/project with SoC designed to bridge the gapbetween high-performance ARM SOCs (like the Orange PI/ systems base on RK3588) and the noisy world of salvaged hardware.

The goal is to create a reliable brain for local AI pipelines, like projects, studyies and deployments of automations in general purpose without risking expensive processors when connecting old motors or recycled sensors.

### 🔌 Hardware Features

- **Galvanic Isolation:** 4-channel input protection using PC817 optocoupler. This keeps high-voltage spikes from de dirty side away from the sensitive SoC GPIOs.
- **Power Mangment:**
Integrated LM2596 buckconverter stage. It steps down 12-19V (from laptop bricks) to a stable 5V rail to power the entire system.
- **Split-Plane Design:** A dedicated physical gap between `GND_CLEA`and `GND_DIRTY`to prevent EMI/RFI noise couplng.
- **Universal Header:** Standard 40-pin (2x20) interface, making it compatible with most modern ARM based single-board microcomputers (or others systems ARM, SoCs).


### Project Structure

*   `BOM.csv`: Complete project Bill of Materials (Main).
*   `/Hardware`: Contains all the hardware design files.
    *   `/Hardware/3D_Models`: Contains the 3D models of the enclosure.
    *   `/Hardware/Fabrication`: Contains the manufacturing files (Gerber, BOM, Pick and Place).
    *   `/Hardware/PCB`: Contains the PCB design files.
    *   `/Hardware/Schematics`: Contains the schematic files.
*   `/Docs`: Contains the documentation for the project.
    *   `/Docs/assets`: Contains the images and other assets for the documentation.

### 📝 Devlogs
Check the `JOURNAL.md`for technical updates and engineering decisions.

***

_Developed as part of the Hack Club Blueprint 2026_