#Dan Campbell
#3/27/2024
#P4HW1
#A grade calculator using loops

'''
get input on # of values
prompt user for values using loop
validate each entry, warn if invalid and reprompt
calculate lowest score
drop lowest score
average score
calculate final grade
'''

#Get input on # of Values
modules = input("How many scores do you want to enter: ")
while modules.isdigit() == False:
    print("You must enter a number")
    modules = input("How many scores do you want to enter: ")

modules = int(modules)
#create empty list
grade_list = []
#assign iteration counter with value of 1
current = 1


#Prompt user for values using loop
for item in range (modules):
    grade = input(f"Enter score #{current}: ")
    #Validate user info, warn if invalid and repompt
    while grade.isdigit() == False:
        print("INVALID score entered!!!")
        print("score should be between 0 and 100")
        grade = input(f"Enter score #{current} again: ")

    grade = float(grade)        
        
    while grade > 100 or grade < 0:
        print("INVALID score entered!!!")
        print("score should be between 0 and 100")
        grade = float(input(f"Enter score #{current} again: "))        
    
    #Add input to list
    grade_list.append (grade)
    #iterate Loop
    current += 1
        




#Calculate lowest score
low = min(grade_list)

#Print Results
print ()
print ("----------Results----------")
print (f'{"Lowest Grade:":<20} {low}')
#Drop Lowest score
grade_list.remove (low)

#print modified list with lowest score dropped
print (f'{"Modified List:":<20} {grade_list}')

#calculate total and average
total = sum(grade_list)
avg = total / len(grade_list)

#print average score
print (f'{"Average:":<20} {avg:.2f}')

#using average, calculate letter grade and print
if avg >= 90:
    print('Your grade is: A')
elif avg >= 80:
    print('Your grade is: B')
elif avg >= 70:
    print('Your grade is: C')
elif avg >= 60:
    print('Your grade is: D')
elif avg >= 50:
    print('Your grade is: F')
else:
    print('Your grade is: F')
print ("---------------------------")




''' OLD CODE

GOOD - Doesnt meet criteria
for item in range (modules):
    grade = float(input(f"Enter score #{current}: "))
    if grade > 100 or grade < 0:
        print("INVALID score entered!!!")
        print("Score should be between 0 and 100")
        grade = float(input(f"Enter score #{current} again: "))
        grade_list.append (grade)
        current += 1        
    else:
        grade_list.append (grade)
        current += 1

GOOD - Doesnt validate for strings
#Prompt user for values using loop
for item in range (modules):
    grade = float(input(f"Enter score #{current}: "))
    #Validate user info, warn if invalid and repompt
    while grade > 100 or grade < 0:
        print("INVALID score entered!!!")
        print("score should be between 0 and 100")
        grade = float(input(f"Enter score #{current} again: "))
    #Add input to list
    grade_list.append (grade)
    #iterate Loop
    current += 1





'''
