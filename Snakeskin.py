from CopperUI import *
import sys
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
                        new = input(file.read())
                        write.write(new + "\n")
        else:
            with open(str(sys.argv[1]), "w") as file:
                file.write("")
            with open(str(sys.argv[1]), "r") as file:
                banner("SnakeSkin", color=green)
                print(f"{str(sys.argv[1])}:")
                print("use ctrl+c to exit \n")
                with open(str(sys.argv[1]), "a+") as write:
                    while True:
                        new = input(file.read())
                        write.write(new + "\n")
            
    except KeyboardInterrupt:
        print("\nSaved and Exiting...")
        sys.exit()

except IndexError:
    banner("SnakeSkin", color=green)
    filename = input("please enter filename: ")
    if os.path.isfile(filename):
        with open(filename, "r") as file:
            banner("SnakeSkin", color=green)
            print(f"{filename}:")
            print("use ctrl+c to exit \n")
            with open(filename, "a+") as write:
                while True:
                    new = input(file.read())
                    write.write(new + "\n")
    else:
        with open(filename, "w") as file:
            file.write("")
        with open(filename, "r") as file:
            banner("SnakeSkin", color=green)
            print(f"{filename}:")
            print("use ctrl+c to exit \n")
            with open(filename, "a+") as write:
                while True:
                    new = input(file.read())
                    write.write(new + "\n")
