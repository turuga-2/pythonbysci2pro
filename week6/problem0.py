import sys
import math


def sum_of_list(example_list):
    the_sum = sum(example_list)
    print(f'the sum is:{the_sum}')
    return the_sum

def main():
    example_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    print(example_list)
    sum_of_list(example_list)
    return 0





if __name__ == "__main__":
    sys.exit(main())
