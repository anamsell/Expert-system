def priorityForOperator(operator):
    priorities = {}
    priorities["("] = 1
    priorities["!"] = 2
    priorities["+"] = 3
    priorities["|"] = 4
    priorities["^"] = 5
    priorities["=>"] = 6
    priorities["<=>"] = 7
    
    return priorities[operator]
