#Dan Campbell
#3/27/2024
#P4Lab2
#Use a while loop


'''
Get 2 integers from user
validate input from user to ensure first number is less than second
increment first input in 5s until second input is met
'''


#Get 2 inputs from user, assign to variables
var1 = int(input("Enter the smaller Integer: "))
var2 = int(input("Enter a larger Integer: "))

#Validate that var1 is less than var2
#If var1 is greater than var2, prompt for new numbers
while var1 >= var2:
    print("PEBKAC ERROR")
    print("Those numbers don't work")
    print("Enter a smaller number first")
    var1 = int(input("Enter a smaller Integer: "))
    var2 = int(input("Enter a larger Integer: "))

#Increment var1 by 5 until second input is met
while var1 <= var2:
    print (var1, end = " ")
    var1 += 5


''' example
for num in range(var1, var2+1, 5):
    print (var1)
'''
        
    
'''    
print ()
print (var1)
print (var2)
'''
