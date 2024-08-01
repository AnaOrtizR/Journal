from utils.BD_Connection import create_connection


def newDiary(connection, diaryName, passwd):
    if len(passwd) < 8: #Validación de largo de la contraseña
        print("La contraseña debe tener al menos 8 carácteres.")
    else: 
        query ="""
                INSERT INTO diary (diaryName, passwd)VALUES (%s, %s)
        """
        cursor = connection.cursor()
        cursor.execute(query,(diaryName, passwd))
        connection.commit()
        cursor.close()
        print("Exitoso")

def listDiary(connection):
    query ="""
            SELECT * FROM diary;
    """
    cursor = connection.cursor()
    cursor.execute(query)
    registros = cursor.fetchall()
    cursor.close()
    return registros

def searchDiary(connection,id):
    query = """
        SELECT * FROM diary WHERE id=%s;
    """
    cursor = connection.cursor()
    cursor.execute(query,(id,))
    registros = cursor.fetchone()
    cursor.close()
    return registros

def editDiaryName(connection,id, diaryName): 
    query = """
    UPDATE diary
    SET diaryName =%s
    WHERE id = %s;
    """
    cursor = connection.cursor()
    cursor.execute(query,(diaryName, id))
    connection.commit()
    cursor.close()
    return "Operación Exitosa"
    

def editDiaryPasswd(connection,id, passwd):
    if len(passwd) < 8:
        print("La contraseña debe tener al menos 8 carácteres.")
    else:  
        query = """
        UPDATE diary
        SET passwd =%s
        WHERE id = %s;
        """
        cursor = connection.cursor()
        cursor.execute(query,(passwd, id))
        connection.commit()
        cursor.close()
        return "Operación Exitosa"

def deleteDiary(connection,id):
    query = """
        DELETE FROM diary
        WHERE id = %s;
    """
    cursor = connection.cursor()
    cursor.execute(query,(id,))
    connection.commit()
    return "Operación Exitosa"
