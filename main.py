from dotenv import load_dotenv

# Set up env variables
load_dotenv()

from argsParse import parser


def main():
    args = parser.parse_args()

    if args.action == 'create':
        exit('Not yet implemented')
    elif args.action == 'load':
        exit('Not yet implemented')
    elif args.action == 'query':
        exit('Not yet implemented')
    elif args.action == 'exit':
        exit('Not yet implemented')


if __name__ == '__main__':
    main()
