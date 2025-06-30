# n=int(input())
# for i in range(1,n+1):
#     print(" "*(n-i)+"*"*(2*i-1))
# for i in range(n-1,0,-1):
#     print(" "*(n-i)+"*"*(2*i-1))




# for i in range(0,26):
#     print((chr(ord('A')+i)),end=" ")



# rows=5
# num=1
# for i in range(1,rows+1):
#     for j in range(i):
#         print(num,end=" ")
#         num+=1
#     print()
# n=4
# for i in range(n):#row
#     for j in range(n):#col
#         if i == 0 or i == n-1 or j == 0 or j == n-1:
#             print("*", end=" ")
#         else:
#             print(" ",end=" ")
#     print( ) 


n=5
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or i==j or j==0 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()





 