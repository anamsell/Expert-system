import string


class Config:
    operation = []
    initials_facts = []
    queries = []
    facts = dict.fromkeys(string.ascii_uppercase, None)
    branch = []
    @staticmethod
    def set_variable_value(variableName, value):
        Config.facts[variableName] = value

    @staticmethod
    def get_variable_value(variableName):
        variable = Config.facts.get(variableName)

        if variable == None:
            return -1

        return variable
