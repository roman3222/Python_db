
def add_client(curs, name_client, surname_client):
    curs.execute("""
           INSERT INTO client (name, surname)
           VALUES (%s, %s);""", (name_client, surname_client))
    # print(curs.fetchall())


def add_info(curs, client_id, phone_client=None, email_client=None):
    curs.execute("""
           INSERT INTO info_client (client_id, phone, email)
           VALUES (%s, %s, %s);""", (client_id, phone_client, email_client))
    # print(curs.fetchall())