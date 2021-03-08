#!/bin/bash

# this script downloads chlorophyll-a concentration data from the ESA Climate Change Initiative for 2010 to 2018

echo 'Download chlorophyll-a concentration data...'
# create data directory if it doesn't yet exist
if [ ! -d ../data ]; then
  mkdir -p ../data;
fi
# create chlorophyll-a concentration directory if it doesn't yet exist
if [ ! -d ../data/chlorophyll_a_concentration ]; then
  mkdir -p ../data/chlorophyll_a_concentration;
fi
# create directories for years if they don't yet exist
for year in {2010..2018}
do
if [ ! -d ../data/chlorophyll_a_concentration/$year ]; then
  mkdir -p ../data/chlorophyll_a_concentration/$year;
fi
# download data
wget --recursive --no-directories --no-clobber --directory-prefix=../data/chlorophyll_a_concentration/$year ftp://anon-ftp.ceda.ac.uk/neodc/esacci/ocean_colour/data/v4.2-release/geographic/netcdf/chlor_a/monthly/v4.2/$year
done
wait
echo 'Download chlorophyll-a concentration data complete.'