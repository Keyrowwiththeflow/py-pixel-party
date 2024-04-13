# Implement a guessing game that uses these concepts.
import random as rnd

# Use a random integer range to generate a random number between 1 and 5
correctAnswer = rnd.randint(1,100)

# Ask the user for their guess
guess = input("What's the lucky number? ")

# Compare their guess to the random number
if int(guess) == correctAnswer:
  print("Are you cheating? I know you are.")
else:
  print("So you aren't cheating.")
 
# Tell them if they are right or wrong
