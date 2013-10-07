import os

filenames = os.listdir(".")

#print filenames

runtimes = list()
for f in filenames:
    for line in file(f, "r").readlines():
        if line.startswith("WR12L2C2"):
            #print line

            linetokens = line.strip().split()
            #print linetokens[5]

            runtimes.append(float(linetokens[5]))
            
runtimes.sort()

print "min=", runtimes[0], "max=", runtimes[-1]