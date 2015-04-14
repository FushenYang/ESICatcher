# parse the file to excel format
import sys  
import re
reload(sys)  
sys.setdefaultencoding('utf8') 
from bs4 import BeautifulSoup



def parse(html):
	dic = {'width':'100%','cellspacing':'0'}

	soup = BeautifulSoup(html)
	table = soup.findAll('table',dic,bgcolor=re.compile(r'#FFFFFF|#FFFFCC'))


	cites = []
	cite = []

	for e in table:
		
		if e.tr.find('td',align='right'):
			cite.append(e.tr.td.contents[0].strip())
			cite.append(e.tr.td.contents[2].string.strip())
		
		if not e.tr.find('td',align='right') :
			tds = e.findAll('td',width='80%')

			title = str(tds[0].next)
			cite.append(title.strip())
			author = ''
			for a in tds[1].contents:
				author+=a.string.strip()
			cite.append(author)

			if len(tds[2]) == 2:
				source = str(tds[2].contents[0].string) 
				cite.append(source)
				page =  str(tds[2].contents[1]).strip()
				cite.append(page)
				cite.append(re.match(r'.*(\d{4})\D*$',page).group(1))
			else:
				source = re.match(r'^(\D*)\d',str(tds[2].string)).group(1).strip()
				cite.append(source)
				page = tds[2].string[len(source):]
				cite.append(page)
				cite.append(re.match(r'.*(\d{4})\D*$',page).group(1))
			cite.append(tds[3].get_text().replace(u'\xa0','').strip())
			cite.append(tds[4].get_text().replace(u'\xa0','').strip())
			cites.append(cite)
			cite = []

	return cites




mf = open('UrlList.txt')
maps =  [e.strip() for e in open('UrlList.txt').readlines()]

for x in maps:
	m = re.search(r'\d+\D*$',x)
	if m:
		page = m.group()
		html = open(page+'.txt','r').read()
		
		cites = parse(html)
		f = open('parse_'+page+'.txt','w')
		for l in cites:
			f.write('\t'.join(l)+'\n')
		f.close()


