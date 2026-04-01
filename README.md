# SHIP HARDWARE, NOT BUDGETS: Industrial Control for under $60

# Edge Nexus: Standalone Industrial Edge Controller

This is a custom industrial carrier board I built for high-noise environments. It uses PC817 optocouplers for isolation and has RS-485/Modbus comms through an SP3485 chip. I wrote all the docs myself, including the 80+ hours of logs in JOURNAL.md. I optimized the budget using AliExpress and LCSC parts to keep the hardware cost under $60.

![Banner](Docs/assets/assembly_view.png)

## Why I built this

Edge Nexus is an industrial controller meant to bridge the gap between standard IoT boards and noisy factory floors. It started as a shield for bigger SBCs, but I decided to make it standalone. It focuses on actual hardware engineering rather than just plugging things into a Linux computer.

I'm a Computer Engineering student and I wanted a reliable, isolated brain for automation and logging that doesn't cost hundreds of dollars for off-the-shelf parts.

## What is on the board

- Brain: ESP32-S3 (WeAct Studio module). It handles the logic, WiFi, and Bluetooth.
- Isolation: 4-channel input protection using PC817 optocouplers. This stops high-voltage spikes from killing the ESP32.
- Comms: SP3485 transceiver for RS-485 / Modbus. This is the standard for industrial PLCs.
- Power: Built-in LM2596 buck converter. You can power the whole thing from a 12-19V laptop brick.
- Relays: Two 5V relays to switch actual loads.
- Sensors: INA219 for power monitoring, SHT41 for temp/humidity, and a DS3231 RTC for keeping time offline.
- Storage: MicroSD slot to save logs without needing a cloud connection.

## Design and Making it

### PCB Layout
![PCB View](Docs/assets/main_shield_3d_v2.png)
*V2 Standalone Controller and the routing details.*

### Mechanicals
I designed the enclosure in OnShape with mounting bosses and enough space for the relays and the ESP32.
- [OnShape Public Link](https://cad.onshape.com/documents/94f51a65c203ef61216a8e76/w/3996b9a7978ffab042ea39f4/e/1a9b65c9926a8d71aaf1da83?renderMode=0&uiState=69c037fa21771c3657426373)

## How I'm assembling it

The PCB is coming bare from JLCPCB. I'm hand-soldering everything myself—optoacopladores, the transceiver, buck converter, and all the headers. I want to verify the isolation gap and continuity manually before I ever turn it on.

## Cost to replicate

This is the price for the parts, not including shipping or taxes.

![Shopping Cart](Docs/assets/jlcpcb_cart_v2.png)
*PCBs from JLCPCB.*

![Parts Inventory](Docs/assets/lcsc_parts_v2.png)
*Parts from LCSC.*

| Item | Qty | From | Price |
| :--- | :--- | :--- | :--- |
| ESP32-S3 WeAct Studio | 1 | AliExpress | $6.66 |
| LCSC Components Batch | 1 set | LCSC | $43.43 |
| PCB Manufacturing | 1 set | JLCPCB | $6.10 |
| **Total** | | | **$56.19** |

Note for people in Brazil (São Paulo): If you are around Santa Ifigênia, you can get most of the passives and connectors there for cheap. The ESP32 and LCSC orders usually stay under the tax limit if you're careful.

Check BOM.csv for the full list of all 33+ parts.

### Shipping info
I used Global Standard Direct Line for the PCBs, which is the cheapest tracked option to Brazil.

![JLCPCB Shipping Options](Docs/assets/jlcpcb_shipping_options.png)

## Folder Structure

```
├── BOM.csv                         # Full parts list
├── JOURNAL.md                      # Engineering logs
├── Hardware/
│   ├── Main_Shield/
│   │   ├── Fabrication/            # Gerbers and BOM
│   │   ├── PCB/                    # EasyEDA files
│   │   └── Schematics/             # PDF Schematic
│   ├── Front_HMI/                  # HMI board files
│   └── 3D_Models/                  # STEP files
├── Docs/                           # Images and renders
└── software/
    └── main.py                     # Firmware
```

---

Developed for Hack Club Blueprint 2026. Designed by @EngThi
