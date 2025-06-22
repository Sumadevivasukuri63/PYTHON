def search(arr,key):
    for ele in arr:
        if ele==key:
            return True
    
    return False

        
key=int(input())
arr=list(map(int, input().split()))
print("YES" if search(arr , key)  else "NO")
