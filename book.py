import random
import pickle
from datetime import datetime
def boarding():
    dir4="data/boarding"
    seat = str(random.randint(1, 21))
    characters = ['A', 'B', 'C', 'D']
    k = random.choice(characters)
    k_1 = f"|___{k}___________✈︎ Alpha Antio Airlines ✈︎________{k}_________|"
    k_2 = "|⚪ Passenger Details  :                                                  |"
    k_3 = f" ▶ Name              : {name:<44}|"
    k_4 = f" ➡ {name:<60}"
    k_5 = f" ▶ Co-traveler Details : {x:<40}|"
    k_6 = f" ➡ There are {x} people accompanying you. Their details are fed into the server under your name"
    k_7 = ap
    k_8 = ap1
    k_11 = f" ▶ {'':^18} : {date_1:<42}|"
    k_12 = f" ➡ {date_1:<60}"
    k_13 = f" ▶ Seat Number       : {seat + k:<43}|"
    k_14 = f" ➡ {seat + k:<60}"
    k_15 = f"|___{k}___________✈︎ Alpha Antio Airlines ✈︎________{k}_________|"

    L2=[k_1,ag,k_2,k_3,k_4,p_1,k_5,k_6,k_7,k_8,k_11,U1,U2,k_12,ml_1,wh_1,k_13,k_14,k_15,lk_1,ct]
    with open(dir4,"rb") as f:
        r=pickle.load(f)
        r.append(L2)
        
    with open(dir4,"wb") as f:
        pickle.dump(r,f)     
def groupST():
    import time
    import pickle
    global U1
    global U2
    import random
    global lk_1
    global ml_1
    global wh_1
    global l3
    global name
    global adh
    global ap
    global ap1
    global ag
    global m
    global date_1
    global d
    global p_1
    global T
    global ct
    global a
    global x   
    print()
    name=input("Kindly enter The  name of the Key Person:")
    name_1='▶ Name of the person : '+ str(name)
    print()
    print("Kindly mention your fare type  :\n 1. Senior Citizen\n 2.Armed Officer\n 3.Student\n 4.Normal\n:")
    cl_1=int(input("Kindly input in numeric codes:"))
    if cl_1==1:
        fl_2='▶ Passenger Type:Senior Citizen'
    elif cl_1==2:
        fl_2='▶ Passenger Type:Armed Force'
    else:
        fl_2='▶ Passenger Type:Students'
    print()
    adh=input("Kindly enter your 10 digit aadhar Card number/Pasport number:")
    adh_1='▶ Adhar/Passport Number of the key Person:'+str(adh)
    print("Kindly wait till we are verifying your details..................................................")
    print("we have verifed your details")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------")
    #Departure
    print()
    print("Kindly enter the details of Departure Airport")
    print("Kindly enter '1' for Domestic and '2' for International:")
    print("1.Domestic Flights\n2.International Flight")
    I_1=int(input("Kindly enter the choice:"))
    print("Kindly wait till we are searching for flights:")
    print()
    dir3='data/airports.txt'
    if I_1==1:
        f=open(dir3,'r')
        print(f.read(330))
        s_1=int(input("Kindly enter the choice for the state of departure :"))
        c1=random.randint(4000,15000)
        if s_1==1:
           print("Ok! You have opted for Chhatrapati Shivaji Maharaj International Airport Mumbai")
           ap='▶Departure Airport: Chhatrapati Shivaji Maharaj International Airport Mumbai'   
        elif s_1==2:
            print("Ok! You have opted for Indira Gandhi International Airport New Delhi")
            ap='▶ Departure Airport :Indira Gandhi International Airport New Delhi'
        elif s_1==3:
            print("Ok! You have opted for Netaji Subhash Chandra Bose International Airport")
            ap='▶ Departure Airport: Netaji Subhash Chandra Bose International Airport Kolkata'
        elif s_1==4:
            print("Ok! You have opted for Kempegowda International Airport Bengaluru")
            ap='▶ Departure Airport:Kempegowda International Airport Bengaluru Karnataka'
        else:
            print("Ok! You have opted for Madras International Airport Chennai")
            ap='▶ Departure Airport:Madras International Airport Chennai'
            print()
        f.close()
    else:
         print("Kindly wait till we are searching for International flights:")
         f=open(dir3,'r')
         f.read(321)
         print(f.read())
         print("Kindly wait till we are searching for flights:")
         print("We are having services in following countries................")
         n_2=int(input("Kindy enter your destination country in numeric codes:"))
         c1=random.randint(80000,150000)
         if n_2==1:
            ap='▶ Departure Airport :Loss Angeles International Airport'
            print("Ok! You have opted for Loss Angeles International Airport")
         elif n_2==2:
          ap='▶ Departure Airport: Winnipeg International Airport'
          print("Ok! You have opted for Winnipeg International Airport")
         elif n_2==3:
          ap='▶ Departure Airport: Mexico City International Airport'
          print("Ok! You have opted for Mexico City International Airport")
         elif n_2==4:
          ap='▶ Departure Airport: Juan Santamaría International Airport costa Rica'
          print("Ok! You have opted for Juan Santamaría International Airport")

         elif n_2==5:
          ap='▶ Departure Airport: São Paulo/Guarulhos International Airport Brazil'
          print("Ok! You have opted for São Paulo/Guarulhos International Airport")

         elif n_2==6:
            print("Ok! You have opted for Zurich International airport")
            ap='▶ Departure Airport: Zurich International airport'
         elif n_2==7:
            ap='▶ Departure Airport: Birmingham International Airport'
            print("Ok! You have opted for Birmingham International Airport")
         elif n_2==8:
             ap='▶ Departure Airport: Frankfurt International Airport'
             print("Ok! You have opted for Frankfurt International Airport")
         elif n_2==9:
           print("Ok! You have opted Narita International Airport Japan")
           ap='▶ Departure Airport: Narita International Airport Japan'

         elif n_2==10:
           print("Ok! You have opted Dubai International Airport")
           ap='▶ Departure Airport: Dubai International Airport'
         elif n_2==11:
           print("Ok! You have opted Singapore Changi Airport")
           ap='▶ Departure Airport: Singapore Changi Airport'
         elif n_2==12:
           print("Ok! You have opted Hong Kong International Airport")
           ap='▶ Departure Airport: Hong Kong International Airport'
         f.close()
         print()
         print()
         print("---------------------------------------------------------------------------------------------------------------------------------------------")
    time.sleep(1)
    #arrival
    print()
    print("Kindly enter the details of arrival Airport")
    print("Kindly enter 1 for domestic and 2 for international")
    print("1.Domestic Flights\n2.International Flight")
    I_1=int(input("KIndly enter the choice:"))
    time.sleep(0.3)
    print()
    if I_1==1:
        f=open(dir3,'r')
        print(f.read(321))
        s_1=int(input("Kindly enter the choice for the state of departure :"))
        c2=random.randint(4000,15000)
        if s_1==1:
           print("Ok! You have opted for Chhatrapati Shivaji Maharaj International Airport Mumbai")
           ap1='▶Arrival Airport: Chhatrapati Shivaji Maharaj International Airport Mumbai'
        elif s_1==2:
            print("Ok! You have opted for Indira Gandhi International Airport New Delhi")
            ap1='▶ Arrival Airport :Indira Gandhi International Airport New Delhi'
        elif s_1==3:
            print("Ok! You have opted for Netaji Subhash Chandra Bose International Airport")
            ap1='▶ Arrival Airport: Netaji Subhash Chandra Bose International Airport Kolkata'
        elif s_1==4:
            print("Ok! You have opted for Kempegowda International Airport Bengaluru")
            ap1='▶ Arrival Airport:Kempegowda International Airport Bengaluru Karnataka'
        else:
            print("Ok! You have opted for Madras International Airport Chennai")
            ap1='▶ Arrival Airport:Madras International Airport Chennai'
            print()
        f.close()
    else:
         print("Kindly wait till we are searching for International flights:")
         f=open(dir3,'r')
         f.read(321)
         print(f.read())
         print("Kindly wait till we are searching for flights:")
         print("We are having services in following countries................")
         n_2=int(input("Kindy enter your destination country in numeric codes:"))
         c2=random.randint(80000,150000)
         if n_2==1:
            ap1='▶ Arrival Airport :Loss Angeles International Airport'
            print("Ok! You have opted for Loss Angeles International Airport")
         elif n_2==2:
          ap1='▶ Arrival Airport: Winnipeg International Airport'
          print("Ok! You have opted for Winnipeg International Airport")
         elif n_2==3:
          ap1='▶ Arrival Airport: Mexico City International Airport'
          print("Ok! You have opted for Mexico City International Airport")
         elif n_2==4:
          ap1='▶ Arrival Airport: Juan Santamaría International Airport costa Rica'
          print("Ok! You have opted for Juan Santamaría International Airport")
         elif n_2==5:
          ap1='▶ Arrival Airport: São Paulo/Guarulhos International Airport Brazil'
          print("Ok! You have opted for São Paulo/Guarulhos International Airport")
         elif n_2==6:
            print("Ok! You have opted for Zurich International airport")
            ap1='▶ Arrival Airport: Zurich International airport'
         elif n_2==7:
            ap1='▶ Arrival Airport: Birmingham International Airport'
            print("Ok! You have opted for Birmingham International Airport")
         elif n_2==8:
             ap1='▶ Arrival Airport: Frankfurt International Airport'
             print("Ok! You have opted for Frankfurt International Airport")
         elif n_2==9:
           print("Ok! You have opted Narita International Airport Japan")
           ap1='▶ Arrival Airport: Narita International Airport Japan'
         elif n_2==10:
           print("Ok! You have opted Dubai International Airport")
           ap1='▶ Arrival Airport: Dubai International Airport'
         elif n_2==11:
           print("Ok! You have opted Singapore Changi Airport")
           ap1='▶ Arrival Airport: Singapore Changi Airport'
         elif n_2==12:
           print("Ok! You have opted Hong Kong International Airport")
           ap1='▶ Arrival Airport: Hong Kong International Airport'
    f.close()
    print()    
    print("-----------------------------------------------------------------------------------------")
    print()
    time.sleep(1)
    current_date  = datetime.now()
    while True:
        date_input = input("Enter the travel date (Month Day format): ")
        date_tuple = date_input.split()

        if len(date_tuple) == 2:
            month, day = date_tuple
            try:
                current_date = datetime.now()
                datetime_str = f"{month} {day} {current_date.year}"
                datetime_obj = datetime.strptime(datetime_str, "%B %d %Y")

                if datetime_obj < current_date:
                    datetime_obj = datetime_obj.replace(year=current_date.year + 1)

                date_1 = '▶ Travelling date:-'+ datetime_obj.strftime("%d/%B/%Y")
                break
            except ValueError:
                print("Invalid date format. Use Month Day (e.g., January 1).")
        else:
            print("Invalid input. Please enter the date in Month Day format.")


    print("We are having Flights for this destination on",date_1,"at:-\n1.  11:00 a.m.\n2.  15:30 p.m.\n3.  21:45 p.m.\n4.  5:00 a.m.")

    ch=int(input("kindly enter the choice:"))
    if ch==1:
        t_1='▶ Boarding Time:-  11:00a.m.'
    elif ch==2:
        t_1='▶ Boarding Time:-  15:30 p.m.'
    elif ch==3:
        t_1='▶ Boarding Time:-  21:45 p.m.'
    else:
        t_1='▶ Boarding Time:-  5:00 a.m.'
    T=t_1
    print()
    print("Checking for availability of flights on this date..............................")
    time.sleep(0.3)
    print("We are having availability of following flights for this destination:")
    time.sleep(0.3)
    print()
    print("Now is the time to enjoy your flight with exclusive features only for you.................")
    time.sleep(0.3)
    class_1=int(input("Kindly enter your travelling class in numeric codes:\n1.First Class\n2.Buisness Class\n3.Premium Economy\n4.Economy\n:-"))
    if class_1==1:
        ag='▶ Travelling Class: First Class'
        c3=random.randint(200000,300000)
    elif class_1==2:
        ag='▶ Travelling Class: Buisness Class'
        c3=random.randint(50000,60000)
    elif class_1==3:
        ag='▶ Travelling Class: Premium Economy'
        c3=random.randint(7000,10000)
    else:
        ag='▶ Travelling Class: Economy'
        c3=random.randint(5000,10000)
    print()
    time.sleep(2)
#For more pasenger  
    print("---------------------------------------------------------------------------------------------------")
    time.sleep(0.3)
    x=int(input("Kindly enter how many more people are there:"))
    L1=[]
    for i in range (x):
          a=input("kindly enter The Name of Co-Traveller :")
          adh_2=input("Kindly Enter Aadhar/Passport Number:")
          p_2=random.randint(1000,100000)
          adh_3 = '▶ Co-Traveller Name: ' + str(a) + ', Passport Number: ' + str(adh_2) 
          L1.append(adh_3)
          print()
    print("Kindly wait till we are verifying idnetity of the passenger.......................................")
    time.sleep(0.3)
    print("The passenger has been verified:-")
    time.sleep(0.1)
    p_1='▶ PNR Number for this ticket :'+ str(random.randint(1000,100000)).lower()
    ml_1='▶ Complimentary Meals : North Indian Deluxe Thali '
    wh_1='▶ Medical Assistance : 	NIL '
    ch2=input("Do you have a registered ALpha Account book using that\n\
          to ger exciting discount upto 12%  ----- enter (y/n):")
    k=12
    if ch2=='y'or ch2=='Y':
       U1=input("Enter your username:")
       U2=input("Enter your password:")
       dir5="data\login"
       with open(dir5,"rb") as f:
            while True:
                try:
                    r=pickle.load(f)
                    if r['U1']==U1 and r['D4']==U2:
                        print("Authentication Successful Welcome",U1)
                        k=random.randint(10,15)
                        break
                    else:
                       k=0
                except EOFError:
                    break
    elif ch2=='n' or ch2=='N':
        U1=0
        U2=0
    ch1=int(input("Kindly enter  1 for 'Yes' To confirm Booking and 2 for 'No' to return to the main menue:"))
    if ch1==1:
        if x==0:
            ct=c1+c2+c3
            ct=ct+(k/100)*ct
            ct=(ct//80)
            lk_1="▶ Co-Traveller Name: NIL"
            cost_1='▶ Total Ticket Price:'+'$'+str(ct)
            b=["1",name_1,p_1,adh_1,fl_2,ap,ap1,cost_1,date_1,t_1,wh_1,ml_1,ag,lk_1,U1,U2]
            for i in range(1,(len(b)-2)):
                 print(b[i])
                 time.sleep(0.3)
        else:
            ct=x*(c1+c2+c3)
            ct=ct+(k/100)*ct
            ct=(ct//80)
            lk_1=L1
            cost_1='▶ Total Ticket Price:'+'$'+str(ct)
            b=["2",name_1,p_1,adh_1,fl_2,ap,ap1,cost_1,date_1,t_1,wh_1,ml_1,ag,lk_1,U1,U2]       # 2 code is for group Booking 
            for i in range(1,(len(b)-3)):
                 print(b[i])
                 time.sleep(0.3)
            print(*lk_1,sep="\n")   # short for of for loop it is used to display iterable charachter in new line
            print()
        confirmation = input("Do you want to confirm your booking (y/n): ")
        if confirmation.lower() == 'y':
            print("Your Ticket has been confirmed and an amount of  :$",ct,"has been deducted")
            dir1="data/pasng"
            with open(dir1,"rb") as f:
                r=pickle.load(f)
                r.append(b)
            f=open(dir1,"wb")
            pickle.dump(r,f)
            f.close()
            current_date = datetime.now().date()
            print("This is your confirmation recipt of ticket kindly come before 48 hrs of flight to get boarding pass")
            print()
            print("--------------------------------------------------------------------")
            print("----------------------Payment recipt--------------------------------")
            print("Customer Name: | ", name,"                                         |")
            print("Payment Amount:                  $",ct                               )
            print(" Transaction date :", current_date                                   )
            print("Payment Credited  to Alpha Antio Oriental Bank account:    119087621")
            print("--------------------------------------------------------------------")
            print()
            print("Kindly wait till we Finalize Your Booking ..........................")
            print()
            print("Boarding Pass can be accessed 48 hrs prior to departure by using your unique PNR Number")
            dir_2="data/trv"
            if U1!=0 and U2!=0:
                L_1=[U1,U2,p_1,ap,ap1,date_1]
                with open(dir_2,"rb") as f1:
                    r=pickle.load(f1)
                    r.append(L_1)
                with open(dir_2,"wb") as f1:
                   pickle.dump(r,f1)
            boarding()
        
        else:
            print("Press 1 to go back to main menue or 2 for more booking ")
            ch=int(input("Enter Choice:")) 
            if ch==1:
                print("-----------------------------------------------------------------------------------------------------------------------------------")
                print("-----------------------------------------Thank You For choosing Alpha Antio Airlines Pvt.Ltd.--------------------------------------")             
                print("-----------------------------------------------------------------------------------------------------------------------------------")
            else:
                groupST()
    else:
       print(" Redirecting to main menue............")
       print()    
    return 0



