import csv, sys #imports

archive = "Database.csv" #archive file .csv
output = "Output.csv"
with open(archive) as f: #open .csv
    reader = csv.DictReader(f, delimiter=";") #read .csv / delimiter by ";"
    data={}

    for row in reader: #loop data lines
        for header, value in row.items():
            try: #try / exception
                data[header].append(value)
                print(row) #print row x data
            except KeyError: #except error
                data[header] = [value] #show exception

#    try: #try / exception
#        for lines in reader: #loop data lines
#            print(lines['TagID']) #print datas
#    except csv.Error as e: #except error
#        sys.exit((archive, e)) #show exception
