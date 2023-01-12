

def create_table(curs):
    curs.execute("""
    CREATE TABLE IF NOT EXISTS client (
        id SERIAL PRIMARY KEY,
        name VARCHAR(30) NOT NULL,
        surname VARCHAR(30) NOT NULL
    );
    """)
    curs.execute("""
    CREATE TABLE IF NOT EXISTS info_client(
        id SERIAL PRIMARY KEY,
        phone VARCHAR(20) UNIQUE NULL,
        email VARCHAR(30) UNIQUE NULL,
        client_id INT REFERENCES client(id)   
    );
    """)