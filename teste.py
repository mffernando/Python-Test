import csv
with open('Database.csv') as f:
    reader = csv.reader(f)
    for line in reader:
        print(line[0])
    
