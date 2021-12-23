from utils import connect

def create_tables(conn):
    cursor = conn.cursor()
    cursor.execute('''DROP TABLE IF EXISTS usuarios''')
    cursor.execute('''CREATE TABLE usuarios(
        id INT NOT NULL,
        rol VARCHAR(255),
        PRIMARY KEY (id)
        )''')

    cursor.execute('''DROP TABLE IF EXISTS mensajes''')
    cursor.execute('''CREATE TABLE mensajes(
        id VARCHAR(255) NOT NULL,
        mensaje VARCHAR(2048),
        PRIMARY KEY (id)
        )''')

    cursor.execute('''DROP TABLE IF EXISTS valoraciones''')
    cursor.execute('''CREATE TABLE valoraciones(
        id INT NOT NULL,
        positivas INT,
        negativas INT,
        PRIMARY KEY (id)
        )''')
    conn.commit()

def create_users(conn):
    cursor = conn.cursor()
    cursor.execute('''DELETE FROM usuarios''')
    cursor.execute('''INSERT usuarios(id,rol) VALUES(207767757,"admin")''')
    cursor.execute('''INSERT usuarios(id,rol) VALUES(267547511,"alumno")''')
    cursor.execute('''INSERT usuarios(id,rol) VALUES(686981968,"alumno")''')
    cursor.execute('''INSERT valoraciones(id,positivas,negativas) VALUES(0,0,0)''')
    conn.commit()

if __name__ == '__main__':

    conn = connect()
    create_tables(conn)
    create_users(conn)
