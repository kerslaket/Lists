#Toby Kerslake
#09-12-2014
#Lists R & R

def ListsRandR():
    loop = False
    NamesList = GetNames()
    while loop == False:
        NameList(NamesList)
        loop,StudentNames = Select(NamesList,loop)
        

def GetNames():
    name1 = ("1. ") + input("Please enter the name of the first student")
    name2 = ("2. ") + input("Please enter the name of the second student")
    name3 = ("3. ") + input("Please enter the name of the third student")
    name4 = ("4. ") + input("Please enter the name of the fourth student")
    name5 = ("5. ") + input("Please enter the name of the fifth student")
    name6 = ("6. ") + input("Please enter the name of the sixth student")
    name7 = ("7. ") + input("Please enter the name of the seventh student")
    name8 = ("8. ") + input("Please enter the name of the eighth student")
    StudentNames = [name1,name2,name3,name4,name5,name6,name7,name8]
    return StudentNames

def NameList(StudentNames):
    numbers = [1,2,3,4,5,6,7,8]
    for each in StudentNames:
        print(each)
    print("0. Exit Program")


def Select(StudentNames,loop):
    number = int(input("Please select a student to edit:"))
    if number == 1:
        name = input("Please enter their new name:")
        StudentNames.insert(0,"1. " + name)
        StudentNames.pop(1)
    elif number == 2:
        name = input("Please enter their new name:")
        StudentNames.insert(1,"2. " + name)
        StudentNames.pop(2)
    elif number == 3:
        name = input("Please enter their new name:")
        StudentNames.insert(2,"3. " + name)
        StudentNames.pop(3)
    elif number == 4:
        name = input("Please enter their new name:")
        StudentNames.insert(3,"4. " + name)
        StudentNames.pop(4)
    elif number == 5:
        name = input("Please enter their new name:")
        StudentNames.insert(4,"5. " + name)
        StudentNames.pop(5)
    elif number == 6:
        name = input("Please enter their new name:")
        StudentNames.insert(5,"6. " + name)
        StudentNames.pop(6)
    elif number == 7:
        name = input("Please enter their new name:")
        StudentNames.insert(6,"7. " + name)
        StudentNames.pop(7)
    elif number == 8:
        name = input("Please enter their new name:")
        StudentNames.insert(7,"8. " + name)
        StudentNames.pop(8)
    else:
        print("Exiting the program")
        loop = True
    return loop,StudentNames


#Main Program
ListsRandR()
                 
                 
          

          
