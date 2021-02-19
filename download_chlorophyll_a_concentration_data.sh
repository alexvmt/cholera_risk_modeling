#!/bin/bash

echo 'Download chlorophyll-a concentration data...'
if [ ! -d ../data/chlorophyll_a_concentration ]; then
  mkdir -p ../data/chlorophyll_a_concentration;
fi
for year in 2010 2011 2012 2013 2014 2015
do
if [ ! -d ../data/chlorophyll_a_concentration/$year ]; then
  mkdir -p ../data/chlorophyll_a_concentration/$year;
fi
wget --recursive --no-directories --no-clobber --directory-prefix=../data/chlorophyll_a_concentration/$year ftp://anon-ftp.ceda.ac.uk/neodc/esacci/ocean_colour/data/v4.2-release/geographic/netcdf/chlor_a/monthly/v4.2/$year
done
wait
echo 'Download chlorophyll-a concentration data complete.'