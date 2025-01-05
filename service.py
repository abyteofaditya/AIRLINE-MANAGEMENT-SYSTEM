import pickle
import random

def ct_ext(p_1):
    global k
    dir2="data/boarding"
    with open(dir2,"rb") as f:
        r=pickle.load(f)
    for i in r:
        if i[5]=='▶ PNR Number for this ticket :'+ p_1:
            ct=i[-1]
            return ct

def cl_1(p_1,c3,ed):
    L2=[]
    global k_1
    dir2="data/boarding"
    with open(dir2,"rb") as f:
        r=pickle.load(f)
    print()
    for i in r:
        L2.append(i)
        if i[5]=='▶ PNR Number for this ticket :'+ p_1:
            z=L2.index(i)
            ct=i[-1]
            L2.pop(z)
            print("Your initial Ticket price is: $",ct)
            k_1=int(ct)+int(c3)
            print("Your New Ticket Price after Upgradation: $",k_1)
            i[-1]=k_1
            i[1]=ed
            L2.append(i)
    print()
            
    with open(dir2,"wb") as f:
        pickle.dump(L2,f)

def ml_1(p_1,ed):
    L2=[]
    dir2="data/boarding"
    with open(dir2,"rb") as f:
        r=pickle.load(f)
    for i in r:
        L2.append(i)
        if i[5]=='▶ PNR Number for this ticket :'+ p_1:
            z=L2.index(i)
            L2.pop(z)
            i[-7]=ed
            L2.append(i)
    with open(dir2,"wb") as f:
        pickle.dump(L2,f)


    
def serv_1():
    L1=[]
    k=1
    dir1="data/pasng"           
    while True:
        print()
        print("We are offering Following additional Upgradation:\n\
        1. Upgrade Your Travelling Class\n\
        2. Add Complimentary Meals\n\
        3. Wheelchair assistance required\n\
        4. Go back to Main Menue")              
        ch=int(input("kindly enter Upgradation choice:"))
        if ch!=4:
            p_1=input("Kindly enter PNR number of the passneger:")
            with open(dir1,"rb") as f:
                    r=pickle.load(f)
            for i in r:
                L1.append(i)
                if i!=[] and i[2]=='▶ PNR Number for this ticket :'+ p_1:
                    k=L1.index(i)
                    L1.pop(k)            
                    print("Current passenger details:-")
                    print("------------------------------------")
                    for z in range(1,len(i)-2):
                        print(i[z])
                    print("------------------------------------")
                    print()
                    break
        if ch==1:
            print("Kindly enter your travelling class in numeric codes:\n\
            1.First Class\n\
            2.Buisness Class\n\
            3.Premium Economy")
            while True:
                class_1=int(input("Kindly enter your travelling class in numeric codes:-"))
                if class_1==1:
                    k=0
                    ed='▶ Travelling Class: First Class'
                    c3=int(40000/80)
                    c1=int(ct_ext(p_1))
                    ct=str(c1+c3)
                    i[-4]=ed
                    i[7]='▶ Total Ticket Price:$'+ct
                    break
                elif class_1==2:
                    k=0
                    ed='▶ Travelling Class: Buisness Class'
                    c3=int(20000/80)
                    c1=int(ct_ext(p_1))
                    ct=str(c1+c3)
                    i[-4]=ed
                    i[7]='▶ Total Ticket Price:'+'$'+ct
                    break
                elif class_1==3:
                    k=0
                    ed='▶ Travelling Class: Premium Economy'
                    c3=int(12000/80)
                    c1=int(ct_ext(p_1))
                    i[-4]=ed
                    ct=str(c1+c3)
                    i[7]='▶ Total Ticket Price:'+'$'+ct
                    break
                else:
                    print("Invalid Input")
            if k==0:
                L1.append(i)
                with open(dir1,"wb") as f:
                        pickle.dump(L1,f)
                        cl_1(p_1,c3,ed)
            
            
        
        elif ch==2:
            print()
            print(" Kindly note for all inetrnational and domestic flights more that 2 hrs we offer north indian Thali to all passengers")
            print()
            print("These are the additional meals that we offer:\n\
            1.Strict Vegetarian Keto Diet\n\
            2.Hyderabadi Biriyani\n\
            3.Non Vegetarian Thali")
            k1=1
            while True:
                ch1=int(input("Kindly enter your additional meal preference in numeric codes:"))
                print()
                if ch1==1:
                    k1=0
                    ed='▶ Complimentary Meals : Strict Vegetarian Keto Diet '
                    i[-5]=ed
                    break
                elif ch1==2:
                    k1=0
                    ed='▶ Complimentary Meals : Hyderabadi Biriyani'
                    i[-5]=ed
                    break
                elif ch1==3:
                    k1=0
                    ed='▶ Complimentary Meals : Non Vegetarian Thali'
                    i[-5]=ed
                    break
                else:
                    print("Invlid Input")
            if k1==0:
                L1.append(i)
                with open(dir1,"wb") as f:
                        pickle.dump(L1,f)
                        ml_1(p_1,ed)
                print()
                print("Your Meal preference has been updated")
                print()
        
        elif ch==3:
            while True:
                    print("We are having wheelchair assistance with us if you want more advanced methods \n\
                    like stretcher, mobile ambulance .....kindly contact our 24/7 Helpline Number 8598XXXXX")
                    ch=int(input("If you want wheelchair assistance press 1 or else press 2:"))
                    if ch==1:
                        k3=0
                        i[-6]='▶ Medical Assistance: Wheelchair'
                        L1.append(i)   
                        with open(dir1,"wb") as f:
                                pickle.dump(L1,f) 
                        L2=[]
                        dir2="data/boarding"
                        with open(dir2,"rb") as f:
                            r=pickle.load(f)  
                            for i in r:
                                L2.append(i)
                                if i[5]=='▶ PNR Number for this ticket :'+ p_1:
                                    z=L2.index(i)
                                    L2.pop(z)
                                    i[-6]='▶ Medical Assistance : Wheelchair'
                                    L2.append(i)
                        with open(dir2,"wb") as f:
                            pickle.dump(L2,f)
                        print("Medical Assistance Updated Successfully")
                        break
                    else:
                        break
        elif ch==4:
            break
        
    return 0



