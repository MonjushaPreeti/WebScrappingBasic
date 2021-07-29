from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url='https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
uClient=uReq(my_url)
page_html=uClient.read()
uClient.close()

page_soup=soup(page_html,"html.parser")

containers=page_soup.find_all("div",{"class": "_13oc-S"})
#print(len(containers))

#print(soup.prettify(containers[0]))

container=containers[0]
#print(container.div.img["alt"])

price=container.find_all("div",{"class": "col col-5-12 nlI3QM"})
print(price[0].text)