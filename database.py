import pymysql
import os
from creation import DROP_TABLES, tables_to_create

mysql_config = {
    'HOST': os.environ.get('HOST'),
    'USER': os.environ.get('USER'),
    'PASS': os.environ.get('PASS'),
    'DATABASE': os.environ.get('DATABASE')
}


def get_connection():
    my_conn = None
    try:
        my_conn = pymysql.connect(
            host=mysql_config['HOST'],
            user=mysql_config['USER'],
            password=mysql_config['PASS'],
            database=mysql_config['DATABASE']
        )
        my_conn.mysql_config = mysql_config

    except Exception as err:
        print(f'Could not connect to database: {err}')
    return my_conn


def drop_all_tables(db_conn):
    cursor = db_conn.cursor()
    cursor.execute(DROP_TABLES)


def create_tables(db_conn):
    query = ''
    for table in tables_to_create:
        query += table
    try:
        cursor = db_conn.cursor()
        cursor.execute(query)
    except Exception as e:
        print(f'Could not connect to database: {e}')
    else:
        cursor.close()


def fill_temporal(db_conn, values):
    query = """
    INSERT INTO `practica1`.`temporal`
    (`artist`,
    `song`,
    `duration_ms`,
    `explicit`,
    `year`,
    `popularity`,
    `danceability`,
    `energy`,
    `llave`,
    `loudness`,
    `mode`,
    `speechiness`,
    `acousticness`,
    `instrumentalness`,
    `liveness`,
    `valence`,
    `tempo`,
    `genre`)
    VALUES
    """
    sql_values = []
    for value in values:
        query += """(%s,%s,%i,%r,%i,%f,%f,%f, %i,%f,%f,%f,%f,%f,%f,%f,%f,%s)"""
        sql_values.append(value)

    print(query)
    print(sql_values)