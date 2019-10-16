from Config import Config


class BinaryRepresentable:


    def resolved(self):
        raise NotImplementedError()


class Variable(BinaryRepresentable):


    def __init__(self, variableName):
        self.variableName = variableName
    

    def resolved(self):
        return Config.get_variable_value(self.variableName)


class SingleAssociativityOperation:


    def __init__(self, element):
        self.element = element


class DoubleAssociativityOperation:


    def __init__(self, left, right):
        self.left = left
        self.right = right


class NOT(BinaryRepresentable, SingleAssociativityOperation):


    def resolved(self):
        element = element.resolved()

        if bool(element):
            return not element
        else:
            return -1


class AND(BinaryRepresentable, DoubleAssociativityOperation):


    def resolved(self):
        self.left = self.left.resolved()
        self.right = self.right.resolved()

        if bool(self.left) and bool(self.right):
            return self.left and self.right
        else:
            return -1


class OR(BinaryRepresentable, DoubleAssociativityOperation):


    def resolved(self):
        self.left = self.left.resolved()
        self.right = self.right.resolved()

        if bool(self.left) and bool(self.right):
            return self.left or self.right
        else:
            return -1


class XOR(BinaryRepresentable, DoubleAssociativityOperation):


    def resolved(self):
        self.left = self.left.resolved()
        self.right = self.right.resolved()

        if bool(self.left) and bool(self.right):
            return ((not self.left) and self.right) or (self.left and (not self.right))
        else:
            return -1


class Implies(BinaryRepresentable, DoubleAssociativityOperation):


    def resolved(self):
        self.left = self.left.resolved()
        return True

        # if bool(self.left) and isinstance(self.right) bool(self.right):
        #     return True
        # else:
        #     return -1


class IfAndOnlyIf(BinaryRepresentable, DoubleAssociativityOperation):


    def resolved(self):
        self.left = self.left.resolved()
        return True
        # if bool(self.left) and isinstance(self.right) :
        #     return True
        # else:
        #     return -1
