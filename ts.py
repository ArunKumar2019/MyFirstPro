import csv
with open('data.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    print(readCSV)
    for row in readCSV:
        #print(row)
        #print(row[0])
        print("Name: ",row[0],"Code: ",row[1])

