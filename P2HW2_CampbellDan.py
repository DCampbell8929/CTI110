#Dan Campbell
#3/4/2024
#P2HW2
#A simple grade calculator

'''
Gather 6 inputs from user
Convert input to list
use list functions to print results for:
Lowest Grade
Highest Grade
Sum of grades
Average
'''

#Gather input from user for 6 grades
grade1 = float(input("Enter grade for Module 1: "))
grade2 = float(input("Enter grade for Module 2: "))
grade3 = float(input("Enter grade for Module 3: "))
grade4 = float(input("Enter grade for Module 4: "))
grade5 = float(input("Enter grade for Module 5: "))
grade6 = float(input("Enter grade for Module 6: "))

#assign inputs to list
grade_list = [grade1, grade2, grade3, grade4, grade5, grade6]



#formating for output
print()
print ("-----------Results-----------")

#Print Lowest grade in list
print (f'{"Lowest Grade: ":<20} {min(grade_list)}')

#print Highest grade
print (f'{"Highest Grade: ":<20} {max(grade_list)}')

#print sum of grades
print (f'{"Sum of Grades: ":<20} {sum(grade_list)}')

#calculate length of list
length = len(grade_list)

#Using sum of grades and length of list, calculate average
print (f'{"Average: ":<20} {(sum(grade_list) / length):.2f}')

#formating for output
print ("-----------------------------")

#Variable Testing
'''
print (grade1)
print (grade2)
print (grade3)
print (grade4)
print (grade5)
print (grade6)
print (grade_list)
print (length)
'''

