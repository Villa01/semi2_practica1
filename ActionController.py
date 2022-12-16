import logging

from dataProcessing import temporal_data_process
from database import get_connection, drop_all_tables, create_tables, fill_temporal, fill_er, query_er


class ActionController:

    def __init__(self, logs='logs.log', silent=False):
        self.conn = None
        self.logs = logs
        self.silent = silent
        if self.logs:
            self.logger = self.configure_logging()

        self.conn = self.set_up_connection()

    def print_handler(self, message, internal=False, logs=True):
        if self.logs and logs:
            self.logger.info(message)

        if not (self.silent or internal):
            print('\033[94m ## ' + message + '\033[0m')

    def configure_logging(self):
        logger = logging.getLogger('SEMI2_PRACTICA1')
        logger.setLevel(logging.DEBUG)
        ch = logging.FileHandler(self.logs)
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        logger.addHandler(ch)
        return logger

    def set_up_connection(self):
        self.print_handler("Setting things up")
        conn = get_connection()
        self.print_handler(f'Database server information: {conn.mysql_config}', internal=True)
        return conn

    def create(self):

        self.print_handler('Starting process')

        self.print_handler('Deleting tables')
        queries, errors = drop_all_tables(self.conn)
        for q in queries:
            self.print_handler(f'Query performed: {q}')

        for e in errors:
            self.print_handler(f'Errors in queries: {e}')

        self.print_handler('Tables deleted')

        self.print_handler('Creating tables')
        queries, errors = create_tables(self.conn)
        for q in queries:
            self.print_handler(f'Query performed: {q}')

        for e in errors:
            self.print_handler(f'Errors in queries: {e}')
        self.print_handler('Tables created')
        self.conn.close()

    def load(self, file_path):
        try:
            file = open(file_path, 'r')
        except FileNotFoundError:
            raise Exception('File provided not found')
        self.print_handler('Loading dataset')
        df = temporal_data_process(file)
        self.print_handler('Dataset loaded')

        self.print_handler('Loading dataset to Temporal')
        result = fill_temporal(self.conn, df.itertuples())
        self.print_handler(result)
        self.print_handler('Dataset loaded to Temporal')

        self.print_handler('Loading dataset to relational model')
        queries, errors = fill_er(self.conn)
        for q in queries:
            self.print_handler(f'Query performed: {q}', internal=True)

        for e in errors:
            self.print_handler(f'Errors in queries: {e}', internal=True)
        self.print_handler('Dataset loaded to relational model')

        self.conn.close()

    def query(self):
        errors, results, queries = query_er(self.conn)
        for q in queries:
            self.print_handler(f'Query performed: {q}')
        for e in errors:
            self.print_handler(f'Errors in queries: {e}')
        print('Results: ', results)
        self.conn.close()

    def exit(self):
        self.print_handler('Program exited succesfully.')
        self.print_handler(f'You can access logs in {self.logs}')
        self.conn.close()
