#Linear Search Function

def Linear_Search(UserList, Search):
    found = False
    counter = 0
    while not found and counter < len(UserList):
        if UserList[counter] == Search:
            found = True
        else:
            counter += 1
    return found


#Main Program
people = ["Ben","Toby","Ashley"]
search = "Mark"
found = Linear_Search(people,search)
if found:
    print("{0} was found in the list".format(search))
else:
    print("{0} was not found in the list".format(search))
