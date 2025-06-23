def is_prime(n):
    if n<2:
        return 0
    for i in range(2,n):
        if n%i==0:
            return False
        return True
        
    
    
n=int(input("Enter a number:")) 
if is_prime(n):
    print("It is prime")
else:
    print("not a prime")
            