import requests
from bs4 import BeautifulSoup
from selenium import webdriver  
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.common.keys import Keys  
import sys

def nykaa_spider(item_type):
	url="http://www.nykaa.com/search/result/?q="+item_type
	k=1

	f=open('products.txt','a')
	f.write("\t***********NYKAA***********\n")

	browser = webdriver.PhantomJS()
	browser.set_window_size(1120, 550)
	browser.get(url)
	source_code = browser.page_source  
	browser.quit()

	soup = BeautifulSoup(source_code,"html.parser")
	#print(soup.prettify())	
	
	for link in soup.findAll('a',{'class':'product-image'}):
		#print(link)
		title = link.get('title')
		if item_type in title:
			href=link.get('href')
			hrefq="http://www.nykaa.com"
			for q in range (0,len(href)):
				if href[q] is not " " or "\n":
					hrefq = hrefq+href[q]
			f.write("\t")			
			f.write(title)			
			f.write("\n\t")
			f.write(hrefq)
			f.write("\n\n")
			k=0

	if k==1:
		f.write("\tPRODUCT N/A")
		f.write("\n\n")
	
	f.close()

#nykaa_spider("Foundation")
