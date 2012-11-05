from urllib2 import urlopen

for i in urlopen('http://symbioses.no'):
    if 'SYMBIOSES' in i:
        print i
