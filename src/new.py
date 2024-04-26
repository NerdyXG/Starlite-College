import psycopg2 as ps
import sys

dbname = "college"
user = input("database user: ")
password = input("database password: ")
host = "localhost"
port = "5432"

try:
    conn = ps.connect(
        dbname = dbname,
        user = user,
        password = password,
        host = host,
        port = port
    )

    cur = conn.cursor()

    print("Connection to Postgres Database was successful...")

except ps.OperationalError as e:
    print(f"Error: {e}")
    sys.exit()


def admin_session():
    while 1:
        print("\nAdmin Menu\n")
        print("\n1. Register New Student")
        print("2. Register New Teacher")
        print("3. Delete Existing Student")
        print("4. Delete Existing Teacher")
        print(". Log out\n")

        option = input("Option: ")

        if option == "1":
            first_name = input("First name: ")
            last_name = input("Last name: ")
            email = input("Email: ")
            username = input("Username: ")
            query_vals = (first_name, last_name, email, username)
            cur.execute(f"INSERT INTO users (first_name, last_name, email, username, privilege) VALUES(%s, %s, %s, %s, 'student')", query_vals)
            conn.commit()
            print(f"{first_name} successfully added!")


def admin_auth():
    print("\nAdmin Login\n")
    username = input("username: ")
    password = input("password: ")
    if username == "admin" and password == "password":
        admin_session()
    else:
        print("Incorrect login details...")

def main():
    while 1:
        print("\nWelcome to College Management System\n")
        print("1. Login as student")
        print("2. Login as teacher")
        print("3. Login as admin\n")
        option = input("Option: ")

        if int(option) < 1 or int(option) > 3:
            sys.exit("Invalid option...")

        elif option == "3":
            ...

        elif option == "3":
            ...

        elif option == "3":
            admin_auth()

            


main()