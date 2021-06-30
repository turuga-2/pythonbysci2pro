import sys
import random


def main():
    L1 = list(random.sample(range(0, 100), 100))
    print(f"L1 is: {L1}")
    # a
    L2 = list(random.sample(range(0, 100), 100))
    print(f"L2 is: {L2}")
    # b
    L3 = list(x+y for x,y in zip(L1, L2))
    print(f"L3 is : {L3}")

    cum_prod = (sum(a*b for a, b in zip(L1,L3)))
    print(f"cum_prod: {cum_prod}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
