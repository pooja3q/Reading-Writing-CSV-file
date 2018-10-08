import pandas
df = pandas.read_csv('hrdata.txt',index_col='Name' , parse_dates= ['Hire Date'])
print(df)
