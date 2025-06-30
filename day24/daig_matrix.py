mat=[[1,2,3]
     [4,5,6]
     [6,7,8]
]
rows=3
col=3
result=[]
for i in range(rows):
    for j in range(col):
        if i==j or i+j==rows-1:
           result+=mat[i][j]

print(result)