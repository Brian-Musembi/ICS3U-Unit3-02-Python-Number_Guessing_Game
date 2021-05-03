#!/usr/bin/env python3

# Created by: Brian Musembi
# Created on: 02 May 2021
# This program allows the user to guess the correct number


def main():
    # this function allows the user to guess the correct number

    # input
    guess = int(input("Enter a number between 0 - 9: "))

    # process & output
    if guess == 5:
        print("You guessed correct!")
    if guess != 5:
        print("You guessed wrong!")
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
