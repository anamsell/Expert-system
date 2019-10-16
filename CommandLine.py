import sys


def number_of_args_is_correct():
    return len(sys.argv) == 2


def get_file_name():
    return sys.argv[1]
