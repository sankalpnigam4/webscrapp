#! /usr/bin/python -tt
import requests

page = requests.get("https://www.google.co.in/search?client=ubuntu&channel=fs&q=flipkart&ie=utf-8&oe=utf-8&gfe_rd=cr&ei=rgzzWKCDI-2K8Qf88LKYCw")

from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')

for i in range(0,5):
	print soup.find_all('h3', class_='r')[8+i].get_text()
	print soup.find_all('span', class_='st')[2+i].get_text()	
	print "\n\n\n"

	







n = len(soup.find_all('span',class_="_gS"))

for i in range(0,n):
	item1 = soup.find_all('span',class_="_gS")[i].get_text()
	item2=soup.find_all('span',class_="_tA")[i].get_text()
	print item1+item2
	print "\n"





