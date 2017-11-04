from utils import *
import csv
from random import randint

if(len(sys.argv) != 3):
	print "Usage: merge_dumps.py <dump_files ',' separated> <output_dump>"
	sys.exit(0)

dumps = sys.argv[1].split(',')

total_data = []

for x in range(0,len(dumps)):
	data = pretty_read(dumps[x])
	for y in range(0,len(data)):
		total_data.append(data[y])

print len(total_data)

pretty_print(sys.argv[2], total_data)
