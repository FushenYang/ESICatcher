#merge the file have format
import re

mf = open('UrlList.txt')
maps =  [e.strip() for e in open('UrlList.txt').readlines()]
fileall = ''




for x in maps:
	m = re.search(r'\d+\D*$',x)
	if m:
		page = m.group()
		f = open('parse_'+page+'.txt','r')
		fileall += f.read()

fw  = open('all.txt','w')
fw.write(fileall)
f.close()