#! usr/bin/env python3
# indeed.py - application to automate the daily indeed apllies which take 10 minutes a day. 
# Change the search thing to since last visit next time I do it. 
# This bot will apply to the first posting. 


import time, random, os, csv, datetime
from selenium import webdriver 
from bs4 import BeautifulSoup
import pickle
import requests

url = "https://www.indeed.co.uk/jobs?as_and=developer&as_phr=&as_any=&as_not=senitor%2C+client&as_ttl=&as_cmp=&jt=all&st=&as_src=&salary=&radius=25&l=ls42pj&fromage=1&limit=50&sort=&psf=advsrch&from=advancedsearch"


# res = requests.get(url)
# res.raise_for_status()
# soup = BeautifulSoup(res.text)


print('Welcome to indeed application bot')
print('Here goes nothing...')

# define browser
browser = webdriver.Firefox()
# url for search "developer" near "LS42PJ" with 50 results on one page for one day. 
browser.get(url) 
# add cookies for password 
cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    browser.add_cookie(cookie)

# refresh browser to sign in now that cookies are here
browser.refresh()

# There are two possible methods
# 1. Click on every link and keep going until it works or doesnt work 
# 2. Only click on links that work - don't click on sponsored ones, or ones without one click apply 


# find job positing element
try: 
    jobDescriptionElem = browser.find_element_by_class_name("jobsearch-SerpJobCard")
    print('Found <%s> element with that class name!' % (jobDescriptionElem.tag_name))
except:
    print('Was not able to find an element with that name.')

# click on the job posting 
jobDescriptionElem.click()

try: 
    applyWithIndeedButton = browser.find_element_by_class_name("indeed-apply-button-inner")
    print('Found <%s> element with that class name. (apply with indeed button)' % (applyWithIndeedButton.tag_name))
except:
    print('did not find indeed apply button')

# click on apply with indeed
applyWithIndeedButton.click()


# switch to iframe which pops up to fill in form 
time.sleep(4)
browser.switch_to.frame(browser.find_element_by_tag_name("iframe"))


uploadCv = browser.find_element_by_xpath('//*[@id="input-applicant.name"]')
uploadCv.click()

# # FILL OUT FORM 
nameElem = browser.find_element_by_id('input-applicant.name')
nameElem.send_keys('Bilal Minhas')
emailElem = browser.find_element_by_css_selector('#input-applicant.name')
emailElem.send_keys('bilalm354@gmail.com')


# UPLOAD CV

# click upload CV 


