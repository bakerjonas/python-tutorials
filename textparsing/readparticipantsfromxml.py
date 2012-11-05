from lxml import etree

events = ("start", )
context = etree.iterparse(file("participants.xml", "r"), events=events)
for a, ele in context:
  print  ele.tag, ele.text
