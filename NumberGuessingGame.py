import random

def guess_game():
    secret = random.randint(1,100)
    print("Welcome to the Guessing Game!")
    while True:
      max_attempts = input("Enter the maximum number of attempts between 1 to 5: ")
      if not max_attempts.isdigit():
            print("Please enter a valid number.")
            continue
      max_attempts = int(max_attempts)
      if 1 <= max_attempts <= 5:
            break
      else:
            print("Please enter a valid number between 1 and 5.")
        
    attempts = 0
    while attempts<max_attempts:
        guess_text= input("Enter your guess (between 1 and 100): ")
        try :
            guess=int(guess_text)

        except ValueError:
            print("Invalid input. Please enter a number between 1 and 100.")
            continue

        if guess< 1 or guess> 100:
            print("Enter a number between 1 to 100: ")
            continue
        attempts += 1
        if guess<secret:
            print("Tour guess is too low")
        elif guess> secret:
            print("Your guess is too high.")
        else:
            print(f"Congratulations! You guessed the number {secret} in {attempts} attempts.")
            return
    print(f"out of attempts! The secret number was {secret}.")

def main():
     while True:
         guess_game()
         again = input("\nPlay again? (y/n) [default: y]: ").strip().lower()
         if again == "" or again == "y":   # Enter or "y" = re
            continue
         else:
            print("Thanks for playing! 👋")
            break

if __name__ == "__main__":
    main()





