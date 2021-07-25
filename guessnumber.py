import random


def guess(x):
    random_number = random.randint(1, x)

    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, you've guessed too low!")
        elif guess > random_number:
            print("Sorry, you've guess too high!")

    print(f"Congrats, you've guessed {random_number} correctly!")


def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high as long as it throws a too low or high
        feedback = input(
            f'Is the {guess} too high {H}, too low {L}, or correct {C}??').lower()
            low = guiess + 1

    print(f"Yay the computer has guessed your number, {guess}, correctly!")


guess(10)
     if feedback == 'h':
            high = guess - 1
        if feedback == 'l':
   
