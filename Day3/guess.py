# Implement a guessing game that uses these concepts.
import random as rnd

lowerNumber = 1
higherNumber = 100
maxGuesses = 5
# Use a random integer range to generate a random number between lowerNumber and higherNumber
correctAnswer = rnd.randint(lowerNumber,higherNumber)

# Ask the user for their guess
print(f"What's the lucky number ({lowerNumber}-{higherNumber})? ")
guessCount = 0
while True:
  guessCount = guessCount + 1

  if guessCount > maxGuesses:
    print("Better luck next time!")
    break

  guess = input(f"Guess #{guessCount}: ")
    # Compare their guess to the random number
  if int(guess) == correctAnswer:
    print("Are you cheating? I know you are.")
    break
  else:  
    if (guessCount != maxGuesses):
      if int(guess) > correctAnswer:
        print("Your guess is too high.")
      elif int(guess) < correctAnswer:
        print("Your guess is too low.")
    elif (guessCount == maxGuesses):
      print(f"The correct answer was: {correctAnswer}. ")

    continue


 
# Tell them if they are right or wrong
