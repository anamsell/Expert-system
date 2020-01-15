from Config import Config
from copy import copy, deepcopy
import Display
import itertools


def fill_result_with_easy_fact(result, values):
    for value in values:
        if value in result:
            continue
        for branch in Config.branch:
            if branch[value] is False:
                break
        else:
            result[value] = True
    for value in values:
        for branch in Config.branch:
            if branch[value] is True:
                break
        else:
            result[value] = False
    for val in result:
        del (values[val])


def fill_result_with_tricky_fact(value_of_tricky_fact, final_value_of_fact):
    number_of_partner = len(value_of_tricky_fact)
    list_of_group_of_partners = []
    while number_of_partner >= 2:
        combinations = itertools.combinations(value_of_tricky_fact, number_of_partner)
        for combination in combinations:
            for branch in Config.branch:
                for fact in combination:
                    if branch[fact] is True:
                        break
                else:
                    break
            else:
                cpy = deepcopy(list_of_group_of_partners)
                for previous_group_of_partners in list_of_group_of_partners:
                    if set(combination).issubset(set(previous_group_of_partners)):
                        del(cpy[cpy.index(previous_group_of_partners)])
                list_of_group_of_partners = cpy
                list_of_group_of_partners += [combination]
        number_of_partner -= 1
    for group in list_of_group_of_partners:
        for ambiguous_fact in group:
            final_value_of_fact[ambiguous_fact] = "undetermined"


def resolve():
    starting_value_of_fact = {}
    fact_with_unknown_value = ""
    final_value_of_fact = {}
    for fact in Config.facts:
        if fact in Config.initials_facts:
            starting_value_of_fact[fact] = True
        elif Config.facts[fact]:
            starting_value_of_fact[fact] = None
            fact_with_unknown_value += fact
    test_vars(starting_value_of_fact, fact_with_unknown_value)
    if not Config.branch:
        Display.error("There is no solution for this")
    fill_result_with_easy_fact(final_value_of_fact, starting_value_of_fact)
    if starting_value_of_fact:
        fill_result_with_tricky_fact(starting_value_of_fact, final_value_of_fact)
    print("\033[94m" + str("Result:") + "\033[0m")
    for query in Config.queries:
        if query not in final_value_of_fact:
            final_value_of_fact[query] = False
        print(query + " is " + "\033[92m" + str(final_value_of_fact[query]) + "\033[0m")


def test_vars(values, to_change):
    for operation in Config.operation:
        if operation.resolved(values) is False:
            return
    if not to_change:
        Config.branch += [values]
        return
    copy0 = copy(values)
    copy0[to_change[0]] = False
    test_vars(copy0, to_change[1:])
    copy1 = copy(values)
    copy1[to_change[0]] = True
    test_vars(copy1, to_change[1:])
