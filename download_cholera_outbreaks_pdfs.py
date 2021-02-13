#!/usr/bin/env python
# coding: utf-8

import os
from bs4 import BeautifulSoup
import requests
import urllib3

if os.path.isdir('../data'):
    pass
else:
    os.mkdir('../data')

os.chdir('../data')

if os.path.isdir('cholera_outbreaks'):
    pass
else:
    os.mkdir('cholera_outbreaks')

os.chdir('cholera_outbreaks')

years = ['2010',
             '2011',
             '2012',
             '2013',
             '2014',
             '2015']

for year in years:
    if os.path.isdir(year):
        pass
    else:
        os.mkdir(year)

def get_file_names(url, ext):
    page = requests.get(url, verify=False).text
    soup = BeautifulSoup(page, 'html.parser')
    return [url + '/' + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]

url = 'https://www.idsp.nic.in/WriteReadData/DOB'

ext = 'pdf'

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

for year in years:
    file_names = []
    for file in get_file_names(url+year, ext):
        file_names.append(file)
    print('Processing {} with {} files...'.format(year, len(file_names)))
    for file in file_names:
        r = requests.get(file, verify=False)
        with open(year+'/'+file.split('/')[-1], 'wb') as f:
            f.write(r.content)