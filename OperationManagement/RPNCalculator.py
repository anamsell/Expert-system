import Regex
import StringManager
import OperationManagement.OperationManager as OperationManager
from OperationManagement.Operation import Variable


class RPN:


    def __init__(self, infix_expression):
        self.infix_expression = infix_expression
        self.postfix_expression = self.__get_postfix_expression()


    def __format_infix_expression(self):
        self.infix_expression = self.infix_expression.replace("<=>", "=")
        self.infix_expression = self.infix_expression.replace("=>", ">")
        self.infix_expression = self.infix_expression.replace(" ", "")
        self.infix_expression = self.infix_expression.replace("\t", "")


    def __get_postfix_expression(self):
        self.__format_infix_expression()

        postfix_expression = []
        operator_stack = []

        for character in self.infix_expression:
            if StringManager.is_operand(character):
                postfix_expression.append(character)
            elif StringManager.is_opening_brace(character):
                operator_stack.append(character)
            elif StringManager.is_closing_brace(character):
                while True:
                    last_operator = operator_stack.pop()
                    if StringManager.is_opening_brace(last_operator):
                        break
                    else:
                        postfix_expression.append(last_operator)
            else:
                while len(operator_stack) != 0 \
                    and StringManager.is_operator(operator_stack[-1]) \
                    and (OperationManager.priority_for_operator(operator_stack[-1]) >= OperationManager.priority_for_operator(character)):
                    postfix_expression.append(operator_stack.pop())
                operator_stack.append(character)
        
        while len(operator_stack) != 0:
            postfix_expression.append(operator_stack.pop())
    
        return postfix_expression
    

    def get_operation_tree(self):
        stack = []

        for element in self.postfix_expression:
            if StringManager.is_operand(element):
                variable = Variable(element)
                stack.append(variable)
            else:
                operation = OperationManager.operation_for_operator(element, stack)
                stack.append(operation)
        
        return stack[0]
