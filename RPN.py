import Regex
import StringManager
import PriorityManager

    
def postfixExpressionFromInfix(string):
    splitedString = Regex.stringSplitedWithPattern(string, "\s")

    postfixExpression = []
    operatorStack = []

    for string in splitedString:
        if StringManager.isSpace(string):
            continue
        elif StringManager.isOperand(string):
            postfixExpression.append(string)
        elif StringManager.isOpeningBrace(string):
            operatorStack.append(string)
        elif StringManager.isClosingBrace(string):
            while True:
                lastOperator = operatorStack.pop()
                if StringManager.isOpeningBrace(lastOperator):
                    break
                else:
                    postfixExpression.append(lastOperator)
        else:
            while len(operatorStack) != 0 and (PriorityManager.priorityForOperator(operatorStack[-1]) >= PriorityManager.priorityForOperator(string)):
                postfixExpression.append(operatorStack.pop())
            operatorStack.append(string)
    
    while len(operatorStack) != 0:
        postfixExpression.append(operatorStack.pop())
    
    return postfixExpression

            
