#!/bin/bash

# this script downloads land surface temperature data from the ESA Climate Change Initiative for 2010 to 2015

echo 'Download land surface temperature data...'
# create directory if it doesn't already exist
if [ ! -d ../data/land_surface_temperature ]; then
  mkdir -p ../data/land_surface_temperature;
fi
for year in 2010 2011 2012 2013 2014 2015 2016 2017 2018
do
if [ ! -d ../data/land_surface_temperature/$year ]; then
  mkdir -p ../data/land_surface_temperature/$year;
fi
# create directories if they don't already exist and download data
for month in 01 02 03 04 05 06 07 08 09 10 11 12
do
wget --recursive --no-directories --no-clobber --directory-prefix=../data/land_surface_temperature/$year --execute robots=off --accept '*MONTHLY_DAY*.nc' --reject index,html,tmp gws-access.jasmin.ac.uk/public/esacci_lst/AQUA_MODIS_L3C/1.00/$year/$month/00/
done
done
wait
echo 'Download land surface temperature data complete.'