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

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
  print("Can get on ride")
  age = int(input('What is your age? '))
  if age < 12:
    print('Please pay $5.')
  elif 12 <= age <= 18:
    print('Please pay $7')
  else:
    print('Please pay $12')
else:
  print("Cannot ride")

