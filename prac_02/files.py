# Gets users name and writes it in a file called name.txt that
# was created by the code
out_file = open('name.txt', 'w')
name = input("what`s your name?   : ")
print(out_file.write(name))
out_file.close()

# using the above program to print a sentence in the file as
# above, with the user input
in_file = open('name.txt', 'r')
name = in_file.read().strip()
in_file.close()
print("Your Name is ", name)

# opens numbers.txt and reads the numbers in that file
# then adds them together
in_file = open("numbers.txt", "r")
num1 = int(in_file.readline())
num2 = int(in_file.readline())
in_file.close()
print(num1 + num2)

in_file = open('numbers.txt', 'r')
total = 0
for line in in_file:
    number = int(line)
    total += number
in_file.close()
print(total)
