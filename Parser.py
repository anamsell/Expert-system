import Display
import re
from Config import Config


def is_operation(line):
    return 0


def queries(line):
    pass


def is_initial_facts(line):
    return re.search(r'^=[A-Z]+$', line)


def parse(file_lines):
    initial_facts = 0
    for index, line in enumerate(file_lines):
        if line.find('#') != -1:
            line = line.split('#')[0]
            if line == '':
                continue
        if initial_facts == 0 and is_operation(line):
                continue
        else :
            Display.error("Line " + str(index) + " must be a rule or initials facts.")
        initial_facts == 1
        if is_initial_facts(line):
            else:
                Display.error("Line " + str(index) + " must be a rule or initials facts.")
        else:
            queries(line)
    if not Config.operation:
        Display.error("There is no operations.")
    if not Config.queries:
        Display.error('There is no queries.')
    if not Config.initials_facts:
        Display.warning("There is no initials_facts.")
    print(file_lines)
