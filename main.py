from dotenv import load_dotenv

# Set up env variables
load_dotenv()

from cli import CliController


def main():
    CliController()


if __name__ == '__main__':
    main()
