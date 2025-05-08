import random

def guessing_game():
    print("Welcome to the 'Guess the Number' game!")
    print("I have chosen a number between 1 and 100. Try to guess it in as few attempts as possible.")
    
    number_to_guess = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter an integer.")
            continue
        
        attempts += 1
        
        if guess < number_to_guess:
            print("Too low, try again.")
        elif guess > number_to_guess:
            print("Too high, try again.")
        else:
            print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
            break

if __name__ == "__main__":
    guessing_game()
