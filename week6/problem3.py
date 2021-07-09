import sys


def string_reversal(test_string):
    reversed_string = ""
    index = len(test_string)
    while index > 0:
        reversed_string += test_string[index - 1]
        index = index - 1

    print(f"The reversed index is : {reversed_string}")


def main():
    print(f"STRING REVERSAL!!")
    test_string = input(f"The string to be reversed is : ")
    string_reversal(test_string)


    return 0


if __name__ == "__main__":
    sys.exit(main())