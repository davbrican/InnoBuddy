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
    
    cursor.execute('''DROP TABLE IF EXISTS eventos''')
    cursor.execute('''CREATE TABLE eventos(
        id BIGINT NOT NULL,
        titulo VARCHAR(1024),
        descripcion VARCHAR(2048),
        inicio DATETIME,
        fin DATETIME,
        PRIMARY KEY (id)
        )''')
    conn.commit()

    cursor.execute('''DROP TABLE IF EXISTS localizaciones''')
    cursor.execute('''CREATE TABLE localizaciones(
        aula VARCHAR(25) NOT NULL,
        ejex INT,
        ejey INT,
        PRIMARY KEY (aula)
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
    
def create_events(conn):
    cursor = conn.cursor()
    cursor.execute('''DELETE FROM eventos''')
    cursor.execute('''INSERT eventos(id,titulo,descripcion,inicio,fin) VALUES(232543201977,"Prueba","Aula A3.10\nSpeaker : Juanra", "2021-12-01T10:00:00", "2021-12-01T12:00:00")''')
    cursor.execute('''INSERT eventos(id,titulo,descripcion,inicio,fin) VALUES(232521435544,"Prueba2","Aula B1.35\nSpeaker : Jesús", "2021-12-26T10:00:00", "2021-12-25T12:00:00")''')
    cursor.execute('''INSERT eventos(id,titulo,descripcion,inicio,fin) VALUES(204365020277,"Lo que nadie me contó durante la universidad","Aula A3.10\nSpeaker : Alberto Fernández", "2021-12-02T10:00:00", "2021-12-02T12:00:00")''')
    conn.commit()

def create_localizaciones(conn):
    cursor = conn.cursor()
    cursor.execute('''DELETE FROM localizaciones''')
    cursor.execute('''INSERT localizaciones(aula,ejex,ejey) VALUES("A0.11", 386, 495)''')
    cursor.execute('''INSERT localizaciones(aula,ejex,ejey) VALUES("A0.30", 344, 495)''')
    cursor.execute('''INSERT localizaciones(aula,ejex,ejey) VALUES("A2.16", 213, 481)''')
    cursor.execute('''INSERT localizaciones(aula,ejex,ejey) VALUES("A3.10", 398, 457)''')
    cursor.execute('''INSERT localizaciones(aula,ejex,ejey) VALUES("A3.11", 298, 457)''')
    cursor.execute('''INSERT localizaciones(aula,ejex,ejey) VALUES("B1.34", 398, 365)''')
    cursor.execute('''INSERT localizaciones(aula,ejex,ejey) VALUES("B1.35", 418, 365)''')
    cursor.execute('''INSERT localizaciones(aula,ejex,ejey) VALUES("H0.12", 601, 441)''')
    cursor.execute('''INSERT localizaciones(aula,ejex,ejey) VALUES("H1.10", 524, 437)''')
    cursor.execute('''INSERT localizaciones(aula,ejex,ejey) VALUES("I2.35", 666, 583)''')
    conn.commit()

if __name__ == '__main__':

    conn = connect()
    create_tables(conn)
    create_users(conn)
    create_localizaciones(conn)
    create_events(conn)
