import psycopg2 as ps
import sys, time

dbname = "college"
user = input("database user: ")
password = input("database password: ")
host = "localhost"
port = "5432"

try:
    conn = ps.connect(dbname=dbname, user=user, password=password, host=host, port=port)

    cur = conn.cursor()

    print("Connection to Postgres Database was successful...")

except ps.OperationalError as e:
    print(f"Error: {e}")
    sys.exit("Unauthorized access to the database!\n")


# admin 
def admin_auth():
    print("\nAdmin Login\n")
    username = input("username: ")
    password = input("password: ")
    
    if username == "admin" and password == "password":
        admin_session()
    else:
        print("Incorrect login details...")

        
def admin_session():
    while 1:
        print("\nAdmin Menu\n")
        print("\n1. Register New Student")
        print("2. Register New Teacher")
        print("3. Delete Existing Student")
        print("4. Delete Existing Teacher")
        print("5. Log out\n")

        option = input("Option: ")

        if option == "1":
            first_name = input("First name: ")
            last_name = input("Last name: ")
            email = input("Email: ")
            username = input("Username: ")
            query_vals = (first_name, last_name, email, username)
            cur.execute(
                f"INSERT INTO users (first_name, last_name, email, username, privilege) VALUES(%s, %s, %s, %s, 'student')",
                query_vals,
            )
            conn.commit()
            print(f"{first_name} has been successfully added as a student with an id of: ")
            cur.execute(f"SELECT id FROM users ORDER BY id DESC LIMIT 1")
            x = cur.fetchone()
            print(x)

        elif option == "2":
            first_name = input("First name: ")
            last_name = input("Last name: ")
            email = input("Email: ")
            username = input("Username: ")
            query_vals = (first_name, last_name, email, username)
            cur.execute(
                f"INSERT INTO users (first_name, last_name, email, username, privilege) VALUES(%s, %s, %s, %s, 'teacher')",
                query_vals,
            )
            conn.commit()
            print(f"{first_name} has been successfully added as a teacher with an id of: ")
            cur.execute(f"SELECT id FROM users ORDER BY id DESC LIMIT 1")
            x = cur.fetchone()
            print(x)
        
        elif option == "3":
            first_name = input("First name: ")
            id = input("id: ")
            cur.execute(f"DELETE FROM users WHERE first_name = '{first_name}' AND id = '{id}' AND privilege = 'student'")
            conn.commit()
            if cur.rowcount:
                print(f"{first_name} has been deleted successfully!")
            else:
                print(f"Error: {first_name} not found!")

        elif option == "4":
            first_name = input("First name: ")
            id = input("id: ")
            cur.execute(f"DELETE FROM users WHERE first_name = '{first_name}' AND id = '{id}' AND privilege = 'teacher'")
            conn.commit()
            if cur.rowcount:
                print(f"{first_name} has been deleted successfully!")
            else:
                print(f"Error: {first_name} not found!")

        elif option == "5":
            break

        else:
            print("Invalid option")

        time.sleep(1)


# teacher
def teacher_session():
    while 1:
        print("\nTeacher's Session\n")
        print("1. Mark Register")
        print("2. View Register")
        print("3. Log out")

        option = input("Option: ")
        
        if option == "1":
            ...

        elif option == "2":
            ...

        elif option == "3":
            break

        else:
            print("Invalid Option...")
    
def teacher_auth():
    print("\nTeacher's Authentification\n")
    id = int(input("Teacher's ID: "))
    password = input("Password: ")
    query_vals = (id, password)
    cur.execute("SELECT id, password FROM users WHERE id = %s AND password = %s AND privilege = 'teacher'", query_vals)
    x = cur.fetchone()
    if x:
        teacher_session()
    else:
        print("Invalid login details...")

def main():
    while 1:
        print("\nWelcome to College Management System\n")
        print("1. Login as student")
        print("2. Login as teacher")
        print("3. Login as admin")
        print("4. Exit\n")
        option = input("Option: ")

        if option == "1":
            ...

        elif option == "2":
            teacher_auth()

        elif option == "3":
            admin_auth()

        elif option == "4":
            sys.exit("Bye!!!")

        else:
            print("Invalid option...")


main()
