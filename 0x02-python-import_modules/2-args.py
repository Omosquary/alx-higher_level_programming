#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    arguments = len(sys.argv) - 1
    if arguments == 0:
        print("0 arguments.")
    elif arguments == 1:
        print("1 argumnents:")
    else:
        print("{} arguments:".format(arguments))
    for x in range(arguments):
        print("{}: {}".format(x + 1, sys.argv[x + 1]))
