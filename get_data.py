from selenium import webdriver
from time import sleep
import os
from subprocess import Popen, PIPE

init_sleep = 1
base_url = "http://www.google.com/maps/place/"

driver = webdriver.Chrome()
driver.get("http://www.google.com")
sleep(init_sleep)
driver.get(base_url+"Hyderabad")

p = Popen("ps -p $(pidof chrome)", shell=True, stdout=PIPE )
out, err = p.communicate()
print out
