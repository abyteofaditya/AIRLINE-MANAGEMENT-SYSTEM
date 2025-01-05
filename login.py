
import pickle
import random

def add_user():
    dir_1 = "data/login"
    a=input("User Name:")
    b=input("Contact number:")
    c=input("Valide email Id:")
    d=input("Kindly enter a login password:")
    d={"U1":a,"B2":b,"C3":c,"D4":d}
    with open(dir_1,"ab") as f:
        pickle.dump(d,f)

def modify_1(a,b,c):
    L=[]
    dir_1 = "data/login"
    with open(dir_1,"rb") as f:
        rec=pickle.load(f)
        L.append(rec)
        while True:
            try:
                for i in range (len(L)):
                     if L[i]['U1']==a:
                        if c=='1':                       
                            L[i]['B2']=b
                        elif c=='2':
                            L[i]['C3']=b
                        elif c=='3':
                            L[i]['U1']=b
                        elif ch=='4':
                            L[i]['D4']=b
                     else:
                        print("Either password or username incorrect")
            except EOFError:
                break  
            with open(dir_1,"wb") as f:
                for i in L:
                    pickle.dump(i,f)
            break

                        

def update_user():
    a=input("Enter your user name:")
    b=input("Enter your password:")
    f=True
    dir_1 = "data/login"
    with open(dir_1,"rb") as f:
        while True:
            try:
                rec=pickle.load(f)
                if rec['U1']==a and rec['D4']==b:
                    print("Welcome",a)
                    f=True
                    print("Authentication Succesful")
                    print("What you want to change ?\n\
                          1.Contact Number\n\
                          2.Email Id\n\
                          3.user name\n\
                          4.password")
                    ch=int(input("Enter choice:"))
                    if ch==1:
                        c='1'
                        b=input("New Contact number:")
                        modify_1(a,b,c)
                        break
                    elif ch==2:
                        c='2'
                        b=input("Email-ID:")
                        modify_1(a,b,c)
                        break
                    elif ch==3:
                        c='3'
                        b=input("New User Name:")
                        modify_1(a,b,c)
                        break
                    elif ch==4:
                        c='4'
                        b=input("New Password:")
                        modify_1(a,b,c)
                        break
                    else:
                        print("Invalid Input")
                        break

            except EOFError:
                break
        if f==False:
            print("Either password or user name incorrect")

def p_1():   
    a=input("Username:")
    b=input("Password:")
    f=False
    dir_1 = "data/login"
    with open(dir_1,"rb") as f:
        while True:
            try:
                r=pickle.load(f)
                if r['U1']==a and r['D4']==b:
                    print("Authentication Successful Welcome",a)
                    print("-"*10)
                    print("Contact Number",r['B2'])
                    print("Email Id",r['C3'])
                    f=True
                    break
                    
            except EOFError:
                break
    if f==False:
        print("Invalid Password or user name")

def trv_1():
    a=input("Username:")
    b=input("Password:")
    dir2="data/trv"
    L=[]
    ctr=0
    with open(dir2,"rb") as f:
        while True:
            try:
                r=pickle.load(f)
                for i in r:
                    if i[0]==a and i[1]==b:
                        L.append(i)

            except EOFError:
                break
            if L!=[]:
                k=1
                print("Previous Travel details with us:-")
                print("--------------------------------------")
                for z in L:
                    print(k,'.',"     ",z[2])
                    print("         ",z[3])
                    print("         ",z[4])
                    print("         ",z[5])
                    print()
                    k=k+1
                print("--------------------------------------")
            else:
                 print(" We dont have any previous Travel History related to your account")




def menue2_1():        
    d=dict()
    print("Main Menue:\n\
    1.Add new user\n\
    2.Update user details\n\
    3.Profile Login\n\
    4.To get Your previous Travel History \n\
    5.Exit")
    while True:
        print()
        ch=int(input("Kindky enter the choice:"))
        print()
        if ch==1:
            add_user()
        elif ch==2:
            update_user()
        elif ch==3:
            p_1()
        elif ch==4:
            trv_1()
        elif ch==5:
            break
    return 0


        

    
        
        

        
