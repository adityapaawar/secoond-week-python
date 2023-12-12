#write a program to perform banking transaction operations: withdrawal, deposit
#and check balance, follow the constraint:
#1. initial balance amount should be 1000
#2. Maintain minimum balance in account always:1000 Rs


def withdrawl(cBalance):
    if cBalance==1000:
        print("Transcation Failed, Low Balance")
        return
    am=int(input("Enter amount: "))
    if am>cBalance-1000:
        print(f"You are only allow to withdrawl {cBalance-1000}")
    else:
        cBalance=cBalance-am
    return cBalance

def deposit(cBalance):
    am=int(input("Enter amount: "))
    cBalance+=am
    return cBalance
    
def checkBalance(cBalance):
    print(f"Your Current Balance is: {cBalance}")
cBalance=1000
while 1:
    print()
    print("*Options*")
    print("1 Withdrawl")
    print("2 Deposit")
    print("3 Check Balance")
    print("4 Exit")

    inp=int(input("Enter your choice: "))
    
    if inp==1:
        cBalance=withdrawl(cBalance)
    elif inp==2:
        cBalance=deposit(cBalance)
    elif inp==3:
        checkBalance(cBalance)
    elif inp==4:
        break
    else:
        print("Wrong Input")
    
