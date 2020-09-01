fhandle = open('mbox-short.txt', 'r')
print(fhandle)

stuff = 'X\nY'
print(stuff)
print(len(stuff))
count = 0
for text in fhandle:
    count = count + 1

print('Line count:', count)

# It seems you cant read the same file variable twice, it closes automatically, so we had to create a new one
fhandle2 = open('mbox-short.txt', 'r')

text = fhandle2.read()  # read, does all the text as one long string
print(len(text))
print(text[:20])

fhandle3 = open('mbox-short.txt', 'r')
for line in fhandle3:
    line = line.rstrip()  # removes the extra newline
    if line.startswith('From:'):
        print(line)
