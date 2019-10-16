import string


class Config:


    operation = []
    initials_facts = []
    queries = []
    facts = dict.fromkeys(string.ascii_uppercase, 0)


    @staticmethod
    def set_variable_value(variableName, value):
        Config.facts[variableName] = value

    
    @staticmethod
    def get_variable_value(variableName):
        return Config.facts.get(variableName)
