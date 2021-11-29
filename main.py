# Virus Game Version 5
# 28/11/2021
# Aaron Sharma




# Lists to hold all country data
names_of_countries = []
infected_percentage_for_countries = []
country_lockdown = []





# Function which collects country data and infected percentage
def add_countries():
    country_add = ""
    # Loop which will keep adding countries until the user if finished
    while True:
        country_add = input(
            "Please write the name of the country you would like to enter. When you are finished adding countries, please type \"done\" and click enter.")
        # If user has entered valid country, create it and add it to the list
        if country_add != "done":
            # Adding validiation to make user is inputting correct data
            infected_percentage = int(
                input("Type the current percentage of infected people for " + country_add + " and then press enter."))
            names_of_countries.append(country_add)
            infected_percentage_for_countries.append(infected_percentage)
            country_lockdown.append(False)
        # If user is finished, break out of the function
        else:
            break




#Function that will ask user what country they want to help
def ask_country_help():
    # Create string to dislpay all of the user's options
    ask_help = "Which country do you want to help, please select from the following:"
    for country in names_of_countries:
        ask_help += "\n" + country
    # Validating that the option the user selected is valid
    while True:
        country_help = input(ask_help)
        # Check the list of countries user entered previously to check if enterd country is valid
        for country in names_of_countries:
            if country_help == country:
                # Return name of entered country if it is valid
                return country_help
        # print error message and loop to beginning of function if entry is invalid
        print("Invalid input, please enter a valid country.")






# Function to show results
def show_data(names_of_countries, infected_percentage_for_countries, country_lockdown):
    data = "" + names_of_countries + " currently has " + str(
        infected_percentage_for_countries) + " percent infected, and "
    if infected_percentage_for_countries >= 80:
        country_lockdown = True
        data += "is in lockdown"
    else:
        data += "is not in lockdown"
    return data






# Function will run every new day, needs arguement for country_help
def new_day(ask_country_help):
    print("*** A NEW DAY ***")
    list_index = 0
    for country in names_of_countries:
        # If a country is helped, its infected percentage will decrease by 40%
        # If a country is already at 40% infected or less, that means there is no way to have less than 0% infected
        if country == ask_country_help:
            if infected_percentage_for_countries[list_index] >= 40:
                infected_percentage_for_countries[list_index] = infected_percentage_for_countries[list_index] - 40
            else:
                infected_percentage_for_countries[list_index] = 0
        # If a country is not helped, its infected percentage rises by 20%
        # If a country already has 80% or more infected, it cannot have more than 100% infected
        else:
            if infected_percentage_for_countries[list_index] >= 80:
                infected_percentage_for_countries[list_index] = 100
            else:
                infected_percentage_for_countries[list_index] = infected_percentage_for_countries[list_index] + 20
        # print current country status
        print(show_data(names_of_countries[list_index], infected_percentage_for_countries[list_index],
                        country_lockdown[list_index]))
        list_index += 1
    print("*** END OF DAY ***")




# main code
add_countries()
for i in range(0, 5):
    new_day(ask_country_help())
