import re

def stringStartWithPattern(string, pattern):
    match = re.match(pattern, string)
    return match != None


def stringContainsPattern(string, pattern):
    search = re.search(pattern, string)
    return search != None