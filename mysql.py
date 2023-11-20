from time import sleep
import pymysql
import os as o

def clear():
    print(o.name)
    if (o.name == "posix"):
        o.system('clear')
    else:
        o.system('cls')

connection = pymysql.connect(
    host='localhost',
    user='system',
    password='gowdaman',
    database='college'
)
def create_table():
    try:
        with connection.cursor() as cursor:
            sql = """
            CREATE TABLE IF NOT EXISTS student (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                age INT
            )
            """
            cursor.execute(sql)
            print("Table created successfully (if it didn't exist)!")
    except Exception as e:
        print(f"Error creating table: {e}")
def create_student(name, email, age):
    try:
        with connection.cursor() as cursor:
            create_table()
            sql = "INSERT INTO student (name, email, age) VALUES (%s, %s, %s)"
            cursor.execute(sql, (name, email, age))
            connection.commit()
            print("student created successfully!")
    except Exception as e:
        print(f"Error creating student: {e}")
def read_student():
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM student"
            cursor.execute(sql)
            result = cursor.fetchall()
            for row in result:
                print(row)
    except Exception as e:
        print(f"Error reading student: {e}")

def update_student(student_id, new_age):
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE student SET age = %s WHERE id = %s"
            cursor.execute(sql, (new_age, student_id))
            connection.commit()
            print("student updated successfully!")
    except Exception as e:
        print(f"Error updating student: {e}")

def delete_student(student_id):
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM student WHERE id = %s"
            cursor.execute(sql, (student_id,))
            connection.commit()
            print("student deleted successfully!")
    except Exception as e:
        print(f"Error deleting student: {e}")

def temp(title):
    print("==============================")
    print(title)
    print("==============================")

def menulogo():
    print("==============================")
    print("Mysql college crud application")
    print("==============================")
    print("1> Create Record")
    print("2> Read Record")
    print("3> Delete Record")
    print("0> Exit CRUD APP")

if __name__ == "__main__":
    while 1 :
        menulogo()
        option = input("Select menu >>")
        if (option == "1"):
            name = input('Enter name : ')
            email = input('Enter Email : ')
            age = input('Enter age : ')
            create_student(name , email , age)
            clear()
            temp('Data added in database')
            sleep(2)
            clear()
            continue
        if (option == "2"):
            clear()
            read_student()
        if (option == "3"):
            clear()
            idno = input('Enter student id :')
            newage = input('Enter new age:')
            update_student(idno , newage)
            clear()
            temp(f'Student id {idno} is updated')
            sleep(2)
            clear()
            continue
        if (option == "0"):
            clear()
            temp("Leaving Crud app")
            break