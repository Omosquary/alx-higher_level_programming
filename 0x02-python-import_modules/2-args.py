#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argum = len(sys.argv) - 1
    if argum == 0:
        print("0 arguments.")
    elif argum == 1:
        print("1 argumnents:")
    else:
        print("{} arguments:".format(argum))
    for x in range(argum):
        print("{}: {}".format(x + 1, sys.argv[x + 1]))
