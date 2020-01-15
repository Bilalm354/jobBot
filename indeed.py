#! usr/bin/env python3
# indeed.py - application to automate the daily indeed apllies which take 10 minutes a day. 
# Change the search thing to since last visit next time I do it. 

import time, random, os, csv, datetime
from selenium import webdriver 
from bs4 import BeautifulSoup
import pickle

print('Welcome to indeed application bot')
print('Here goes nothing...')

# define browser
browser = webdriver.Firefox()
# url for search "developer" near "LS42PJ" with 50 results on one page for one day. 
browser.get("https://www.indeed.co.uk/jobs?as_and=developer&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&as_src=&salary=&radius=25&l=ls42pj&fromage=1&limit=50&sort=&psf=advsrch&from=advancedsearch") 
# add cookies for password 
cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    browser.add_cookie(cookie)

# refresh browser to sign in now that cookies are here
browser.refresh()
