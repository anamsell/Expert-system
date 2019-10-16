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

from OperationManagement.RPNCalculator import RPN

if __name__ == "__main__":
    # main()
    rpn = RPN("A | B | C | D")
    print(rpn.postfixExpression)
    print(rpn.getOperationTree())
