# b) As shown in the last 2 classes, install and import the module psycopg2.
# and write a Python function which connects to your database  playground
# with the default postgres user or by creating your own user.

# c) If you successfully confirmed your PostgreSQL version, create a new variable
# which contains an INSERT query so you manually execute and insert a new member to your members table.

# d) After this, load the previous json file back into your code insert every user to our database.
# If you successfully managed to do so,
# write a new function which executes the query SELECT COUNT(*) FROM MEMBERS
# and returns the fetched value in your terminal. It should be an integer.

from configparser import ConfigParser
from db_modules import db_module_pro
import psycopg2

if __name__ == '__main__':

    members_list = db_module_pro.read_jsonfile("selfdev_members.json")

    db_login_data = ConfigParser()
    db_login_data.read("database.ini")

    db_connection = None
    try:
        with psycopg2.connect (
            host=db_login_data.get('postgresql', 'host'),
            dbname=db_login_data.get('postgresql', 'database'),
            user=db_login_data.get('postgresql', 'user'),
            password=db_login_data.get('postgresql', 'password'),
            port=db_login_data.getint('postgresql', 'port')
                                ) as db_connection:

            with db_connection.cursor() as db_cursor:

                db_cursor.execute('DROP TABLE IF EXISTS members')

                create_script = """ CREATE TABLE IF NOT EXISTS members (
                                        name                text,
                                        discord_name        text,
                                        reason_to_code      text,
                                        addicted_to         text)"""

                db_cursor.execute(create_script)


                # task 12/c
                postgresql_version = """ SELECT version()"""
                db_cursor.execute(postgresql_version)
                print([x for x in db_cursor])

                # task 12/c
                insert_members = 'INSERT INTO members (name, discord_name, reason_to_code, addicted_to) VALUES (%s,%s,%s,%s)'
                for values_in_members_list in members_list:
                    db_cursor.execute(insert_members, values_in_members_list)

                db_cursor.execute('SELECT COUNT(*) FROM members')
                print([x[0] for x in db_cursor])

    except Exception as error:
        print(error)
    finally:
        if db_connection is not None:
            db_connection.close()


