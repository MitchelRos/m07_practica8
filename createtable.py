from conection import conexio

def crearTaula(name_Table):
    #Fa la conexio a la bbdd
    connection = conexio()
    #Ajuda a recorre la llista de elements
    cursor = connection.cursor()
    #Fa una query predefinida per a crear una taula
    sqlCreateTable = "create table " + name_Table + " (id bigint, name varchar(128), surname varchar(256), age bigint);"
    #Executa la sql
    cursor.execute(sqlCreateTable)
    connection.commit()

crearTaula("alumne")