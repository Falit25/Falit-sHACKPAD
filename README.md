# Falit'sHackpad – 10-Key Macro Pad

Falit's Hackpad is a custom 10-key macro pad built using a XIAO RP2040 DIP board.
It uses KMK firmware (CircuitPython) and is designed for productivity shortcuts like launching apps, switching desktops, and system controls.

---

## Features

* 10 mechanical keys
* 4× SK6812 RGB LEDs
* XIAO RP2040 DIP controller
* USB-C connection
* KMK firmware
* Custom 3D-printed case
* App-launch and system macros (Windows)

---

## Hardware

* Controller: Seeed XIAO RP2040 DIP
* Switches: MX-style mechanical switches
* LEDs: SK6812 Mini (NeoPixel-compatible)
* PCB: Custom KiCad design
* Case: Custom Fusion 360 model
* Connection: USB-C

---

## Firmware

Firmware is written using **KMK** and runs on **CircuitPython**.

### Steps

1. Install CircuitPython on XIAO RP2040
2. Copy the KMK firmware folder to the board
3. Upload `main.py` to the CIRCUITPY drive
4. Reboot the board

---

## Notes

* App-launch shortcuts use AutoHotkey for reliability
* LEDs are driven from GPIO3
* Keys are connected using direct GPIO pins
* Modify `main.py` to change macros or lighting behavior

---

## License

This project is for personal and educational use.

---

## Author

Mahi
B.Tech Student – VIT Bhopal
Specialization: AI & ML
