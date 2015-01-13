#Table Function

def TableFunction(NestedList):
    for item in NestedList:
        print("| {0:<12} | {1:<5} |".format(item[0], item[1]))

def findWidth(NestedList,column):
    width = 0
    for item in NestedList:
        if len(item[column]) > length:
            length = len(item[column])
    return length
    


#main program
testList = [["Name","K:D",],["K1LLmAchine","51:49"],["bob7424","5:99"],["hAxOr12","72:30"]]
length = findWidth(testList,testList[0]
#TableFunction(testList)
