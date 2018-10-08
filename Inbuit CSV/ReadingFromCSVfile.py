import csv
'''with open('employee_birthday.txt') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    line_count=0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {",".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and born in {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines')
'''
#####  Reading CSV Files Into a Dictionary With csv
with open ('employee_birthday.txt', mode = 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count =0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {",".join(row)}')
            line_count += 1
        else:
            print(f'\t{row["name"]} work in the {row["department"]} department , and born in {row["birthday month"]}.')
            line_count +=1
    print(f'Processed {line_count} lines')
 