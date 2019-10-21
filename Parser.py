import Display
import Regex
import Operation_checker
from Config import Config
from OperationManagement.RPNCalculator import RPN


def contains_multiple_implications(line):
    occurences = Regex.occurences_of_pattern_in_string(line, "(=>)|(<=>)")
    return occurences > 1


def is_initial_facts(line):
    return Regex.string_contains_pattern(line, "^=[A-Z]*$")


def is_queries(line):
    return Regex.string_contains_pattern(line, "^\?[A-Z]*$")


def parse(file_lines):
    initial_facts = 0
    for index, initial_lines in enumerate(file_lines):
        initial_lines = initial_lines.replace("\n", "")
        if initial_lines.find("#") != -1:
            line = initial_lines.split("#")[0]
        else:
            line = initial_lines
        line = Regex.string_replacing_with_pattern(line, "\\s", "")
        if not line:
            continue
        if not initial_facts:
            if contains_multiple_implications(line):
                Display.error("Line " + str(index + 1) + " contains multiple implications.\n\"" + line + "\"")
            if Operation_checker.check(line):
                rpn = RPN(line.replace("!!", ""))
                Config.operation.append(rpn.get_operation_tree())
                continue
            if is_initial_facts(line):
                for fact in line[1:]:
                    Config.initials_facts += fact
                initial_facts = 1
                continue
        if not is_queries(line):
            Display.error("Line " + str(index + 1) + " is not a rule, initial fact or queries.\n\"" +
                          initial_lines + "\"")
        for query in line[1:]:
            Config.queries += query
            if not Config.facts[query]:
                Display.warning("The variable " + query + " is a query but is never used in the facts.")
        if index + 1 < len(file_lines):
            for index_comment, comment_line in enumerate(file_lines[index+1:]):
                if len(Regex.string_replacing_with_pattern(comment_line, "\\s", "")) > 0:
                    Display.warning("Queries are already fetched, line " + str(index + index_comment + 1) + " will not be interpreted.")
        break
    if not Config.queries:
        Display.error("There is no queries.")
    if not Config.initials_facts:
        Display.warning("There is no initials_facts.")
    if not Config.operation:
        Display.warning("There is no operations.")
