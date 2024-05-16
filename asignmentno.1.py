# 1. Write a program to find the maximum between two numbers.

numb1 = int(input("Enter a first number: "))
numb2 = int(input("Enter a second number: "))
if numb1 > numb2:
  print("The maximum number is :", numb1)
else:
  print("The maximum number is :", numb2)  


# 2. Write a program to find the maximum between three numbers.

numb1 = int(input("Enter a first number: "))
numb2 = int(input("Enter a second number: "))
numb3 = int(input("Enter a third number: "))
if numb1 > numb2 and numb1 > numb3:
  print("The maximum number is :", numb1)
elif numb2 > numb1 and numb2 > numb3:
  print("The maximum number is :", numb2)
else:
  print("The maximum number is :", numb3)


# 3. Write a program to check whether a number is negative, positive or
# zero.
numb = int(input("Enter a number: "))
if numb > 0:
  print("The number is positive")
elif numb < 0:
  print("The number is negative")
else:
  print("The number is zero")


# 4. Write a program to check whether a number is divisible by 5 and 11 or
# not.
numb = int(input("Enter a number: "))
if numb % 5 == 0 and numb % 11 == 0:
  print("The number is divisible by 5 and 11")
else:
  print("The number is not divisible by 5 and 11")

# 5. Write a program to check whether a number is even or odd.
numb = int(input("Enter a number: "))

if numb % 2 == 0:
  print("The number is even")
else:
  print("The number is odd")

# 6. Write a program to check whether a year is leaping year or not.

year = int(input("Enter a year: "))
if year % 4 == 0:
  print("The year is leaping year")
else:
  print("The year is not leaping year")

# 7. Write a program to input any alphabet and check whether it is vowel or
# consonant.

alphabet = input("Enter a alphabet: ")
if alphabet == "a" or alphabet == "e" or \
   alphabet == "i" or alphabet == "o" or \
   alphabet == "u":
  print("The alphabet is vowel")
else:
  print("The alphabet is consonant")


# 8. Write a program to check whether a character is uppercase or
# lowercase alphabet.

alphabet = input("Enter a alphabet: ")
if alphabet >= "A" and alphabet <="Z":
  print(alphabet, "is uppercase")
elif alphabet >= "a" and alphabet <= "z":
  print(alphabet , "is lowercase")
else:
  print("Please eneter valid alphabet")


# 9. Write a program to input the week number and print weekday.
week = int(input("Enter a week number: "))
if week == 1:
  print("Monday")
elif week == 2:
  print("Tuesday")
elif week == 3:
  print("Wednesday")  
elif week == 4:
  print("Thursday")
elif week == 5:
  print("Friday")
elif week == 6:
  print("Saturday")
elif week == 7:
  print("Sunday")
else:
  print("Invalid week number")


# 10. Write a program to input the month number and print the number of
# days in that month.
month = int(input("Enter a month number: "))
if month == 1:
  print("31 days")
elif month == 2:
  print("28 days")
elif month == 3:
  print("31 days")
elif month == 4:
  print("30 days")
elif month == 5:
  print("31 days")
elif month == 6:
  print("30 days")
elif month == 7:
  print("31 days")
elif month == 8:
  print("30 days")
elif month == 9:
  print("31 days")
elif month == 10:
  print("30 days")
elif month == 11:
  print("31 days")
elif month == 12:
 print("30 days")
else:
  print("invalid month number")


# 11. Write a program to count a minimum number of notes in a given
# amount.

amount = int(input("Enter a amount: "))
note_100 = amount // 100
note_50 = (amount % 100) // 50
note_10 = ((amount % 100) % 50) // 10
print("100 rupee notes:", note_100)
print("50 rupee notes:", note_50)
print("10 rupee notes:", note_10)


# 12. Write a program to input marks of five subjects Physics, Chemistry,
# Biology, Mathematics, and Computer. Calculate percentage and grade
# according to the following:
# Percentage >= 90% : Grade A
# Percentage >= 80% : Grade B
# Percentage >= 70% : Grade C
# Percentage >= 60% : Grade D
# Percentage >= 40% : Grade E
# Percentage < 40% : Grade F

physics = int(input("Enter a physics marks: "))
chemistry = int(input("Enter a chemistry marks: "))
biology = int(input("Enter a biology marks: "))
mathematics = int(input("Enter a mathematics marks: "))
computer = int(input("Enter a computer marks: "))
total_marks = physics + chemistry + biology + mathematics + computer
percentage = (total_marks / 500) * 100
if percentage >= 90:
  print("Grade A")
elif percentage >= 80:
  print("Grade B")
elif percentage >= 70:
  print("Grade C")
elif percentage >= 60:
  print("Grade D")
elif percentage >= 40:
  print("Grade E")
elif percentage < 40:
  print("Grade F")  
else:
  print("Invalid marks")


# 13. Write a program to input the basic salary of an employee and calculate
# its Gross salary according to the following:
# Basic Salary <= 10000 : HRA = 20%, DA = 80%
# Basic Salary <= 20000 : HRA = 25%, DA = 90%
# Basic Salary > 20000 : HRA = 30%, DA = 95%


basic_salary = int(input("Enter a basic salary: "))
if basic_salary <= 10000:
  hra = basic_salary * 0.2
  da = basic_salary * 0.8
  gross_salary = basic_salary + hra + da
  print("Gross salary:", gross_salary)
elif basic_salary <= 20000:
  hra = basic_salary * 0.25
  da = basic_salary * 0.9
  gross_salary = basic_salary + hra + da
  print("Gross salary:", gross_salary)
elif basic_salary > 20000:
  hra = basic_salary * 0.3
  da = basic_salary * 0.95
  gross_salary = basic_salary + hra + da
  print("Gross salary:", gross_salary)
else:
  print("Invalid basic salary")


# 14. Write a program to input electricity unit charges and calculate total
# electricity bill according to the given condition:
# For the first 50 units Rs. 0.50/unit
# For the next 100 units Rs. 0.75/unit
# For the next 100 units Rs. 1.20/unit
# For units above 250 Rs. 1.50/unit
# An additional surcharge of 20% is added to the bill


electricity_unit = int(input("Enter a electricity unit: "))
if electricity_unit <= 50:
  bill = electricity_unit * 0.5
  print(" Your Bill Is:", bill)
elif electricity_unit <= 150:
  bill = electricity_unit * 0.75
  print("Your Bill Is:", bill)
elif electricity_unit <= 250:
  bill = electricity_unit * 1.2
  print("Your Bill Is:", bill)
elif electricity_unit > 250:
  bill = electricity_unit * 1.5 * 1.2
  print("Your Bill Is:", bill)
else:
  print("Invalid electricity unit")

    