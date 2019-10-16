import re


def string_start_with_pattern(string, pattern):
    match = re.match(pattern, string)
    return match != None
    

def string_contains_pattern(string, pattern):
    search = re.search(pattern, string)
    return search != None
    

def string_splited_with_pattern(string, pattern):
    return re.split(pattern, string)
