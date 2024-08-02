# Anna's Cake
# By Anna and Doug

# We want to build custom cakes
# Small, medium and large ($5, $7, $9)


# Toppings ($3):
## - sprinkles
## - cherries
## - icing
## - birthday candles


## - custom lettering ($1 / letter)

# flavors:
## - chocolate
## - vanilla
## - party cake

# Decorations ($10):
## - Darth Vader
## - Princess Leia
## - Luke Skywalker
## - Darth Maul
## - Yoda / Grogu
## - Storm Trooper

# Pickup or Delivery? ($2 for delivery)

print("Hi! Welcome to Anna's Bakery! Made by Anna & Doug.")
bill = 0
size = input('What size cake would you like? (S, M, or L) ')
if size == 'S':
  price = 5
  bill = 5
  size = 'Small'
elif size == 'M':
  price = 7
  bill = 7
  size = 'Medium'
elif size == 'L':
  price = 9
  bill = 9
  size = 'Large'

flavor = input('What type of cake would you like? Chocolate, Vanilla, or Party? ')

toppings = []
sprinkles = input('Add sprinkles? Y or N ')
if sprinkles == 'Y':
  bill += 3
  toppings.append('sprinkles')
cherries = input('Add cherries? Y or N ')
if cherries == 'Y':
  bill += 3
  toppings.append('cherries')
icing = input('Add icing? Y or N ')
if icing == 'Y':
  bill += 3
  toppings.append('icing')
candles = input('Add candles? Y or N ')
if candles == 'Y':
  bill += 3
  toppings.append('candles')

custom_l = input('Would you like to add custom lettering? Y or N ')
if custom_l == 'Y':
  custom_message = input('Enter your custom message ($1 per letter) ')
  count = custom_message.split()
  letters = 0
  for i in count:
    letters += len(i)
  print(f'You will be charged ${letters}')
  bill += letters

special = input('Would you like a decorative cake? ($10) Y or N ')
dec = ['Darth Vader', 'Princess Leia', 'Luke Skywalker', 'Darth Maul', 'Yoda / Grogu', 'Storm Trooper', 'Rapunzel']
if special == 'Y':
  print('You may choose from: ')
  list_num = 1
  for character in dec:
    print(f'{list_num}. {character}')
    list_num += 1
  decoration = int(input('Enter the number you would like: '))
  print(f'You have chosen {dec[decoration - 1]}')
  bill += 10

delivery = input('Would you like pickup or delivery. Delivery is an extra $2. Y (for delivery) or N ')
if delivery == 'Y':
  bill += 2

print('')
print("Here's your cake: ")
print(f"{size} {flavor} cake: ${price}")
if len(toppings) == 0:
  print('With no toppings')
else:
  print(f"With toppings: ")
  for topping in toppings:
    print(topping)
  print(f"${len(toppings) * 3}")
if custom_l == 'Y':
  print(f'Your custom message: {custom_message}: ${letters}')
if special == 'Y':
  print(f"Decorative {dec[decoration - 1]}: $10 ")
if delivery == 'Y':
  print('Delivery fee: $2 ')
print(f'Your total is ${bill}')