import logging
from database import get_connection


def configure_logging():
    logger = logging.getLogger('SEMI2_PRACTICA1')
    logger.setLevel(logging.DEBUG)
    ch = logging.FileHandler('logs.log')
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger


class ActionController:

    def __init__(self, logs=True, silent=False):
        self.silent = silent
        self.logs = logs
        if self.logs:
            self.logger = configure_logging()

        self.display_menu()

    def print_handler(self, message, internal=False, logs=True):
        if self.logs and logs:
            self.logger.info(message)

        if not (self.silent or internal):
            print(message)

    def display_menu(self):
        self.print_handler("Setting things up")
        conn = get_connection()

        self.print_handler(f'Database server information: {conn.mysql_config}', internal=True)

