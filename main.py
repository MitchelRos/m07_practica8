import psycopg2


connection = psycopg2.connect(user="postgres",
                                  password="postgres",
                                  host="192.168.159.128",
                                  port="8080",
                                  database="template1")
cursor = connection.cursor()

postgreSQL_select_Query = "select * from personas"

cursor.execute(postgreSQL_select_Query)
