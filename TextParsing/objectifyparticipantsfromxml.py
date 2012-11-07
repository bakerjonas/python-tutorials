from lxml import objectify

f = file("participants.xml", "r")
participants = objectify.parse(f)

for p in participants.iter():
    print p.tag, p.text

