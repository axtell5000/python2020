purse = dict()
purse['money'] = 100
purse['lipstick'] = 2
purse['tissues'] = 20
print(purse)

# another way
books = {'Jade City': 'Fonda Lee', 'Jade War': 'Fonda Lee',
         'The Great Hunt': 'Robert ordan'}
print(books)
print(books['Jade City'])

# counting
counts = dict()
names = ['csev', 'chen', 'csev', 'chen', 'rgain', 'chen']

for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1

print(counts)

# as above but shortening it using get()
authors = dict()
names2 = ['Joe Abercrombie', 'Fonda Lee', 'Brent Weeks',
          'Rebecca Kuang', 'Joe Abercrombie', 'Brent Weeks']
for name in names2:
    # the 0 in the get is the default value
    authors[name] = authors.get(name, 0) + 1

print(authors)

# Another way to declare dictionary
stuff = {'Roy': 5, 'Claire': 33, 'Ian': 69}
for key in stuff:
    print(key, stuff[key])

print(stuff.keys())
print(stuff.values())
print(stuff.items())

# another way we can loop through
for aaa, bbb in stuff.items():
    print(aaa, bbb)

# reading from a file
handle = open('mbox-short.txt', 'r')

counts2 = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts2[word] = counts2.get(word, 0) + 1

bigcount = None
bigword = None
for word, count in counts2.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)

fname = input('Enter filename: ')
if len(fname) < 1:
    fname = 'clown.txt'
hand = open(fname)
di = dict()

for line in hand:
    line = line.rstrip()
    # print(line)
    words = line.split()
    print(words)
    for w in words:
        if w in di:
            di[w] = di[w] + 1
        else:
            di[w] = 1
            print('***New***')
        print(w, di[w])

# NB we can use get() in dictionaries as well
