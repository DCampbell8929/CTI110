#Dan Campbell
#02.28.2024
#P2LAB2
#Calculate simple statistics from user input

'''
Obtain input from user
Obtain input from user
Obtain input from user
Obtain input from user
Calculate the product of the provided input as rounded integers
calculate the average of provided input as rounded integers
calculate the product (multiplication) of the provided input as floating-point numbers to 3 decimal places
calculate the average of provided input as floating-point numbers to 3 decimal places
'''

#Obtain 4 inputs from user and assign to variable
num1 = float(input("Enter a number with a decimal: "))
num2 = float(input("Enter a number with a decimal: "))
num3 = float(input("Enter a number with a decimal: "))
num4 = float(input("Enter a number with a decimal: "))

#Assign inputs to list
num_list = [num1, num2, num3, num4]

#calculate the product of list as rounded integer and assign to variable
product = num1 * num2 * num3 * num4

#Calculate sum of input values
total = num1 + num2 + num3 + num4


#Define length of list, assign to variable
length = len(num_list)

#Calculate the average of provided input as rounded integer
avg = total / length

#Print Rounded product, and rounded average
print()
print ("Numbers to 0 decimal places")
print (f'The product of the input is {product:.0f}')
print (f'The average of the input is {avg:.0f}')
print()
#Print product to 3 decimal places and average to 3 decimal places
print ("Numbers to 3 decimal places")
print (f'The product of the input is {product:.3f}')
print (f'The average of the input is {avg:.3f}')
print()



#printable variables for verification
#print (num_list)
#print (product)
#print (avg)
#print (total)
#print (length)


