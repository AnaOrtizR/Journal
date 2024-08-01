from utils.BD_Connection import create_connection

def newEntry(connection, title, texto, diary_id):
        query ="""
                INSERT INTO entry (title, texto, datePosted, dateUpdated, diary_id)VALUES (%s, %s, now(), now(), %s)
        """
        cursor = connection.cursor()
        cursor.execute(query,(title, texto, diary_id))
        connection.commit()
        cursor.close()
        print("Exitoso")

def editEntryTitle(connection, id, title): 
    query = """
    UPDATE entry
    SET title =%s
    WHERE id = %s;
    """
    cursor = connection.cursor()
    cursor.execute(query,(title, id))
    connection.commit()
    cursor.close()
    return "Operación Exitosa"

def editEntryBody(connection, id, texto): 
    query = """
    UPDATE entry
    SET texto =%s
    WHERE id = %s;
    """
    cursor = connection.cursor()
    cursor.execute(query,(texto, id))
    connection.commit()
    cursor.close()
    return "Operación Exitosa"

def searchEntry(connection,id):
    query = """
        SELECT * FROM entry WHERE id=%s;
    """
    cursor = connection.cursor()
    cursor.execute(query,(id,))
    registros = cursor.fetchone()
    cursor.close()
    return registros

def searchEntryByWord(connection, word):
    query = """
        SELECT * FROM entry WHERE title LIKE %s;
    """
    cursor = connection.cursor()
    cursor.execute(query, ('%' + word + '%',))
    registros = cursor.fetchall()
    cursor.close()
    return registros

def searchEntryByDate(connection, datePosted):
    query = """
        SELECT title, texto, date(datePosted) FROM entry WHERE date(datePosted)=%s;
    """
    cursor = connection.cursor()
    cursor.execute(query, (datePosted,))
    registros = cursor.fetchall()
    cursor.close()
    return registros

def listEntries(connection):
    query ="""
            SELECT * FROM entry;
    """
    cursor = connection.cursor()
    cursor.execute(query)
    registros = cursor.fetchall()
    cursor.close()
    return registros

def listEntriesByDatePosted(connection):
    query ="""
            SELECT * FROM entry
            ORDER BY datePosted DESC;
    """
    cursor = connection.cursor()
    cursor.execute(query)
    registros = cursor.fetchall()
    cursor.close()
    return registros

def listEntriesByDateUpdated(connection):
    query ="""
            SELECT * FROM entry
            ORDER BY dateUpdated DESC;
    """
    cursor = connection.cursor()
    cursor.execute(query)
    registros = cursor.fetchall()
    cursor.close()
    return registros

def deleteEntry(connection,id):
    query = """
        DELETE FROM entry
        WHERE id = %s;
    """
    cursor = connection.cursor()
    cursor.execute(query,(id,))
    connection.commit()
    return "Operación Exitosa"
