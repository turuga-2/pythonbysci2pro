import sys
import random


def main():
    l = list(random.sample(range(0, 100), 100))
    print(l)

    new_1 = []
    n = 0
    for x in range(0, len(l)):
        n += l[x]
        new_1.append(n)
    print(new_1)

    new_2 = list(q + r for q, r in zip(l, l[1:]))
    new_2.append(0)
    print(new_2)
    print(len(new_2))

    # this is quite advanced syntax; impressive
    # persuade me that this is not a google answer ;-)
    new_3 = list(a + b + c for a, b, c in zip(l, l[2:], l[4:]))
    new_3.append(0)
    print(new_3)
    print(len(new_3))

    return 0


if __name__ == "__main__":
    sys.exit(main())
