#Toby Kerslake
#30-12-2014
#Lists Development Exercise 1
import random

def Assign_List():
    countriesAndCapitals = [["England","France","Germany","Spain","Japan","U.S.A","Republic of Kazakhstan","Pakistan","Brazil","Nigeria"],["London","Paris","Berlin","Madrid","Tokyo","Washington D.C","Astana","Islamabad","Brasilia","Abuja"]]
    return countriesAndCapitals

def Random_Country(countriesAndCapitals):
    num = random.randint(0,9)
    country = countriesAndCapitals[0][num]
    userAnswer = input(("What is the capital of {0}? ".format(country)))
    if userAnswer == countriesAndCapitals[1][num]:
        print("You are correct!")
    else:
        print("You are incorrect!")

def Main_Program():
    countriesAndCapitals = Assign_List()
    Random_Country(countriesAndCapitals)

#Main program
Main_Program()
