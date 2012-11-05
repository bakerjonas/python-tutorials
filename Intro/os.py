import os

user = os.getenv('LOGNAME')
cwd = os.getcwd()

# there are better ways than this...
os.system('mkdir tmp.{}'.format(os.getpid())) 

print os.times()
