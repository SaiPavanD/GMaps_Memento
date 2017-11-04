from utils import *
import csv
from random import randint

if(len(sys.argv) != 5):
	print "Usage: data2csv.py <dump_file> <num_cities> <num_iterations> <test_data_percent>"
	sys.exit(0)

data = pretty_read(sys.argv[1])
print len(data)

n = int(sys.argv[2])
m = int(sys.argv[3])

dat = []
max_size = -1

for x in range(0,n):
	for y in range(0,m):
		max_size=max(max_size,len(data[x*m+y][1]))

max_size=1578
for x in range(0,n):
	for y in range(0,m):
		if(len(data[x*m+y][1])==0):
			continue;
		tmp = [x]
		for z in range(0,len(data[x*m+y][1])):
			tmp.append(data[x*m+y][1][z])
		for z in range(0,max_size-len(data[x*m+y][1])):
			tmp.append(data[x*m+y][1][len(data[x*m+y][1])-1])
		dat.append(tmp)

print len(dat)

test_num = int(len(dat)*float(sys.argv[4]))

test_data = [] 

for x in range(0,test_num):
	test = randint(0,len(dat)-1)
	test_data.append(dat[test])
	dat.pop(test)

with open("train_data_sse_3.csv", "wb") as f:
	writer = csv.writer(f)
	writer.writerows(dat)

with open("test_data_sse_3.csv", "wb") as f:
	writer = csv.writer(f)
	writer.writerows(test_data)