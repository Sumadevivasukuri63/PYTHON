arr=[2,1,4,5,1,1,1,1,3,2]
target=3
long=0
i=0
j=0
sub_sum=arr[i]
while i<len(arr)-1 and j<len(arr)-1:
    if sub_sum<target:
        j+=1
        sub_sum+=arr[j]
        
    elif sub_sum>target:
        sub_sum-=arr[i]
        i+=1
    else:
       print(i,j)
       long=max(j-i+1,long)
       j+=1
       sub_sum+=arr[j]
print(long)