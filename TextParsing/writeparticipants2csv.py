import csv

fd = file("Python-workshop-participants.rst", "r")

participants = list()
for line in fd.readlines():
    if '@' in line:
        _, name, email, affiliation = map(str.strip, line.split(','))
        p = dict(name=name, email=email, affiliation=affiliation)
        participants.append(p)
    if 'pending' in line:
        break

csvfile = file("participants.csv", "w")
writer = csv.writer(csvfile)
writer.writerow(["Name", "Email", "Affiliation"])
for p in participants:
    writer.writerow([p["name"], p["email"], p["affiliation"]])