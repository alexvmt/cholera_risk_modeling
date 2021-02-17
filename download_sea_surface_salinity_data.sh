#!/bin/bash

echo 'Download sea surface salinity data...'
if [ ! -d ../data/sea_surface_salinity ]; then
  mkdir -p ../data/sea_surface_salinity;
fi
for year in 2010 2011 2012 2013 2014 2015
do
if [ ! -d ../data/sea_surface_salinity/$year ]; then
  mkdir -p ../data/sea_surface_salinity/$year;
fi
wget --mirror --continue --no-clobber --no-host-directories --directory-prefix=../data/sea_surface_salinity/$year ftp://anon-ftp.ceda.ac.uk/neodc/esacci/sea_surface_salinity/data/v02.31/30days/$year
mv ../data/sea_surface_salinity/$year/neodc/esacci/sea_surface_salinity/data/v02.31/30days/$year/* ../data/sea_surface_salinity/$year
rm -rf ../data/sea_surface_salinity/$year/neodc
done
wait
echo 'Download sea surface salinity data complete.'