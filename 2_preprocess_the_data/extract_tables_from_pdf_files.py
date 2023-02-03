#!/bin/python

# this script extracts tables from the downloaded cholera outbreaks PDF files

print('Extract tables from cholera outbreaks PDF files...')

# import packages
import os
import glob
import numpy as np
import pandas as pd
import camelot

# make list of desired years
years = list(np.arange(2010, 2019))

# set path for reading cholera outbreaks data
path = '../../data/cholera_outbreaks'

# create empty dataframe
cholera_outbreaks_raw = pd.DataFrame(columns=['file_name'])

# loop through years
for year in years:
    
    print(f'Processing {year}...')
    
    # get all pdf files in directory
    files = glob.glob(os.path.join(path, str(year), '*.pdf'))
    
    # loop through files
    for file in files:
        
        file_name = file.split('/')[-1]
        print(f'    {file_name}')
        
        # read tables, fill text vertically and skip new line characters
        if (year == 2016 and int(file_name[:-11]) >= 14) or year in [2017, 2018]:
            tables = camelot.read_pdf(file, pages='3-end', copy_text=['v'], strip_text='\n', process_background=True) # skip title page and summary page
        else:
            tables = camelot.read_pdf(file, pages='2-end', copy_text=['v'], strip_text='\n', process_background=True) # skip title page
        
        # concat extracted tables
        all_tables = pd.DataFrame()
        for i in range(0, len(tables)):
            all_tables = pd.concat([all_tables, tables[i].df], ignore_index=True)
        
        # add file name
        all_tables['file_name'] = file_name
        
        # add all extracted tables to previously created dataframe
        cholera_outbreaks_raw = pd.concat([cholera_outbreaks_raw, all_tables], ignore_index=True)

# write extracted tables to csv
cholera_outbreaks_raw.to_csv(os.path.join(path[:-18], 'cholera_outbreaks_raw.csv'), index=False)

print('Extract tables from cholera outbreaks PDF files complete.')