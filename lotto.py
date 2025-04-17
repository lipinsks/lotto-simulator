import random
import sys
import argparse

# max number allowed on each ball
max_number = 49

amount_of_balls = 6
counter = 0

winner = []
guess = []
used = []

parser = argparse.ArgumentParser(
    description="Pick your  numbers and see how long before the machine selects them!"
)
parser.add_argument('numbers', nargs=amount_of_balls, type=int, help="Your lotto numbers")
args = parser.parse_args()
guesses = args.numbers

# alternative approach to drawing guess numbers based on random
def generate():
    while len(guess) != amount_of_balls:
        some_number = random.randint(0, max_number)
        if some_number not in guess:
            guess.append(some_number)


def guess_by_input():
    for i in guesses:
        guess.append(i)


def game():
    guess_by_input()
    global counter, max_number, amount_of_balls, guess, used, winner
    running = True
    while running:
        counter += 1 
        winner = random.sample(range(max_number + 1), amount_of_balls)
        print(winner)
        if set(winner) == set(guess):
            print(f"guess - {guess}, winner - {winner}")
            print(f"win after {counter} draws")
            print(f"you would have paid {counter * 12} PLN before winning")
            running = False
        else:
            winner = []

game()
