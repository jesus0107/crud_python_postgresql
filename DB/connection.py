from msilib.schema import Error
import psycopg2

class DAO:
    def __init__(self):
        try:
            conn = psycopg2.connect(
                user = 'postgres',
                password = 'fiona',
                host = 'localhost',
                port = '5432',
                database = 'people_db'
            )
        except Error as ve:
            print(f"Error: {ve}")
            
    def print_people(self):
        pass
# cursor = conn.cursor()
# sql_sentence = 'SELECT * FROM people'
# cursor.execute(sql_sentence)
# data = cursor.fetchall()

# print(data)

# cursor.close()
# conn.close()
# print('Se cerro la conexion')

