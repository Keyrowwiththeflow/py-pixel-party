scores = ['Tom: 5', 'Eric: 23', 'June: 50']
print(scores)
scores[0];
# print(scores[0]) # Tom: 5
# parts = scores[0].split(":") # ['Tom', ' 5']
# print(int(parts[1].strip()) + 1); # 6
# print(parts)

scores_dictionary = {
  'Tom': 5,
  'Eric': 23,
  'June': 50
}

print(scores_dictionary)
scores_dictionary['Tom'] = "RARRR"
print(scores_dictionary)

tom = {
  'name': 'Tom',
  'age': 54,
  'score': 12
}

kiro = {
  'name': 'Kiro',
  'age': 15,
  'score': 100
}

mike = {
  'name': 'Dad',
  'age': 47,
  'score': 50,
  'favorite_food': ['beer','wine','alcohol','shakes']
}

people = [tom, kiro, mike]
print(people)
print(people[2]['favorite_food'])