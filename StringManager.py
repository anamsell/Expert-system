import Regex


def isOperator(string):
    return Regex.stringContainsPattern(string, "(\\!)|(\\+)|(\\|)|(\\^)|(=>)|(<=>)")


def isOperand(string):
    return Regex.stringContainsPattern(string, "[A-Z]")


def isSpace(string):
    return Regex.stringContainsPattern(string, "\s")
    

def isOpeningBrace(string):
    return string == "("


def isClosingBrace(string):
    return string == ")"
