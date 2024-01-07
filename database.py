import mysql.connector


def Database_Create():
    mydb = mysql.connector.connect(host="127.0.0.1", user="root", passwd="123sumit")
    Cursor = mydb.cursor()
    Cursor.execute("CREATE DATABASE IF NOT EXISTS Hospital")
    Cursor.close()
    mydb.close()


def Create_Table():
    mydb = mysql.connector.connect(
        host="127.0.0.1", user="root", passwd="123sumit", database="Hospital"
    )
    Cursor = mydb.cursor()
    Cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Patient(
            Patient_ID INT AUTO_INCREMENT PRIMARY KEY,
            room_id INT,
            Patient_Name VARCHAR(255),
            Patient_Address VARCHAR(255),
            Patient_Phone VARCHAR(255),
            Patient_Disease VARCHAR(255)
        )
    """
    )
    Cursor.close()
    mydb.close()
