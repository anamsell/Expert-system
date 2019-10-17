from Config import Config
from collections import OrderedDict
import copy

class TMPConfig:

    def __init__(self, used_variables):
        self.used_variables = used_variables
        self.current_config = {}
        self.current_var_index = 0
        self.__init_config()
    
    def __init_config(self):
        for variable_name in self.used_variables:
            is_initial_fact = variable_name in Config.initials_facts

            if is_initial_fact:
                self.current_config[variable_name] = True
            else:
                self.current_config[variable_name] = None
    
    def goto_next_variable(self):
        self.current_var_index += 1

    def current_variable_value(self):
        variable_name = self.used_variables[self.current_var_index]
        return self.current_config[variable_name]
    
    def set_current_variable_value(self, value):
        variable_name = self.used_variables[self.current_var_index]
        self.current_config[variable_name] = value
    
    def set_variable_value(self, variable_name, value):
        self.current_config[variable_name] = value
    
    def is_testing_last_variable(self):
        return self.current_var_index == len(self.used_variables)
    
    def is_all_true_or_false(self):
        state_to_test = self.current_config[self.used_variables[0]]

        if state_to_test == None:
            return False
        
        for variable_name in self.used_variables:
            if self.current_config[variable_name] != state_to_test:
                return False
        
        return True

    
    def current_varible_is_initial_fact(self):
        variable_name = self.used_variables[self.current_var_index]
        return variable_name in Config.initials_facts


def resolve():
    used_variables = get_used_variables()
    tmp_config = TMPConfig(used_variables)
    final_config = generate_truth_table(tmp_config)

    if final_config != None:
        print(final_config.current_config)
    else:
        print("No config")


def generate_truth_table(tmp_config):
    if tmp_config.is_testing_last_variable():
        return resolve_from_config(tmp_config)

    false_config = None

    if not tmp_config.current_varible_is_initial_fact():
        false_config_copy = copy.deepcopy(tmp_config)
        false_config_copy.set_current_variable_value(False)
        false_config_copy.goto_next_variable()
        false_config = generate_truth_table(false_config_copy)

    true_config_copy = copy.deepcopy(tmp_config)
    true_config_copy.set_current_variable_value(True)
    true_config_copy.goto_next_variable()
    true_config = generate_truth_table(true_config_copy)

    if false_config == None:
        return true_config
    elif true_config == None:
        return false_config
    else:
        # if false_config.is_all_true_or_false():
        #     return false_config
        # elif true_config.is_all_true_or_false():
        #     return true_config
        # else:
        # print("\n\n")
        # print(tmp_config.used_variables[tmp_config.current_var_index])
        # print(tmp_config.current_config)
        merge_configs(tmp_config, false_config, true_config)
        # print(false_config.current_config)
        # print(true_config.current_config)
        # print("\n\n")
        # tmp_config.set_current_variable_value(None)
        return tmp_config


def merge_configs(tmp_config, false_config, true_config):
    for variable_name in tmp_config.current_config:
        current_variable_value = tmp_config.current_config[variable_name]
        false_variable_value = false_config.current_config[variable_name]
        true_variable_value = true_config.current_config[variable_name]

        if false_variable_value == True and true_variable_value == True:
            if current_variable_value == None:
                tmp_config.set_variable_value(variable_name, True)
        elif false_variable_value == False and true_variable_value == False:
            if current_variable_value == True:
                tmp_config.set_variable_value(variable_name, None)
            else:
                tmp_config.set_variable_value(variable_name, False)
        elif false_variable_value == False and true_variable_value == True:
            if current_variable_value == None:
                tmp_config.set_variable_value(variable_name, False)
            else:
                tmp_config.set_variable_value(variable_name, None)
        else:
            continue


def resolve_from_config(tmp_config):
    print(tmp_config.current_config)
    for operation in Config.operation:
        if not operation.resolved(tmp_config):
            print(operation)
            print("False")
            print("\n")
            return None
    
    print("True")
    print("\n")
    return tmp_config


def get_used_variables():
    used_variables = []

    for key in Config.facts:
        if Config.facts[key] == 1:
            used_variables.append(key)
    
    return used_variables
