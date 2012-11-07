import csv

csvfile = file("participants.csv", "r")
reader = csv.reader(csvfile)
for row in reader:
    print row