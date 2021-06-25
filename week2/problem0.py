import sys
import os


def main():
    name = input("Please enter your full name")
    age = input("Please enter your current age")

    print(f'Hello my name is {name} and I am {age} years old.')

    return 0


if __name__ == "__main__":
    sys.exit(main())
