'''

	Given the organization, the repository and the date, output the list of urls of issue/pull requests on that date

	Input:
		A single line containing the organization, repository name and the date in format DD-MM-YYYY
		e.g atom atom 27-02-2013
	-Output:
		n line each containing an url of issu/pull requests. The urls should be in ascending order of time when the issue/pull
		was created.
'''

import requests
import requests.exceptions
from bs4 import BeautifulSoup
import urllib2
import json
import urllib

#url = 'https://api.github.com/atom/atom/pulls'
#url = 'https://api.github.com/repos/cagrawal11/Python-scripting-hands-on/pulls'
#url = 'https://api.github.com/repos/bernd/statsd-influxdb-backend/pulls'
#url = 'https://api.github.com/repos/atom/atom/pulls'
Base_url = 'https://api.github.com/repos'

input_string = raw_input("Enter input as e.g. atom atom 27-02-2015: \n")
input_string = input_string.split(' ')
org = input_string[0]   #get organization name
repo = input_string[1]   #get the repo name
date = input_string[2]    #get date
date = '-'.join(date.split('-' )[::-1])

url = Base_url + '/' + org +'/' + repo + '/' + 'pulls'
print url
response = requests.get(url).json()

'''Pathetic way to chk if repo exist. REDO how handle this case'''
if 'Not Found' in response['message']:
	print "no such repo"
else:
	for pullRequests in response:
		if (date in pullRequests['created_at']):
			print pullRequests['url']
#except requests.exceptions.RequestException	 as e:
#	print e