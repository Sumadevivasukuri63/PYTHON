# n =int(input())
# for i in range(1,n+1):
#     print("* " * i)
# for i in range(n-1,0,-1):
#     print("* " * i)


list=[1,6,3,4,5]
max=list[0]
secondmax=0
for i in range(len(list)):
    if max<list[i]:
        max=list[i]
for i in range(len(list)):
    if list[i]>secondmax and list[i]!=max:
        secondmax=list[i]
print(secondmax)