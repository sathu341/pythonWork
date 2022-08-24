import pandas  as pd
tech=[
    ("Python",30000,'90days',1000),
    ("Java",28000,'90days',1000),
    ("AI",60000,'120days',900),
    ("Hadoop",30000,'90days',1500),
]
df=pd.DataFrame(tech,columns=['course','Fees','Duration','Discount'])
print(df.head())
#convert to json
df2=df.to_json(orient='columns')
print(df2)
df3=df.to_csv()
print("csv data ")
print(df3)

