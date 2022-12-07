import argparse

parser = argparse.ArgumentParser()

supported_actions = ['create', 'load', 'query', 'exit']
parser.add_argument('action', help='Action to perform', choices=supported_actions)
parser.add_argument('-v', '--verbose', help='Allows to print an output', action="store_true")
parser.add_argument('-l', '--logs',
                    help='Allows to write logs in a file provided',
                    default='./logs.log',
                    required=False)
