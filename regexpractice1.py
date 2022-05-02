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
usersmatches : list
usersmatches = []
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
def user_search(data,field):
    if(field == 1):
        i = 0
        for i in range (0, len(usersdata)):
            if(re.findall("^" + data,usersdata[i][0])):
                if(len(usersmatches) != 0):
                    usersmatches.clear()
                usersmatches.append(usersdata[i])
                return True
            else:
                return False
    elif(field == 2):
        i = 0
        for i in range (0, len(usersdata)):
            if(re.findall(data + "$",usersdata[i][1])):
                if(len(usersmatches) != 0):
                    usersmatches.clear()
                usersmatches.append(usersdata[i])
                return True
            else:
                return False
    elif(field == 3):
        i = 0
        for i in range (0, len(usersdata)):
            if(re.findall(data,usersdata[i][2])):
                if(len(usersmatches) != 0):
                    usersmatches.clear()
                usersmatches.append(usersdata[i])
                return True
            else:
                return False
    elif(field == 4):
        i = 0
        for i in range (0, len(usersdata)):
            if(re.findall("^" + data + "$",usersdata[i][3])):
                if(len(usersmatches) != 0):
                    usersmatches.clear()
                usersmatches.append(usersdata[i])
                return True
            else:
                return False

def console_text_search():
    print("What do you want to search for?")
    print("Options:")
    print("1-User Name / 2-User Surname / 3-User Age / 4-User Mail")
    action = int(input("Introduce the option number: "))
    #Name option
    if(action == 1):
        userinput = input("Introduce the users name: ")
        result = data_check(userinput,str)
        if(result):
            namehelper = userinput.lower()
            result = user_search(namehelper,1)
            if(result):
                print("---MATCHES FOUND---")
                print(usersmatches)
            else:
                print("---NOT MATCHES FOUND---")
        else:
            #Error
            print("---ERROR---")
            print("Try again, please")
        print("Press Enter to continue...")
        m.getch()
        if(len(usersmatches) != 0):
            usersmatches.clear()
        os.system('cls')
    #Surname option
    elif(action == 2):
        userinput = input("Introduce the users surname: ")
        result = data_check(userinput,str)
        if(result):
            surnamehelper = userinput.lower()
            result = user_search(surnamehelper,2)
            if(result):
                print("---MATCHES FOUND---")
                print(usersmatches)
            else:
                print("---NOT MATCHES FOUND---")
        else:
            #Error
            print("---ERROR---")
            print("Try again, please")
        print("Press Enter to continue...")
        m.getch()
        if(len(usersmatches) != 0):
            usersmatches.clear()
        os.system('cls')
    #Age option
    elif(action == 3):
        numuserinput = input("Introduce the users age: ")
        result = data_check(numuserinput,int)
        if(result):
            agehelper = numuserinput
            result = user_search(agehelper,3)
            if(result):
                print("---MATCHES FOUND---")
                print(usersmatches)
            else:
                print("---NOT MATCHES FOUND---")
        else:
            #Error
            print("---ERROR---")
            print("Try again, please")
        print("Press Enter to continue...")
        m.getch()
        if(len(usersmatches) != 0):
            usersmatches.clear()
        os.system('cls')
    #Mail option
    elif(action == 4):
        userinput = input("Introduce the users mail: ")
        result = data_check(userinput,str)
        if(result):
            namehelper = userinput.lower()
            result = user_search(namehelper,4)
            if(result):
                print("---MATCHES FOUND---")
                print(usersmatches)
            else:
                print("---NOT MATCHES FOUND---")
        else:
            #Error
            print("---ERROR---")
            print("Try again, please")
        print("Press Enter to continue...")
        m.getch()
        if(len(usersmatches) != 0):
            usersmatches.clear()
        os.system('cls')
    #Error option
    else:
        print("---ERROR---")
        print("The entered data is incorrect, please enter it again")
        print("Press Enter to continue...")
        m.getch()
        os.system('cls')

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
        console_text_search()
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