from dotenv import load_dotenv
# Set up env variables
load_dotenv()

from ActionController import ActionController
from argsParse import parser


def main():
    args = parser.parse_args()
    logs_file = None
    if args.logs is not None:
        logs_file = args.logs

    ac = ActionController(logs=logs_file)
    if args.action == 'create':
        ac.create()
    elif args.action == 'load':
        exit('Not yet implemented')
    elif args.action == 'query':
        exit('Not yet implemented')
    elif args.action == 'exit':
        exit('Not yet implemented')


if __name__ == '__main__':
    main()
