colors = ['red', 'green', 'blue']
print(colors)
print(colors[1])
# lists are mutable unlike strings
colors[0] = 'purple'
print(colors)
colorString = 'pink'
print(colorString)
# colorString[0] = 'P' This wont work

print(colors[0:])

# another way to create a list
goodies = list()
goodies.append('book')
goodies.append('rice')
goodies.append('guitar')
print(goodies)

numlist = list()
while True:
    inpt = input('Enter a number: ')
    if inpt == 'done':
        break
    value = float(inpt)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print('Average: ', average)

# with a file
handle = open('mbox-short.txt', 'r')

for line in handle:
    line.rstrip()
    words = line.split()
    # guardian statement
    if len(words) < 1:
        continue
    if words[0] != 'From':
        continue
    print(words[2])
10
