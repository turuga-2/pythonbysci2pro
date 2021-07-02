import sys
import random


def main():
    l = list(random.sample(range(0, 100), 100))
    print(f"the list L is :{l}")
    print(len(l))

    x = 0
    n = 0
    new_1 = []
    while x <= 100:
        n = n + l[x]
        new_1.append(n)
        x = x + 1
        if x == 100:
            print(new_1)
            print(len(new_1))

    return 0


if __name__ == "__main__":
    sys.exit(main())
