import pymysql
import os
from queries import DROP_TABLES, CREATE_TABLES, INSERT_DATA, QUERY_DATA

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
    queries = DROP_TABLES.split(';')
    errors = execute_queries(db_conn, queries)
    return queries, errors


def create_tables(db_conn):
    queries = CREATE_TABLES.split(';')
    errors = execute_queries(db_conn, queries)
    return queries, errors


def query_er(db_conn):
    queries = QUERY_DATA.split(';')[:-1]
    errors, results = execute_queries(db_conn, queries, True)
    return errors, results, queries


def execute_queries(db_conn, queries, fetch=None):
    errors = []
    results = []
    for q in queries:
        error, result = execute_query(db_conn, q, fetch)
        if error:
            errors.append(result)
            continue
        results.append(result)
    db_conn.commit()
    return errors, results


def execute_query(db_conn, query, fetch=False):
    try:
        cursor = db_conn.cursor()
        if fetch:
            cursor.execute(query)
            result = cursor.fetchall()
            print(cursor.description)
        else:
            result = cursor.execute(query)
    except Exception as e:
        return True, f'Could not perform {query}\n{e}'
    else:
        cursor.close()

    return False, result


def fill_er(db_conn):
    queries = INSERT_DATA.split(';')
    errors = execute_queries(db_conn, queries)
    return queries, errors


def fill_temporal(db_conn, values):
    original_query = """
    USE `practica1`;
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
    batch_size = 500
    batch_count = 0
    sql_values = ()
    count = 0
    i = 0
    query = original_query
    errors = 0
    values_list = list(values)
    max_length = len(values_list)
    for value in values_list:
        i += 1
        if i >= batch_size or count + i >= max_length - 1:
            query = query[:-2] + ';'
            queries = (query % sql_values).split(';')[:-1]
            err, queries = execute_queries(db_conn, queries)
            count += i
            batch_count += 1
            errors += len(err)
            query = original_query
            sql_values = ()
            i = 0

        query += """('%s','%s',%i,%r,%i,%f,%f,%f,%i,%f,%f,%f,%f,%f,%f,%f,%f,'%s'),\n"""
        sql_values += (value.artist, value.song, value.duration_ms, value.explicit, value.year, value.popularity,
                       value.danceability, value.energy, value.key, value.loudness, value.mode, value.speechiness,
                       value.acousticness, value.instrumentalness, value.liveness, value.valence, value.tempo,
                       value.genre)

    db_conn.commit()
    return f'Inserted {count} registries in {batch_count} batches, error #: {errors}'
