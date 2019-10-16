import string


class Config:
    operation = list()
    initials_facts = list()
    queries = list()
    facts = dict.fromkeys(string.ascii_uppercase, 0)
