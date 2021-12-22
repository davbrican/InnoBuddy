from utils import connect

def create_tables(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE usuarios(
        id INT NOT NULL,
        rol VARCHAR(255),
        PRIMARY KEY (id)
        )''')
    cursor.execute('''CREATE TABLE mensajes(
        id VARCHAR(255) NOT NULL,
        mensaje VARCHAR(2048),
        PRIMARY KEY (id)
        )''')
    cursor.execute('''CREATE TABLE valoraciones(
        id INT NOT NULL,
        positivas INT,
        negativas INT,
        PRIMARY KEY (id)
        )''')
    conn.commit()

if __name__ == '__main__':

    conn = connect()
    create_tables(conn)
