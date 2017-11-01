from utils import *
import collections
import csv
from random import randint
from selenium.common.exceptions import TimeoutException  
from selenium.common.exceptions import NoSuchElementException

if(len(sys.argv)!=4):
	print "Usage : python gen_data.py <input_cities_list> <output_dump_file> <number of cities>"
	sys.exit(0)

# global shared vars for communicating b/w thread and main
drs = []
loop_cond = True

# base params
base_url = 'http://www.google.com/maps/place/'
cities = read_cities(sys.argv[1])
op = []

def read_vals(pid):
	global loop_cond
	global drs
	while(loop_cond):
		temp_drs = int(run_cmd('cat /proc/'+tab_pid+'/statm').split(' ')[1])
		drs.append(temp_drs)

def load_page(url):
	global loop_cond
	global driver
	driver.get(url)
	# wait for ajax items to load
	WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//script[@async and @src]')), "Timeout waiting for page to load")
	loop_cond = False
	# re initialize the tab
	driver.get("http://google.com")

for q in xrange(int(sys.argv[3])):
	#randomly selecting argv[3] number of cities from dataset
	i = randint(0, 2000)
	for j in xrange(5):
		# init chrome		
		driver = webdriver.Chrome()
		driver.get("http://google.com")
		tab_pid = run_cmd('ps -p $(pidof chrome) | grep -- "--type=renderer" | grep -v -- "--extension"').strip().split(' ')[0]

		# init the shared vars
		drs = []
		loop_cond = True
		# init the threads
		t1 = threading.Thread(target=load_page, args=(base_url+cities[i],))
		t2 = threading.Thread(target=read_vals, args=(tab_pid,))
		# start the threads
		t1.start()
		t2.start()
		# wait for threads to finish
		t1.join()
		t2.join()
		driver.quit()
		counter=collections.Counter(drs)
		vals = counter.most_common()
		#vals now contains tuples of the form (value,frequency)
		for k in xrange(len(vals)):
			op.append([q,i,cities[i],vals[k][0],vals[k][1]])
		print q
	cities.pop(i)

with open(sys.argv[2], "wb") as f:
	writer = csv.writer(f)
	writer.writerows(op)
