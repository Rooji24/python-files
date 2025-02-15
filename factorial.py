def recur_factorial(n):
    if n==1:
        return n
    else:
        return n* recur_factorial(n-1)
    
num = int(input("Enter the number"))
if num< 0:
    print("Negative numbers are not allowed")
elif num ==0:
    print("Factorial of number is 1")
else:
    print("The facrotial of is" , recur_factorial(num))    
     