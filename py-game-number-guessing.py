import random

def play_game():
    level = 1
    max_guesses = 5
    
    print("Welcome to the Number Guessing Game!")
    
    while True:
        # Increase the range of numbers as the level increases
        upper_limit = level * 10
        secret_number = random.randint(1, upper_limit)
        
        print(f"\n--- Level {level} ---")
        print(f"Guess a number between 1 and {upper_limit}.")
        print(f"You have {max_guesses} attempts.")
        
        attempts = 0
        won_level = False
        
        while attempts < max_guesses:
            try:
                guess = int(input(f"Attempt {attempts + 1}/{max_guesses}: "))
            except ValueError:
                print("Please enter a valid number.")
                continue
                
            attempts += 1
            
            if guess == secret_number:
                print("Congratulations! You guessed it right!")
                won_level = True
                break
            elif guess < secret_number:
                print("Too low!")
            else:
                print("Too high!")
        
        if won_level:
            level += 1
            max_guesses += 1  # Add 1 more attempt for every level cleared
            print(f"Level cleared! Moving to level {level}...")
        else:
            print(f"Game Over! The number was {secret_number}.")
            break

if __name__ == "__main__":
    play_game()