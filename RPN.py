import Regex
import StringManager
import PriorityManager

    
def postfixExpressionFromInfix(string):
    string = string.replace("=>", ">")
    string = string.replace("<=>", "=")
    string = string.replace(" ", "")
    string = string.replace("\t", "")

    postfixExpression = []
    operatorStack = []

    for character in string:
        if StringManager.isSpace(character):
            continue
        elif StringManager.isOperand(character):
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
                and (PriorityManager.priorityForOperator(operatorStack[-1]) >= PriorityManager.priorityForOperator(character)):
                postfixExpression.append(operatorStack.pop())
            operatorStack.append(character)
        
    while len(operatorStack) != 0:
        postfixExpression.append(operatorStack.pop())
    
    return postfixExpression
