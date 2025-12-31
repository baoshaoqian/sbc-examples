from periphery import I2C

def i2c_device_detection():
    """I2C Test - Check if device exists
    Pin reference: PJ23 (SDA), PJ22 (SCL)
    """
    # Modify according to your hardware connection
    # Common I2C bus devices: /dev/i2c-0, etc.
    I2C_BUS = "/dev/i2c-7"
    TARGET_ADDR = 0x3C  # Target address to check

    i2c = None  # Initialize I2C object reference
    try:
        # Initialize I2C object
        i2c = I2C(I2C_BUS)

        # Attempt a simple read/write operation to detect device
        # Sending a single 0x00 byte as test communication
        msgs = [I2C.Message([0x00])]
        i2c.transfer(TARGET_ADDR, msgs)

        print(f"I2C Test: Device found at address 0x{TARGET_ADDR:02X}")
        return True

    except Exception as e:
        # Exception (e.g., IOError) usually indicates no device or no response
        print(f"I2C Test: No device or no response at address 0x{TARGET_ADDR:02X}: {e}")
        return False
    finally:
        # Ensure I2C resources are released
        if i2c is not None:
            try:
                i2c.close()
            except:
                pass

if __name__ == "__main__":
    print("Starting I2C Device Detection...")
    i2c_device_detection()
    print("I2C Test completed")
