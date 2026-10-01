# CTI 110
# P3HW1- fixing problems in a codespace to have grades show up correctly.
# Austin Lee
# 9/29/2026
 

# This program takes a number grade , determines average and displays letter grade for average.
# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5]
# TO DO: determine lowest, highest , sum and average for grades

lowest_grade = min(grades)
highest_grade = max(grades)
total = sum(grades)
count = len(grades)
avg = total / count

# determine letter grade for average

print("-------------------------------------")
print(f"Grades: {grades}")
print("----------------Results------------------")
print(f"{"Lowest Grade:":<25} {lowest_grade:<25.1f}")
print(f"{"Highest Grade:":<25} {highest_grade:<25.1f}")
print(f"{"Sum Of Grades:":<25} {total:<25.1f}")
print(f"{"Average:":<25} {avg:<25.2f}")
print("---------------------------------------------")

if avg >= 90:
 print('Your grade is: A')
elif avg >= 80:
 print('Your grade is: B')
elif avg >= 70:
 print('Your grade is: C')
elif avg >= 60:
 print('Your grade is: D')
else:
 print('Your grade is: F') # TO DO: finish this




