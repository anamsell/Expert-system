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
                self.current_config[variable_name] = False
    
    def goto_next_variable(self):
        self.current_var_index += 1
    
    def goto_previous_variable(self):
        self.current_var_index -= 1

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

    print("\n\n")
    # print(tmp_config.used_variables[tmp_config.current_var_index])
    # print(not tmp_config.current_varible_is_initial_fact())
    print("Current config ", tmp_config.current_config)
    if false_config != None:
        print("False config ", false_config.current_config)
    if true_config != None:
        print("True config", true_config.current_config)

    if true_config == None:
        print("\n\n")
        return false_config
    elif false_config == None:
        print("\n\n")
        return true_config
    else:
        # if false_config.is_all_true_or_false():
        #     return false_config
        # elif true_config.is_all_true_or_false():
        #     return true_config
        # else:
        
        tmp_config = merge_configs(tmp_config, false_config, true_config)
        print(" -> New config", tmp_config.current_config)
        print("\n\n")
        # tmp_config.set_current_variable_value(None)
        return tmp_config


def merge_configs(tmp_config, false_config, true_config):
    ambiguous_variables = []

    for index in range(tmp_config.current_var_index, len(tmp_config.used_variables)):
        variable_name = tmp_config.used_variables[index]
        true_variable_value = true_config.current_config[variable_name]
        false_variable_value = false_config.current_config[variable_name]

        if isinstance(false_variable_value, bool) and isinstance(true_variable_value, bool) and false_variable_value != true_variable_value:
            if not variable_name in Config.initials_facts:
                ambiguous_variables.append(variable_name)
    
    if len(ambiguous_variables) == 0:
        return tmp_config

    new_config = copy.deepcopy(tmp_config)

    print(ambiguous_variables)
    for (index_1, variable_1) in enumerate(ambiguous_variables):
        for (index_2, variable_2) in enumerate(ambiguous_variables):
            if variable_1 == variable_2:
                continue
        
            current_variable_name = ambiguous_variables[index_1]
            previous_variable_name = ambiguous_variables[index_2]

            false_current_variable_value = false_config.current_config[current_variable_name]
            false_previous_variable_value = false_config.current_config[previous_variable_name]
            true_current_variable_value = true_config.current_config[current_variable_name]
            true_previous_variable_value = true_config.current_config[previous_variable_name]

            if (false_previous_variable_value or false_current_variable_value) != False and (true_previous_variable_value or true_current_variable_value) != False:
                new_config.current_config[current_variable_name] = None
                new_config.current_config[previous_variable_name] = None
    
    return new_config




def resolve_from_config(tmp_config):
    # print(tmp_config.current_config)
    for operation in Config.operation:
        if not operation.resolved(tmp_config):
            return None
    
    # print("True")
    # print("\n")
    return tmp_config


def get_used_variables():
    used_variables = []

    for key in Config.facts:
        if Config.facts[key] == 1:
            used_variables.append(key)
    
    return used_variables
