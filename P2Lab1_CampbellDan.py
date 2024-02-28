#Dan Campbell
#02.28.2024
#P2LAB1
#A program to calculate the cost of driving different distances using user provided input
#for MPG and costs of gas

'''
Get Input from user for car's gas mileage (float)
Get Input from user for Price of Gas (float)
Calculate cost of driving 20 miles using input, assign to variable
calculate cost of driving 75 miles using input, assign to variable
calculate cost of driving 500 miles using input, assign to variable
Print cost of driving 20 miles
print cost of driving 75 miles
print cost of driving 500 miles
'''

#Gather input from user and assign to variables
mpg = float(input("Enter your car's mileage per gallon: "))
price = float(input("Enter the current price of gas: "))

#Calculate Cost of driving various distances based on above input and assign to variables
miles20 = (20 / mpg) * price
miles75 = (75 / mpg) * price
miles500 = (500 / mpg) * price

#print various prices and format to 2 decimal places
print (f'It would cost, ${miles20:.2f}, to drive 20 miles')
print (f'It would cost, ${miles75:.2f}, to drive 75 miles')
print (f'It would cost, ${miles500:.2f}, to drive 500 miles')
