print("Central Bank of India")
balance=500
restart=('y')
chance=3
while chance>=0:
    pin=int(input("Enter your pin"))
    if pin==1213:
        while restart not in ('n','N','NO','no'):
            print("Type 1 for balance check:")
            print("Type 2 for balance withdrawal")
            print("Type 3 to pay in")
            print("Type 4 for exit")
            option=int(input())
            if option==1:
                print("Balance is:",balance,'\n')
                restart=input("would you want to move back")
                if restart in ('n','N','NO','no'):
                    print("thank you")
                    break
            elif option==2:
                withdrawl=int(input("How much would you like to withdraw?\n10/50/100/200/500"))
                if withdrawl in [10,50,100,200,500]:
                    balance=balance-withdrawl
                    print("\nyour balance is now:",balance)
                    restart = input("would you want to move back")
                    if restart in ('n', 'N', 'NO', 'no'):
                        print("thank you")
                        break
                elif withdrawl !=[10,50,100,200,500]:
                    print("please enter valid amount\n")
                    restart=('y')
            elif option==3:
                payin=int(input("Enter the amount:"))
                balance=balance+payin
                print("\nNew balance is: ",balance)
                restart = input("\nwould you want to move back")
                if restart in ('n', 'N', 'NO', 'no'):
                    print("thank you")
                    break
            elif option==4:
                print("Thank you for you service")
                break
            else:
                print("please enter a correct number.\n")
                restart=('y')
    elif pin !=1213:
        print("Incorrect password")
        chance=chance-1
        if chance == 0:
            print("\nNo more tries")
            break
