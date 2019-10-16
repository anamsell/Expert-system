class Config:


    operation = []
    initials_facts = []
    queries = []
    variables = {}


    @staticmethod
    def set_variable_value(variableName, value):
        Config.variables[variableName] = value

    
    @staticmethod
    def get_variable_value(variableName):
        return Config.variables.get(variableName)
