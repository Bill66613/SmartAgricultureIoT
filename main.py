from physical import *

def demo():
    print("I have pasted a snake game code.\nIf you want to try, run python snake.py.")
    print("But I don't think it can be run in the lab development environment.")

def main():
    setDevice1(True)
    print("Relay 1 ON: " + serial_read_data(ser))
    setDevice2(True)
    print("Relay 2 ON: " + serial_read_data(ser))

    setDevice1(False)
    print("Relay 1 OFF: " + serial_read_data(ser))
    setDevice2(False)
    print("Relay 2 OFF: " + serial_read_data(ser))

    print("Read Temperature: " + readTemperature())
    print("Read Moisture" + readMoisture())

    distance9 = [9, 3, 0, 5, 0, 1, 149, 67]
    distance12 = [12, 3, 0, 5, 0, 1, 149, 22]
    print("Starting loop of 2 second task...")
    timer = 2
    counter = 0
    while True:
        if timer <= 0:
            timer = 2
            counter = counter + 1
            print(f"**Loop {counter}:")
            ser.write(distance9)
            print("distance9: " + serial_read_data(ser))
            ser.write(distance12)
            print("distance12: " + serial_read_data(ser))

        timer = timer - 1
        # Time base for this loop
        time.sleep(1)

if __name__ == "__main__":
    # demo()
    main()
