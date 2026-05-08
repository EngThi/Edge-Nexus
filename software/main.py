# Edge Nexus V2 - ESP32-S3 Standalone Industrial Controller
# MicroPython bring-up firmware
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

import os
import time
from machine import Pin, SDCard, SoftI2C, UART


I2C_SDA = 8
I2C_SCL = 9
SD_CS = 10

RS485_DE = 4
RS485_TX = 5
RS485_RX = 6

RELAY_1 = 11
RELAY_2 = 12
ISO_INPUT_PINS = (14, 15, 16, 17)

SHT41_ADDR = 0x44
INA219_ADDRS = (0x40, 0x41)
DS3231_ADDR = 0x68


i2c = SoftI2C(scl=Pin(I2C_SCL), sda=Pin(I2C_SDA), freq=400_000)

relay1 = Pin(RELAY_1, Pin.OUT, value=0)
relay2 = Pin(RELAY_2, Pin.OUT, value=0)

rs485_de = Pin(RS485_DE, Pin.OUT, value=0)
uart = UART(1, baudrate=9600, tx=RS485_TX, rx=RS485_RX)

iso_inputs = [Pin(pin, Pin.IN, Pin.PULL_UP) for pin in ISO_INPUT_PINS]


def bcd_to_dec(value):
    return ((value >> 4) * 10) + (value & 0x0F)


def i2c_scan():
    try:
        return i2c.scan()
    except Exception:
        return []


def sht41_read():
    """Return (temperature_C, humidity_pct), or (None, None) on error."""
    try:
        i2c.writeto(SHT41_ADDR, bytes([0xFD]))
        time.sleep_ms(10)
        raw = i2c.readfrom(SHT41_ADDR, 6)
        t_raw = (raw[0] << 8) | raw[1]
        h_raw = (raw[3] << 8) | raw[4]
        temp = -45 + 175 * t_raw / 65535
        hum = -6 + 125 * h_raw / 65535
        return round(temp, 2), round(max(0, min(100, hum)), 2)
    except Exception:
        return None, None


def ina219_read_voltage(addr):
    """Return bus voltage in volts, or None on error."""
    try:
        i2c.writeto(addr, bytes([0x02]))
        time.sleep_ms(2)
        raw = i2c.readfrom(addr, 2)
        v_raw = ((raw[0] << 8) | raw[1]) >> 3
        return round(v_raw * 0.004, 3)
    except Exception:
        return None


def ds3231_read_time():
    """Return a compact timestamp from DS3231, or uptime fallback."""
    try:
        i2c.writeto(DS3231_ADDR, bytes([0x00]))
        raw = i2c.readfrom(DS3231_ADDR, 7)
        sec = bcd_to_dec(raw[0] & 0x7F)
        minute = bcd_to_dec(raw[1])
        hour = bcd_to_dec(raw[2] & 0x3F)
        day = bcd_to_dec(raw[4])
        month = bcd_to_dec(raw[5] & 0x1F)
        year = 2000 + bcd_to_dec(raw[6])
        return f"{year:04d}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:{sec:02d}"
    except Exception:
        return f"uptime_ms={time.ticks_ms()}"


def mount_sd():
    try:
        sd = SDCard(slot=2, cs=Pin(SD_CS))
        os.mount(sd, "/sd")
        return True
    except Exception:
        return False


def append_log(line):
    try:
        with open("/sd/edge_nexus.csv", "a") as log:
            log.write(line + "\n")
    except Exception:
        pass


def rs485_send(data):
    rs485_de.value(1)
    time.sleep_ms(1)
    uart.write(data)
    time.sleep_ms(4)
    rs485_de.value(0)


def build_telemetry():
    temp, hum = sht41_read()
    voltages = [ina219_read_voltage(addr) for addr in INA219_ADDRS]
    iso_state = [pin.value() for pin in iso_inputs]
    timestamp = ds3231_read_time()

    # Inputs are active-low after the optocoupler stage.
    relay1.value(1 if iso_state[0] == 0 else 0)
    relay2.value(1 if iso_state[1] == 0 else 0)

    return {
        "timestamp": timestamp,
        "temp": temp,
        "hum": hum,
        "v0": voltages[0],
        "v1": voltages[1],
        "iso": iso_state,
        "relay1": relay1.value(),
        "relay2": relay2.value(),
    }


def telemetry_line(data):
    iso_bits = "".join(str(value) for value in data["iso"])
    return (
        f"EN2,{data['timestamp']},"
        f"T={data['temp']},H={data['hum']},"
        f"V0={data['v0']},V1={data['v1']},"
        f"ISO={iso_bits},R1={data['relay1']},R2={data['relay2']}"
    )


print("Edge Nexus V2 - booting...")
print("I2C devices:", [hex(addr) for addr in i2c_scan()])

sd_ready = mount_sd()
print("MicroSD logging:", "enabled" if sd_ready else "not mounted")

if sd_ready:
    append_log("timestamp,temp,hum,v0,v1,iso,relay1,relay2")

while True:
    telemetry = build_telemetry()
    line = telemetry_line(telemetry)

    print(line)
    rs485_send((line + "\r\n").encode())

    if sd_ready:
        append_log(
            f"{telemetry['timestamp']},{telemetry['temp']},{telemetry['hum']},"
            f"{telemetry['v0']},{telemetry['v1']},"
            f"{''.join(str(value) for value in telemetry['iso'])},"
            f"{telemetry['relay1']},{telemetry['relay2']}"
        )

    time.sleep(5)
