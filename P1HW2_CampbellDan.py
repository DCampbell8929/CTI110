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


#prompt user for input and define variable
budget = int(input('Enter Budget: '))

#prompt user for input and define variable
destination = input("Enter your travel destination: ")

#prompt user for input and define variable
gas = int(input("How much do you think you will spend on gas? "))

#prompt user for input and define variable
hotel = int(input("Approximately, how much will you need for accomodation/hotel? "))

#prompt user for input and define variable
food = int(input("Last, how much do you need for food? "))


#Calculate Expenses
print("------------Travel Expenses------------")

print("Location:",destination)
print("Initial Budget:",budget)
print()
print("Fuel:",gas)
print("Accomodation:",hotel)
print("Food:",food)
print()
print("Remaining Balance:",budget-gas-hotel-food)

