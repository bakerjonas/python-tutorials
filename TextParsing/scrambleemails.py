import re

emails=re.compile("([^ ,]+)(@[^ ,]+)")

text = file("Python-workshop-participants.rst", "r").read()
newtext = emails.sub(r"\1-nospam\2", text)
print newtext

  
