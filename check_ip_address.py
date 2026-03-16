import json
from urllib.request import urlopen
import requests

url = 'http://ipinfo.io/json'


response = requests.get(url)

IP = response.json()['ip']
org = response.json()['org']
city = response.json()['city']
country = response.json()['country']
region = response.json()['region']


print('\nYour IP detail\n')
print('IP : {4} \nRegion : {1} \nCountry : {2} \nCity : {3} \nOrg : {0}\n'.format(org, region, country, city, IP))