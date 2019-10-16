import OperationManagement.Operation as Operation


def priority_for_operator(operator):
    priorities = {"(": 6, "!": 5, "+": 4, "|": 3, "^": 2, ">": 1, "=": 0}
    return priorities[operator]


def is_single_associativity_operator(operator):
    return operator == "!"


def operation_for_operator(operator, stack):
    element2 = stack.pop()
    element1 = None

    if not is_single_associativity_operator(operator):
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
