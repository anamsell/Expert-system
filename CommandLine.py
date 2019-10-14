import sys


class CommandLine:


    @staticmethod
    def numberOfArgsIsCorrect():
        return len(sys.argv) == 2
    

    @staticmethod
    def getFileName():
        return sys.argv[1]