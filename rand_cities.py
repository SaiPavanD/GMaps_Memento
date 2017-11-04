from utils import *

if(len(sys.argv)!=4):
	print "Usage : python rand_cities.py <input_cities_list> <output_cities_list> <number_of_cities>"
	sys.exit(0)

cities = read_cities(sys.argv[1])
num = int(sys.argv[3])
rand_cities = random.sample(cities, num)

with open(sys.argv[2], "w") as fout:
    for i in rand_cities:
        fout.write(i+"\n")
