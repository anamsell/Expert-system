def priorityForOperator(operator):
    priorities = {}
    priorities["("] = 6
    priorities["!"] = 5
    priorities["+"] = 4
    priorities["|"] = 3
    priorities["^"] = 2
    priorities[">"] = 1
    priorities["="] = 0

    return priorities[operator]
