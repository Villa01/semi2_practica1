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
    original_query = """
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
    batch_size = 50
    batch_count = 1
    sql_values = ()
    i = 0
    query = original_query
    errors = 0
    for value in values:
        if i == batch_size:
            batch_count += 1
            query = query[:-2] + ';'
            try:
                cursor = db_conn.cursor()
                cursor.execute(query % sql_values)
            except Exception as e:
                errors += 1
                print(query % sql_values)
                print(f'Could not load data into Temporal table: {e}')
            else:
                cursor.close()
            query = original_query
            sql_values = ()
            i = 0

        query += """('%s','%s',%i,%r,%i,%f,%f,%f,%i,%f,%f,%f,%f,%f,%f,%f,%f,'%s'),\n"""
        sql_values += (value.artist, value.song, value.duration_ms, value.explicit, value.year, value.popularity,
                       value.danceability, value.energy, value.key, value.loudness, value.mode, value.speechiness,
                       value.acousticness, value.instrumentalness, value.liveness, value.valence, value.tempo,
                       value.genre)
        i += 1

    db_conn.commit()
    return f'Inserted {batch_count} batches, error #: {errors}'
