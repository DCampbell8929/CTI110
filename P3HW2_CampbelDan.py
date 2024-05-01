'''
Dan Campbell
3/18/2024
P3HW2

A payroll calculator to 
Practice formatting strings to display in desired formats


Pseudocode:
Get input from user
assign input to variables
math some new variables based on user input
format and print information
'''

#Get User Input: Name, Hours Worked, Pay rate
name = input("Enter empolyee's name: ")
worked = float(input("Enter number of hours worked: "))
pay = float(input("Enter employee's pay rate: "))

#assign additional variables
if worked > 40:
    ot = worked - 40
    otpay = pay * 1.5 * ot 
else:
    ot = 0
    otpay = 0

reghour = pay * (worked - ot)
gross = reghour + otpay

#format and display results
print ("--------------------------------")
print (f'{"Employee name:":<15} {name:<40}')
print ()
print (f'{"Hours Worked":<15}{"Pay Rate":<15}{"Overtime":<15}{"Overtime Pay":<25}{"RegHour Pay":<25}{"Gross Pay":<15}')
print ("----------------------------------------------------------------------------------------------------------------------------")
print (f'{worked:<15}${pay:<14.2f}{ot:<15.2f}${otpay:<24.2f}${reghour:<24.2f}${gross:<15.2f}')

#Variable Testing

#print ()
#print ()
#print ()
#print ("Name: ", name)
#print ("Worked: ", worked)
#print ("Pay: ", pay)
#print ("OT: ", ot)
#print ("OT Pay", otpay)
#print ("Reghour: ", reghour)
#print ("Gross: ", gross)
