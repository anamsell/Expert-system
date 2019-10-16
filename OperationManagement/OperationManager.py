import OperationManagement.Operation as Operation


def priorityForOperator(operator):
    priorities = {}
    priorities["("] = 6
    priorities["!"] = 5
    priorities["+"] = 4
    priorities["|"] = 3
    priorities["^"] = 2
    priorities[">"] = 1
    priorities["="] = 0

    return priorities[operator]


def isSingleAssociativityOperator(operator):
    return operator == "!"


def operationForOperator(operator, stack):
    element2 = stack.pop()
    element1 = None

    if not isSingleAssociativityOperator(operator):
        element1 = stack.pop()

    if operator == "!":
        return Operation.NOT(element2)
    elif operator == "+":
        return Operation.AND(element1, element2)
    elif operator == "|":
        return Operation.OR(element1, element2)
    elif operator == "^":
        return Operation.XOR(element1, element2)
    elif operator == ">":
        return Operation.Implies(element1, element2)
    elif operator == "=":
        return Operation.IfAndOnlyIf(element1, element2)
        
    return None
