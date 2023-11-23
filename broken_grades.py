# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student iis failing.

exam_one = int(input("Input exam grade one: "))               #Added int

exam_two = int(input("Input exam grade two: "))               #Added int

exam_three = int(input("Input exam grade three: "))           #Replaced the str conversion with int and changed the variable name from exam_3 to exam_three

grades = [exam_one, exam_two, exam_three]                     #Added commas to seperate the elements
sum = 0
for grade in grades:                                          #Added an s to grade to refer correctly to the list 'grades'
  sum = sum + grade

avg = sum / len(grades)                                       #changed grdes to grades
avg=round(avg)                                                #added a round() function
if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90:                                  #Added a colon after 90
    letter_grade = "B"
elif avg >=70 and avg < 80:                                   #Added an equal to after '>' and changed 69 to 70
    letter_grade = "C"                                        # Fixed the inverted commas
elif avg >= 60 and avg <70:                                   #Changed the numerical ranges 69 and 65 and comparison operator
    letter_grade = "D"
else:                                                         #Changed elif to else
    letter_grade = "F"

print("Exam: ", end='')                                       #Changed Exam to Exams, brought statement out of for-loop to avoid printing thrice,added an end argument
i=1                                                           #initializing i to print properly
for grade in grades:
     i+=1                                                     #incrementing i
     print(str(grade), end='')    
     if i<=len(grades):                                       #added if-else statements for printing elements properly in a row
        print(',', end='')                                    #added an end to print elements of list seperated by commas
     else:
       print()                                                #when last element of list becomes grade, cursor goes to newline

print("Average: " + str(avg))                                 #Removed from the for loop block

print("Grade: " + letter_grade)                               #Removed from the for loop block

if letter_grade == "F":                                       #changed letter-grade to letter_grade, changed 'is' to '=='
    print ("Student is failing.")                             #Added parenthesis
else:
    print ("Student is passing.")                             #Added parenthesis
