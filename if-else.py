age = 17

if (age > 18):
    print('You are old enough to drive')
else:
    print('You are to young to drive')

print('Finished')

x = 1
if x > 1:
    print('More than one')
    if x < 100:
        print('Less than 100')

print('All done')

if x < 2:
    print('small')
# like a else if
elif x < 10:
    print('medium')
else:
    print('large')

print('All done')

astr = "Hello Stephen"
try:
    astr = int(astr)
except:
    astr = -1

print("First", astr)
