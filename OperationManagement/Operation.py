from Config import Config
from Solver import TMPConfig


class BinaryRepresentable:

    def resolved(self, config):
        raise NotImplementedError()


class Variable(BinaryRepresentable):

    def __init__(self, variable_name):
        self.variableName = variable_name

    def resolved(self, config):
        return config.current_config[self.variableName]


class SingleAssociativityOperation:

    def __init__(self, element):
        self.element = element


class DoubleAssociativityOperation:

    def __init__(self, left, right):
        self.left = left
        self.right = right


class NOT(BinaryRepresentable, SingleAssociativityOperation):

    def resolved(self, config):
        r_element = self.element.resolved(config)

        if isinstance(r_element, bool):
            return not r_element
        else:
            return False


class AND(BinaryRepresentable, DoubleAssociativityOperation):

    def resolved(self, config):
        r_left = self.left.resolved(config)
        r_right = self.right.resolved(config)

        if isinstance(r_left, bool) and isinstance(r_right, bool):
            return r_left and r_right
        elif (isinstance(r_left, bool) and r_left == False) or (isinstance(r_right, bool) and r_right == False):
            return True
        else:
            return False


class OR(BinaryRepresentable, DoubleAssociativityOperation):

    def resolved(self, config):
        r_left = self.left.resolved(config)
        r_right = self.right.resolved(config)

        if isinstance(r_left, bool) and isinstance(r_right, bool):
            return r_left or r_right
        elif (isinstance(r_left, bool) and r_left == True) or (isinstance(r_right, bool) and r_right == True):
            return True
        else:
            return False


class XOR(BinaryRepresentable, DoubleAssociativityOperation):

    def resolved(self, config):
        r_left = self.left.resolved(config)
        r_right = self.right.resolved(config)

        if isinstance(r_left, bool) and isinstance(r_right, bool):
            return ((not r_left) and r_right) or (r_left and (not r_right))
        else:
            return False


class Implies(BinaryRepresentable, DoubleAssociativityOperation):

    def resolved(self, config):
        r_left = self.left.resolved(config)
        r_right = self.right.resolved(config)

        if isinstance(r_left, bool) and isinstance(r_right, bool):
            return not (r_left == True and r_right == False)
        else:
            return False


class IfAndOnlyIf(BinaryRepresentable, DoubleAssociativityOperation):

    def resolved(self, config):
        r_left = self.left.resolved(config)
        r_right = self.right.resolved(config)
        
        if isinstance(r_left, bool) and isinstance(r_right, bool):
            return r_left == r_right
        else:
            return False
