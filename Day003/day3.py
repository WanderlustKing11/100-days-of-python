#---------- Day 3 Lesson ----------#

# Topics: Conditional Statements, Logical Operators, Code Blocks and Scope


# Attempt it Yourself!!!
# Today's project is a "Choose Your Adventure" game. It will have a created image,
# and some logic to take a user through a story to "find the treasure".

#1. Add your own ASCII art
    #   _._     _,-'""`-._
    #  (,-.`._,'(       |\`-/|
    #      `-.-' \ )-`( , o o)
    #            `-    \`_`"'-

#2. Greet user to "Treasure Island"
#3. Give instructions: "find the treasure"
#4. "You're at a cross road. Where do you wna to go? Type "left" or "right"
#5. If pick left: "You come at a lake. There is an island in the middle of the lake. Type 'wait' to wait for
#   a boat. Type 'swim' to swim across."
#6. If pick wait: "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and 
#   one blue. Which color do you choose?"
#7. If pick red: "It's a room full of fire. Game Over."

# The game lets you pick your decisions, and depending on what they choose it contains the 
# game's story.


#################################################################################

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# if height > 120:
#     print("Can get on ride")
# else:
#     print("Cannot ride")



#################################################################################

###### Day 3 Exercise: Odd or Even ######

# number = int(input("Which number do you want to check? "))
# if number % 2 == 0:
#     print("Is even")
# else:
#     print("Is odd")


#################################################################################

##### Nested if and elif statements

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height > 120:
#   print("Can get on ride")
#   age = int(input('What is your age? '))
#   if age < 12:
#     print('Please pay $5.')
#   # elif age <= 18:
#   elif 12 <= age <= 18:
#     print('Please pay $7')
#   else:
#     print('Please pay $12')
# else:
#   print("Cannot ride")


#################################################################################

##### BMI 2.0

# # Enter your height in meters e.g, 1.55
# height = float(input('What is your height (in meters)? '))
# # Enter your weight in kilograms e.g., 72
# weight = float(input('What is your weight (in kg)? '))
# bmi = (weight) / (height * height)
# message = 'clinically obese'
# if bmi < 18.5:
#     message = 'are underweight'
# elif bmi >= 18.5 and bmi < 25:
#     message = 'have a normal weight'
# elif bmi >= 25 and bmi < 30:
#     message = 'are slightly overweight'
# elif bmi >= 30 and bmi < 35:
#     message = 'are obese'
# elif bmi >= 35:
#     message = 'are clinically obese'

# print(f"Your BMI is {bmi}, you {message}.")


#################################################################################

##### Leap Year

# year = int(input())

# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 == 0:
#       print("Leap year")
#     else:
#       print("Not leap year")
#   else:
#     print("Leap year")
# else:
#   print("Not leap year")


#################################################################################

##### Continuing Roller Coaster example to learn how to use multiple 'if' statements

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height > 120:
  print("You can ride the rollercoaster!")
  age = int(input('What is your age? '))
  if age < 12:
    bill = 5
  elif 12 <= age <= 18:
    bill = 7
  else:
    bill = 12
  photo = input('Would you like a photo? y/n ')
  if photo == 'y':
    bill += 3
  print(f'Please pay ${bill}.')
else:
  print("Sorry, you have to grow taller before you can ride.")
