import re

hand = open('mbox-short.txt', 'r')

# for line in hand:
#     line = line.rstrip()
#     if re.search('^D.*: ', line):  # starts with a D and then ayother characters
#         print(line)

for line in hand:
    line = line.rstrip()
    if re.search('^From (\S+@\S+)', line):  # starts with a D and then ayother characters
        print(line)

x = 'My 2 favourite numbers are 7 and 1000'
y = re.findall('[0-9]+', x)  # + means 1 or more
print(y)

y2 = re.findall('[AEIOU]+', x)  # finds nothing
print(y2)

# Starts with M, 1 or more characters, ends in e and is not greedy
y3 = re.findall('^M.+?e', x)
print(y3)  # ['My 2 favourite']
