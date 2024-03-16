def ATM():
    username=["teju","bindu","ramtej"]
    password=["teju05","bindu12","ramtej22"]
    pin=[1111,2222,3333]
    bal=[5000,2000,3000]
    print("Enter the Username:")
    userid=input() 
    if userid in username:
        ind=username.index(userid)
        print("Enter Password: ")
        passid=input()
        flag=0
        if passid != password[ind]:
            print("Wrong password entered ,2 more chances left")
            print("ReEnter Password: ")
            passid=input()
            if passid != password[ind]:
                print("Wrong password entered ,1 more chance left")
                print("ReEnter Password: ")
                passid=input()
                if passid != password[ind]:
                    print("Wrong password,Account blocked")
                else:
                    flag=1
            else:
                flag=1
        else:
            flag=1
        if flag==0:
            print("***End***")
            exit()
        else:
            print("1.Withdraw")
            print("2.Deposit")
            print("3.CheckBalance")
            print("4.Change Password")
            print("Enter your choice: ")
            while(1):
                choice=int(input())
                if choice in [1,2,3,4]:
                    break
                else:
                    print("Please enter Valid Choice,Renter Choice")
            if(choice==1):
                withdraw(bal,ind,pin)
            elif(choice==2):
                deposit(bal,ind,pin,username)
            elif(choice==3):          
                checkbalance(pin,ind,bal)
            elif(choice==4):
                changepassword(pin,ind)
    else:
        print("Invalid User")
        exit()
def changepassword(pin,ind):
    print("Password Change Process:")
    print("Enter pin")
    pinid=int(input())
    if pinid==pin[ind]:
        print("Enter New Password: ")
        newpass=input()
        print("Confirm Password : ")
        while(1):
            conpass=input()
            if(newpass==conpass):
                print("Password of account has been Updated Sucessfully")
                break
            else:
                print("Please reenter the Confirm Password correctly")
    else:
        print("Invalid Pin")
        print("***End***")
        exit()

def withdraw(bal,ind,pin):                      
    print("Enter the Amount of Withdrawl: ")
    with1=int(input())
    print("Enter pin")
    pinid=int(input())
    if pinid==pin[ind]:
        if with1<=bal[ind]:
            bal[ind]=bal[ind]-with1
            print("Collect You Amount",with1)
            response(bal,ind)
        else:
            print("Isufficient Balance")
    else:
        print("Invalid Pin")
        print("___End___")
        exit()  

def deposit(bal,ind,pin,username):
                print("Enter the Amount of Deposit: ")
                deposit1=int(input())
                print("Enter pin")
                pinid=int(input())
                if pinid==pin[ind]:
                    bal[ind]=bal[ind]+deposit1
                    print("Amount ",deposit1," is Added to your account",username[ind])
                    response(bal,ind)
                else:
                    print("Invalid Pin")
                    print("___End___")
                    exit()

def checkbalance(pin,ind,bal):
                print("Enter pin")
                pinid=int(input())
                if pinid==pin[ind]:
                    response(bal,ind)
                else:
                    print("Invalid Pin")
                    print("___End___")
                    exit()

def response(bal,ind):
    print("Check Your Balance (yes or no):")
    while(1): 
        resp=input()
        if(resp=="yes"):
            print("Current Balance : ",bal[ind])
            break
        elif(resp=="no"):
            print("Thank You!")
            print("___End___")
            exit()
        else:
            print("Please Enter Any of Above 2 options") 

def strongpass():
    pass

ATM()