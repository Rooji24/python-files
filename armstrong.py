n = int(input("Enter a number: "))  

digits = len(str(n))  
total = sum(int(d) ** digits for d in str(n))  

if n == total:  
    print(f"{n} is an Armstrong number.")  
else:  
    print(f"{n} is not an Armstrong number.")