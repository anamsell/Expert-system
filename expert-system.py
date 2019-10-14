from CommandLine import CommandLine
from FileManager import FileManager
from Parser import Parser
from Error import Error


def checkArgumentNumber():
    if not CommandLine.numberOfArgsIsCorrect():
        Error.showError("Incorrect number of arguments.")
        exit(0)


def parseFile():
    fileName = CommandLine.getFileName()
    fileContent = FileManager.getContentOfFileNamed(fileName)

    parser = Parser(fileContent)
    parser.parse()


def main():
    checkArgumentNumber()
    parseFile()


if __name__ == "__main__":
    main()