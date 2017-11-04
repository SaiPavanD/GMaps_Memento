from utils import *

if(len(sys.argv)!=4):
	print "Usage : python gen_data.py <input_cities_list> <output_dump_file> <num_iterations>"
	sys.exit(0)

# global shared vars for communicating b/w thread and main
drs = []
loop_cond = True

# base params
base_url = 'http://www.google.com/maps/place/'
cities = read_cities(sys.argv[1])
city_file = []
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
	WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '//script[@async and @src]')), "Timeout waiting for page to load")
	loop_cond = False

for i in xrange(len(cities)):
	for j in xrange(int(sys.argv[3])):
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

		# counter=collections.Counter(drs)
		op.append((cities[i],drs))
	print i

pretty_print(sys.argv[2], op)