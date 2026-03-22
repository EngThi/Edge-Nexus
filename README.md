# 🛰️ Edge Nexus: Industrial Isolation for Jetson AI

**A custom carrier-shield and rugged enclosure for the NVIDIA Jetson Orin Nano Super.**

![Banner](Docs/assets/complete_render_enclousure.png)

## 🚀 The Vision

Edge Nexus bridges the gap between high-performance AI SoCs and the "dirty" world of salvaged industrial hardware. It provides a reliable brain for local AI pipelines, automation, and computer vision without risking expensive processors when connecting unshielded sensors or recycled motors.

Originally designed for generic ARM SoCs (RK3588), the project **pivoted to the NVIDIA Jetson Orin Nano Super** to leverage professional-grade CUDA/TensorRT acceleration, while adding a custom industrial safety layer and a rugged, EMI-aware housing.

## 🔌 Core Hardware Features

- **Galvanic Isolation:** 4-channel input protection using PC817 optocouplers. This physically decouples high-voltage spikes from "dirty" field sensors from the sensitive Jetson GPIOs.
- **Power Management:** Integrated LM2596 buck converter stage. It steps down 12-19V (from laptop bricks) to a stable 5V rail to power both the SoC and the HMI layer.
- **Split-Plane Design:** A dedicated physical "no-man's-land" gap between `GND_CLEAN` and `GND_DIRTY` on the PCB to prevent EMI/RFI noise coupling.
- **Front HMI Module:** A dedicated 70x20mm PCB with 4x WS2812B LEDs and a Mode/Emergency button for real-time status feedback.

## 🛠️ Design & Fabrication

### PCB Design (EasyEDA / KiCad)
![PCB View](Docs/assets/3Dcopper.png)
*Left: Isolation Shield Layout | Right: Front HMI Routing.*

### Mechanical Engineering (OnShape)
The enclosure features integrated mounting bosses, internal standoffs at Z=35mm, and optimized airflow paths to prevent thermal throttling under high AI workloads.
- **[OnShape Public Document Link (PENDING - PLEASE UPDATE)]**

## 📂 Project Structure

*   `BOM.csv`: Complete project Bill of Materials with purchase links.
*   `/Hardware`:
    *   `/Hardware/3D_Models`: `.STEP` and `.STL` files for enclosure and PCBs.
    *   `/Hardware/Fabrication`: Production-ready Gerbers, BOM, and Pick & Place files.
    *   `/Hardware/PCB`: Original EDA source files (`.epro`).
    *   `/Hardware/Schematics`: Schematic diagrams and wiring info.
*   `/Docs`:
    *   `/Docs/assets`: Documentation images, renders, and screenshots.
*   `JOURNAL.md`: The complete technical development log.

## 📝 How to Use
1.  **Fabricate:** Send the Gerber files in `/Hardware/Fabrication` to a PCB house like JLCPCB.
2.  **Assemble:** Use the `BOM.csv` to source parts. Solder components onto the Isolation Shield and HMI board.
3.  **3D Print:** Print the enclosure files from `/Hardware/3D_Models`.
4.  **Connect:** Stack the Edge Nexus Shield onto the NVIDIA Jetson 40-pin header.

***

_Developed for the Hack Club Blueprint 2026._
_Designed by @EngThi_
