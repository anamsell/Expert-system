from Config import Config
from collections import OrderedDict
from copy import copy

def resolve():
    variables = {"A": None, "B": True, "C": None}
    print(variables)

    test_vars(variables, 1)


def test_vars(variables, counter):
    for operation in Config.operation:
        print(copy(operation).resolved(variables))
        if not copy(operation).resolved(variables):
            return 0

    # if variables[] == None:
    #     test_vars[variables] = False
    # else:
    #     test_var[svariable] = True:
