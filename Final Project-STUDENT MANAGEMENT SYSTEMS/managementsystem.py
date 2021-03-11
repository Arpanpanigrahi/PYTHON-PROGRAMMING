#STUDENT MANAGEMENT SYSTEM

print("=====WELCOME TO STUDENT MANAGEMENT SYSTEM=====")
user=input("Enter The Default Username")
pas=input("Enter The Default Password")
temp1,temp2="u","p"
l=[]
while 1:
    f=0
    if user=="u" and pas=="p":
                temp1 = input("reset the username:")
                print("RULES FOR PASSWORD:")
                print("1-the length of the password must be between 8 to 12 characters\n2-the password must contain an uppercase letter\n3-the password must contain a special character\n4-the password must contain numbers")
                print("for student 1st character of the password must be s \n for teacher the 1st character of password must be t\n for admin the 1st character of password must be a")
                temp2 = input("reset the password:")
                if len(temp2)>=6 and len(temp2)<=12:
                    f=1
                    for i in temp2:
                        if i.isupper():
                            f+=1
                            break
                    for i in temp2:
                        if i.isnumeric():
                            f+=1
                            break
                    for i in temp2:
                        if i.isalnum()==False:
                            f+=1
                            break
    else:
        print("the default username and password is wrong")
        break
    if f>0:
        if f==4:
            file = open("login.txt", 'a')
            l=[temp1,temp2]
            file.write(str(l) + "\n")
            break
        else:
            print("the password has not written according to the rules\nplease enter again")


def addStudent(id, name, grade, m1=0, m2=0, m3=0, m4=0, m5=0):
    file = open("students.txt", 'a')
    details = [id,name,grade,m1,m2,m3,m4,m5]
    file.write(str(details) + "\n")
    file.close()
    print(details)


def addTeachers(id, name, grade, subject):
    file = open("teachers.txt", 'a')
    my_text = [id,name,grade,subject]
    file.write(str(my_text) + "\n")
    file.close()

def searchstudent(id):
    try:
        file=open("students.txt","r")
        a=file.readlines()
        data=[i.strip() for i in a]
        file.close()
        for line in data:
            if str(id) in line:
                print(line)
    except:
        print("File Not Aviailabe")

def searchteacher(id):
    try:
        file = open("teachers.txt", "r")
        a = file.readlines()
        data = [i.strip() for i in a]
        file.close()
        for line in data:
            if str(id) in line:
                print(line)
    except:
        print("File Not Available")

def updatestudent(id,name,grade,m1,m2,m3,m4,m5):
    file=open("students.txt",'r')
    a = file.readlines()
    data = [i.strip() for i in a]
    for i,line in enumerate(data):
        if str(id) in line:
            data[i]=str([id,name,grade,m1,m2,m3,m4,m5])
    file=open("students.txt",'w')
    for i in data:
        file.write(i+"\n")

def updateteacher(id,name,grade,subject):
    file=open("teachers.txt",'r')
    a=file.readlines()
    data = [i.strip() for i in a]
    for i, line in enumerate(data):
        if str(id) in line:
            data[i] = str([id, name, grade,subject])
    file = open("teachers.txt", 'w')
    for i in data:
        file.write(i + "\n")

def studentlogin():
        while 1:
            print("=====welcome student=====")
            ch=input("press:\n1-search a student's details\n2-search a teacher's details")
            if ch=="1":
                id=input("enter the id of the student to be searched")
                searchstudent(id)
            elif ch=="2":
                id=input("enter the id of the teacher to be searched")
                searchteacher(id)
            ch=input("press E to go back to login page or press any key to continue again")
            if(ch=="E"):
                break

def teacherlogin():
    while 1:
        print("=====welcome teacher=====")
        ch=input("press:\n1-search a student's details\n2-search a teacher's details\n3-add a student's details\n4-update a student's details")
        if ch=="1":
            id = input("enter the id of the student to be searched")
            searchstudent(id)
        elif ch == "2":
            id = input("enter the id of the teacher to be searched")
            searchteacher(id)
        elif ch=="4":
            id=input("enter the id of the student to be updated")
            name=input("enter the name to be updated")
            grade=input("enter the grade to be updated")
            m1 = input("enter the new mark1")
            m2 = input("enter the new mark2")
            m3 = input("enter the new mark3")
            m4 = input("enter the new mark4")
            m5 = input("enter the new mark5")
            updatestudent(id,name,grade,m1,m2,m3,m4,m5)
        elif ch=="3":
            id = input("enter the id of the new student")
            name = input("enter the name of the new student")
            grade = input("enter the grade of the new student")
            m1 = input("enter the mark1")
            m2 = input("enter the mark2")
            m3 = input("enter the mark3")
            m4 = input("enter the mark4")
            m5 = input("enter the mark5")
            addStudent(id,name,grade,m1,m2,m3,m4,m5)
        else:
            print("wrong choice")
        ch = input("press E to go back to login page or press any key to continue again")
        if (ch == "E"):
            break

def adminlogin():
    while 1:
        print("=====welcome admin=====")
        ch = input("press:\n1-search a student's details\n2-search a teacher's details\n3-add a student's details\n4-add a teacher's details\n5-update a student's details\n6-update a teacher's details")
        if ch == "1":
            id = input("enter the id of the student to be searched")
            searchstudent(id)
        elif ch == "2":
            id = input("enter the id of the teacher to be searched")
            searchteacher(id)
        elif ch == "5":
            id = input("enter the id of the student to be updated")
            name = input("enter the name to be updated")
            grade = input("enter the grade to be updated")
            m1 = input("enter the new mark1")
            m2 = input("enter the new mark2")
            m3 = input("enter the new mark3")
            m4 = input("enter the new mark4")
            m5 = input("enter the new mark5")
            updatestudent(id, name, grade, m1, m2, m3, m4, m5)
        elif ch == "3":
            id = input("enter the id of the new student")
            name = input("enter the name of the new student")
            grade = input("enter the grade of the new student")
            m1 = input("enter the mark1")
            m2 = input("enter the mark2")
            m3 = input("enter the mark3")
            m4 = input("enter the mark4")
            m5 = input("enter the mark5")
            addStudent(id, name, grade, m1, m2, m3, m4, m5)
        elif ch=="4":
            id = input("enter the id of the new teacher")
            name = input("enter the name of the new teacher")
            grade = input("enter the grade of the new teacher")
            subj = input("enter the teaching subject")
            addTeachers(id,name,grade,subj)
        elif ch=="6":
            id = input("enter the id of teacher to be updated")
            name = input("enter the name of the teacher to be updated")
            grade = input("enter the grade of the teacher to be updated")
            subj = input("enter the teaching subject to be updated")
            updateteacher(id,name,grade,subj)
        else:
            print("wrong choice")
        ch = input("press E to go back to login page or press any key to continue again")
        if (ch == "E"):
            break


while(1):
    per1=input("enter your username")
    per2=input("enter your password")
    pl=[per1,per2]
    pll=str(pl)
    file = open("login.txt", 'r')
    a = file.readlines()
    dat = [i.strip() for i in a]
    if pll in dat:
        if per2[0]=="s":
            studentlogin()
        elif per2[0]=="t":
            teacherlogin()
        elif per2[0]=="a":
            adminlogin()
        else:
            print("warning!!!!!")
        ch=input("press STOP to stop the management system or press any key to login again")
        if ch=="STOP":
            print("THANK YOU AND HAVE A NICE DAY")
            break
    else:
        print("password is wrong\n please enter the password again")


















