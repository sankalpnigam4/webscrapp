#! /usr/bin/python -tt
import requests

page = requests.get("https://www.google.co.in/search?client=ubuntu&channel=fs&q=snapdeal&ie=utf-8&oe=utf-8&gfe_rd=cr&ei=e3DuWLe0KPGK8Qfjq73IAg#q=snapdeal&channel=fs&tbm=nws")
#print page.content
#print "hello"
from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())
#html=list(soup.children)[2]
print "\n\n\n\n\n\t\t\t"
#body=list(html.children)[3]
#print list(body.children)
soup = BeautifulSoup(page.content, 'html.parser')
#print soup.find_all(class_='ts _V6c _Zmc _XO _knc _d7c')
for i in soup.find_all('span',class_='st'):
	print "\n\n\n\n"	
	print i
#for i in soup.find_all(class_='_RBg'):
#	print "\n\n\n\n"	
#	print i
