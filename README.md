# SBC Examples

## 0.96" OLED Display with I2C Interface

### I2C Setup

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

### Python Setup

1. Make sure you have the required Python libraries installed. You can install them using pip:

```bash
# It is recommended to use a virtual environment,
# create a virtual environment in your project directory and activate it.
python3 -m venv venv
source venv/bin/activate

# Make sure the virtual environment is activated,
# then install the required libraries:
pip install python-periphery
```

2. Run the provided Python scripts to test I2C communication and display a message on the OLED screen:
> Be sure to adjust the I2C bus number in the scripts if necessary (e.g., `/dev/i2c-1` for Raspberry Pi, `/dev/i2c-7` for Cubie A7A, etc.).


```bash
# Run the I2C test script to verify communication with the OLED display
python i2c_test.py

# Run the OLED display script to see the output on the screen
python oled_hello.py
```


