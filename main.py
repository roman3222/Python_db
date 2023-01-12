import psycopg2

from add_values import add_client, add_info
from create_table import create_table
from delete import del_client, del_phone, del_email
from find import find_client
from update import update_client, update_info


with psycopg2.connect(database='python_db', user='postgres', password='') as conn:
    with conn.cursor() as curs:

        create_table(curs)
        add_client(curs)
        add_info(curs)
        update_client(curs)
        update_info(curs)
        del_client(curs)
        del_phone(curs)
        del_email(curs)
        find_client(curs)


    curs.close()




