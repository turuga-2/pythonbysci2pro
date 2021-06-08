import sys


def main():
    # creating a tuple
    example0 = tuple()
    print(example0, type(example0))
    example1 = (1,)
    print(example1, type(example1))
    example2 = 3, 4, 5, 6
    print(example2, type(example2))

    # immutability cannot change a tuple once it is created
    # stings are also immutable
    example1 = (2, 4, 6, 8, 10)
    print(example1, type(example1))
    print(f'The object at index 0 of the tuple is {example1[0]}')
    # you can only make a new tuple
    example3 = (4,) * 4
    print(example3)

    # stings are also immutable

    return 0


if __name__ == "__main__":
    sys.exit(main())
