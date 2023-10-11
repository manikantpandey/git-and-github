import random

def main():
    # Generate a random number between 1 and 10
    secret_number = random.randint(1, 10)
    
    # Initialize the number of guesses
    attempts = 0
    
    print("Welcome to the Guess the Number game!")
    print("I'm thinking of a number between 1 and 10.")
    
    while True:
        try:
            # Ask the user for a guess
            guess = int(input("Take a guess: "))
            attempts += 1
            
            # Check if the guess is correct
            if guess == secret_number:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                break
            elif guess < secret_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
