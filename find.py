

def find_client(curs, name=None, surname=None, phone=None, email=None):
    # building a dynamic SQL statement
    sql = "SELECT client.id, client.name, client.surname FROM client " \
          "LEFT JOIN info_client ON info_client.client_id = client.id WHERE"
    data = []
    if name:
        sql += " name=%s AND"
        data.append(name)
    if surname:
        sql += " surname=%s AND"
        data.append(surname)
    if phone:
        sql += " phone=%s AND"
        data.append(phone)
    if email:
        sql += " email=%s AND"
        data.append(email)
    sql = sql[:-4]
    curs.execute(sql, data)
    print(curs.fetchall())