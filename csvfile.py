import  pandas as pd

fl=pd.read_csv(r'myfile.csv',header=None,skiprows=lambda x :x%2!=0)



l=len(fl)
print(fl.head())



 