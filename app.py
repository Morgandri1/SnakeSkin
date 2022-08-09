from CopperUI import *
import sys
import keyboard
import os

try:
    try:
        if os.path.isfile(str(sys.argv[1])):
            with open(str(sys.argv[1]), "r") as file:
                banner("SnakeSkin", color=green)
                print(f"{str(sys.argv[1])}:")
                print("use ctrl+c to exit \n")
                with open(str(sys.argv[1]), "a+") as write:
                    while True:
                        if keyboard.is_pressed(""):
                            """"""
                        new = input(file.read())
                        write.write(new + "\n")
        else:
            with open(str(sys.argv[1]), "w") as file:
                file.write(input(""))
    except KeyboardInterrupt:
        print("\nSaved and Exiting...")
        sys.exit()

except IndexError:
    banner("SnakeSkin", color=green)
    input("please enter filename: ")
