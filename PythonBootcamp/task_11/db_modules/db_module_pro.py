import json

# my credentials
hostname = 'localhost'
database = 'playground'
username = 'postgres'
pwd = 'jonnyssecret'
port_id = 5432


# function to create a table in PostgreSQL with user input
def create_table():
    name_table = input("Please name your table: ")
    number_columns = input("How many columns do you need? ")
    list_columns = []
    list_records = []
    number_index = 1
    while number_index <= int(number_columns):
        list_columns.append(input(f"Column Number {number_index} name please: "))

        list_records.append(input(f"Please enter datatype (please be very specific - e.g. if you use varchar() please also put a number into the brackets: "))
        number_index += 1

    lists_records = []
    for column_name, column_type in zip(list_columns, list_records):
        string_placeholder = f"{column_name} {column_type}"
        lists_records.append(string_placeholder)

    records_printed = (" ,".join(lists_records))
    create_script = f'''CREATE TABLE IF NOT EXISTS {name_table} (
                          {records_printed})
                          '''
    return create_script




