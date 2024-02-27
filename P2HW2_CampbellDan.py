#Dan Campbell
#2/14/2024
#P1HW2
#A budget calculator for an upcoming trip

#Pseudocode:
#Get Budget
#Get Destination
#Get Gas
#Get Hotel
#Get Food
#Add Expenses
#budget - expenses
#Display Results

print("This program calculates and displays travel expenses")
print()

#prompt user for input and define variable
budget = float(input('Enter Budget: '))
print()

#prompt user for input and define variable
destination = input("Enter your travel destination: ")
print()

#prompt user for input and define variable
gas = float(input("How much do you think you will spend on gas? "))
print()

#prompt user for input and define variable
hotel = float(input("Approximately, how much will you need for accomodation/hotel? "))
print()

#prompt user for input and define variable
food = float(input("Last, how much do you need for food? "))
print()

#Calculate Expenses
print("------------Travel Expenses------------")

print(f'{"Location:":<20} {destination}')
print(f'{"Initial Budget:":<20} ${budget:.2f}')
print(f'{"Fuel:":<20} ${gas:.2f}')
print(f'{"Accomodation:":<20} ${hotel:.2f}')
print(f'{"Food:":<20} ${food:.2f}')
print("---------------------------------------")
print()
print(f'{"Remaining Balance:":<20} ${budget-gas-hotel-food:.2f}')


