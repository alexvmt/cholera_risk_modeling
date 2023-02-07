#!/bin/python

# this script downloads and preprocesses daily day land surface temperature data from the ESA Climate Change Initiative for a given month of a given year
# https://catalogue.ceda.ac.uk/uuid/ef8ce37b6af24469a2a4bdc31d3db27d

# import packages
import sys
import os
from bs4 import BeautifulSoup
import requests
import nctoolkit as nc
from time import sleep

params = sys.argv
year = params[1]
month = params[2]

print(f'Download land surface temperature data for {month}/{year}...')

# create data directory if it doesn't yet exist
if not os.path.exists('../../data'):
    os.mkdir('../../data')

os.chdir('../../data')

# create land surface temperature directory if it doesn't yet exist
if not os.path.exists('land_surface_temperature'):
    os.mkdir('land_surface_temperature')

os.chdir('land_surface_temperature')

# create directory for year if it doesn't yet exist
if not os.path.exists(year):
    os.mkdir(year)

os.chdir(year)

# create url
url = f'http://dap.ceda.ac.uk/thredds/fileServer/neodc/esacci/land_surface_temperature/data/MULTISENSOR_IRCDR/L3S/0.01/v2.00/daily/'{year}'/'{month}

# get page
page = requests.get(url, verify=False).text

# create soup object
soup = BeautifulSoup(page, 'html.parser')

# get and clean days available at url to create valid download links
days = soup.find('pre').text.split(' ')
while('' in days):
    days.remove('')
days = [i.replace('\r', '') for i in days]
days = [i.replace('\n', '') for i in days]
days = [i.replace('/', '') for i in days]
days = [i.replace('-', '') for i in days]
days = [i.replace('.', '') for i in days]
days = [i for i in days if len(i) == 2]

# set min and max values for longitude and latitude
lon_min, lon_max, lat_min, lat_max = 60, 100, 0, 40

# set desired spatial resolution in degrees
spatial_resolution = 0.05

# set evaluation to lazy
nc.options(lazy=True)

# download and preprocess daily data
for day in days:
    
    print (f'Downloading and processing day {day}...')
    
    # create file name
    file_name = f'ESACCI-LST-L3S-LST-IRCDR_-0.01deg_1DAILY_DAY-'{year}{month}{day}'000000-fv2.00.nc'
        
    try:
        # download data
        ds = nc.open_url(f'{url}/{day}/{file_name}')
    except ValueError:
        # try downloading data again in case it failed the first time
        print('Download failed. Trying again...')
        sleep(60)
        ds = nc.open_url(f'{url}/{day}/{file_name}')
    
    # select land surface temperature variable
    ds.select(variables='lst')
    
    # crop to desired longitude and latitude values
    ds.crop(lon=[lon_min, lon_max], lat=[lat_min, lat_max])
    
    # resample to desired spatial resolution
    ds.to_latlon(lon=[lon_min, lon_max], lat=[lat_min, lat_max], res=[spatial_resolution, spatial_resolution])
    
    # run commands
    ds.run()
    
    # save data
    ds.to_nc(file_name, overwrite=True)

print(f'Download land surface temperature data for {month}/{year} complete.')