import Display
import re
import Operation_checker
from Config import Config
from OperationManagement.RPNCalculator import RPN


def is_initial_facts(line):
    return re.search(r'^=[A-Z]*$', line)


def is_queries(line):
    return re.search(r'^\?[A-Z]*$', line)


def parse(file_lines):
    initial_facts = 0
    for index, initial_lines in enumerate(file_lines):
        initial_lines = initial_lines.replace('\n', '')
        if initial_lines.find('#') != -1:
            line = initial_lines.split('#')[0]
        else:
            line = initial_lines
        line = re.sub(r'/s', '', line)
        if not line:
            continue
        if not initial_facts:
            if Operation_checker.check(line):
                rpn = RPN(line.replace("!!", ''))
                Config.operation.append(rpn.get_operation_tree())
                continue
            if is_initial_facts(line):
                for fact in line[1:]:
                    Config.initials_facts += fact
                initial_facts = 1
                continue
        if not is_queries(line):
            Display.error("Line " + str(index + 1) + " is not a rule, initials facts and queries.\n/""" +
                          initial_lines + "/'")
        for query in line[1:]:
            Config.queries += query
            if not Config.facts[query]:
                Display.warning("The Fact " + query + " is a query but not use in the rules.")
        if index + 1 < len(file_lines):
            for index_comment, comment_line in enumerate(file_lines[index+1:]):
                if re.sub(r"/s", "", comment_line)[0] != '#':
                    Display.warning("Queries are already get, line " + str(index + index_comment + 1) + " is count as "
                                                                                                        "comment.")
        break
    if not Config.queries:
        Display.error('There is no queries.')
    if not Config.initials_facts:
        Display.warning("There is no initials_facts.")
    if not Config.operation:
        Display.warning("There is no operations.")
