import Regex


def is_operator(string):
    return Regex.string_contains_pattern(string, "(\\!)|(\\+)|(\\|)|(\\^)|(=>)|(<=>)")


def is_operand(string):
    return Regex.string_contains_pattern(string, "[A-Z]")


def is_space(string):
    return Regex.stringContainsPattern(string, "\s")
    

def is_opening_brace(string):
    return string == "("


def is_closing_brace(string):
    return string == ")"
