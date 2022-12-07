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


class CliController:

    def __init__(self, logs=True, silent=False):
        self.silent = silent
        self.logs = logs
        if self.logs:
            self.logger = configure_logging()

        self.display_menu()

    def create_log(self, message, internal=False):
        if self.logs:
            self.logger.info(message)

        if not self.silent or internal:
            print(message)

    def display_menu(self):
        self.create_log("Setting things up")
        conn = get_connection()
        conn.
        self.create_log(f'Database server information: {conn.get_server_info()}', internal=True)
