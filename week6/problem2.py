import sys


# todo: give the function a better name; this name suggests that it returns a palindrom
# remember what we said about naming functions
def palindrome():
    # todo: add a docstring; see class notes on how to do this
    test_string = input("please input the string to be tested")
    # excellent that you have considered case
    test_string = test_string.casefold()
    # fixme: avoid using builtin functions for this problem
    reverse_test_string = reversed(test_string)
    if list(test_string) == list(reverse_test_string):
        print(f"The string {test_string} is a palindrome")
    else:
        print(f"The string {test_string} is NOT a palindrome")


def main():
    print(f"Hello this is to check whether the string is a palindrome a palindrome"
          f"is a word that spells the same from the beginning and the end")

    palindrome()

    return 0


if __name__ == "__main__":
    sys.exit(main())
