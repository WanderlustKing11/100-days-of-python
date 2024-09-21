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

max_score = 0
for score in student_scores:
  if score > max_score:
    max_score = score
print(max_score)

#################################################################################

#### For loops and the range() function

