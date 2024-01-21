"""We are going to create a short program that is a "band name generator".
This is my attempt to do this on my own."""

# cityName = input("What is the name of the city you grew up in?")

# petName = input("What's your pet's name?")

# print("Your band name could be", cityName, petName)



# Topics for Day 1
# print()
# Strings are anyting in between quotes " "
# Syntax highlighting, how our Code Editors give us clues as to what code is

# Here is the Day 1 Printing exercise:

# Print the three lines correctly, and submit to test if it's correct.
# Below is the correct answer.

print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")


# More topics:
# printing mutliple lines


print(""" This is how
      you can print
           multiple lines""")

print("Here's another way to print \n     on multiple lines")

# Here's how to concatenate
print('May ' + 'the ' + 'force ' + 'be ' + 'with ' + 'you' + '!')

# Indentation error
# In Python, spaces are very important. Always start your code at the beginning of the line
# to avoid unecessary indentation errors.

# debugging

# We have a Day 1 Debugging Practice exercise
# This is the desired output:
"""
Day 1 - String Manipulation
String Concatenation is done with the "+" sign.
e.g. print("Hello " + "world")
New lines can be created with a backslash and n.
"""

# This is the given code:
# print(Day 1 - String Manipulation")
# print("String Concatenation is done with the "+" sign.")
#   print('e.g. print("Hello " + "world")')
# print(("New lines can be created with a backslash and n.")

# And here is the correct answer:
#print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")


# Here's the Day 1 Practice:
# Write some code that will print you multiplying num1 with num2.
# num1 = int(input())
# num2 = int(input())
# print(num1 * num2)

# Now write some code that will print the number of charcters in a name from a given input:
name = input("What's your name? ")
print(len(name))