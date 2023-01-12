
def del_client(curs, id_client):
    curs.execute("""
           DELETE FROM client WHERE id=%s;
           """, (curs, id_client,))


def del_phone(curs, id_client, id_info):
    curs.execute("""
           UPDATE info_client SET phone=NULL WHERE client_id=%s AND id=%s;
           """, (id_client, id_info))


def del_email(curs, id_client, id_info):
    curs.execute("""
           UPDATE info_client SET email=NULL WHERE client_id=%s AND id=%s;
           """, (id_client, id_info))
