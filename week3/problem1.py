import sys
import random


def main():
    random_list = random.sample(range(0, 9), 5)
    print(random_list)
    # prompting the user to input a number between 0 and 9
    print(f"This is a guessing  game")
    guess = int(input("Please choose a number between 0 and 9"))

    if guess in random_list:
        print(f"You win!")
    else:
        print(f"You lose!")

    return 0


if __name__ == "__main__":
    sys.exit(main())
