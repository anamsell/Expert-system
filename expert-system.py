import CommandLine
import FileManager
import Parser
import Display
import Regex


def checkArgumentNumber():
    if not CommandLine.numberOfArgsIsCorrect():
        Display.error("Incorrect number of arguments.")


def parseFile():
    fileName = CommandLine.getFileName()
    fileContent = FileManager.getContentOfFileNamed(fileName)

    Parser.parse(fileContent)


def main():
    checkArgumentNumber()
    parseFile()


if __name__ == "__main__":
    main()
