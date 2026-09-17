# CTI 110
# P2HW2 - just the setup

# This example only uses three numbers, the full uses six.
# get the grades
grade1 = float(input("Enter grade for module 1: "))
grade2 = float(input("Enter grade for module 2: "))
grade3 = float(input("Enter grade for module 3: "))
grade4 = float(input("Enter grade for module 4: "))
grade5 = float(input("Enter grade for module 5: "))
grade6 = float(input("Enter grade for module 6: "))

# put them all into a new list
grade_list = grade1, grade2, grade3, grade4, grade5, grade6

# do some calculations -- minimum, maximum, and average
min_grade = min(grade_list)
max_grade = max(grade_list)
total     = sum(grade_list)
count     = len(grade_list)
# TODO: calc average (total / count)

average = total / count

# Print the output
print("-------------------------------------")
print(f"Grades: {grade_list}")
print("----------------Results------------------")
print(f"{"Lowest Grade:":<25} {min_grade:<25.1f}")
print(f"{"Highest Grade:":<25} {max_grade:<25.1f}")
print(f"{"Sum Of Grades:":<25} {total:<25.1f}")
print(f"{"Average:":<25} {average:<25.2f}")
print("---------------------------------------------")