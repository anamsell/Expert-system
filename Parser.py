class Parser:


    def __init__(self, fileLines):
        self.fileLines = fileLines


    def parse(self):
        print(self.fileLines)






class Config:

    calculus: [Operation]
    facts: {"A": True}
    queries: ["A", "B"]



class ORop:

    def __init__(self, boolA, boolB):
        self.boolA = boolA
        self.boolB = boolB
    

    def resolve(self):
        self.boolA = self.boolA.resolve()
        self.boolB = self.boolB.resolve()
        return self.boolA or self.boolB
