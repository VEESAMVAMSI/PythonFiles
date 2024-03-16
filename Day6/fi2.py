import csv
with open("student.csv","r",newline="") as file:
    read=csv.DictReader(file)
    for row in read:
        print(row["studentid"],"=",row["name"])