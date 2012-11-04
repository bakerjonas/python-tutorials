hello = " Hello world!   "

len(hello)  # get string lenght

print "'" + hello.strip() + "'" # Try rstrip() and lstrip()
print "'" + hello + "'" 
print hello.upper()             # Try lower() 
print hello.title()             
print hello.strip().capitalize()
print hello.find('orl')         # Try rfind()

print hello.split()   
print hello.split('l')
print hello.split('ll')

print "%d: You could get %s" % (42, 'stabbed') 
print "{0} (cruel) {1}!".format('Goodbye', 'world')
