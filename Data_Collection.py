import sqlite3
import csv
import os
import platform

def fetch_data_from_database(database):
    # Getting list of tables to fetch from database
    table_to_access = []
    file_name = os.path.basename(database) #filename for database
    while True:
        table_name = input("Enter tables to access in " + file_name + " (or 'done' to finish): : ")
        if table_name == "done":
            break
        table_to_access.append(table_name)

    # Connecting to the database passed by the user
    connection = sqlite3.connect(database)
    # Creating a cursor
    cursor = connection.cursor()
    
    # Fetch data from each specified table
    table_data = []
    for table_name in table_to_access:
        query = f"SELECT * FROM {table_name}"
        cursor.execute(query)
        data = cursor.fetchall()
        table_data.extend(data)

    # Close cursor and connection to database
    cursor.close()
    connection.close()
    return table_data

def sort_and_store(table_data, file_path):
    # Sorting data alphabetically based on the second column
    sorted_combined_data = sorted(table_data, key=lambda x: x[1]) #change x[] to adjust the column to alphabetize

    # Store data into a file
    with open(file_path, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(sorted_combined_data)

def open_output_file(file_path):
    if platform.system() == 'Windows':
        os.startfile(file_path)
    elif platform.system() == 'Darwin':
        os.system(f'open {file_path}')
    elif platform.system() == 'Linux':
        os.system(f'xdg-open {file_path}')
    else:
        print("Error, unable to open file automatically")

def main():
    #database_paths = ['/Users/jacobmartin/Documents/Code/DataCollection/wwe_db.sqlite']    
    database_paths = []
    # Get databases from user
    while True:
        name = input("Enter path to databases (or 'done' to finish): ")
        if name.lower() == "done":
            break
        database_paths.append(name)

    # Fetch data from each database
    combined_data = []
    for database in database_paths:
        data = fetch_data_from_database(database)
        combined_data.extend(data)
    
    # Store the sorted data into a file
    sort_and_store(combined_data, 'output_file.csv')

    # Automatically open 'output_file.csv'
    open_output_file('output_file.csv')

if __name__ == "__main__":
    main()