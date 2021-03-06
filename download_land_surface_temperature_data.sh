#!/bin/bash

# this script downloads land surface temperature data from the ESA Climate Change Initiative for 2010 to 2018

echo 'Download land surface temperature data...'
# create data directory if it doesn't yet exist
if [ ! -d ../data ]; then
  mkdir -p ../data;
fi
# create land surface temperature directory if it doesn't yet exist
if [ ! -d ../data/land_surface_temperature ]; then
  mkdir -p ../data/land_surface_temperature;
fi
# create directories for years if they don't yet exist
for year in {2010..2018}
do
if [ ! -d ../data/land_surface_temperature/$year ]; then
  mkdir -p ../data/land_surface_temperature/$year;
fi
# create directories for months if they don't yet exist
for month in {01..12}
do
# download data
wget --recursive --no-directories --no-clobber --directory-prefix=../data/land_surface_temperature/$year --execute robots=off --accept '*MONTHLY_DAY*.nc' --reject index,html,tmp gws-access.jasmin.ac.uk/public/esacci_lst/AQUA_MODIS_L3C/1.00/$year/$month/00/
done
done
wait
echo 'Download land surface temperature data complete.'