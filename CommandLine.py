import sys


def numberOfArgsIsCorrect():
    return len(sys.argv) == 2


def getFileName():
    return sys.argv[1]