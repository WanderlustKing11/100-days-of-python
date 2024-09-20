#---------- Day 4 Lesson ----------#

# Topics: Randomization, creating modules, understanding lists

#################################################################################

#### Randomization ####

# This invovles using the Mersenne Twister as a Pseudorandom number generator

# https://docs.python.org/3/library/random.html

import random

random_integer = random.randint(1, 10)  # (Inclusive)
# print(random_integer)

random_number_0_to_1 = random.random()
# print(random_number_0_to_1)
# print(random_number_0_to_1 * 10)

random_float = random.uniform(1, 10) # inclusive of 10
# print(random_float)

#################################################################################

# Modules 
# import my_module

# print(my_module.my_favorite_number)


#################################################################################

#### Head or Tails ####

# random_num_gen = random.random() * 10
# if random_num_gen < 5:
#   print(f'Num generated = {random_num_gen}: Heads')
# else:
#   print(f'Num generated = {random_num_gen}: Tails')
  
# random_num_gen = random.randint(0, 1)
# if random_num_gen == 0:
#   print(f'Num generated = {random_num_gen}: Heads')
# else:
#   print(f'Num generated = {random_num_gen}: Tails')

#################################################################################

#### Lists ####

# matrix_characters = []

# matrix_characters.append('Neo')
# matrix_characters.append('Trinity')
# matrix_characters.append('Morpheus')

# print(matrix_characters)
# print(matrix_characters[0])


#################################################################################

#### Code challenge: Who will pay the bill? ####

friends = ['Doug', 'AJ', 'Derek', 'Fred']

# random_index = random.randint(0, 3)

# print(f'{friends[random_index]} pays the bill today!')

#### Use the choice method

# print(random.choice(friends))


#################################################################################

#### The Dirty Dozen ####

# dirty_dozen = ['Strawberries', 'Spinach', 'Kale', 'Nectarines', 'Apples', 'Grapes', 'Peaches', 'Cherries', 'Pears', 'Tomatoes', 'Celery', 'Potatoes']

# Nested list:

# fruits = ['Strawberries', 'Nectarines', 'Apples', 'Grapes', 'Peaches', 'Cherries', 'Pears']
# vegetables = ['Spinach', 'Kale', 'Tomatoes', 'Celery', 'Potatoes']

# dirty_dozen = [fruits, vegetables]

# print(dirty_dozen)
# print(dirty_dozen[0][2])  # Apples



#################################################################################

#### Rock, Paper, Scissors

rock = '''
       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
'''

paper = '''
           ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----' 
'''

scissors = '''
         _______
----/ \ )_______)
   (  (/()______)
        ()__)
----\___()_)
'''

game_list = [rock, paper, scissors]

player_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: '))
print(f'You chose {player_choice}')
print(f'{game_list[player_choice]}')

computer_choice = random.randint(0, 2)
print(f'Computer chose:')
print(f'{game_list[computer_choice]}')

if player_choice == computer_choice:
  print("It's a tie.")
elif (player_choice == 0 and computer_choice == 1) or (player_choice == 1 and computer_choice == 2) or (player_choice == 2 and computer_choice == 0):
  print('Computer wins')
elif (computer_choice == 0 and player_choice == 1) or (computer_choice == 1 and player_choice == 2) or (computer_choice == 2 and player_choice == 0):
  print('You win')