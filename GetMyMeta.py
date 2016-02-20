'''
	Write a script that takes URL as input and outputs the metadata found at that URL. You should only consider the 
	meta tags that have attributes name or content.You can make use of requests scripting library present in scripting environment.

	the input shall contain valid url, the output in given format(can't get the format)
	#e.g URL: http://www.voidspace.org.uk -----has content attribute
	#e.g. URL: http://python.org
'''

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