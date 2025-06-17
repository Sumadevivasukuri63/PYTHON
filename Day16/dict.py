sen="apple orange mango apple apple"
words=sen.split()
fre_dict={}
for word in words:
   fre_dict[word]=fre_dict.get(word,0)+1
print(fre_dict)




def swap_positions(list):
   if len(list)>=1:
      list[0],list[-1]=list[-1],list[0]
   return list
numbers=[1,2,3,4,5]
print(swap_positions(numbers))