import mysql.connector

conn = mysql.connector.connect(user='root', password='Jushank@2021',host='localhost',database='face_reco',port=3306)
cursor = conn.cursor()

cursor.execute("show databases")

data = cursor.fetchall()

print(data)

conn.close()