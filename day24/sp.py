# n=int(input())
# for i in range(1,n+1):
#     print(" "*(n-i)+"*"*(2*i-1))
# for i in range(n-1,0,-1):
#     print(" "*(n-i)+"*"*(2*i-1))




# for i in range(0,26):
#     print((chr(ord('A')+i)),end=" ")



rows=5
num=1
for i in range(1,rows+1):
    for j in range(i):
        print(num,end=" ")
        num+=1
    print()

   