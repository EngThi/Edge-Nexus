# Budget Breakdown — Edge Nexus V2

All prices below are merchandise cost only. Shipping, taxes, and import fees are excluded from the total. The goal was to keep the replication cost under $60 using LCSC for components and JLCPCB for the PCB.

## PCB

| Item | Supplier | Price |
| :--- | :--- | :--- |
| Edge Nexus V2 PCB (5 units min.) | [JLCPCB](https://jlcpcb.com) | $6.10 |

The $6.10 figure uses the Global Standard Direct Line shipping to Brazil, which is the cheapest tracked option at checkout. A screenshot of the shipping options is in `Docs/assets/jlcpcb_shipping_options.png`.

## Components (LCSC)

Ordered as a single cart. The full pick-and-place and BOM files are in `Hardware/Main_Shield/Fabrication/`.

| Category | Key Parts | Cost |
| :--- | :--- | :--- |
| MCU | ESP32-S3 WeAct Studio (AliExpress) | $6.66 |
| Comms | SP3485 RS-485 transceiver | $0.45 |
| Power | LM2596S-ADJ buck converter | $0.57 |
| Isolation | PC817C optocouplers x4 | $0.16 |
| Actuation | 5V relays x2 | $0.84 |
| Sensors | INA219 x2, SHT41, DS3231 RTC | $4.55 |
| Storage | MicroSD slot | $0.15 |
| Discretes | Transistors, diodes | $0.20 |
| Passives | Resistors, capacitors, inductor | $1.55 |
| Connectors | Headers, screw terminals, battery holder | $2.34 |
| **LCSC subtotal** | | **$10.81** |

Cart screenshot: `Docs/assets/lcsc_parts_v2.png`

## Total

| Vendor | Amount |
| :--- | :--- |
| AliExpress (ESP32-S3) | $6.66 |
| LCSC (all other components) | $10.81 |
| JLCPCB (PCB) | $6.10 |
| **Total** | **$23.57** |

This is the raw parts cost for one unit. The LCSC cart originally showed $43.43 because the minimum order quantities push some passive reels above single-unit needs. The $23.57 figure is the per-unit cost when MOQ overhead is factored out. Full cart screenshot with the $43.43 total is in `Docs/assets/lcsc_parts_v2.png`.

## Notes

- Passives (resistors, capacitors) are ordered in reels of 50–100 pieces due to MOQ. The actual per-unit cost for those is fractions of a cent each.
- No PCBA service is being used. All soldering is done by hand, so the JLCPCB order is bare PCB only.
- For complete part numbers and LCSC links, see the root `BOM.csv`.
