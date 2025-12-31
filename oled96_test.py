from periphery import I2C
import time

I2C_ADDR = 0x3c
I2C_BUS = "/dev/i2c-1"

i2c = I2C(I2C_BUS)

# SSD1306 init_cmds
init_cmds = [
    0xAE,  # Display off
    0x00,  # Set lower column address
    0x10,  # Set higher column address
    0x40,  # Set display start line
    0xB0,  # Set page address
    0x81,  # Set contrast control
    0xCF,
    0xA1,  # Set segment remap
    0xA6,  # Normal display
    0xA8,  # Set multiplex ratio
    0x3F,
    0xC8,  # Set COM output scan direction
    0xD3,  # Set display offset
    0x00,
    0xD5,  # Set display clock divide ratio/oscillator frequency
    0x80,
    0xD9,  # Set pre-charge period
    0xF1,
    0xDA,  # Set COM pins hardware configuration
    0x12,  
    0xDB,  # Set VCOMH deselect level
    0x40,
    0x8D,  # Enable charge pump regulator
    0x14,
    0xAF   # Display on
]

for cmd in init_cmds:
    i2c.transfer(I2C_ADDR, [I2C.Message([0x00, cmd])])

def oled_clear():
    for page in range(8):
        i2c.transfer(I2C_ADDR, [I2C.Message([0x00, 0xB0 + page])])
        i2c.transfer(I2C_ADDR, [I2C.Message([0x00, 0x00])])
        i2c.transfer(I2C_ADDR, [I2C.Message([0x00, 0x10])])
        for _ in range(128):
            i2c.transfer(I2C_ADDR, [I2C.Message([0x40, 0x00])])

oled_clear()

# Place a single pixel in the center of the display
i2c.transfer(I2C_ADDR, [I2C.Message([0x00, 0xB0 + 4])])  # Page 4
i2c.transfer(I2C_ADDR, [I2C.Message([0x00, 0x00])])      # Lower column address 0
i2c.transfer(I2C_ADDR, [I2C.Message([0x00, 0x10])])      # Higher column address 64 (0x40)
i2c.transfer(I2C_ADDR, [I2C.Message([0x40] + [0x00]*63 + [0x01] + [0x00]*64)])  # Set pixel at (64, 32)

i2c.close()
