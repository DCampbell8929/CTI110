#Dan Campbell
#12/14/2024
#P1HW1
#A basic math calculator using user input to calculate squares and
#cubes, then taking additional user input to add numbers together


#Gather input from user, and convert that input to an integer
print('Enter an integer:')
num1 = int(input())

#Define additional variables to support math functions
square = num1 ** 2
cubed = num1 ** 3

#Show user math operations performed with user input numbers
print("You entered:",num1)
print(num1, "squared is",square)
print("And", num1, "cubed is", cubed,"!!")

#gather additional user input, and convert that input to an integer
print('Enter another integer:',)
num2 = int(input())

#combine both user inputs to perform arithmatic operations
print(num1, "+", num2, "is", num1+num2)
print(num1, "*", num2, "is", num1*num2)
