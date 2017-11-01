from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from subprocess import Popen, PIPE
import csv

import os
import threading
import sys
import collections

# runs cmd and returns the output
def run_cmd(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE)
    out, err = p.communicate()
    return out

# returns the list of cities
def read_cities(inp):
    with open(inp) as f:
        content = f.readlines()
    return [x.strip() for x in content]
