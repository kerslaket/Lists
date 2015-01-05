#Toby Kerslake
#29-12-2014
#Lists Revision Exercise 2

def Get_Names():
    names = []
    for count in range(6):
        num = (input("Please enter a name: "))
        names.append(num)
    return names

def Display_Names(names):
    print("What range do you want to print")
    start = int(input("Start:" )) - 1
    end = int(input("End: "))
    for name in names[start:end]:
        print(name)

def Populate_List():
    names = Get_Names()
    Display_Names(names)

#main program
Populate_List()
