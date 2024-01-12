from database import *


def initialize_database():
    Database_Create()
    Create_Table()


def add_patient():
    room_id = int(input("Enter Room ID: "))
    patient_name = input("Enter Patient Name: ")
    patient_address = input("Enter Patient Address: ")
    patient_phone = input("Enter Patient Phone: ")
    patient_disease = input("Enter Patient Disease: ")

    mydb = mysql.connector.connect(
        host="127.0.0.1", user="root", passwd="123sumit", database="Hospital"
    )
    Cursor = mydb.cursor()
    query = """
        INSERT INTO Patient (room_id, Patient_Name, Patient_Address, Patient_Phone, Patient_Disease)
        VALUES (%s, %s, %s, %s, %s)
    """
    data = (room_id, patient_name, patient_address, patient_phone, patient_disease)
    Cursor.execute(query, data)
    mydb.commit()
    Cursor.close()
    mydb.close()


def search_patient():
    room_id = int(input("Enter Room ID to search: "))

    mydb = mysql.connector.connect(
        host="127.0.0.1", user="root", passwd="123sumit", database="Hospital"
    )
    Cursor = mydb.cursor()
    query = "SELECT * FROM Patient WHERE room_id = %s"
    data = (room_id,)
    print("Searching for patient...")
    Cursor.execute(query, data)
    result = Cursor.fetchone()

    if result:
        print("Patient Details:")
        print(f"Patient ID: {result[0]}")
        print(f"Room ID: {result[1]}")
        print(f"Name: {result[2]}")
        print(f"Address: {result[3]}")
        print(f"Phone: {result[4]}")
        print(f"Disease: {result[5]}")
    else:
        print("Patient not found.")

    Cursor.close()
    mydb.close()


def discharge_patient():
    room_id = int(input("Enter Room ID to discharge: "))

    mydb = mysql.connector.connect(
        host="127.0.0.1", user="root", passwd="123sumit", database="Hospital"
    )
    Cursor = mydb.cursor()

    query_check = "SELECT * FROM Patient WHERE room_id = %s"
    data_check = (room_id,)
    Cursor.execute(query_check, data_check)
    result_check = Cursor.fetchone()

    if result_check:
        query_discharge = "DELETE FROM Patient WHERE room_id = %s"
        data_discharge = (room_id,)
        Cursor.execute(query_discharge, data_discharge)
        mydb.commit()

        if Cursor.rowcount > 0:
            print("Patient discharged successfully!")
        else:
            print("Error discharging patient.")
    else:
        print("Patient not found.")

    Cursor.close()
    mydb.close()


def patient_details():
    mydb = mysql.connector.connect(
        host="127.0.0.1", user="root", passwd="123sumit", database="Hospital"
    )
    Cursor = mydb.cursor()
    Cursor.execute("SELECT * FROM Patient")
    results = Cursor.fetchall()

    if results:
        print("Patient Details:")
        for result in results:
            print(
                f"Patient ID: {result[0]}, Room ID: {result[1]}, Name: {result[2]}, Address: {result[3]}, Phone: {result[4]}, Disease: {result[5]}"
            )
    else:
        print("No patients in the database.")

    Cursor.close()
    mydb.close()


def exit_program():
    print("Exiting Hospital Management System. Goodbye!")
    exit()


def main_menu():
    while True:
        print("\n=== Hospital Management System ===")
        print("1. Add Patient")
        print("2. Search Patient")
        print("3. Discharge Patient")
        print("4. View Patient Details")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_patient()
        elif choice == "2":
            search_patient()
        elif choice == "3":
            discharge_patient()
        elif choice == "4":
            patient_details()
        elif choice == "5":
            exit_program()
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    initialize_database()  # Initialize the database before starting the program
    main_menu()
