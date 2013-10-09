from urllib2 import urlopen

for i in urlopen('http://localhost:8008/urls.py'):
    print i,
