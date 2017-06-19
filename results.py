#Author: Rahul Harikumar.
from bs4 import BeautifulSoup
import mechanize
import urllib2
# Create a Browser
b = mechanize.Browser()
# Disable loading robots.txt
b.set_handle_robots(False)
b.open('http://aucoe.annauniv.edu/result/134679852/cgrade.html')
b.select_form(name='result')
#Replace Register Number
b['regno'] = 'xxxxxxxxxxxx'
fd = b.submit()
soup = BeautifulSoup(fd.read(),'html.parser')
tables = soup.findAll("table")
for table in tables:
    for row in table.findAll("tr"):
      print row.getText()
      break;
      
