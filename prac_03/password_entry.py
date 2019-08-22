"""Cassandra King"""

def main():
    def get_password():
        password = input("Password: ")
        while len(password) <= 3:
            print("Password should be longer then 3 characters.")
            password = input("Password: ")
        else:
            return password

    password = get_password()
    print('*' * len(password))


main()
