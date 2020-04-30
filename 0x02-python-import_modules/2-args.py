#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    len = len(argv) - 1
    print("{} argument".format(len), end='')
    if len == 0:
        print("s.")
    elif len == 1:
        print(":")
    else:
        print("s:")
    for i in range(1, len + 1):
        print("{}: {}".format(i, argv[i]))
        
