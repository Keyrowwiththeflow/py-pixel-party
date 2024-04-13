# Implement a guessing game that uses these concepts.
import random as rnd

lowerNumber = 1
higherNumber = 100
# Use a random integer range to generate a random number between lowerNumber and higherNumber
correctAnswer = rnd.randint(lowerNumber,higherNumber)

def evaluateAnswer(guess, answer) -> bool:
  result = False
  if int(guess) > answer:
    print("Your guess is too high.")
  elif int(guess) < answer:
    print("Your guess is too low.")
  elif int(guess) == answer:
    print("Are you cheating? I know you are.")
    result = True

  return result

# Ask the user for their guess
print(f"What's the lucky number ({lowerNumber}-{higherNumber})? ")
for guessCount in range(1,6):
  guess = input(f"Guess #{guessCount}: ")
    # Compare their guess to the random number
  isCorrectAnswer = evaluateAnswer(guess, correctAnswer)

  if isCorrectAnswer:
    break

if not isCorrectAnswer:
  print(f"Better luck next time. The correct answer was: {correctAnswer}")
   


