from periphery import GPIO
import time

def read_gpio_input():
    # Configure GPIO input (modify pin number according to actual hardware)
    # Using pin 324 of /dev/gpiochip0 here (corresponds to PK4)
    try:
        # Initialize GPIO in input mode
        gpio_in = GPIO("/dev/gpiochip0", 324, "in")

        print("Starting GPIO input reading (press Ctrl+C to exit)")
        while True:
            # Read pin value
            value = gpio_in.read()
            print(f"GPIO input value: {value} (True=High, False=Low)")
            time.sleep(1)  # Read once per second

    except KeyboardInterrupt:
        print("\nProgram exited")
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        # Ensure resources are released
        try:
            gpio_in.close()
        except:
            pass

if __name__ == "__main__":
    read_gpio_input()
