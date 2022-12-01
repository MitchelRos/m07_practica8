import psycopg2

#Crea una conexio a la base de dades.
def conexio():
    connection = None
    try:
        # Si funciona conecta
        connection = psycopg2.connect(user="",
                                      password="",
                                      host="localhost",
                                      port="5432",
                                      database="bida")
    except:
        #Si falla mostra 'Problema de conexio'
        print("Problema en la conexio")
        
    return connection

