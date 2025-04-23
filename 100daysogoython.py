#print("hello world")
#this piece of code in programming is called stringswhich consist of character.

#print("hello world\nhello world\nhello world")
#print("hello + Aman")
#this is called escape sequence in programming

# print("hello"+ "aman")
# # so now how we can add space in between
# print("hello" + " " + "aman")

# INPUT FUNCTION 
# main function to take input from user
#print("hello " + input("what is your name"))

#write a program that print the number of character in a user name 
#print(len(input("what is your name")))

#VARIABLE IN PYTHON
# name = input("what is your name")
# print(name)  # prints the name of the user

# name = input("what is your name")
# length = len(name)
# print(length)

# WAP that switches the values stored in the variable a and b
# a = 10
# b = 20

# # Swapping
# a, b = b, a

# # Output the result
# print("After swapping:")
# print("a =", a)
# print("b =", b)

# Using a Temporary Variable

# a = 10
# b = 20

# # Swapping using a temporary variable
# temp = a
# a = b
# b = temp

# print("a =", a)
# print("b =", b)

# Using Arithmetic Operations (only for numbers)

# a = 10
# b = 20

# # Swapping using arithmetic
# a = a + b
# b = a - b
# a = a - b

# print("a =", a)
# print("b =", b)

#day 1 project
# WELCOME TO THE BAND NAME GENERATOR
# This program generates a random band name based on a list of words

#CREATE A GREETING FOR YOUR PROGRAM
# print("Welcome to the Band Name Generator")
# # ASK THE USER FOR THE CITY THEY GREW UP IN 
# city = input("What city did you grow up in?\n")
# # ASK THE USER FOR THE NAME OF A PET
# pet = input("What was the name of your first pet?\n")
# # COMBINE THE NAME OF THEIR CITY AND PET AND SHOW THEM THEIR BAND NAME
# print("your band name could be " + city + " " + pet) 

#day2 
#primitive data type


# #string
# print("hello"[4])
#this will give output as o

# print("123" + "456")
#output = 123456

#INTEGER
# print(10 + 20)
#output = 30

#FLOAT
# print(10.5 + 20.5)
#output = 31.0

#BOOLEAN
# print(10 > 5)
#output = True
#output = False

#TYPE ERROR
# num_char = len(input("what is your name"))
# print("your name has " + num_char + " letters") #this will give error because we cannot concatenate integer and string 
# #to solve this we can convert integer to string using str() function
# print("your name has " + str(num_char) + " letters") #this will give output

#or we can use type function 
# num_char = len(input("what is your name"))
# print("your name has " + num_char + " letters")
# print(type(num_char))

#Q. WAP that adds the digits in a two digits number e.g. if the input was 35 , then the output should be 3+5=8
# num = (input("enter a two digit number:"))
# a = int(num[0])
# b = int(num[1])
# result = a + b
# print("the sum is:" + str(result))

#MATHEMATICAL OPERATION IN PYTHON
# print(10 + 20) ADD
# print(10 - 20) SUBTRACT
# print(10 * 20) MULTIPLY
# print(10 / 20) DIVISION
# print(10 % 20) MODULO
# print(10 ** 20) POWER

#PRIORITY OF THESE ARE LIKE PEDMAS
# ()
# **
# *
# /
# +
# -

# print(3 * 3 + 3 / 3 - 3)
#output = 7.0
# print(3 * (3 + 3) / 3 - 3)
#output = 3.0

#BMI CALCULATOR
# WAP TO CALCULATE THE BMI FROM A USER'S WEIGHT AND HEIGHT.
# height = input("enter the height in m:")
# weight = input("enter the weight in kg:")

# bmi = int(weight) / float(height) ** 2
# a = int(bmi)
# print("your bmi is: " + str(a))

#Round of the number
# print(round(8 / 3))
#output = 3
# print(round(8 / 3, 2))
#output = 2.67 the 2 here means rounding of upto 2 digit
# print(8 / 3) #output = 2.6666666666666665
# print(8 // 3) #output = 2 the // here is floor division operator
# print(8 % 3) #output = 2 the % here is modulus operator

# score = 0
# height = 1.8
# isWinning = True
# # now to print all these things like all are of different types one is int, float and boolean so we need to use str before merging the two so now in python there is different method also
# # we can use f- String
# print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")
# #output = your score is 0, your height is 1.8, you are winning

# WAP using maths and f- string that tells us how many days , weeks , months we have left if we live until 90 years old.
# age = input("what is your current age:")
# age = int(age)
# a = 90 - age
# b = a * 365 # days remaining
# c = a * 52 # week remaining
# d = a * 12 # month remaining
# print(f"you have {a} years left, {b} days left, {c} week left, {d} month left")

#DAY 2 PROJECT Calculator
# print("Welcome to tip Calculator!")
# bill = float(input("What was the total bill? $"))
# tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
# people = int(input("How many people to split the bill?"))
# # bill_with_tip = tip / 100 * bill + bill
# # print(bill_with_tip)
# # or
# tip_as_percent = tip / 100
# total_tip_amount = bill * tip_as_percent
# total_bill = bill + total_tip_amount
# bill_per_person = total_bill / people # now we have to round this to two digit
# final_amount = round(bill_per_person, 2)# here we use 2 to round the float function upto two decimal place
# print(f"Each person should pay: ${final_amount}") # here we are using f-string to

#DAY 3 CONDITIONAL STATEMENT, LOGICAL OPERTOR ,CODE BLOCKS AND SCOPE
#if else
#syntax:
# if condition:
#     #code block
# else:
#     #code block

# print("Welcome to rollarcoaster!")
# height = int(input("How tall are you in cm? "))
# if height >= 120:
#     print("You can ride the rollercoaster!")
# else:
#     print("Sorry, you have to grow taller!")

#Exercise
# WAP that works out weather if a given number is an odd or even number
# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print("This is an even number")
# else:
#     print("This is an odd number")

#NESTED IF/ELSE:

# print("Welcome to rollarcoaster!")
# height = int(input("How tall are you in cm? "))
# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("what is you age"))
#     if age <= 18:
#       print("please pay $7")
#     else:
#        print("please pay $12")
# else:
#     print("Sorry, you have to grow taller!")

# IF/ELIF/ELSE

# print("Welcome to rollarcoaster!")
# height = int(input("How tall are you in cm? "))
# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("what is you age"))
#     if age < 12:
#        print("please pay $5")
#     elif age <= 18:
#       print("please pay $7")
#     else:
#        print("please pay $12")
# else:
#     print("Sorry, you have to grow taller!")

 
# Exxercise
# WAP that interprets the body mass index based on user weight and height

# height = float(input("enter your height in cm:"))
# weight = float(input("enter your height in kg:"))

# bmi = round(weight / height ** 2) # we use round to round the output to the nearest integer
# if bmi < 18.5:
#     print(f"your bmi is {bmi}, you are underweight")
# elif bmi < 25:
#     print(f"your bmi is {bmi}, you are have a normal weight")
# elif bmi < 30:
#     print(f"your bmi is {bmi}, you are overweight")
# elif bmi < 35:
#         print(f"your bmi is {bmi}, you are obeset")
# else:
#     print(f"your bmi is {bmi}, you are clinically obese")

# LEAP YEAR EXERCISE

# year = int(input("Which year do you want to check?"))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("leap year")
#         else:
#             print("not a leap year")
#     else:
#         print("leap year")
# else:
#     print("not a leap year")

# multiple if statement:
# print("Welcome to rollarcoaster!")
# height = int(input("How tall are you in cm? "))
# bill = 0
# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("what is you age"))
#     if age < 12:
#        bill = 5
#        print("child tickets are $5")
#     elif age <= 18:
#       bill = 7
#       print("Youth tickets are $7")
#     else:
#        bill = 12
#        print("Adult tickets are $12")
    
#     want_photo = input("Do you want a photo taken? Y or N. ")
#     if want_photo == "Y":
#        bill = bill + 3 # we are adding $ 3 to original bill if they take a photo
#     # here if we do not add else statement then its ok as if Y is not then definitely its N

#     print(f"your total bill is {bill}")

# else:
#     print("Sorry, you have to grow taller!")

# EXERCISE= PIZZA ORDER
# print("Welcome to pizza order")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = ("Do you want pepperoni? Y or N")
# extra_cheese = ("Do you want cheese? Y or N")

# bill = 0
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# elif size == "L":
#     bill += 25

# if add_pepperoni == "Y":
#     if size == "S":
#         bill  += 2
#     else:
#         bill += 3
    
# if extra_cheese == "Y":
#     bill  += 1

# print(f"your final bill is ${bill}")

#Logical Operator

# print("Welcome to rollarcoaster!")
# height = int(input("How tall are you in cm? "))
# bill = 0
# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("what is you age"))
#     if age < 12:
#        bill = 5
#        print("child tickets are $5")
#     elif age <= 18:
#       bill = 7
#       print("Youth tickets are $7")
#     elif age >= 45 and age <=55:
#       print("Everything is going to be ok. Have a free ride on us!")
#     else:
#        bill = 12
#        print("Adult tickets are $12")
    
#     want_photo = input("Do you want a photo taken? Y or N. ")
#     if want_photo == "Y":
#        bill = bill + 3 # we are adding $ 3 to original bill if they take a photo
#     # here if we do not add else statement then its ok as if Y is not then definitely its N

#     print(f"your total bill is {bill}")

# else:
#     print("Sorry, you have to grow taller!")
#DAY 4
# Randomisation and python lists
# Randomisation means doing things in a random or unpredictable way.

# In Python, we can use a module called random to pick or shuffle things randomly.
# It's like rolling a dice or picking a card without looking
# import random

# names = ["Aman", "Priya", "Raj", "Simran"]
# print(random.choice(names))  # Picks one name randomly

# A list in Python is like a box that holds many values together, such as numbers, names, etc.
# fruits = ["apple", "banana", "cherry"]

# import random
# random_integer = random.randint(1, 10)
# # means here it generate any integer no from 1 to 10
# print(random_integer)

# now how we will create random floating number
# import random
# random_float = random.random()
# # generates a random float between 0.0 and 1.0
# print(random_float)

# # To create a random float between a specific range, you can multiply the random float by the range size and add the minimum value.
# now if we want to multiply the random float number
# import random
# random_float = random.random() * 10  # generates a random float between 0.0 and 10.0
# print(random_float)

#HEAD AND TAILS EXERCISE
# import random
# coin = "Heads" if random.randint(0, 1) == 0 else "Tails"
# print(coin)

# or

# import random
# random_side = random.randint(0, 1)
# if random_side == 1:
#     coin = "Heads"
# else:
#     coin = "Tails"
# print(coin)

#Python list
# fruits = ["apple", "banana", "cherry"]
# fruits.append("orange") # this will add "orange" to the list
# fruits.remove("banana") # this will remove "banana" from the list
# print(fruits)

#exercise
# you are going to write a program which will select a random name from a list of names. the person selected will have to pay for everybody food bill

#split in python
# import random

# names = ["Aman", "Priya", "Raj", "Simran"]
# selected_name = random.choice(names)
# print(f"{selected_name} is going to pay for everybody's food bill!")

# now write the code as th input is given by the user and it should be divided by comma
# import random
# names = input("Enter names separated by commas: ").split(",")
# selected_name = random.choice(names)
# print(f"{selected_name.strip()} is going to pay for everybody's food bill!")
# Note: Ensure to strip any extra spaces from the names
# Note: Ensure to handle cases where the input might be empty or invalid

#make a list pf two different thing and now merge 
# fruits = ["apple", "banana", "cherry"]
# vegetables = ["carrot", "broccoli", "spinach"]
# combined_list = fruits + vegetables
# print(combined_list)

# create a list of name of state of india
# states_of_india = ["Maharashtra", "Karnataka", "Tamil Nadu", "Gujarat", "Rajasthan", "West Bengal", "Uttar Pradesh", "Kerala", "Andhra Pradesh", "Punjab"]
# num_of_state = len(states_of_india)
# print(states_of_india[num_of_state - 1])

#exercise
#teasure nap 
#see video 44 for question or screenshort

#start from video 47
#DAY 5 
#FOR LOOPS, RANGE AD CODE BLOCKS
# loops means things that happen again and again
# For loops are used to iterate over a sequence (like a list or a string) or to repeat a block of code a certain number of times.
# For loops can be used to iterate over a range of numbers or elements in a list.
#syntax for FOR loop 
# for item in list_of_items:
# do something to each item
# for number in range(start, end):
#     do_something(number)

# fruits = ["apple", "mango", "banana"]
# for fruit in fruits:
#     print(fruit)



  


