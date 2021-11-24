#Number Guesseing Game version 2
#25/11/2021
#Aaron Sharma

#importing a module
import random


#Target variable to store a random target number for the user to guess
target = random.randint(1, 100)
#guess variable to store user's guessed number


run_loop = True

while run_loop:
  guess = int(input("Please guess a number between 1-100"))

  while not(guess >=1 and guess <= 100):
    guess = int(input("That is not a valid entry, Please enter a number between 1-100"))



  if guess < target:
   print("Your guess was too low")
  elif guess > target:
    print("Your guess was too high")
  elif guess == target:
    run_loop = False



print("Congratulations, you guessed correctly")