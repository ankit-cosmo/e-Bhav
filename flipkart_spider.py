import requests
from bs4 import BeautifulSoup


def flipkart_spider(item_type):

	url = 'http://www.flipkart.com/search?q='+item_type+'&as=on&as-show=on&otracker=start'
	k=1

	f=open('products.txt','a')
	f.write("\n\t**********FLIPKART**********\n")

	source_code = requests.get(url)
	plain_text = source_code.text
	soup = BeautifulSoup(plain_text,"html.parser")
	
	for link in soup.findAll('a',{'data-tracking-id':'prd_title'}):
		title = link.get('title')
		if item_type in title:
			href="http://www.flipkart.com"+link.get('href')
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
