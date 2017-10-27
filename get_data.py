from utils import *

base_url = 'http://www.google.com/maps/place/'

driver = webdriver.Chrome()

for i in xrange(10):
    driver.get(base_url+"Chennai")
    tab_pid = run_cmd('ps -p $(pidof chrome) | grep -- "--type=renderer" | grep -v -- "--extension"').split(' ')[0]
    #wait for ajax items to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//script[@async and @src]')), "Timeout waiting for page to load")
    print run_cmd('cat /proc/'+tab_pid+'/statm')
