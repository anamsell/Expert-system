from Config import Config


class BinaryRepresentable:

    def resolved(self, config):
        raise NotImplementedError()


class Variable(BinaryRepresentable):

    def __init__(self, variable_name):
        self.variableName = variable_name

    def resolved(self, config):
        return config[self.variableName]


class SingleAssociativityOperation:

    def __init__(self, element):
        self.element = element


class DoubleAssociativityOperation:

    def __init__(self, left, right):
        self.left = left
        self.right = right


class NOT(BinaryRepresentable, SingleAssociativityOperation):

    def resolved(self, config):
        self.element = self.element.resolved(config)

        if isinstance(self.element, bool):
            return not self.element
        else:
            return True


class AND(BinaryRepresentable, DoubleAssociativityOperation):

    def resolved(self, config):
        self.left = self.left.resolved(config)
        self.right = self.right.resolved(config)

        if isinstance(self.left, bool) and isinstance(self.right, bool):
            return self.left and self.right
        elif (isinstance(self.left, bool) and self.left == False) or (isinstance(self.right, bool) and self.right == False):
            return False
        else:
            return True


class OR(BinaryRepresentable, DoubleAssociativityOperation):

    def resolved(self, config):
        self.left = self.left.resolved(config)
        self.right = self.right.resolved(config)

        if isinstance(self.left, bool) and isinstance(self.right, bool):
            return self.left or self.right
        elif (isinstance(self.left, bool) and self.left == True) or (isinstance(self.right, bool) and self.right == True):
            return True
        else:
            return True


class XOR(BinaryRepresentable, DoubleAssociativityOperation):

    def resolved(self, config):
        self.left = self.left.resolved(config)
        self.right = self.right.resolved(config)

        if isinstance(self.left, bool) and isinstance(self.right, bool):
            return ((not self.left) and self.right) or (self.left and (not self.right))
        else:
            return True


class Implies(BinaryRepresentable, DoubleAssociativityOperation):

    def resolved(self, config):
        self.left = self.left.resolved(config)
        self.right = self.right.resolved(config)

        if isinstance(self.left, bool) and isinstance(self.right, bool):
            return not (self.left == True and self.right == False)
        else:
            return True


class IfAndOnlyIf(BinaryRepresentable, DoubleAssociativityOperation):

    def resolved(self, config):
        self.left = self.left.resolved(config)
        self.right = self.right.resolved(config)
        
        if isinstance(self.left, bool) and isinstance(self.right, bool):
            return self.left == self.right
        else:
            return True
