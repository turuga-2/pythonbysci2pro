import sys
import random


def main():
    l = [random.sample(range(0, 100), 100)]
    print(l)

    new_1 = []
    n = 0
    for x in range(0, len(l)):
        n += l[x]
        new_1.append(n)

    print(new_1)

    # new_1 =list(new_1[n-1] = list1[0] + list1[1])

    return 0


if __name__ == "__main__":
    sys.exit(main())
