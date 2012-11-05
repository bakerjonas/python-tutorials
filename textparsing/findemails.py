import re

emails=re.compile("([^ ,]+@[^ ,]+)")

text = file("Python-workshop-participants.rst", "r").read()
for m in emails.findall(text):
  print m
  
  
