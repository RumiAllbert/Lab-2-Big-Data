import mysql.connector
import sys
 
wordcount = {}
 
for line in sys.stdin:
    line = line.strip()

    word, count = line.split('\t', 1)

    try:
        count = int(count)
    except ValueError:
        continue
 
    try:
        wordcount[word] = wordcount[word]+count
    except:
        wordcount[word] = count

connection = mysql.connector.connect(
    host='localhost',
    database='Homework',
    user='root',
    password='Zhengnian13'
)
cursor = connection.cursor()

def inserttosql (Word, Count):
    sql = """INSERT INTO Homework2 (Word, Count) VALUES (%s, %s)""" 
    val = (Word, Count)
    cursor.execute(sql)
    connection.commit()

for word in wordcount.keys():
    inserttosql(str(word), int(wordcount[word]))
    print('%s\t%s' % ( word, wordcount[word]))

cursor.close()

print("\nData succesfully loaded to your SQL Database")


