import random

key_num = random.randint(1, 10)

print("Welcome to the Guess the Number Game!!!")
print("I'm thinking of a number between 1 and 10.")
print("")

guess = None
num_attempts = 0

while guess != key_num:
    guess = int(input("Enter your guess: "))
    num_attempts += 1

    if guess < key_num:
        print("Too low! Guess a higher number.")
    elif guess > key_num:
        print("Too high! Guess a lower number.")
    else:
        print(f"Congratulation! You guess the number in {num_attempts} attempts.")
