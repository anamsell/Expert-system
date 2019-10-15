import re


class Regex:


    @staticmethod
    def stringStartWithPattern(string, pattern):
        match = re.match(pattern, string)
        return match != None
    

    @staticmethod
    def stringContainsPattern(string, pattern):
        search = re.search(pattern, string)
        return search != None