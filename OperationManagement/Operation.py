class BinaryRepresentable:


    def resolved(self):
        raise NotImplementedError()


class Variable(BinaryRepresentable):


    def __init__(self, variableName):
        self.variableName = variableName
    

    def resolved(self):
        result = Config.vars[self.variableName]
        return True


class SingleAssociativityOperation:


    def __init__(self, element):
        self.element = element


class DoubleAssociativityOperation:


    def __init__(self, left, right):
        self.left = left
        self.right = right
         

class OR(BinaryRepresentable, DoubleAssociativityOperation):


    def resolved(self):
        self.left = self.left.resolved()
        self.right = self.right.resolved()

        if bool(self.left) and bool(self.right):
            return self.left or self.right
        else:
            return -1
        