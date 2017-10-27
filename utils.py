from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from subprocess import Popen, PIPE

import os

# runs cmd and returns the output
def run_cmd(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE )
    out, err = p.communicate()
    return out

# reu
# def ajax_complete(driver):
#     try:
#         return 0 == driver.execute_script("return jQuery.active")
#     except WebDriverException:
#         pass
