def game():
    import random
    #defining level
    def level(level,n,turn):
        ran=random.randint(0,n)
        print('Level -',level)
        j=1
        while j<=3:
            num=int(input(f'Enter any number from 0 to {n} : '))
            if num in range(n+1):
                if num>ran:
                    print('The correct number is less than you entered!! ')
                    j+=1
                elif num<ran:
                    print('The correct number is more than you entered!! ')
                    j+=1
                elif num==ran:
                    print('Bravo!! you have won the game!!')
                    ask=input('Do you want to continue ahead : Yes(Press Y)/No(Press N)----->')
                    if ask=='y' or ask=='Y':
                        print('Great choice !! :) :)')
                        menu()
                    elif ask=='n' or ask=='N':
                        print('Thanks for playing our game!!')
                        break
        else :
            print('You lose the Game!! :(:(')
            print('The correct answer was ,',ran)
            ask=input('Do you want to continue ahead : Y/N----->')
            if ask=='y' or ask=='Y':
                print('Great choice !! :) :)')
                menu()
            elif ask=='n' or ask=='N':
                print('Thanks for playing our game!!')
    #defining main menu.           
    def menu():
         print('Press 1 for easy level')
         print('Press 2 for medium level')
         print('Press 3 for hard level')
         ch_level=int(input('Enter which level you want to play : '))
         if ch_level==1:
            level(1,9,3)
         elif ch_level==2:
            level(2,16,4)
         elif ch_level==3:
            level(3,30,5)
         else:
            print('Invalid input')
    menu()    
    #levels choice1

        
        


        

