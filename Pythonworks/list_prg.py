#list Prg
a=[23,45,45,67,89]
print(a[2])
#append() function used to insert value into list variable
a.append(90)#insert 90 into the "a" list variable
print(a) # to display all elements
l=len(a) # to find the  length of list variable
print("Length of the  list",l)

a.remove(45)#to remove element from list
print(a)
# insert(index,value)
a.insert(2,100)
print(a)
# pop(index no) which remove data by its index no
a.pop(3)
print(a)

#append(),insert(),len(),remove(),pop()

b=['apple','orange','grape','apple','mango','apple','bannana','apple']
cnt=b.count('apple')
print("count of repeat value",cnt)
#index()
print("index no ",b.index("orange"))
#count index()


