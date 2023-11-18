import random
from art import logo
print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

random_number = random.randint(0, 100)

print(f"Pssst, the correct answer is {random_number}")
ask_user = input("Choose a difficulty. Type 'easy' or 'hard': ")


end_game = False

if ask_user == "easy":
  attempts = 10
  print(f"You have {attempts} attempts remaining to guess the number.")
  guess = int(input("Make a guess: "))

elif ask_user == "hard":
  attempts = 5
  print(f"You have {attempts} attempts remaining to guess the number.")
  guess = int(input("Make a guess: "))

while not end_game:
  
  if guess !=random_number:
    if guess > random_number:
      attempts -= 1
      print("Too high")
      print("Guess again.")
      print(f"You have {attempts} attempts remaining to guess the number.")
      guess = int(input("Make a guess: "))
      if attempts  == 0: 
        end_game = True
        print("You've run out of guesses, you lose.")
      

    elif guess < random_number:
      attempts -= 1
      print("Too low")
      print("Guess again.")
      print(f"You have {attempts} attempts remaining to guess the number.")
      guess = int(input("Make a guess: "))
      if attempts  == 0:
        end_game = True
        print("You've run out of guesses, you lose.")
  else:
    print(f"You got it! The answer was {random_number}.")
    end_game = True
  
