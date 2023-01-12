def update_client(curs, id_client, name_client=None, surname_client=None):
    sql = 'UPDATE client SET'
    if name_client:
        sql += ' name=%s,'
    if surname_client:
        sql += ' surname=%s,'
    sql = sql[:-1] + ' WHERE id=%s;'
    data = []
    if name_client:
        data.append(name_client)
    if surname_client:
        data.append(surname_client)
    data.append(id_client)
    curs.execute(sql, data)


def update_info(curs, id_info, id_client, phone=None, email=None):
    upd = 'UPDATE info_client SET'
    if phone:
        upd += ' phone=%s,'
    if email:
        upd += ' email=%s,'
    upd = upd[:-1] + ' WHERE id=%s AND client_id=%s;'
    data = []
    if phone:
        data.append(phone)
    if email:
        data.append(email)
    data.append(id_info)
    data.append(id_client)
    curs.execute(upd, data)
