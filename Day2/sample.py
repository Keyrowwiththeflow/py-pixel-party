import random as rnd

friends = []

while True:
  friend = input("What is your friend's name? ")
  if friend.strip() == "":
     break
  
  if friend in friends:
     print("Pick another friend.")
     continue



  friends.append(friend)

  

  # try:
  #    friends.index(friend)
  #    print(f"Your friend, {friend}, already exists in the array!")
  #    continue
  # except ValueError:
  #    friends.append(friend)
     

r = rnd.randint(0,len(friends)-1)
# print(r)
print(f"Your bestie today is: {friends[r]}!")

# loop through every character in the string and print it
print("These are your friends: ")
for i in range(len(friends)):
   print(friends[i])

#print(name[1])