import csv
# Writing CSV file 
'''with open('employee_birthday.txt', mode ='a+') as csv_file:
    employee_writer = csv.writer(csv_file, delimiter=',')
    employee_writer.writerow(['Arun Yadav' , 'IT' , 'December'])

'''
# Writing CSV file from a Dictionary With csv
with open('employee_file2.csv', mode='w') as csv_file:
    fieldnames = ['emp_name', 'dept', 'birth_month']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'emp_name': 'Pooja Yadav', 'dept': 'Accounting', 'birth_month': 'November'})
    writer.writerow({'emp_name': 'Arun yadav', 'dept': 'IT', 'birth_month': 'March'})    