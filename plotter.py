import matplotlib.pyplot as plt
from utils import *

if(len(sys.argv) != 2):
    print "Usage: plotter.py <dump_file>"
    sys.exit(0)

dat = pretty_read(sys.argv[1])
print len(dat)

plt.xlabel("Time (index)")
plt.ylabel("DRS value")

for j in xrange(100):
    for i in xrange(20*j,20*j+20):
        plt.plot(xrange(len(dat[i][1])),dat[i][1])
        plt.title(dat[i][0].decode('utf-8'))
    plt.savefig(str(j)+".png")
    plt.cla()
    plt.clf()
