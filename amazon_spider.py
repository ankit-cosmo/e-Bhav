import requests
from bs4 import BeautifulSoup
from selenium import webdriver  
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.common.keys import Keys  
import sys

def amazon_spider(item_type):
	url = "http://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords="+item_type
	k=1
		    
	f=open('products.txt','a')
	f.write("\n\t**********AMAZON***********\n")
	
	browser = webdriver.PhantomJS()
	browser.set_window_size(1120, 550)
	browser.get(url)
	source_code = browser.page_source  
	browser.quit()
	
	soup = BeautifulSoup(source_code,"html.parser")
	
	for link in soup.findAll('a',{'class':'a-link-normal s-access-detail-page  a-text-normal'}):
		title = link.get('title')
		if item_type in title:
			href = link.get('href')
			f.write("\t")			
			f.write(title)			
			f.write("\n\t")
			f.write(href)
			f.write("\n\n")
			k=0
		
	if k==1:
		f.write("\tPRODUCT N/A")
		f.write("\n\n")
	
	f.close()

