#llama el archivo python que es el connection.py
from connection import conexio

def deletepy(nId):
    #Si connecta la BBDD retorna que s'ha eliminat sino retornara un error de que no es pot borrar
    try:
        #Truca la funcio connection.py que ho importa
        conn = connexio()
        cur= conn.cursor()
        #executara la query
        cur.execute("DELETE FROM ALUMNE where id = %s", (nid,))
        conn.commit()
        cur.close()
        print("Deleted "+str(nid))
    except:
        print("No s'ha pogut boorrar")
#Truca la funcio i les pasa les funcions de la id del alumne
deletepy(10)
deletepy(11)
deletepy(12)