"""
In today's program, we will cover Data Types, Operations, Type Conversion,
and f-Strings. By the end of it, we will know enough to build a tip calculator.


I'm commenting out each topic so they don't overlap and to clean up the terminal
Uncomment any code sections you see to see the lesson and how it prints

Just below is my attempt at doing it on my own.
"""


'''
#1. Greeting
print("Welcome to the tip calculator")
#2. Ask user what was the total bill.
total = input("What was the total bill? $")
#3. Ask user how many people will split the bill.
numOfPeople = input("How many people to split the bill? ")
#4. Ask user what percentage tip they would like to give.
percent = input("What percentage tip would you like ot give? 10, 15, or 20? ")
#5. Calculate the amount tip
conversion = float(percent) * 0.01
tip = (float(total) * conversion) / float(numOfPeople)
#6. Return to the user how much teap each person should pay.
print("Each person should pay: " + "$" + "%.2f" % tip)
'''

####################################################################

# Topic: Primitive Data Types - Strings, Integers, Floats, and Booleans

# print(len(12345678))   This creates an error, no len on int
# print("12345678")
# or print(len(str(12345678))

# The method of pulling out a particular element from a striing is called 'Subscripting'
# print("Hello"[0:4])
# print('World'[4])

# print(int("1234") + 3210)

##################################

# num_char = len(input("What is your name?"))
# print("Your name has " + str(num_char) + " characters.")

# You can use the function type() to find out what type of data an element is
# print(type(num_char))   # prints <class 'int'>
# new_num_char = str(num_char)
# print("Your name has " + new_num_char + " characters.")     # This works!

# Type casting is converting one Data Type into another
# str()
# int()
# float()
# bool()


#####################################################

##### Day 2 - Data Types Exercise #####
# Write a program that adds the digits in a 2 digit number. 
# e.g. if the input was 35, then the output should be 3 + 5 = 8
# The given input is 39

#1. Convert into a string
# two_digit_number = input("Enter a 2 digit number: ")
# first_digit = int(two_digit_number[0])
# second_digit = int(two_digit_number[1])
# sum = first_digit + second_digit
# print(sum)

#####################################################

# Note: all division operations return a float
# print(type(6 / 2))

# Here we can test some basic math to see how Python priritizes its operators
# print(3 * 3 + 3 / 3 - 3)    # prints 7.0

# What's an easy way that we add something to this equation and make the result 3?
# print(3 * (3 + 3) / 3 - 3)  # prints 3.0


######################################################

##### Day 2 - BMI Calculator #####

# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# Print the answer as a whole number

# weight = float(input('Enter your weight (in kg): '))
# height = float(input('Enter your height (in meters): '))
# bmi = (weight) / (height ** 2)
# print(int(bmi))

######################################################

# Using int() on a float chops off everything after the decimal point.
# If you want to round to the nearest whole number, use round()

divide = 8 / 3

# print(divide)
# print(round(divide))
# print(type(round(divide)))  # Here you'll see that when we use round, we convert float to an int
# print(round(divide, 2))     # The second parameter of round allows us to choose where to round it off to

# We can use floor to instantly convert a float to an int, but will not round up
floor = 8 // 3
# print(floor)


# f-Strings allows us use multiple data types within a string
score = 0
height = 1.8
isWinning = True
print(f"Your score is {score}, your height is {height}, and it's {isWinning} that you're winning!")

######################

tip_percent = 12.00
bill = input('How much was the bill? $')
tip = float(bill) * (tip_percent / 100)
print(f'Your tip will be ${round(tip, 2)}.')

