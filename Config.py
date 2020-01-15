import string


class Config:
    operation = []
    initials_facts = []
    queries = []
    facts = dict.fromkeys(string.ascii_uppercase, None)
    branch = []
    @staticmethod
    def set_variable_value(variable_name, value):
        Config.facts[variable_name] = value

    @staticmethod
    def get_variable_value(variable_name):
        variable = Config.facts.get(variable_name)

        if variable is None:
            return -1

        return variable
