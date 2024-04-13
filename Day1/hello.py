# Create a program that will read in a persons name, append it to the contents of a file and then print the contents of that file.
import re

maxLength = 16

pattern = r'[^a-zA-Z]+'

while True:
  print("What's your name?")
  name = input()

# check to see if the name that was input is the same length as after you run a regex on it substituting an empty character for every non-matched character
  tempName = re.sub(pattern,"",name)
  if tempName != name:
    print("ERROR FOUND: Invalid characters (Only alphabetical letters)")
    continue

  if len(name) > maxLength:
    print("ERROR FOUND: Too many characters (" + str(maxLength) + " characters is the max)!")
    continue
  else:
    if len(name) > 0:
      print("What's up, " + name + "?")
      break

# Write the name to a file
with open("kavadaba.txt","w") as fileName:
  fileName.write("Welcome to the backrooms, ")
  fileName.write(name)
  fileName.write("\n")
