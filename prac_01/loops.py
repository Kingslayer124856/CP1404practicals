for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 110, 10):
    print(i, end=' ')
print()

for i in reversed(range(21)):
     print(i, end=' ')
print()

num = int(input("Number of Stars : "))
for i in range(num):
    print("*", end=' ')

for i in range(0, 5):
    print("*" * i)
print()