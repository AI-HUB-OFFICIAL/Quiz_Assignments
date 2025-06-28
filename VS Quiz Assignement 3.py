#1. Create a variable greeting and store a message. Print it.
greeting = "Hello World"
print(greeting)
#2. Change the value of greeting and print the new message.
greeting = "Hello AI Hub"
print(greeting)
#3. Create first_name and last_name, then print full name using f-string.
first_name = "Nehan"
last_name = "Mustafa"
print(f"{first_name} {last_name}")#combined the full name by f-string.
#4. Print a famous quote with author’s name using f-string.
author = "Quaid-e-Azam Muhammad Ali Jinnah"
print(f' "Failure is the word unknown to me"\n Author:"{author}"')#combined the quote and author's name using f-string
#5. Store a name with extra spaces, strip them, and print clean output.
name = "          Nehan Mustafa   "
print(name)
print(name.strip())
#6. Take a number, add 5, multiply by 2, subtract 3, and print the result.
num = 2
#there can be two possible situation according to the statement.
# No.1 Without BODMAS rule.
result1 = (num + 5) * 2 - 3
print(result1)
# No.2 With BODMAS rule.
result2 = num + 5 * 2 - 3
print(result2)
#7. Create a and b; print their sum, difference, product, and quotient.
a = 6
b = 5
print(a + b)#Sum
print(a - b)#Difference
print(a * b)#Product
print(a / b)#Quotient
#8. Find square and cube of a number using ** operator.
num = 5
print(num ** 2)#Square
print(num ** 3)#Cube
#9. Add three floating-point numbers and print the total.
num1 = 4.67
num2 = 5.33
num3 = 7.39
total = num1 + num2 + num3 #Adding all three numbers
print(total)
#10. Assign x, y, z in one line and print them.
x, y, z = 4, 6, "Hello World"
print(x, y, z)
#11. Create a list of 5 favorite fruits and print each one separately.
fruits = ["mango", "banana", "apple", "apricot", "watermelon"]
for fruit in fruits:  #using for loop to print each fruit separately.
    print(fruit)
#12. Modify the 2nd item in the list and print the updated list.
fruits[1] = "cherry"
print(fruits)
#13. Append a new fruit and insert one at the beginning.
fruits.append("grapes") #appending an item at the last.
print(fruits)
fruits.insert(0, "peach")# inserting an item at the beginning by writing the index.
print(fruits)
#14. Delete items using del, pop(), and remove().
del fruits[0]#using del and index to delete an item.
print(fruits)
removed_item = fruits.pop(2)
print(removed_item)#pop() shows the removed item from the list.
print(fruits)
fruits.remove("cherry")#remove() deletes the specified item from the list.
print(fruits)
#15. Use sort() and sorted() to sort the list. Show before and after.
print("Before: ", fruits)
fruits.sort()
print("After sort(): ", fruits)#sorts the list alphabetically
print("After sorted(): ", sorted(fruits))
#16. Create a list of dream travel destinations:
#  - Sort alphabetically
#  - Reverse the order
#  - Count total destinations
dream_travel_dests = ["Makkah", "Madinah", "Switzerland", "Kashmir"]
dream_travel_dests.sort()
print(dream_travel_dests)
dream_travel_dests.reverse()
print(dream_travel_dests)
print(len(dream_travel_dests))
#17. Start with an empty guest list:
#  - Append 3 guests
#  - Insert 1 at the beginning
#  - Remove one using pop()
#  - Print final list
guest_list = []
guest_list.append("Aslam")
guest_list.append("Hasan")
guest_list.append("Ali")
print(guest_list)
guest_list.insert(0, "Usman")#writing index to insert item in the beginning
print(guest_list)
removed_item = guest_list.pop(1)
print(removed_item)
print(guest_list)
#18. Access the last 3 elements of a list without negative indexing.
my_list = [5, 6, 8, 9, 11]
print(my_list[2:])#slicing the list to print last 3 elements
#19. From a list of numbers, print only even numbers.
num_list = [1, 2, 6, 15, 16, 20, 23]
even = []
for num in num_list: #using for loop to access each item seperatly
    if num%2 == 0:
        even.append(num)
print(even)
#20. Print squares of the first 10 natural numbers in a list.
square_list = []
for num in range(1, 11):
    squares = num**2
    square_list.append(squares)
print(square_list)
#Ask the user for 5 favorite movies.
#Store them in a list.
#Print them sorted alphabetically.
movie1 = input("Enter first movie here: ")
movie2 = input("Enter second movie here: ")
movie3 = input("Enter third movie here: ")
movie4 = input("Enter fourth movie here: ")
movie5 = input("Enter fifth movie here: ")
movie_list = [movie1, movie2, movie3, movie4, movie5]
print(sorted(movie_list))
