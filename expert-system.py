import CommandLine
import FileManager
import Parser
import Display
import Regex
from Config import Config


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
    rpn = RPN("A <=> B")
    print(rpn.postfixExpression)
    tree = rpn.getOperationTree()

    Config.set_variable_value("A", True)
    Config.set_variable_value("B", True)

    print(tree.resolved())

    main()
