import time
import random


def read_sensor():
    # read sensor data and return it
    # the specific code for reading the sensor data will depend on the type of sensor being used
    return random.uniform(0, 1) # placeholder random value


def test_sensor():
    for i in range(10): # read sensor 10 times
        data = read_sensor()
        print(f"Reading {i + 1}: {data}")
        time.sleep(1) # wait for 1 second before next reading


if __name__ == '__main__':
    test_sensor()

