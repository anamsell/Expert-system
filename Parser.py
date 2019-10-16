import Display
import re
import Operation_checker
from Config import Config
from OperationManagement.RPNCalculator import RPN


def is_initial_facts(line):
    return re.search(r'^=[A-Z]+$', line)


def is_queries(line):
    return re.search(r'^\?[A-Z]+$', line)


def parse(file_lines):
    initial_facts = 0
    for index, initial_lines in enumerate(file_lines):
        initial_lines = initial_lines.replace('\n', '')
        if initial_lines.find('#') != -1:
            line = initial_lines.split('#')[0]
        else:
            line = initial_lines
        line = line.replace(' ', '')
        if not line:
            continue
        if not initial_facts:
            if Operation_checker.check(line):
                rpn = RPN(line.replace("!!",''))
                Config.operation.append(rpn.get_operation_tree())
                continue
            if is_initial_facts(line):
                for fact in line[1:]:
                    Config.initials_facts += fact
                initial_facts = 1
                continue
            Display.error("Line " + str(index + 1) + " must be a rule or initials facts.\n" + initial_lines)
        if not is_queries(line):
            print(line)
            Display.error("Line " + str(index + 1) + " must be a queries.\n" + initial_lines)
        for query in line[1:]:
            Config.queries += query
            if not Config.facts[query]:
                Display.warning("The Fact " + query + " is a query but not use in the rules.")
        if index + 1 < len(file_lines):
            Display.warning("Queries are already get, lines after " + str(index + 1) + " are count as comment")
        break
    if not Config.operation:
        Display.error("There is no operations.")
    if not Config.initials_facts:
        Display.error("There is no initials_facts.")
    if not Config.queries:
        Display.error('There is no queries.')
