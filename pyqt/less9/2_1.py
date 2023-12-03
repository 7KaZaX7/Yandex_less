import csv

with open('wares.csv', newline='') as file:
    reader = csv.reader(file, delimiter=";")
    next(reader)
    for i in reader:
        name, op, np = i
        if int(np) < int(op):
            print(name)