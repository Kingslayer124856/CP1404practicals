"""Cassandra King"""

password = input("Password: ")
while len(password) <= 3:
    print("Password should be longer then 3 characters.")
    password = input("Password: ")
else:
    print('*' * len(password))