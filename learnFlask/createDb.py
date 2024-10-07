import mysql.connector

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '@Dmin123',
}

db = mysql.connector.connect(**db_config)
cursor = db.cursor()

cursor.execute('Show databases')