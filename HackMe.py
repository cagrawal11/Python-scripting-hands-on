'''
	Tony has found a bug in website which allows him to change the website source. Write script to modify source as follows:
	1. Change title of webpage and all headings(h1..h6) to "hackedbyxyz". In the modified version of source keep the lowecase
	version of tags. e.g. <TITLE>Home</TITLE> => <title>hackedbyxyz</title>
	2. Modify all the href attribute to point to "http://hackedbyxyz.com". Keep the lowecase version of href.

	Input will be a valid url

	Input url is hard-code now
'''

import requests
from bs4 import BeautifulSoup
import re

url = 'http://www.voidspace.org.uk'

response = requests.get(url)
soup = BeautifulSoup(response.content)
#print soup.prettify()

print '\n\n'

titleTag = soup.title
titleTag.string = "hackedbychetan"

#reg = re.compile('h[1-6]')

for tag in soup.find_all(re.compile('h[1-6]|a', re.IGNORECASE)):
	if tag.name == re.compile('h[1-6]'):
		tag.string = "hackedbychetan"
	else:
		tag['href'] = 'http://hackedbyxyz.com'

print '\n\n'

print soup.prettify()
