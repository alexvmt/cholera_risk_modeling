#!/bin/bash

# this script downloads sea surface salinity data from the ESA Climate Change Initiative for 2010 to 2015

echo 'Download sea surface salinity data...'
# create directory if it doesn't already exist
if [ ! -d ../data/sea_surface_salinity ]; then
  mkdir -p ../data/sea_surface_salinity;
fi
# create directories if they don't already exist and download data
for year in 2010 2011 2012 2013 2014 2015
do
if [ ! -d ../data/sea_surface_salinity/$year ]; then
  mkdir -p ../data/sea_surface_salinity/$year;
fi
wget --recursive --no-directories --no-clobber --directory-prefix=../data/sea_surface_salinity/$year ftp://anon-ftp.ceda.ac.uk/neodc/esacci/sea_surface_salinity/data/v02.31/30days/$year
done
wait
echo 'Download sea surface salinity data complete.'