from physical import *

def demo():
    print("I have pasted a snake game code.\nIf you want to try, run python snake.py.")
    print("But I don't think it can be run in the lab development environment.")

def main():
    setDevice1(True)
    setDevice2(True)

    print(readTemperature())
    print(readMoisture())

    setDevice1(False)
    setDevice2(False)

    print("Starting loop...")
    timer = 2
    counter = 0
    while True:
        if timer <= 0:
            timer = 2
            counter = counter + 1
            print(f"**Loop {counter}:")
            print(readTemperature())
            print(readMoisture())

        timer = timer - 1
        # Time base for this loop
        time.sleep(1)

if __name__ == "__main__":
    # demo()
    main()
