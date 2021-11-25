#Virus Simulator version 4
#25/11/2021
#Aaron Sharma

#To enhance the user experience by managing how text is displayed.
import time
import sys
#welcome message
time.sleep(.75)
print("Welcome to the Pap High Virus Simulator\n Please follow the prompts")


#To store and track user input
country_list = []
num_infected = []
max_length_list = 3

#Asking user the name of there chosen country
def get_infected_percentage(num):
  num = int(num)
  if num >= 0:
    return (1 * int(num))
  else:
    print("Invalid entry")
  
try:
  infected_percentage = input("What is the percentage of infected people in your chosen country?")
  print(get_infected_percentage(infected_percentage))

except:
  print("Invalid entry, try again")
