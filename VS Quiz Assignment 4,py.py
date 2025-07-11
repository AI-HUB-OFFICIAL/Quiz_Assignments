#1. Create two variables a = 10 and b = 3.
#Perform and print: addition (+), subtraction (−), multiplication (×), division (/), modulus (%), exponentiation (), and floor division (//).**
a = 10
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)
print(a // b)
#2. Compare a and b using comparison operators: ==, !=, >, <, >=, <=
#Print the result of each comparison.
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
#3. Create two boolean variables: x = True, y = False.
#Perform and print results of: x and y, x or y, and not x.
x = True
y = False
print(x and y)
print(x or y)
print(not x)
#4. Create num = 5 and perform assignment operations: +=, -=, *=, /=, %=, **=, //=
#Print the result after each operation.
num = 5
num += 1
print(num)
num -= 1
print(num)
num *= 5
print(num)
num /= 2
print(num)
num %= 7
print(num)
num //= 2
print(num)
#5.  Create m = 100, n = 100.
#Check if they are the same object using is and is not, and print the result.
m = 100
n = 100
print(m is n)
print(m is not n)
#6. Create a string text = "Python Programming"
#Check if "Python" is in text and if "Java" is not in text.
text = "Python Programming"
print("Python" in text)
print("Java" not in text)
#7. Write a Python program to print all keywords using the keyword module.
import keyword
print(keyword.kwlist)
#8. Declare: name = "Ali", age = 20, height = 5.9
#Print their values and data types using the type() function.
name = "Ali"
age = 20 
height = 5.9
print(name, type(name))
print(age, type(age))
print(height, type(height))
#9. Write 5 valid variable names (e.g., user_name, x1, _value, TotalAmount, data123)
#Also write 3 invalid ones (as comments): 1name, user-name, class
#Explain why invalid names are not allowed.
user_name = "Nehan"
x1 = 2
_value = 4
TotalAmount = 200
data123 = 123
#1name = "Ahmed"  # VAriable name cannot start with a number
#user-name = "fahad" # variable name cannot contain hyphen
# class = "int" #reserve words cannot be used as variable names

#10. Create special-naming variables: _hidden = 5, __private = 10, MAX_SIZE = 100
#Print their values.
_hidden = 5
__private = 10
MAX_SIZE = 100
print(_hidden)
print(__private)
print(MAX_SIZE)
#11.  Assign values in one line: x = 1, y = 2, z = 3
#Print them.
x, y, z = 1, 2, 3
print(x, y, z)
#12. Assign same value 0 to a, b, c in one line
#Print them.
a = b = c = 0
print(a, b, c)
#13. Create temp = 100, print it, delete it using del, then try to print again and observe the error.
temp = 100
print(temp)
del temp
#print(temp) #uncomment to see error
#14. Create a string using triple single quotes: '''Hello'''
#Print it.
my_string = '''Hello'''
print(my_string)
#15.  **Create a multi-line string using triple double quotes:
#"""This is line one.\nThis is line two."""
#Print it.**
m_line_string = """This is line one.\nThis is line two."""
print(m_line_string)
#16.  **Use type() to check and print the data types of:
#An integer
#A float
#A string
#A boolean**
print(type(234))
print(type(45.67))
print(type("Hello"))
print(type(True))
#17. Create score = 85
#Check: score > 50 and score < 100
#Print the result.
score = 85
print(score>50 and score<100)
#18. Create message = "Welcome to Python"
#Use in and not in to check for the word "Python"
#Print the result.
message = "Welcome to Python"
print("Python" in message)
print("Python" not in message)
#19. Write a code block using only comments that explains what your program does.
#My program explains different steps and working of Python
#20. Create data = 123
#Use id(data) to print its memory address.
data = 123
print(id(data))