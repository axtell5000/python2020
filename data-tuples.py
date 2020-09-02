# Tuples are immutable
t = tuple()
print(dir(t))
t2 = ('a', 'b', 'd', 'c')
# t2.sort() cant do this

# tuples are comparable
print((0, 1, 3) < (5, 4, 3))

fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst = list()
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)

lst = sorted(lst, reverse=True)

for val, key in lst[:10]:
    print(key, val)
