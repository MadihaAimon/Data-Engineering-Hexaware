import random

def guessing_game():
    target_number = random.randint(1, 10)

    while True:
        user_guess = int(input("Guess the number between 1 and 10: "))

        if user_guess == target_number:
            print("Correct answer!")
            break
        elif user_guess < target_number:
            print("Too small. Try again.")
        else:
            print("Too large. Try again.")

# Call the function
guessing_game()