sen="apple orange mango apple apple"
words=sen.split()
fre_dict={}
for word in words:
   fre_dict[word]=fre_dict.get(word,0)+1
print(fre_dict)





