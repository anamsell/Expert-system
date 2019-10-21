import re
from Config import Config


def operator(previous_char):
    return re.search(r'[A-Z)]', previous_char)


def close_parenthesis(previous_char):
    return re.search(r'[A-Z)]', previous_char)


def fact(previous_char):
    return re.search(r'[|+^>(!]', previous_char)


def open_parenthesis(previous_char):
    return re.search(r'[|+^>(!]', previous_char)


def negation(previous_char):
    return re.search(r'[|+^>(!]', previous_char)


def check(line):
    previous_char = '('
    parentheses_number = 0

    line_iter = iter(line)
    for index, actual_char in enumerate(line_iter):
        if actual_char is ' ' or actual_char is '\t':
            continue
        if actual_char is '(' or actual_char is '!':
            if not open_parenthesis(previous_char):
                return 0
            if actual_char == '(':
                parentheses_number += 1
        elif actual_char == ')':
            if not close_parenthesis(previous_char):
                return 0
            if parentheses_number < 1:
                return 0
            parentheses_number -= 1
        elif re.search(r'[A-Z]', actual_char):
            if not fact(previous_char):
                return 0
            else:
                Config.facts[actual_char] = True
        elif re.search(r'[|+^]', actual_char):
            if not operator(previous_char):
                return 0
        elif actual_char is '!':
            if not negation(previous_char):
                return 0
        elif actual_char is '<' or actual_char is '=':
            if actual_char is '<':
                try:
                    actual_char = next(line_iter)
                except StopIteration:
                    return 0
                if actual_char is not '=':
                    return 0
            try:
                actual_char = next(line_iter)
            except StopIteration:
                return 0
            if actual_char is not '>':
                return 0
            if not operator(previous_char):
                return 0
            if parentheses_number != 0:
                return 0
        else:
            return 0
        previous_char = actual_char
    if not close_parenthesis(previous_char):
        return 0
    return not parentheses_number
