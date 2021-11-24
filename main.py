#Number Guesseing Game version 1
#25/11/2021
#Aaron Sharma

#importing a module
import random


#Target variable to store a random target number for the user to guess
target = random.randint(1, 100)
#guess variable to store user's guessed number
guess = int(input("Please guess a number between 1-100"))

if guess == target:      #If user guesses target number
  print("Congratulations, you guessed correctly")
elif guess < target:  #if user guess is below target number 
  print("Your guess was too low")
elif guess > target:   #if user guess is higher than target number
  print("Your guess was too high")
elif guess < 1:    #if user guess is higher than range
  print("Invalid entry, please try again")
elif guess > 100:     #if user guess is lower than range
  print("Invalid entry, please try again")