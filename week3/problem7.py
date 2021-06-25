import sys
import math


def main():
    x = 1
    y = (pow(x, 3) - 9 * x) / (pow(x, 2) - 2 * x + 1)
    try:

    except  ZeroDivisionError:
        return 0

    print(y)

    return 0


if __name__ == "__main__":
    sys.exit(main())
