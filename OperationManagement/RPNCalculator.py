import Regex
import StringManager
import OperationManagement.OperationManager as OperationManager
from OperationManagement.Operation import Variable


class RPN:


    def __init__(self, infixExpression):
        self.infixExpression = infixExpression
        self.postfixExpression = self.__getPostfixExpression()


    def __formatInfixExpression(self):
        self.infixExpression = self.infixExpression.replace("=>", ">")
        self.infixExpression = self.infixExpression.replace("<=>", "=")
        self.infixExpression = self.infixExpression.replace(" ", "")
        self.infixExpression = self.infixExpression.replace("\t", "")


    def __getPostfixExpression(self):
        self.__formatInfixExpression()

        postfixExpression = []
        operatorStack = []

        for character in self.infixExpression:
            if StringManager.isOperand(character):
                postfixExpression.append(character)
            elif StringManager.isOpeningBrace(character):
                operatorStack.append(character)
            elif StringManager.isClosingBrace(character):
                while True:
                    lastOperator = operatorStack.pop()
                    if StringManager.isOpeningBrace(lastOperator):
                        break
                    else:
                        postfixExpression.append(lastOperator)
            else:
                while len(operatorStack) != 0 \
                    and StringManager.isOperator(operatorStack[-1]) \
                    and (OperationManager.priorityForOperator(operatorStack[-1]) >= OperationManager.priorityForOperator(character)):
                    postfixExpression.append(operatorStack.pop())
                operatorStack.append(character)
        
        while len(operatorStack) != 0:
            postfixExpression.append(operatorStack.pop())
    
        return postfixExpression
    

    def getOperationTree(self):
        stack = []

        for element in self.postfixExpression:
            if StringManager.isOperand(element):
                variable = Variable(element)
                stack.append(variable)
            else:
                operation = OperationManager.operationForOperator(element, stack)
                stack.append(operation)
        
        return stack[0]
