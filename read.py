from conection import conexio

def llegirTot():
    try:
        #Crida la funcio de conexio
        conn = conexio()
        #Ajuda a recorre la llista de elements
        cursor = conn.cursor()
        #Fa la query de seleccionar tots
        cursor.execute("SELECT * FROM alumne")
        #Fa print de tots els element
        for table in cursor.fetchall():
            print(table)
    except Exception:
        #Si no ho aconsegueix dona aquest error
        print("I can't do the query correctly")

llegirTot()