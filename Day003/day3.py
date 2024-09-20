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
ascii = '''
    _._     _,-'""`-._
    (,-.`._,'(       |\`-/|
        `-.-' \ )-`( , o o)
              `-    \`_`"'-
'''
print(ascii)
print('Welcome to Treasure Island!')
print('Your mission is to find the treasure.')
print("You're at a cross road. Where do you want to go?")
choice_1 = input('Type "left" or "right": ').lower()
if choice_1 == "left":
  print('You come at a lake. There is an island in the middle of the lake.')
  choice_2a = input('Type "wait" to wait for a boat. Type "swim" to swim across: ').lower()
  if choice_2a == "wait":
    print('You arrive at the island unharmed. There is a house with 3 doors.')
    choice_3a = input('One red, one yellow and one blue. Which color do you choose? ').lower()
    if choice_3a == "red":
      print("It's a room full of fire.")
      print("Game over.")
    elif choice_3a == "yellow":
      print("The room is filled with gold! You found the treasure!!")
      print("You win!!")
    elif choice_3a == "blue":
      print("You entered a room. The door closes behind you and starts filling with water. There's no way out!")
      print("Game over.")
    else:
      print("Wrong input. You lose.")
  elif choice_2a == "swim":
    print("As you get half-way accross the lake, a monster comes from the depths and pulls you under.")
    print("Game over.")
  else:
      print("Wrong input. You lose.")
elif choice_1 == "right":
  print("There was a trap door underneith you. You fell into a pit of spikes and are bleeding out.")
  print("Game over.")


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

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0

# if height > 120:
#   print("You can ride the rollercoaster!")
#   age = int(input('What is your age? '))
#   if age < 12:
#     bill = 5
#     print('Child tickets are $5.')
#   elif age <= 18:
#     bill = 7
#     print('Youth tickets are $7.')
#   elif age >= 45 and age <= 55: # elif 45 <= age <= 55:
#     print("Everything's going to be ok. Have a free ride on us!")
#   else:
#     bill = 12
#     print('Adult tickets are $12.')

#   photo = input('Would you like a photo? Y or N: ')
#   if photo == 'Y':
#     bill += 3

#   print(f'Your final bill is ${bill}')

# else:
#   print('Sorry, you have to grow taller before you can ride.')


#################################################################################

##### Pizza Order Practice

# print('Welcome to Python Pizza Deliveries!')
# size = input('What size pizza do you want? S, M or L: ')
# pepperoni = input('Do you want pepperoni on you pizza? Y or N: ')
# extra_cheese = input('Do you want extra cheese? Y or N: ')

# bill = 0
# if size == 'S':
#   bill += 15
# elif size == 'M':
#   bill += 20
# elif size == 'L':
#   bill += 25
# else:
#   print('You typed the wrong inputs.')

# if pepperoni == 'Y':
#   if size == 'S':
#     bill += 2
#   else:
#     bill += 3

# if extra_cheese == 'Y':
#   bill += 1

# print(f'Your final bill is: ${bill}.')


#################################################################################

