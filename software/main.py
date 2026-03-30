# Edge Nexus V2 - ESP32-S3 Standalone Industrial Controller
# MicroPython Firmware
# Author: @EngThi
#
# Pinout (WeAct Studio ESP32-S3):
#   SDA  -> GPIO 8
#   SCL  -> GPIO 9
#   SD CS -> GPIO 10
#   RS485 DE/RE -> GPIO 4
#   RS485 TX -> GPIO 5
#   RS485 RX -> GPIO 6
#   RELAY_1 -> GPIO 11
#   RELAY_2 -> GPIO 12
#   ISO_IN_1..4 -> GPIO 14, 15, 16, 17

import time
from machine import Pin, I2C, SPI, UART, SoftI2C

# ── I2C Bus (SHT41, INA219, DS3231) ────────────────────────────────────────
i2c = SoftI2C(scl=Pin(9), sda=Pin(8), freq=400_000)

# ── Relay outputs ───────────────────────────────────────────────────────────
relay1 = Pin(11, Pin.OUT, value=0)
relay2 = Pin(12, Pin.OUT, value=0)

# ── RS-485 UART ─────────────────────────────────────────────────────────────
rs485_de = Pin(4, Pin.OUT, value=0)   # Drive Enable (LOW = receive)
uart = UART(1, baudrate=9600, tx=5, rx=6)

# ── Isolated digital inputs ─────────────────────────────────────────────────
iso_inputs = [Pin(p, Pin.IN, Pin.PULL_UP) for p in (14, 15, 16, 17)]

# ── SHT41 helpers (I2C addr 0x44) ──────────────────────────────────────────
SHT41_ADDR = 0x44

def sht41_read():
    """Returns (temperature_C, humidity_pct) or (None, None) on error."""
    try:
        i2c.writeto(SHT41_ADDR, bytes([0xFD]))   # high-precision measure
        time.sleep_ms(10)
        raw = i2c.readfrom(SHT41_ADDR, 6)
        t_raw = (raw[0] << 8) | raw[1]
        h_raw = (raw[3] << 8) | raw[4]
        temp = -45 + 175 * t_raw / 65535
        hum  = -6  + 125 * h_raw / 65535
        return round(temp, 2), round(max(0, min(100, hum)), 2)
    except Exception:
        return None, None

# ── INA219 helpers (I2C addr 0x40) ─────────────────────────────────────────
INA219_ADDR = 0x40

def ina219_read_voltage():
    """Returns bus voltage in volts or None on error."""
    try:
        i2c.writeto(INA219_ADDR, bytes([0x02]))  # Bus voltage register
        time.sleep_ms(2)
        raw = i2c.readfrom(INA219_ADDR, 2)
        v_raw = ((raw[0] << 8) | raw[1]) >> 3
        return round(v_raw * 0.004, 3)           # 4mV LSB
    except Exception:
        return None

# ── RS-485 transmit helper ──────────────────────────────────────────────────
def rs485_send(data: bytes):
    rs485_de.value(1)   # enable transmit
    uart.write(data)
    time.sleep_ms(2)
    rs485_de.value(0)   # back to receive

# ── Main loop ───────────────────────────────────────────────────────────────
print("Edge Nexus V2 — booting...")

while True:
    temp, hum = sht41_read()
    voltage   = ina219_read_voltage()
    iso_state = [p.value() for p in iso_inputs]

    print(f"[ENV] Temp: {temp}°C  Hum: {hum}%")
    print(f"[PWR] Bus voltage: {voltage}V")
    print(f"[ISO] Inputs: {iso_state}")

    # Example: activate relay 1 if ISO input 1 is triggered (active-low)
    relay1.value(1 if iso_state[0] == 0 else 0)

    # Broadcast telemetry over RS-485 every 5 s
    if temp is not None:
        msg = f"EN2,{temp},{hum},{voltage}\r\n"
        rs485_send(msg.encode())

    time.sleep(5)
