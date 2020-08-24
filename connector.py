import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    database='Homework',
    user='root',
    password='Zhengnian13'
)
cursor = connection.cursor()

sql = """INSERT INTO Homework.Homework2 (Word, Count) VALUES (%s, %s)"""
temp = "Text"
counter = 3
val = (temp, counter)
cursor.execute(sql, val)
connection.commit()
cursor.close()