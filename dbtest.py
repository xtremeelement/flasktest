import mysql.connector
from datetime import datetime

db = mysql.connector.connect(
    host="localhost",
    user="root",
    database="postdb"
)

cursor = db.cursor(dictionary=True)

def getAll():
    cursor.execute("SELECT * FROM blog_post ORDER BY created_at DESC;")
    result = cursor.fetchall()
    return result
    
def create(title, content, author):
    date = datetime.utcnow()
    cursor.execute("INSERT INTO blog_post(title,content,author, created_at) VALUES(%s, %s, %s, %s)",(title, content, author, date))
    db.commit()