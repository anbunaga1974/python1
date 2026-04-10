s=int(input("Enter Employee salary:"))
n=int(input("Enter no. of days absent:"))
if n>2:
    fs=s-((n-2)*500)
    print("Final salary:",fs)
else:
    print("Final salary:",s)
