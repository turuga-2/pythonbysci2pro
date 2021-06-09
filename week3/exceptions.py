import sys


def main():
    # index error
    exe0 = list(range(10))

    # print(exe0[11])

    # catching exceptions
    try:
        v = exe0[11]
    except IndexError as ex:
        print(f"WARNING: {ex}; THE LIST YOU PROVIDED WAS TOO SHORT!!")
        v = 0
    print(f"v = {v}")
    # catching multiple exceptions
    try:
        v = "s" + exe0[4]
    except TypeError as le:
        print(f"WARNING: {le}; not the right type")
        v = "s0"
    print(f"v = {v}")
    # assertion
    age = int(input("Your age"))
    try:
        assert 0 < age < 120
    except AssertionError:
        print(f"error: invalid age {age}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
