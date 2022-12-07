import logging
from database import get_connection, drop_all_tables, create_tables


class ActionController:

    def __init__(self, logs='logs.log', silent=False):
        self.conn = None
        self.logs = logs
        self.silent = silent
        print(f'Logs {logs}')
        if self.logs:
            self.logger = self.configure_logging()

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
        self.conn = self.set_up_connection()
        self.print_handler('Starting process')
        self.print_handler('Deleting tables')
        drop_all_tables(self.conn)
        self.print_handler('Tables deleted')
        self.print_handler('Creating tables')
        create_tables(self.conn)
