no=(34,56,7)
print(no)
#collection converter  list(),tuple(),set(),dict()
no=list(no)
no[2]=25
no.append(100)
print(no)
no=tuple(no)
print(no)

#set
st={4,5,4,4,4,7,8}
print(st)

#dictionary

dt={'R':'Rose','J':'Jasmine'}
print(dt['R'])
name=[]
ph=[]
print("name")
name.append(input())
print("phone no")
ph.append(input())
dct=zip(name,ph)#zip function is used to mapping
dct=dict(dct)
print(dct)


