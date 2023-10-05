print("Demo of function:program to find factorial of a number")
def fact(n):
    if n==1:
        return 1
    else:
        return(n*fact(n-1))
n=int(input("Enter a number:"))
print("Factorial : ",fact(n))

//

Demo of function:program to find factorial of a number
Enter a number:5
Factorial :  120

Process finished with exit code 0
