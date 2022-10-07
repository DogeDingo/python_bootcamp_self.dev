import psycopg2
from db_modules import db_module_pro
from db_modules.db_module_pro import hostname

if __name__ == '__main__':
    with psycopg2.connect(
                host=db_module_pro.hostname,
                dbname=db_module_pro.database,
                user=db_module_pro.username,
                password=db_module_pro.pwd,
                port=db_module_pro.port_id
                            ) as db_connector:

        with db_connector.cursor() as db_cursor:
                pass #remove pass and write your PostgreSQL here




    db_connector.close()


