#catch pages from url list

import urllib2
import cookielib
import re

cj = cookielib.LWPCookieJar()
cookie_support = urllib2.HTTPCookieProcessor(cj)
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
urllib2.install_opener(opener)


urllib2.urlopen('http://www.webofknowledge.com/?DestApp=ESI')



mf = open('UrlList.txt')
maps =  [e.strip() for e in open('UrlList.txt').readlines()]

i = 0
for x in maps:
	response = urllib2.urlopen(x)
	html = response.read()
	m = re.search(r'\d+\D*$',x)  
	if m:
		page = m.group()
		f = open(page+'.txt', 'w')
		f.write(html)
		f.close()