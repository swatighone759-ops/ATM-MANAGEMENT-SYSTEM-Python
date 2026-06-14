balance = 2340974702000000
def Check_Balance():
    
    print(f"Total Balance = {balance}")

def Deposit_money():
    deposit_money = int(input("Enter Deposit :- "))
    print(f"{deposit_money} Has been deposited successfully...")
    print(f"New balance = {(balance)+(deposit_money)}")

def Withdraw():
        
    Withdraw = int(input("Enter Amount :-"))
        
    if Withdraw > balance:
        print("You Dont Have Enough Money,Withdraw amount is greater than your balance")
                  
    else:
        print(f"{Withdraw} cash has been withdraw")
        print(f"Remain Amount = {balance - Withdraw}")


attempts = 0      
while attempts<=2:
        attempts = attempts+1
        print("\n.....Welcome To ATM.....")
        print("1. Check Balance.")
        print("2. Deposit Money.")
        print("3. Withdraw Money.")
        print("4. Exit.")
                
        choice = int(input("Enter your choice : "))

        if choice == 1:
            Check_Balance()

        elif choice == 2:
            Deposit_money()

        elif choice == 3:
            Withdraw()
            continue

        elif choice == 4:
            print("Thank you for using our ATM...")
            break
 
        else:
            print("Invalid Choice!!!!!")
                


    

