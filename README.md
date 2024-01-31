# Data_Collection
 
 Description: 
 This Python script enables users to fetch data from specified tables in one or more SQLite databases, sort the combined data alphabetically based on a chosen column, and store the sorted data into a CSV file. Additionally, it provides an option to automatically open the output file based on the user's operating system.

About:
- fetch_data_from_database : A function to fetch data from specified tables in an SQLite database.
- sort_and_store : A function to sort data alphabetically based on a chosen column and store it in a CSV file.
- open_output_file : A function to automatically open the output file based on the user's operating system.
- Main : The main part of the script where the user inputs database paths, tables to access, and column for sorting.

Note:
- Ensure that the SQLite databases exist at the specified paths.
- The output file will be automatically opened after processing.