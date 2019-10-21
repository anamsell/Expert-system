import re


def string_start_with_pattern(string, pattern):
    match = re.match(pattern, string)
    return match != None
    

def string_contains_pattern(string, pattern):
    search = re.search(pattern, string)
    return search != None


def first_occurence_of_pattern_in_string(string, pattern):
    return re.search(pattern, string)


def occurences_of_pattern_in_string(string, pattern):
    search = re.findall(pattern, string)
    return len(search)
    

def string_replacing_with_pattern(string, pattern, replacement):
    return re.sub(pattern, replacement, string)
