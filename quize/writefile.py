try:
    #mode:w,a,x
    fw=open('datastore.txt','a')
    print('type  some  string')
    s=input()
    fw.write(s)
except Exception as e:
    print(e)