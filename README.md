# 🛰️ Edge Nexus: Standalone Industrial Edge Controller

**An autonomous ESP32-S3 based industrial gateway with galvanic isolation and RS-485 communication.**

![Banner](Docs/assets/assembly_view.png)

## 🚀 The Vision

Edge Nexus is a custom-built industrial controller designed to bridge the gap between IoT microcontrollers and high-noise environments. Originally a shield for AI SoCs, the project **pivoted to a standalone architecture** to focus on true hardware engineering and deterministic industrial automation.

Designed by a Computer Engineering student, Edge Nexus provides a reliable, isolated brain for edge automation, telemetry, and local data logging without the need for expensive, off-the-shelf single-board computers.

## 🔌 Core Hardware Features

- **Brain:** Powered by the **ESP32-S3 (WeAct Studio)**, providing high-performance dual-core processing, WiFi, and Bluetooth.
- **Galvanic Isolation:** 4-channel input protection using PC817 optocouplers. This physically decouples high-voltage spikes from "dirty" industrial sensors from the sensitive MCU logic.
- **Industrial Comms:** Integrated **SP3485 transceiver** for RS-485 / Modbus communication, standard for industrial PLC and sensor networks.
- **Power Management:** Integrated LM2596 buck converter stage. It steps down 12-19V (from laptop bricks) to a stable 5V rail to power the entire system.
- **Actuation & Telemetry:** 
    - Dual **5V Relays** for physical load control.
    - **INA219** for real-time voltage and current monitoring.
    - **DS3231 RTC** with backup battery for precise offline timestamps.
    - **AHT20** sensor for environmental (temperature/humidity) monitoring.
- **Storage:** Onboard **MicroSD slot** for long-term offline data logging.

## 🛠️ Design & Fabrication

### PCB Design (EasyEDA)
![PCB View](Docs/assets/main_shield_3d_render.png)
*Left: Edge Nexus V2 Standalone Controller | Right: Isolation Gap and Routing.*

### Mechanical Engineering (OnShape)
The enclosure features integrated mounting bosses and optimized internal clearances to house the ESP32-S3 and the dual-relay setup.
- **[OnShape Public Document Link](https://cad.onshape.com/documents/94f51a65c203ef61216a8e76/w/3996b9a7978ffab042ea39f4/e/1a9b65c9926a8d71aaf1da83?renderMode=0&uiState=69c037fa21771c3657426373)**

## 🛒 Replication Cost & BOM

This Bill of Materials (BOM) focuses on the **replication cost** for a single unit, excluding shipping, taxes, and import fees.

![Shopping Cart](Docs/assets/jlcpcb_cart_v2.png)
*Ordering both V2 PCBs (Main Shield & HMI) from JLCPCB.*

![Parts Inventory](Docs/assets/lcsc_parts_v2.png)
*V2 Components (Relays, ESP32 headers, RS-485 transceiver) from LCSC/Arrow.*
## 🛒 Replication Cost & BOM

This Bill of Materials (BOM) focuses on the **replication cost** for a single unit, strictly considering the merchandise price (excluding shipping, taxes, and import fees).

![Shopping Cart](Docs/assets/jlcpcb_cart_v2.png)
*Ordering both V2 PCBs (Main Shield & HMI) from JLCPCB.*

![Parts Inventory](Docs/assets/lcsc_parts_v2.png)
*V2 Components (33 items including Relays, Transceivers, and Sensors) from LCSC.*

| Component | Quantity | Supplier | Unit Price (Merchandise) | Link |
| :--- | :--- | :--- | :--- | :--- |
| **ESP32-S3 WeAct Studio** | 1 | AliExpress | $6.66 | [Link](https://pt.aliexpress.com/item/1005005592730189.html) |
| **LCSC Components Batch** | 1 set | LCSC | $43.43 | [Cart Total] |
| **PCB Manufacturing** | 1 set | JLCPCB | $6.10 | [Link](https://jlcpcb.com) |
| **Total Project Cost** | **-** | **-** | **$56.19** | **(No tax/shipping)** |

> **🇧🇷 Note for Brazilian Devs (São Paulo/Hack Clubbers):** For builders in São Paulo, the final cost to have all these parts in hand should stay very close to this total. Many passives and standard connectors can be found at Santa Ifigênia for similar prices, and the ESP32/LCSC imports (when below the tax threshold) maintain this competitive cost.

For the complete list of all 33+ parts with MPN and MOQ, check the main `BOM.csv` file.

## 📂 Project Structure

*   `BOM.csv`: Complete project Bill of Materials (Main).
*   `/Hardware`:
    *   `/Hardware/3D_Models`: Enclosure and board `.STEP` files.
    *   `/Hardware/Main_Shield`: Fabrication files for the standalone controller.
    *   `/Hardware/PCB`: Original EDA source files (`.epro`).
*   `/Docs`: Assets and documentation images.
*   `JOURNAL.md`: The complete technical development log.

***

_Developed for the Hack Club Blueprint 2026._
_Designed by @EngThi_
