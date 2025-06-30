
s= [[1, 2,3],[4,5,6],[1,2,3]]
     

p= [[5, 6,7],[1,2,3],[7, 8,6]]
     


#result = [[0, 0],
         # [0, 0]]
#rows=len(s)
#col=len(s[0])
rows=3
col=3
result=[]

for i in range(rows):
    rowList=[]
    for j in range(col):
       # result[i][j] = s[i][j] + p[i][j]
       #  rowList.append(s[i][j]+p[i]+[j])
       rowList.append(rowList)

print("Sum of the matrices:",result)
