#Toby Kerslake
#29-12-2014
#Lists Revision Exercise 1

def Get_Names():
    names = []
    num = 0
    for count in range(6):
        num = (input("Please enter a name: ")
        names.append(num)
    return names

def Display_Names(names):
    for name in names:
        print(name)

def Populate_List():
    names = Get_Names()
    Display_Names(names)

#main program
Populate_List()
