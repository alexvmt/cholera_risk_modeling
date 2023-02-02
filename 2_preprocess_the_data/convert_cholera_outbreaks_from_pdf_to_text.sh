#!/bin/bash

echo 'Converting cholera outbreaks from PDF to text...'

for year in {2010..2018}
do
echo "Processing $year..."
for file in ../data/cholera_outbreaks/$year/*.pdf
do
pdftotext "$file"
done
done

wait
echo 'Converting cholera outbreaks from PDF to text complete.'