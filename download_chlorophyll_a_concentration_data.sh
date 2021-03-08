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
<<<<<<< HEAD
# create directories for years if they don't yet exist
for year in 2010 2011 2012 2013 2014 2015 2016 2017 2018
=======
# create directories if they don't already exist and download data
ffor year in {2010..2018}
>>>>>>> fea8c016ea8be8d0ef32020bebaa97d8fdb8f4ab
do
if [ ! -d ../data/chlorophyll_a_concentration/$year ]; then
  mkdir -p ../data/chlorophyll_a_concentration/$year;
fi
# download data
wget --recursive --no-directories --no-clobber --directory-prefix=../data/chlorophyll_a_concentration/$year ftp://anon-ftp.ceda.ac.uk/neodc/esacci/ocean_colour/data/v4.2-release/geographic/netcdf/chlor_a/monthly/v4.2/$year
done
wait
echo 'Download chlorophyll-a concentration data complete.'
