import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = '2002'
DATABASE = 'ibam'

#Coneection à la BD



try:
    connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
    print("connection reussie!!")
except psycopg2.Error as e:
    print("connection refusé veillez verifir les paramettre de connection!!")

#Creation de la table student
cursor = connection.cursor()
#cursor.execute("CREATE TABLE student (name VARCHAR(255), firstname VARCHAR(255), phone VARCHAR(255), address VARCHAR(255));")

#Lecture ds données

sql1 = "SELECT * FROM student;"
cursor.execute(sql1)
#cursor.fetchall()
for data in cursor.fetchall():
    print(data)



