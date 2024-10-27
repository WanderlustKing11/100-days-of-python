#---------- Day 6 Lesson ----------#

# Topics: Python Functions & Karel

#################################################################################

# Defining and Calling Python Functions

# Python has many Built-in Functions that we can use
python_docs = 'https://docs.python.org/3/library/functions.html'

# Methods are easy to identify because they have () after their name. Here's one we're very
# familiar with:
# print('Hello, world!')
# num_char = len('Hello')
# print(num_char)

# What if we wanted to make our own functions? Use the key word 'def' to define our funciton, then
# give it a name, then the () and whatever parameters go in there, and finally a ':'.

def my_function():
  print('Hello')
  print('Bye')

# To call the function, type the name of the function, and add the () with whatever necessary parameters
# my_function()

# Go to https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json
# You can practice using functions and methods to move a robot


#################################################################################

# The Hurdles Loop Challenge

# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json


#################################################################################


# Indentation in Python

# Python is very stict about its indentation. Anything within a function must be indented under
# the defining line, or else it won't be a part of the function

def my_other_function():
  print("This line is indented")

print("This line is not indented, and thus not part of the 'my_other_function()'")

# You can think of it like file stucture, and how nested documents and folders live inside of
# other folders or directories. If it's not indented, then it's the same level of the higher folder

def more_examples():
  if sky == 'clear':
    print('blue')
  elif sky == 'cloudy':
    print('gray')
  print('Hello')
print('World')

# There is a lot of debate between spaces vs tabs lol. #SiloconValley
# Technically, in the official guide from the Python community, they straight up say that
# Spaces are the prefered indentation method, and that it should be indented 4 spaces per
# indentation level


#################################################################################

# While Loops

def my_while_loop_function():
    count = 6
    while count > 0:
      count -= 1
    if count == 0:
      print("This While Loop is complete")
    
# my_while_loop_function():
#     while not at_goal():
#         jump()

#################################################################################

# Reeborg's Maze Puzzle Solution

# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

def reeborgsMaze1():
  while not at_goal():
    if front_is_clear() == True:
        move()
    elif not front_is_clear() and right_is_clear():
        turn_right()
    elif not front_is_clear() and not right_is_clear():
        turn_left()
        if front_is_clear() == True:
            while not right_is_clear() and not wall_in_front():
                move()
            turn_right()
            if at_goal() == True:
                break
            elif front_is_clear():
                move()
                if front_is_clear():
                    turn_right()
                    if front_is_clear():
                        move()
            else:
                turn_left()

# Another solution

def reeborgsMaze2():
    while front_is_clear():
      move()
    turn_left()

    while not at_goal():
        if right_is_clear():
            turn_right()
            move()
        elif front_is_clear():
            move()
        else:
            turn_left()


#################################################################################

