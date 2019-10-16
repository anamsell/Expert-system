# from CommandLine import CommandLine
# from FileManager import FileManager
# from Parser import Parser
# from Error import Error
# from Regex import Regex


def checkArgumentNumber():
    if not CommandLine.numberOfArgsIsCorrect():
        Error.showError("Incorrect number of arguments.")


def parseFile():
    fileName = CommandLine.getFileName()
    fileContent = FileManager.getContentOfFileNamed(fileName)

    parser = Parser(fileContent)
    parser.parse()


def main():
    checkArgumentNumber()
    parseFile()

from OperationManagement.RPNCalculator import RPN

if __name__ == "__main__":
    # main()
    rpn = RPN("A | B | C | D")
    print(rpn.postfixExpression)
    print(rpn.getOperationTree())
