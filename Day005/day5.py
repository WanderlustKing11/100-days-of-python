#---------- Day 5 Lesson ----------#

# Topics: Python loops, for loops and range()

#################################################################################

#### For loop

# fruits = ['Apple', 'Peach', 'Pear']

# for fruit in fruits:
#   print(fruit)

#################################################################################

#### Max Score

student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 90, 125]

total_exam_score = sum(student_scores)
# print(f'total exam score = {total_exam_score}')

# max_score = 0
# for score in student_scores:
#   if score > max_score:
#     max_score = score
# print(max_score)

#################################################################################

#### For loops and the range() function

# for number in range(1, 10):
  # print(number) # Prints 1 - 9 on separate lines (excludes 10)

# for skip_numbers in range (1, 11, 3):
#   print(skip_numbers)  # prints 1 - 10, but in increments of 3... 1, 4, 7, 10

# Add all the numbers together from 1 - 100:
# sum = 0
# for num in range(1, 101):
#   sum += num

# print(sum)  # 5050

#################################################################################

#### FizzBuzz

# for num in range(1, 101):
#     if num % 15 == 0:
#         print('FizzBuzz')
#     elif num % 5 == 0:
#         print('Buzz')
#     elif num % 3 == 0:
#         print('Fizz')
#     else:
#         print(num)

#################################################################################

#### Random Password Generator

import random

print('Welcome to the PyPassword Generator!')
num_letters = int(input('How many letters would you like in your password?\n'))
num_symbols = int(input('How many symbols would you like?\n'))
num_numbers = int(input('How many numbers would you like?\n'))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Tracking remaining coutns of each
remaining_letters = num_letters
remaining_symbols = num_symbols
remaining_numbers = num_numbers

total_length_of_pw = num_letters + num_symbols + num_numbers

password_arr = []


# loop through the length of the password
for char in range(total_length_of_pw):  

  available_types = []
  if remaining_letters > 0:
    available_types.append('letter')
  if remaining_symbols > 0:
    available_types.append('symbol')
  if remaining_numbers > 0:
    available_types.append('number')
  print(available_types)

  # Randomly select which type of character to add next
  char_type = random.choice(available_types)
  print(f'next char type = {char_type}')

  # Add the selected character to the password and upadate the corresponding count
  if char_type == 'letter':
    random_letter = random.choice(letters)
    random_size = random.randint(0, 1)
    if random_size == 0:
      password_arr.append(random_letter.lower())
    else:
      password_arr.append(random_letter.upper())
    remaining_letters -= 1
  
  elif char_type == 'symbol':
    random_symbol = random.choice(symbols)
    password_arr.append(random_symbol)
    remaining_symbols -= 1

  elif char_type == 'number':
    random_number = random.choice(numbers)
    password_arr.append(random_number)
    remaining_numbers -= 1
  print(password_arr)

print(password_arr)

# Shuffle the final password to ensure randomness (redundant)
random.shuffle(password_arr)

print(f'Your random password is: {"".join(password_arr)}')
