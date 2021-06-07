import sys
import os


def main():
    name = input("Please enter your full name")
    age = int(input("Please enter your current age"))
    birth_year = 2021 - age
    seventy_seven = birth_year + 77

    print(f'Hello my name is {name} and I am {age} years old.')
    print(f'My birth year was {birth_year} and in {seventy_seven} I will be seventy seven years old')

    return 0


if __name__ == "__main__":
    sys.exit(main())
