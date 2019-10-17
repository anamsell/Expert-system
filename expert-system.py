import CommandLine
import FileManager
import Parser
import Display
from Solver import resolve
from Config import Config


def check_argument_number():
    if not CommandLine.number_of_args_is_correct():
        Display.error("Incorrect number of arguments.")


def parse_file():
    file_name = CommandLine.get_file_name()
    file_content = FileManager.get_content_of_file_named(file_name)

    Parser.parse(file_content)


def main():
    check_argument_number
    parse_file()
    resolve()


if __name__ == "__main__":
    main()
