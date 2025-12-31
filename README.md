# 0.96 inch OLED Display Example Code

This repository contains example code for interfacing with a 0.96 inch OLED display using various microcontrollers. The code demonstrates how to initialize the display, draw shapes, and display text.

## Hardware

- A 0.96 inch OLED display (typically using the SSD1306 driver)
- A microcontroller (Tested with Raspberry Pi 4, Raspberry Pi 5, Radxa Cubie A7A)

## Software

First, enable I2C on your microcontroller and connect the OLED display according to the following pinout:
- VCC to 3.3V or 5V
- GND to Ground
- SCL to I2C Clock
- SDA to I2C Data

To detect the I2C address of your OLED display, you can use the following command on Linux-based systems:

```bash
# For Raspberry Pi
sudo i2cdetect -y 1
# For Cubie A7A
sudo i2cdetect -y 7
```

### Cubie A7A

1. OS: Debian Bullseye
2. Install necessary libraries:
   ```bash
   sudo pip3 install python-periphery
   ```
3. Run the example code:
   - i2c_teset.py
   - oled96_hello.py

### Raspberry Pi 4 / Raspberry Pi 5

1. OS: Raspberry Pi OS

TODO
