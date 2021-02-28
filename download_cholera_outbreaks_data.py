#!/bin/python

# this script downloads cholera outbreaks pdf files from the Integrated Disease Surveillance Programme (IDSP) for 2010 to 2018

print('Download cholera outbreaks data...')

# import packages
import os
import numpy as np
from bs4 import BeautifulSoup
import requests
import urllib3

# create data directory if it doesn't yet exist
if os.path.isdir('../data'):
    pass
else:
    os.mkdir('../data')

os.chdir('../data')

# create cholera outbreaks directory if it doesn't yet exist
if os.path.isdir('cholera_outbreaks'):
    pass
else:
    os.mkdir('cholera_outbreaks')

os.chdir('cholera_outbreaks')

# create directories for years if they don't yet exist
years = list(np.arange(2010, 2019))
for year in years:
    if os.path.isdir(str(year)):
        pass
    else:
        os.mkdir(str(year))

# disable insecure request warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# specify url and file extension
url = 'https://www.idsp.nic.in/index4.php?lang=1&level=0&linkid=406&lid=3689'
ext = 'pdf'

# get page
page = requests.get(url, verify=False).text

# create soup object
soup = BeautifulSoup(page, 'html.parser')

# extract table
table = soup.find('table')

# extract table rows
rows = table.find_all(lambda tag: tag.name=='tr')

# download cholera outbreaks pdf files
for row in range(12, 3, -1):
    
    # get year and number of files in row
    year = rows[row].find('div').text
    number_of_files = len(rows[row].find_all('a'))
    
    print('Processing {} with {} files...'.format(year, number_of_files))
    
    # get already existing file names from directory
    files_in_directory = os.listdir(year)
    
    for file_number in range(0, number_of_files):
        
        # get file and week
        file = rows[row].find_all('a')[file_number].get('href')
        week = rows[row].find_all('a')[file_number].text
          
        # make file name from week, year and extension
        file_name = week + '_' + year + '.' + ext
          
        # skip file if it already exists
        if file_name in files_in_directory:
            pass
        # the links to some files seem to be broken
        elif file_name == '52nd_2011.pdf':
            r = requests.get('https://www.idsp.nic.in/WriteReadData/DOB2011/52nd_wk11_u.pdf', verify=False)
            with open(year+'/'+file_name, 'wb') as f:
                f.write(r.content)
        elif file_name == '9th_2013.pdf':
            r = requests.get('https://www.idsp.nic.in/WriteReadData/DOB2013/9th_wk13.pdf', verify=False)
            with open(year+'/'+file_name, 'wb') as f:
                f.write(r.content)
        elif file_name == '15th_2016.pdf':
            r = requests.get('https://www.idsp.nic.in/WriteReadData/l892s/25655158311465983344.pdf', verify=False)
            with open(year+'/'+file_name, 'wb') as f:
                f.write(r.content)
        elif file_name == '4th_2017.pdf':
            r = requests.get('https://www.idsp.nic.in/WriteReadData/l892s/15366628751488435411.pdf', verify=False)
            with open(year+'/'+file_name, 'wb') as f:
                f.write(r.content)
        # download file and save it in the respective directory
        else:
            r = requests.get(file, verify=False)
            with open(year+'/'+file_name, 'wb') as f:
                f.write(r.content)

print('Download cholera outbreaks data complete.')