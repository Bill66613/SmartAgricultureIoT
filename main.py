from physical import *

def demo():
    print("I have pasted a snake game code.\nIf you want to try, run python snake.py.")
    print("But I don't think it can be run in the lab development environment.")

def main():
    setDevice1(True)
    setDevice2(True)

    readTemperature()
    readMoisture()

    setDevice1(False)
    setDevice2(False)
    # counter = 5
    # while True:
    #     if counter <= 0:
    #         counter = 5
    #         readTemperature()
    #         readMoisture()

    #     counter = counter - 1
    #     # Time base for this loop
    #     time.sleep(1)

if __name__ == "__main__":
    # demo()
    main()
