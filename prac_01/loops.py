for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 110, 10):
    print(i, end=' ')
print()

for i in reversed(range(21)):
     print(i, end=' ')
print()

num_of_stars = int(input("Number of Stars : "))
for i in range(num_of_stars):
    print("*", end=' ')

total = num_of_stars + 1
for i in range(total):
    print("*" * i)
