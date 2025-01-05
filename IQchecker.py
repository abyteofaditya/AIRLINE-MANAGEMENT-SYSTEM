def IQ():
    import time
 
    #introduction
    print("Welcome !!!!!!! To tripple Alpha Antio IQ Testing services")

    print("Rules of the game are:")
    age=int(input('Enetr your age : ')) 
    print("1.Iq test initiation.......")

    print("2. you will get +10 for ever correct answer....")

    print("3. you will get -3 point for each wrong one")

    print("wait preparing the test.............")

    print("Kindly answer the following questions .......")



    #ques 1

    d=eval(input("Q1. what is (365*8*9)/72 ..............waiting for your respnse............."))

    if d==365:
        print("Wow!!! you scored 10 points")
        u=10

    else:
        print("Sorry nice try....... you got -3 points ")
        u=-3


    # ques2
    print("Time for next question.......")




    t=eval(input("Q2.how many squares are there in chessboard of 8 X 8 ......................."))

    if t==204:
        print("Congo,you scored one more point")
        pt1=10

    else:
        print("sorry try next time")
        pt1=-3

    # ques 3
    print("time for next question.......")

    ques3=eval(input("Q3.Gueses the pattern in the following: 37, 34, 31, 28 _____"))

    if ques3==25:
        print(" You are a champion..... congragulations scored one more point")
        pt3=10
    else:
        print("sorry nice try ")
        pt3=-3

    #result


    print("Time for results....................calculating..........")


    total=u+pt1+pt3

    if 25<=total>=30:
        print("congo you are a genius....Your score is",total)

    else:
        print("Sorry try next time its just a test dont take it seriously...........your score",total)
    

    print("Time to get you IQ score")

    IQ= (age/12)*100

    print("Your IQ is",IQ)

    print("Thank you .................. Bye Bye............")


   
    





