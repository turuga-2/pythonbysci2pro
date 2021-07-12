import sys
import random


def main():
    l = list(random.sample(range(0, 100), 100))
    print(f"List l :{l}")

    new_1 = []
    n = 0
    for x in range(0, len(l)):
        n += l[x]
        new_1.append(n)
    print(f"new_1: {new_1}")

    new_2 = list(q + r for q, r in zip(l, l[1:]))
    new_2.append(0)
    print(f"new 2: {new_2}")
    print(len(new_2))

    # this is quite advanced syntax; impressive
    # persuade me that this is not a google answer ;-)

    # I simply put the question down in writing as you said then I used q and r to
    # represent the numbers in the first random list l then after addition I used
    # the zip function to zip the additions together to form the new list.
    # I also used the for loop to avoid repeating my code

    new_3 = list(a + b + c for a, b, c in zip(l, l[2:], l[4:]))
    new_3.append(0)
    print(f"new 3: {new_3}")
    print(len(new_3))

    return 0


if __name__ == "__main__":
    sys.exit(main())
