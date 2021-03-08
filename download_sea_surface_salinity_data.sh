#!/bin/bash

# this script downloads sea surface salinity data from the ESA Climate Change Initiative for 2010 to 2018

echo 'Download sea surface salinity data...'
# create data directory if it doesn't yet exist
if [ ! -d ../data ]; then
  mkdir -p ../data;
fi
# create sea surface salinity directory if it doesn't yet exist
if [ ! -d ../data/sea_surface_salinity ]; then
  mkdir -p ../data/sea_surface_salinity;
fi
# create directories for years if they don't yet exist
for year in {2010..2018}
do
if [ ! -d ../data/sea_surface_salinity/$year ]; then
  mkdir -p ../data/sea_surface_salinity/$year;
fi
# download data
wget --recursive --no-directories --no-clobber --directory-prefix=../data/sea_surface_salinity/$year ftp://anon-ftp.ceda.ac.uk/neodc/esacci/sea_surface_salinity/data/v02.31/30days/$year
done
wait
echo 'Download sea surface salinity data complete.'