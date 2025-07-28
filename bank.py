acc={101:10000,102:40000,103:5000}

acno=int(input("enter acc.no:-"))
mode=input("enter the mode of transaction(w/d/b/i):")
if mode != 'b':
    amt=int(input("enter amount:"))

if acc.get(acno)!=None:
    if mode=='w':
        if amt<=acc[acno]:
            acc[acno]-=amt
            print("available balance after withdrawl:",acc[acno])
        else:
            print("insufficient balance")
    elif mode=='d':
        acc[acno]+=amt
        print("total available balance after deposit:",acc[acno])
    elif mode=='b':
        print("available balance:",acc[acno])
    else:
        print("invalid option!!")
elif mode=='i':
    acc[acno]=amt
    print("new account created!!")
    print("avilable balnce in new account:",acc[acno])
else:
    print("invalid option")