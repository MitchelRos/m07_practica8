# establece conexion importando de connection la fun conexio
from conection import conexio

# hacemos la variable inser donde se tiene que introducir los datos de value
def update(name, surname, age, id):
    # si el try falla llamara a exeption que imprimira ayuda + Exeption
    try:
        # establecemos en variables la funcion cenexio...
        conn = conexio()
        # la funcion conn.cursor la guradamos en cursor 
        # (se utiliza para las conecciones de base de datos este recibira informacion de ella o la llamara)
        cursor = conn.cursor()
        # en query insertamos la linea que se ejecutara a la base de datos
        query = "UPDATE alumne SET name = %s, surname = %s, age = %s WHERE id = %s;"
        # Esto ejecutara y enviara los resultados del resultado
        cursor.execute(query,(name, surname, age, id))
        conn.commit()
        # Con los comando siguiente cerramos la consulta con la bease de datos
        cursor.close()
        conn.close()
    except Exception:
        print("ayuda: ",Exception)

# Iniciamos al funcion con los datos que se necesita
update("melooo","cotoooon",22,2)