n = 5
# indefinite loop
while n > 0:
    print(n)
    n = n - 1

print('Blastoff')

# definite loop
for i in [5, 4, 3, 2, 1]:
    print(i)

print('Blastoff')


friends = ['Ian', 'Glenda', 'Tom', 'Eric']

for friend in friends:
    print('Hi there', friend)

print('Done')

largest_so_far = -1
print("Before:", largest_so_far)

for the_num in [9, 41, 33, 55, 9, 100, 22, 57]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)

print('After:', largest_so_far)
