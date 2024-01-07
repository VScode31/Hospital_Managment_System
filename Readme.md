# Hospital Management System

## Overview

The Hospital Management System is a command-line project built using Python and MySQL. It allows users to manage patient information within a hospital setting, providing functionalities such as adding patients, searching for patients, discharging patients, and viewing patient details.

## Features

- **Add Patient:** Enter patient details, including room ID, name, address, phone, and disease, to add a new patient to the system.

- **Search Patient:** Search for a patient using their room ID and view their details.

- **Discharge Patient:** Remove a patient from the system based on their room ID.

- **View Patient Details:** Display details of all patients currently stored in the system.

- **Exit:** Close the program.

## Database Setup

The system utilizes MySQL as its database backend. The database setup is handled by the `database.py` script, creating a database named `Hospital` and a table named `Patient` to store patient information.

## Methods Overview

Here's an overview of the methods used in the project:

| Method                              | Description                                                                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `initialize_database()`             | Initializes the database by creating the `Hospital` database and the `Patient` table using the `Database_Create()` and `Create_Table()` functions.        |
| `add_patient()`                     | Allows the user to add a new patient to the system by entering patient details.                                                                             |
| `search_patient()`                  | Enables the user to search for a patient based on their room ID and view their details.                                                                     |
| `discharge_patient()`               | Removes a patient from the system based on their room ID.                                                                                                   |
| `patient_details()`                 | Displays details of all patients currently stored in the system.                                                                                            |
| `exit_program()`                    | Exits the Hospital Management System.                                                                                                                      |
| `Database_Create()`                 | Custom function to create the `Hospital` database if it doesn't exist.                                                                                      |
| `Create_Table()`                    | Custom function to create the `Patient` table if it doesn't exist.                                                                                          |
| `mysql.connector.connect()`         | Establishes a connection to the MySQL database. Requires parameters such as `host`, `user`, `passwd`, and optionally `database`.                           |
| `mydb.cursor()`                     | Creates a new cursor object for executing SQL statements.                                                                                                   |
| `Cursor.execute(query, data)`       | Executes a SQL query. `query` is the SQL statement, and `data` is a tuple containing values to be substituted into the query.                                  |
| `Cursor.fetchone()`                 | Retrieves the next row of the result set as a tuple. Returns `None` if there are no more rows to fetch.                                                     |
| `Cursor.fetchall()`                 | Retrieves all rows of the result set as a list of tuples. It fetches all remaining rows after the last call to `fetchone`.                                    |
| `mydb.commit()`                     | Commits the current transaction. Necessary when changes (e.g., INSERT, UPDATE, DELETE) are made to the database to persist those changes.                    |
| `Cursor.close()`                     | Closes the cursor. It's good practice to close the cursor when it's no longer needed to free up resources.                                                |
| `mydb.close()`                       | Closes the database connection. Essential to close the connection when it's no longer needed.                                                               |

## Installation

1. Clone the repository to your local machine:

   ```bash
   https://github.com/VScode31/Hospital_Managment_System.git
