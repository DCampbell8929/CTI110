'''
Dan Campbell
3/27/2024
P4HW2

Payroll Calculator for multiple employees



Pseudocode:
Get input from user (name, pay, hours)
calculate otpay, regpay, gross pay
add values to list
repeat on loop until "done" is entered
Print totals for regpay, otpay, grosspay
'''

#Create Lists
names = []
regpay = []
otpay = []
grosspay = []

#Get User Input: Name, Hours Worked, Pay rate
name = input("Enter empolyee's name or 'done' to terminate: ")

#Calculate pay, display results, restart loop or terminate
while name != 'done':
    worked = float(input(f"How many hours did {name} work? "))
    pay = float(input(f"What is {name}'s pay rate? "))
    #assign additional variables
    if worked > 40:
        ot = worked - 40
        ot_pay = pay * 1.5 * ot 
    else:
        ot = 0
        ot_pay = 0
    reg_pay = pay * (worked - ot)
    gross_pay = reg_pay + ot_pay
    names.append  (name)
    regpay.append (reg_pay)
    otpay.append (ot_pay)
    grosspay.append (gross_pay)
    #format and display results
    print ("--------------------------------")
    print (f'{"Employee name:":<15} {name:<40}')
    print ()
    print (f'{"Hours Worked":<15}{"Pay Rate":<15}{"Overtime":<15}{"Overtime Pay":<25}{"RegHour Pay":<25}{"Gross Pay":<15}')
    print ("----------------------------------------------------------------------------------------------------------------------------")
    print (f'{worked:<15}${pay:<14.2f}{ot:<15.2f}${ot_pay:<24.2f}${reg_pay:<24.2f}${gross_pay:<15.2f}')
    name = input("Enter empolyee's name or 'done' to terminate: ")


#Calculate Totals
total_names = len(names)
total_reg = sum(regpay)
total_ot = sum(otpay)
total_gross = sum(grosspay)
print ("--------------------------------")
print (f"Total number of employees entered: {total_names}")
print (f"Total amount paid for overtime: ${total_ot:.2f}")
print (f"Total amount paid for regular hours: ${total_reg:.2f}")
print (f"Total amount pad in gross: ${total_gross:.2f}")

    




    
