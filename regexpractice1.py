from ast import Continue
import re
import os
import msvcrt as m

#Variables
action : int
action = 0
usaerinput : str
userinput = ""
numusaerinput : int
numuserinput = 0
result : bool
result = True
inputresult : bool
inputresult = True
usersdata : list
usersdata = []
namehelper : str
namehelper = ""
surnamehelper : str
surnamehelper = ""
agehelper : int
agehelper = 0
mailhelper : str
mailhelper = ""

#Code Begins
#Data type check function
def data_check(data,typeneeded):
    if(type(data) == typeneeded):
        return True
    else:
        return False

#Data input function
def data_input():
    error = False
    #User name
    userinput = input("Write users name: ")
    result = data_check(userinput,str)
    if(result):
        namehelper = userinput.lower()
        error = False
    else:
        error = True
    if(error):
        return False
    else:
        #User surname
        userinput = input("Write users surname: ")
        result = data_check(userinput,str)
        if(result):
            surnamehelper = userinput.lower()
            error = False
        else:
            error = True
        if(error):
            return False
        else:
            #User age
            numuserinput = int(input("Write users age: "))
            result = data_check(numuserinput,int)
            if(result):
                agehelper = numuserinput
                error = False
            else:
                error = True
            if(error):
                return False
            else:
                #User mail
                userinput = input("Write users mail: ")
                result = data_check(userinput,str)
                if(result):
                    result = mail_check(userinput)
                    print(result)
                    if(result):
                        mailhelper = userinput.lower()
                        error = False
                    else:
                        error = True
                else:
                    error = True
                if(error):
                    return False
                else:
                    #List creation
                    usersdata.append((namehelper, surnamehelper, agehelper, mailhelper))
                    return True

#Email format check function
def mail_check(data):
    if(re.findall("^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$",data)):
        return True
    else:
        return False

#Data search function
def user_search():
    pass

#Main while
while True:
    print("---USERS DATA BASE---")
    print("What do you want to do?")
    print("Options:")
    print("1-Create New User / 2-Search User / 3-Exit")
    action = int(input("Introduce the option number: "))
    #Creation option
    if(action == 1):
        os.system('cls')
        print("---NEW USER CREATION---")
        #Data_input
        inputresult = data_input()
        if(inputresult):
            #End Message
            print("---USER CREATED---")
        else:
            #End Message
            print("---ERROR OCURRED---")
            print("Try again, please")
        print("Press Enter to continue...")
        m.getch()
        os.system('cls')
    #Search option
    elif(action == 2):
        os.system('cls')
        print("---USER SEARCH---")
        print(usersdata)
        #Requests the that wants to be found
        #Calls user_search(parameters)
        #Prints results
        print("Press Enter to continue...")
        m.getch()
        os.system('cls')
    #Exit option
    elif(action == 3):
        os.system('cls')
        print("---PROGRAM SHUT DOWN---")
        print("Press Enter to continue...")
        m.getch()
        os.system('cls')
        exit()
    #Error option
    else:
        os.system('cls')
        print("---ERROR---")
        print("The entered data is incorrect, please enter it again")
        print("Press Enter to continue...")
        m.getch()
        os.system('cls')