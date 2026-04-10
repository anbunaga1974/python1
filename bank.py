ia=int(input("Enter initial account balance:"))
m=int(input("Enter mode of transaction(1.Deposit 2.Withdraw):"))
if m==1:
    d=int(input("Enter amount to deposit:"))
    if d>=1000 :
        u=ia+d
        print("Updated amount=",u)
    else:
        print("Amount can not deposit")
        print("Updated amount=",ia)
elif m==2:
    w=int(input("Enter amount to withdraw:"))
    if w<ia:
        u=ia-w
        if u>=1000:
            print("Updated amount=",u)
        else:
            print("Amount can not withdraw")
            print("Updated amount=",ia)
    else:
        print("Amount can not withdraw")
        print("Updated amount=",ia)
else:
    print("Invalid choice")
