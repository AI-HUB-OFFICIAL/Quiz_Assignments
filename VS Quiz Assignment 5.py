#1.Write a program that checks if a number is positive or negative.
# If it is zero, print "Zero".
z = 0
if z > 0:
    print("The number is positive")
elif z < 0:
    print("The number is negative")
else:
    print("Zero")
#2.  Input a number from the user and print whether it is even or odd.
num = int(input("Enter a number here: "))
if num%2 == 0:
    print("The number is even.")
else:
    print("The number is odd")
#3. Ask the user to enter their age.
#👉 If age is 18 or above, print "Eligible to vote"
#👉 Else, print "Not eligible"
age = int(input("Enter your age here: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")
#4. Enter a number and check whether it is divisible by:
#✔ 3
#✔ 5
#✔ Both
#Print an appropriate message.
_num = 15
if _num%3 == 0 and _num%5 == 0:
    print("The number is divisible by both 3 and 5")
elif _num%3 == 0:
    print("The number is divisible by 3")
elif _num%5 == 0:
    print("The number is divisible by 5")
else:
    print("The number is not divisible by any of these numbers")
#5. **Ask for a student's marks and assign a grade:
#90+ → "A+"
#80+ → "A"
#70+ → "B"
#Otherwise → "Fail"**
marks = int(input("Enter your marks here: "))
if marks > 90:
    print("Grade: A+")
elif marks > 80:
    print("Grade: A")
elif marks > 70:
    print("Grade: B")
else:
    print("Fail")
#6. **Take a temperature input:
#Above 40 → "Too hot"
#Below 10 → "Too cold"
#Otherwise → "Moderate weather"**
temp = int(input("Enter the temperature here: "))
if temp > 40:
    print("Too hot")
elif temp < 10:
    print("Too cold")
else:
    print("Moderate temperature")
#7. Ask the user to enter a year.
#👉 Check whether it is a leap year or not.
year = int(input("Enter a year: "))
if year%4 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
#8. Input three numbers and print the largest one.
num1 = int(input("Enter first number here: "))
num2 = int(input("Enter second number here: "))
num3 = int(input("Enter third number here: "))
if num1 > num2 and num1 > num3:
    print(f"{num1} is the largest number")
elif num2 > num1 and num2 > num3:
    print(f"{num2} is the largest number")
else:
    print(f"{num3} is the largest number")
#9. Ask the user to enter a password.
#👉 If password matches "admin123" → print "Access granted"
#👉 Else → "Access denied"
password = input("Enter a password: ")
if password == "admin123":
    print("Access granted")
else:
    print("Access denied")
#10.  **Take an integer input.
#If number > 0, check if it’s less than 100
#Print appropriate messages for both checks**
inp = int(input("Enter a number: "))
if inp > 0 and inp < 100:
    print("The number is greater than 0 and less than 100")
elif inp > 0:
    print("The number is greater than 0")
elif inp < 100:
    print("The number is less than 100")

