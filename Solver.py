from Config import Config
from copy import copy
import Display


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
    other_fact_tricky = [*value_of_tricky_fact]
    for fact in value_of_tricky_fact:
        if fact in final_value_of_fact:
            continue
        cpy = copy(other_fact_tricky)
        del (cpy[cpy.index(fact)])
        for partner in other_fact_tricky:
            for branch in Config.branch:
                if branch[fact] is False and branch[partner] is False:
                    break
            else:
                final_value_of_fact[fact] = "Ambiguous"
                final_value_of_fact[partner] = "Ambiguous"
                break
        else:
            final_value_of_fact[fact] = False


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
    for query in Config.queries:
        print(query + ': ' + '\033[92m' + str(final_value_of_fact[query]) + '\033[0m')


def test_vars(values, to_change):
    for operation in Config.operation:
        if not operation.resolved(values):
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
