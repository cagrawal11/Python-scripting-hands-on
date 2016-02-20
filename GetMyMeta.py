import urllib2
from bs4 import BeautifulSoup
from urlparse import urlparse

parse_url = urlparse(raw_input("Enter the URL: "))
if not bool(parse_url.scheme):
	url = 'http://'+parse_url.geturl() #parse_url._replace(**{"scheme":"http"})
else:
	url = parse_url.geturl()

try:
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
except urllib2.URLError as e:
	print e.reason
else:
	thePage = response.read()
	soup = BeautifulSoup(thePage)
	try:
		soup.meta['content']
	except:
		print "No meta with content attribute"
	else:
		print soup.meta


'''Using Request library'''

import requests
#BeautifulSoup is already loaded
print "Again same using Request library"

r = requests.get(url)
soup = BeautifulSoup(r.content)
try:
	soup.meta['content']
except:
	print 'no meta'
else:
	print soup.meta

#e.g URL: http://www.voidspace.org.uk -----has content attribute
#e.g. URL: http://python.org