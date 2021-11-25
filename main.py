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

name_country = ""


#Collecting data
while len(name_country) < max_length_list:
  name_country = str(input("Please enter a country name")).upper()
  country_list.append(name_country)
  infected_percent = int(input("Please enter the number infected"))
  num_infected.append(infected_percent)


print(country_list,"is the country and ", num_infected, "is the amount infected")



#Function to print details
def print_details(self):
  details = "" + self.name_country + "currently has " + str(self.infected_percent) + "percent infected, and "
  if self.is_in_lockdown == True:
    details += "is in lockdown"

#Function to ask for help (work in progress)
def ask_for_assist(name_country):
  ask_help = input("Which country would you like to assist?, Choose from the following")
  for name_country in country_list:
    ask_help += "\n" + name_country.country_list
    while True:
      ask_for_assist

