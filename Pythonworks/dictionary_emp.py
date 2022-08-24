#two dimensional
nlist=['kumar','krihna priya','athul','Ravi']
deglist=['developer','tester','junior developer','HR']
salary=[54000,40000,30000,55000]
emp={'name':nlist,'Designation':deglist,'Salary':salary}
print(emp['name'][0])
lg=len(emp)
print("Name,Designation,Salary")
for j in range(lg):
    print(emp['name'][j],emp['Designation'][j],emp['Salary'][j])
a=12    