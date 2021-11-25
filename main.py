#Number Guesseing Game version 1
#25/11/2021
#Aaron Sharma

#importing a module
import time

#welcome message
sleep.(.75)
print("Welcome to the Pap High Virus Simulator\n Please follow the prompts")


#List for country name
country_name = []
#List for number of infected
num_infected = []


#Target variable to store a random target number for the user to guess
target = random.randint(1, 100)
#guess variable to store user's guessed number


Virus_data_collection = True

while Virus_data_collection:
  
  name_country = str(input("Please enter the name of a country:"))
