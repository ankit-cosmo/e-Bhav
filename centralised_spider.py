import requests
import flipkart_spider
import amazon_spider
import ebay_spider
import snapdeal_spider
import nykaa_spider

pf = open("file.txt")
a=pf.read()
pf.close()

l=len(a)
i=0
q=1
name=''

f=open('products.txt','w')
f.close()

for i in range(0,l):
	if(a[i]!='\n'):	
		name+=a[i]
	else:
		item_type=name
		f=open('products.txt','a')		
		f.write(str(q))
		f.write("\t")
		f.write(item_type)
		f.write("\n")
		f.close()
		flipkart_spider.flipkart_spider(item_type)
		amazon_spider.amazon_spider(item_type)
		ebay_spider.ebay_spider(item_type)
		snapdeal_spider.snapdeal_spider(item_type)
		#nykaa_spider.nykaa_spider(item_type)
		name=''		
		q+=1
	i+=1
