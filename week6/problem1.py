import random
import sys


def maxmini(example1):
    # todo: add a docstring; see class notes on how to do this
    # fixme: do not use max() and min(); come up with your own way to determine min and max
    maximum = max(example1)
    minimum = min(example1)
    print(f"the maximum in the list is {maximum} , while the minimum is {minimum} .")
    return maximum,minimum


def main():
    example1 = list(random.sample(range(1, 20, 2), 10))
    print(f"example 1:{example1}")
    maxmini(example1)
    return 0


if __name__ == "__main__":
    sys.exit(main())
