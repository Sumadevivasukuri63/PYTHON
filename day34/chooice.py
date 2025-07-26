import heapq
queue=[]
dict={}

while True:
    print("Menu List")
    print("1.Add element")
    print("2.Enter the number to delete")
    choices=int(input("Enter your choice:"))
    if choices==1:
        name=input("Enter name:")
        priority_order=int(input("Enter priority:"))
        heapq.heappush(queue,(name,priority_order))
        
        
        print(queue)
    if choices==2:
        heapq.heappop(queue)
        print(queue)
        
    





