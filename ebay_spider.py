import requests
from bs4 import BeautifulSoup


def ebay_spider(item_type):
	url = 'http://www.ebay.in/sch/i.html?_from=R40&_trksid=p2050601.m570.l1313.TR10.TRC0.A0.H0.Xt-shirts.TRS0&_nkw='+item_type+'&_sacat=0'
	
	k=1

	f=open('products.txt','a')
	f.write("\t**********eBAY**********\n")

	source_code = requests.get(url)
	plain_text = source_code.text
	soup = BeautifulSoup(plain_text,"html.parser")

	for link in soup.findAll('a',{'class':'vip'}):		
		title = link.string
		if title is not None:
			if item_type in title:
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

