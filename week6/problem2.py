import sys


def palindrome():
    test_string = input("please input the string to be tested")
    test_string = test_string.casefold()
    reverse_test_string = reversed(test_string)
    if list(test_string) == list(reverse_test_string):
        print(f"The string {test_string} is a palindrome")
    else:
        print(f"The string {test_string} is NOT a palindrome")


def main():
    print(f"Hello this is to check whether the string is a palindrome")

    palindrome()

    return 0


if __name__ == "__main__":
    sys.exit(main())
