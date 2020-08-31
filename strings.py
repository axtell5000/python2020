fruit = 'apple'
letter = fruit[1]
print(letter)  # p
print(len(fruit))
index = 0

while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1

print('-----------------')

book = 'Jade War'

for letter in book:
    print(letter)

print('-----------------')

count = 0
for letter in book:
    if letter == 'a':
        count = count + 1

print('Amount of letters:', count)

movie = 'Star Wars'
# like JavaScript slice, doest include the letter in index 3
print(movie[0: 3])
print(movie[3:])  # r Wars
print(movie[:2])  # St
print(movie.lower())
print(movie.upper())

greeting = '    Hello Stephen    '
print(greeting)
print(greeting.lstrip())
print(greeting.rstrip())
print(greeting.strip())
