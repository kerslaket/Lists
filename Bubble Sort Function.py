#Python Bubble Sort Function

def Bubble_Sort(UserList):
    n = len(UserList)
    check = False
    while check == False:
        check = True
        for person in range(0,n-1):
            if UserList[person] > UserList[person+1]:
                temp = UserList[person]
                UserList[person] = UserList[person+1]
                UserList[person+1] = temp
                check = False
    print(UserList)


#Main Program
people = ["Ben","Toby","Ashley","xaNDU","Marc Gonzalex","Zebra"]
Bubble_Sort(people)

