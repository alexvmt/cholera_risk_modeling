#!/bin/python

# this script downloads cholera outbreaks data from the Integrated Disease Surveillance Programme (IDSP) for 2010 to 2015

print('Download cholera outbreaks data...')

# import packages
import os
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
years = [2010, 2011, 2012, 2013, 2014, 2015]
for year in years:
    if os.path.isdir(str(year)):
        pass
    else:
        os.mkdir(str(year))

# define function to retrieve file names from url
def get_file_names(url, ext):
    
    """
    This function takes a url and a file extention as input.
    It then parses the given url and extract all file names with the given extension.
    Finally, it returns a list of file names with the given extension.
    """
    
    page = requests.get(url, verify=False).text
    soup = BeautifulSoup(page, 'html.parser')
    return [url + '/' + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]

# disable insecure request warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# download cholera outbreaks pdf files from the IDSP
url = 'https://www.idsp.nic.in/WriteReadData/DOB'
ext = 'pdf'
for year in years:
    # get file names from url
    file_names = get_file_names(url+str(year), ext)
    # get already existing file names from directory
    files_in_dir = os.listdir(str(year))
    print('Processing {} with {} files...'.format(year, len(file_names)))
    for file in file_names:
        # skip file if it already exists
        if file.split('/')[-1] in files_in_dir:
            pass
        # otherwise download it and save it in the respective directory
        else:
            r = requests.get(file, verify=False)
            with open(str(year)+'/'+file.split('/')[-1], 'wb') as f:
                f.write(r.content)

print('Download cholera outbreaks data complete.')