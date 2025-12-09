import sqlite3

# connect to database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    course TEXT
)
""")
conn.commit()


def add_student(name, email, course):
    cursor.execute("INSERT INTO students (name, email, course) VALUES (?, ?, ?)", 
                   (name, email, course))
    conn.commit()
    print("Student Added Successfully!")


def view_students():
    cursor.execute("SELECT * FROM students")
    for row in cursor.fetchall():
        print(row)


def update_student(id, name, email, course):
    cursor.execute("""
    UPDATE students 
    SET name=?, email=?, course=?
    WHERE id=?
    """, (name, email, course, id))
    conn.commit()
    print("Student Updated Successfully!")


def delete_student(id):
    cursor.execute("DELETE FROM students WHERE id=?", (id,))
    conn.commit()
    print("Student Deleted Successfully!")


# simple menu
while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Name: ")
        email = input("Email: ")
        course = input("Course: ")
        add_student(name, email, course)

    elif choice == "2":
        view_students()

    elif choice == "3":
        sid = input("Student ID to update: ")
        name = input("New Name: ")
        email = input("New Email: ")
        course = input("New Course: ")
        update_student(sid, name, email, course)

    elif choice == "4":
        sid = input("Student ID to delete: ")
        delete_student(sid)

    elif choice == "5":
        print("Bye!")
        break

    else:
        print("Invalid choice")
