import sys
import random

def main():
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    cum_list = []
    y = 0
    for x in range(0, len(list)):
        y += list[x]
        cum_list.append(y)
    print(list)
    print(cum_list)
    return 0


if __name__ == "__main__":
    sys.exit(main())
