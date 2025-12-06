import pymysql

# Step-2 connect Database
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    database="test",
    cursorclass=pymysql.cursors.DictCursor
)

try:
    with connection.cursor() as cursor:

        # CREATE TABLE
        create_query = """
        CREATE TABLE IF NOT EXISTS employees(
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            department VARCHAR(100)
        )
        """
        cursor.execute(create_query)

        # INSERT DATA
        insert_query = "INSERT INTO employees (name, department) VALUES (%s, %s)"
        values = [("Johnson", "ELE"), ("Sumathi", "HW"), ("Akash", "CA")]
        cursor.executemany(insert_query, values)
        connection.commit()

        # SELECT DATA
        select_query = "SELECT * FROM employees"
        cursor.execute(select_query)
        result = cursor.fetchall()

        with open("python_file_handling/employees.txt", "w") as file:
            for row in result:
                file.write(f"{row}\n")
                print(row)



finally:
    connection.close()