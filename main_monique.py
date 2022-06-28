import mysql.connector

cnx = mysql.connector.connect(user='root',
                              password='gweelos18',
                              host='127.0.0.1',
                              database='employees')

cursor = cnx.cursor()

INSERT_ALUNO = """INSERT INTO aluno (nome) value ('Monique');"""

cursor.execute(INSERT_ALUNO)

cnx.commit()

cursor.close
cnx.close()
