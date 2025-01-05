import time
import pickle
from book import*
from cancellation import*  
from Game_1 import*
from IQchecker import*
from login import*
from service import*


def adv():
      print("....................................................................................................................................................")
      print("....................................................................................................................................................")
      print("------------------------------------------------------------Alpha Antio Airlines Pvt.Ltd.-----------------------------------------------------------")
      print("....................................................................................................................................................")
      print("....................................................................................................................................................")
      print()
      print("✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈   Welcome to the world of  Alpha Airlines  ✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈")
      print()
      print("Flying Like Maharaja")
      print("Carry More Pay Less")
      print("Get Upto 20 % discount on your first booking from our airlines !!")
      print()
      print("For any complaints or queries kindly contact our 24/7 customer care number 8598XXXXXX")
      print("We would be glad to hear your feedback")
      print()


def menue():
      print("----------------------------------✈✈✈✈✈✈✈✈✈✈✈✈✈✈✈---------------------------------------------")
      while True: 
          print()
          print()
          print("⚪ MAIN  MENUE")
          print("______________________________________________________________________________________________________")
          print("1. To know more about us.")
          print("2.For Booking with our amazing airlines ")
          print("3.Relieve your stress by playing our games")
          print("4.For cancelling your ticket")
          print("5.Manage Your Booking ")
          print("6.Web Checkin and to print boarding pass")
          print("7.To manage your airline profile")
          print("8.Exit.")
          print("_____________________________________________________________________________________________________")          
          choice=int(input('Kindly enter you choice in numeric codes : \n'))
# choice 1
          if choice==1:
             dir1="data/abt.txt"
             f = open('data/abt.txt', 'r')
             k=f.readlines()
             for i in k:
                print(i,end='')
             f.close()
# choice 2

          elif choice==2:
             k=groupST()
             if k==0:
                 menue()
# choice 3

          elif choice==3:
             print("Hmmmm Seems you have lot of stress ......Now is the time to chill out under our amazing Games")
             print('Press 1 for playing RANDOM NUMBER GENERATOR GAME.')
             print('Press 2 for playing IQCHECKER GAME.')
             ch=int(input())
             if ch==1:
                 game()
             elif ch==2:
                 IQ()
             else:
                 print('Ohh!! seems You have lot of stress kindly look at the option once more !!!')

# Choice 4
          elif choice==4:
               k=menu_1()
               if k==0:
                menue()

# choice 5

          elif choice==5:
             k=serv_1()
             if k==0:
                menue()
               
# Choice 6                                                                              
                       
          elif choice==6:
                L2=[]
                p_1=input("Kindly PNR of the ticket:")
                dir2="data/boarding"
                k=0
                with open(dir2,"rb") as f1:
                   r=pickle.load(f1)
                for i in r:
                     L2.append(i)
                     if i!=[] and i[5]=='▶ PNR Number for this ticket :'+ p_1:
                         print()
                         print()
                         print(">->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->>->->->->->->->->->->->->->->->>->->->->->->->->->->->->->->->->->->->")
                         print(">                                                                                                                                         >")
                         print(">                                                               BOARDING PASS                                                             >")
                         print(">                                                                                                                                         >")
                         print(">->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->>->->->->->->->->->->->->->->->>->->->->->->->->->->->->->->->->->->")
                         for z in i :
                            if i.index(z) not in [11,12,len(i)-1]:
                               print(z)
                         k=1
                         break
                if k==0:
                   print("No booking Found for this PNR")
                  
          elif choice==7:
              k=menue2_1()
              if k==0:
                 menue()
                          
# choice 7                               
          elif choice==8:
            print("Quitting.......")
            print('Successfully Quitted!!')
            print()
            print("Thank You For choosing our Airlines !!!")
            print("Have a great Day")
            print()
            print("---------------------------------------------------------------------------------------------------------------------------------------")
            print("-----------------------------------------------Thank You For choosing Alpha Antio Airlines Pvt.Ltd.------------------------------------")             
            print("---------------------------------------------------------------------------------------------------------------------------------------")

            break
          else:
               print("Invalid Input ,Try again!!")


