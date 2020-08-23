import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    database="postdb"
)

cursor = db.cursor(dictionary=True)

def getAll():
    cursor.execute("SELECT * FROM blog_post")
    result = cursor.fetchall()
    return result
    
def create(title, content, author):
    cursor.execute("INSERT INTO blog_post(title,content,author) VALUES(%s, %s, %s)",(title, content, author))
    db.commit()