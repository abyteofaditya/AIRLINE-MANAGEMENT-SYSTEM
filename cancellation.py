#cancel
import time
import random
import pickle


def board_1(p_1):
   global k1
   L2=[]
   z=0
   dir2="data/boarding"
   with open(dir2,"rb") as f1:
      r=pickle.load(f1)
   for i in r:
      L2.append(i)
      if i!=[] and i[5]=='▶ PNR Number for this ticket :'+ p_1:
         a=L2.index(i)
         L2.pop(a)
         z=z+1
   if z>0:   
      with open(dir2,"wb") as f1:
         pickle.dump(L2,f1)
   k1=0




def log_1(c,d,p_1):
   global k2
   L3=[]
   k=0
   dir3="data/trv"
   with open(dir3,"rb") as f1:
      r=pickle.load(f1)
   for i in r:
      L3.append(i)
      if i[0]==d and i[1]==c and i[2]=='▶ PNR Number for this ticket :'+ p_1:
         a=L3.index(i)
         L3.pop(a)
         k=k+1

   if k>0:      
       with open(dir3,"wb") as f1:
          pickle.dump(L3,f1)
      
   k2=0

def menu_1():
   ctr=0
   L1=[]
   z=0
   p_1=input("Enter the PNR of the ticket:")
   dir1="data/pasng"
   with open(dir1,"rb") as f:
      r=pickle.load(f)
   k=0
   op=0
   for i in r:
       L1.append(i)
       if i!=[] and i[2]=='▶ PNR Number for this ticket :'+ p_1:
          a=L1.index(i)
          k=1
          if i[-1]!=0 and i[-2]!=0:
             c=i[-1] # user password
             d=i[-2] #user ID
             op=1
             print("welcome",i[-2])
          print("---------------------------------")
          print("Details Of the Journey:-")
          for z in range(1,len(i)-2):
             print(i[z])
             z=z+1
          print("---------------------------------")
          break
   if z==0:
      print("No booking found for the given PNR")
   else:
      print("As our Airline is new so we have Full refund Cancellation Policy !!!")
      ch2=input("Are you sure you want to cancel your ticket ----- enter (y/n):")
      if ch2=='y'or ch2=='Y':
          L1.pop(a)
          with open(dir1,"wb") as f:
             pickle.dump(L1,f)
          board_1(p_1)
          if op==1:
             log_1(c,d,p_1)
          if k1==0 and k2==0:
             print("Your Ticket has been cancelled Successfully:")
          
      elif ch2=='n' or ch2=='N':
           pass              
   return 0
