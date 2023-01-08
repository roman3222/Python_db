import psycopg2

with psycopg2.connect(database='python_db', user='postgres', password='') as conn:
    with conn.cursor() as curs:
        def create_table():
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
            conn.commit()


        def add_client(name_client, surname_client):
            curs.execute("""
            INSERT INTO client (name, surname)
            VALUES (%s, %s);""", (name_client, surname_client))
            curs.execute("""
            SELECT * FROM client;
            """)
            conn.commit()


        def add_info(client_id, phone_client=None, email_client=None):
            curs.execute("""
            INSERT INTO info_client (client_id, phone, email)
            VALUES (%s, %s, %s);""", (client_id, phone_client, email_client))
            curs.execute("""
            SELECT * FROM info_client;
            """)
            print(curs.fetchall())


        def update_client(id_client, name_client=None, surname_client=None):
            curs.execute("""
            UPDATE client SET name=%s, surname=%s WHERE id=%s;
            """, (id_client, name_client, surname_client))
            curs.execute("""
            SELECT * FROM client;
            """)
            print(curs.fetchall())


        def update_info(info_id, phone=None, email=None):
            curs.execute("""
            UPDATE info_client SET phone=%s, email=%s WHERE id=%s;
            """, (phone, email, info_id))
            curs.execute("""
            SELECT * FROM info_client;
            """)
            print(curs.fetchall())


        def del_client(id_client):
            curs.execute("""
            DELETE FROM client WHERE id=%s;
            """, (id_client,))
            conn.commit()


        def del_phone(id_client, id_info):
            curs.execute("""
            UPDATE info_client SET phone=NULL WHERE client_id=%s AND id=%s;
            """, (id_client, id_info))
            conn.commit()


        def del_email(id_client, id_info):
            curs.execute("""
            UPDATE info_client SET email=NULL WHERE client_id=%s AND id=%s;
            """, (id_client, id_info))
            conn.commit()

       
        def find_client(name=None, surname=None, phone=None, email=None):
            curs.execute("""
            SELECT client name, surname FROM client
            JOIN info_client  ON client.id = info_client.client_id 
            WHERE name=%s OR surname=%s OR phone=%s OR email=%s;
            """, (name, surname, phone, email))
            print(curs.fetchall())


        create_table()
        add_client()
        add_info()
        update_client()
        update_info()
        del_phone()
        del_phone()
        find_client()
    curs.close()




