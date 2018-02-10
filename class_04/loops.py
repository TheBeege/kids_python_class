# This is an infinite loop
# If the thing between "while" and ":" is true,
# the loop will repeat what's after the ":"
# while True:
#     print('trollololol')
# This will print trollololol forever
# You can stop it using ctrl + c

i = 0
while i < 10:
    print(i)
    i += 1

# Same as above
# i = 0
# while True:
#     if i >= 10:
#         break
#     print(i)
#     i += 1

print('FOR')
for i in range(10):
    print(i)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print('LIST')
fruits = ['apple', 'banana', 'pear', 'pineapple']
for fruit in fruits:
    print(fruit)

print('LIST INDEX')
print(fruits[3])

fruits.append('yujin snack')
print(fruits)

print('DICTIONARY')
person = {
    'name': 'beege',
    'job': 'programmer',
    'country': 'korea',
    'pants': 'jeans',
    'is_alive': True,
    'number_of_legs': 2
}
print('person:', person)

print('job:', person['job'])
print(person['pants'])

person['has_snacks'] = True
print(person)
