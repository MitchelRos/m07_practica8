# establece conexion importando de connection la fun conexio
from conection import conexio

# hacemos la variable inser donde se tiene que introducir los datos de value
def insert(name, surname, age):
    # si el try falla llamara a exeption que imprimira ayuda + Exeption
    try:
        # establecemos en variables la funcion cenexio...
        conn = conexio()
        # la funcion conn.cursor la guradamos en cursor 
        # (se utiliza para las conecciones de base de datos este recibira informacion de ella o la llamara)
        cursor = conn.cursor()
        # en query insertamos la linea que se ejecutara a la base de datos
        query = "INSERT INTO alumne (name, surname, age) VALUES (%s, %s, %s)"
        # Esto ejecutara y enviara los resultados del resultado
        cursor.execute(query,(name, surname, age))
        conn.commit()
        # Con los comando siguiente cerramos la consulta con la bease de datos
        cursor.close()
        conn.close()
    except Exception:
        print("ayuda: "+Exception)

# Iniciamos al funcion con los datos que se necesita
insert("melo","coton",22)