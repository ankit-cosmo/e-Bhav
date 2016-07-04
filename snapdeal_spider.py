import requests
from bs4 import BeautifulSoup
from selenium import webdriver  
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.common.keys import Keys  
import sys

def snapdeal_spider(item_type):
	url='http://www.snapdeal.com/search?keyword='+item_type+'&santizedKeyword=&catId=&categoryId=0&suggested=false&vertical=&noOfResults=48&clickSrc=go_header&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy'
	k=1

	f=open('products.txt','a')
	f.write("\t***********SNAPDEAL***********\n")

	browser = webdriver.PhantomJS()
	browser.set_window_size(1120, 550)
	browser.get(url)
	source_code = browser.page_source  
	browser.quit()

	soup = BeautifulSoup(source_code,"html.parser")
	
	#print(soup.prettify())

	for link in soup.findAll('a'):
		#print(link.p)
		if link.p is not None:
			title = link.p.get('title')
			if title is not None:
				if item_type in title:
					#print(title)
					href=link.get('href')					
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

#snapdeal_spider("Shoes")


