import csv
with open('data.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
#    print(readCSV)
    centre = []
    course = []
    for row in readCSV:
#       print(row)
 #     print(row[2:4])
#       print(row[0],row[1],row[2])
#       print("StudId", row[1],"Name : ",row[2])
        cid=row[0]
        cname=row[2]
        centre.append(cid)
        course.append(cname)
    #print(len(course))
    sa=0    
    for i in range(len(course)):
        if course[i]=="IT0T1":
            sa=sa+1
            #print("Course Avilable")
        else:
            sa=0
            #print("Course Not Avilable")
    print(str(sa)+" times aviable")
