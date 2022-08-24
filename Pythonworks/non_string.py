str1=input("Enter string")

char=[]
l=len(str1)
# for i in range(0,l):
#     count=str1.count(str1[i])
#     if not(count>1):
#         char.append(str(str1[i]))

# print("non repeating character=",char)                

removech=input("enter character to remove")
print("replace",str1.replace(removech,""))
for j in range(0,l):
    char.append(str1[j])
    if str1[j]==removech:
        char.remove(removech)
        continue
for k in char:
    print(k,end="")    