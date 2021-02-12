import csv

with open('data/phone_book.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file, skipinitialspace=True)
    #next(csv_reader, None) #with this line we will skip the header in a csv
    #line_count = 0
    
    for row in csv_reader:
        #print(type(row))
        #print(row[0],":", row[2]) #When we work with csv.reader we get a list calss in response and we slice it like this. 
        print(row['first_name'],":",row['phone_number']) # or print(f"{row['last_name']}: {row['phone_number']}")
        #line_count += 1