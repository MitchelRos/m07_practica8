import psycopg2

#Crea una conexio a la base de dades.
def conexio():
    connection = None
    try:
        # Si funciona conecta
        connection = psycopg2.connect(user="",
                                      password="",
                                      host="-1.amazonaws.com",
                                      port="5432",
                                      database="")
    except:
        #Si falla mostra 'Problema de conexio'
        print("Problema en la conexio")
    return connection

def crearTaula(name_Table):
    #Fa la conexio a la bbdd
    connection = conexio()
    #Ajuda a recorre la llista de elements
    cursor = connection.cursor()
    #Fa una query predefinida per a crear una taula
    sqlCreateTable = "create table " + name_Table + " (id bigint, title varchar(128), summary varchar(256), story text);"
    #Executa la sql
    cursor.execute(sqlCreateTable)
    connection.commit()


def insertar(nid, ntitle, nsummary, nstory):
    conn = conexio()
    #Ajuda a recorre la llista de elements
    cursor = conn.cursor()
    cursor.execute("INSERT INTO persona (id, title, summary, story) VALUES ({},{},{},{}); ".format(nid, ntitle, nsummary, nstory))
    cursor.close()
    conn.close()

def llegirTot():
    conn = conexio()
    #Ajuda a recorre la llista de elements
    cursor = conn.cursor()
    # cursor.execute("""SELECT * FROM information_schema.tables WHERE table_schema = 'public'""")
    cursor.execute("SELECT * FROM persona")
    for table in cursor.fetchall():
        print(table)

insertar(1,"pedro","lucas","jorge")