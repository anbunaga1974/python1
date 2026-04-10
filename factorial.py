n=int(input("Enter a number:"))
fact=1
if n<0:
    print("Factorial doesn't exist for negative nos.")
elif n==0:
    print("Factorial of 0 is 1")
else:
    for i in range(1,n+1):
        fact*=i
    print("Factorial of",n,"is",fact)
