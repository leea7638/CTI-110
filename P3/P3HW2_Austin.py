# CTI 110
# P3HW2
# Austin Lee
# 10/01/2026

employee = input("Enter employee's name: ")
hours = float(input("Enter the number of hours worked: "))
rate = float(input("Enter the employee's pay rate: "))
if hours > 40:
    overtime_hours = hours - 40
    overtime_pay = overtime_hours * (rate * 1.5)
    regular_pay = 40 * rate
    gross_pay = regular_pay + overtime_pay
print("-------------------------------------------")
print("Employee name:", employee)
print(f"{"Hours Worked":<15} {"Pay Rate":<15} {"Overtime":<15} {"Overtime Pay":<15} {"RegHour Pay":<15} {"Gross Pay":<15}")
print("-------------------------------------------------------------------------------------------------")
print(f"{hours:<15} {rate:<15} {overtime_hours:<15} {overtime_pay:<15} {regular_pay:<15} {gross_pay:<15}")