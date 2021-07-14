import sys
import math


def sum_of_list(example_list):
    # todo: add a docstring; see class notes on how to do this
    # fixme: do not use sum()
    the_sum = sum(example_list)
    print(f'the sum is:{the_sum}')
    return the_sum

def main():
    # todo: give your list a better name
    example_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    print(example_list)
    sum_of_list(example_list)
    return 0





if __name__ == "__main__":
    sys.exit(main())
