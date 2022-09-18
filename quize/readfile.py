from ast import Try

try:
   fr=open('datastore.txt','r')  
#    print(fr.readline())
#    print(fr.readline())
   print(fr.read())
except Exception as e:
    print(e)    