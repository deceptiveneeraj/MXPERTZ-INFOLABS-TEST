import pymysql as sql

mydb = sql.connect(
    host="localhost",
    user="root",
    passwd="Neer@j0506",
    database="test_db1"
)
mycursor = mydb.cursor()

def insert_data(mycursor, mydb):
    name = input("Enter name: ")
    email = input("Enter email: ")
    position = input("Enter position: ")
    salary = int(input("Enter salary: "))
    city = input("Enter city: ")
    mycursor.execute(
        "INSERT INTO employees (name, email, position, salary, city) VALUES (%s, %s, %s, %s, %s)",
        (name, email, position, salary, city)
    )
    mydb.commit()
    print("Data inserted successfully.")

def update_data(mycursor, mydb):
    user_id = int(input("Enter user ID to update: "))
    mycursor.execute("SELECT name, email, position, salary, city FROM employees WHERE id=%s", (user_id,))
    row = mycursor.fetchone()
    if row:
        current_name, current_email, current_position, current_salary, current_city = row
        print(f"Current name: {current_name}")
        new_name = input("Enter new name (press Enter to keep current): ")
        print(f"Current email: {current_email}")
        new_email = input("Enter new email (press Enter to keep current): ")
        print(f"Current position: {current_position}")
        new_position = input("Enter new position (press Enter to keep current): ")
        print(f"Current salary: {current_salary}")
        new_salary = input("Enter new salary (press Enter to keep current): ")
        print(f"Current city: {current_city}")
        new_city = input("Enter new city (press Enter to keep current): ")

        final_name = new_name if new_name else current_name
        final_email = new_email if new_email else current_email
        final_position = new_position if new_position else current_position
        final_salary = int(new_salary) if new_salary else current_salary
        final_city = new_city if new_city else current_city

        mycursor.execute(
            "UPDATE employees SET name=%s, email=%s, position=%s, salary=%s, city=%s WHERE id=%s",
            (final_name, final_email, final_position, final_salary, final_city, user_id)
        )
        mydb.commit()
        print("Data updated successfully.")
    else:
        print("User ID not found.")

def show_data(mycursor):
    mycursor.execute("SELECT * FROM employees")
    rows = mycursor.fetchall()
    if rows:
        print("\nAll users:")
        for row in rows:
            print(row)
    else:
        print("No data found.")

def delete_data(mycursor, mydb):
    user_id = int(input("Enter user ID to delete: "))
    mycursor.execute("DELETE FROM employees WHERE id=%s", (user_id,))
    mydb.commit()
    if mycursor.rowcount:
        print("Data deleted successfully.")
    else:
        print("User ID not found.")

def main():
    while True:
        print("\n------ MENU ------")
        print("1. Insert data")
        print("2. Update data")
        print("3. Show data")
        print("4. Delete data")
        print("5. Exit")
        choice = input("Enter choice (1-5): ")
        if choice == '1':
            insert_data(mycursor, mydb)
        elif choice == '2':
            update_data(mycursor, mydb)
        elif choice == '3':
            show_data(mycursor)
        elif choice == '4':
            delete_data(mycursor, mydb)
        elif choice == '5':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter 1-5.")
    mycursor.close()
    mydb.close()

if __name__ == "__main__":
    main()
