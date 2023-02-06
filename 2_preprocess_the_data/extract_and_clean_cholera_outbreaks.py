#!/bin/python

# this script extracts and cleans cholera outbreaks from the downloaded outbreaks PDF files

print('Extract and clean cholera outbreaks...')

# import packages
import os
import glob
import numpy as np
import pandas as pd
import camelot

# define function to squeeze empty cells
def squeeze_empty_cells(row):
    
    squeezed_cells = [i for i in row.tolist() if i != '']
    
    for i in range(0, len(squeezed_cells)):
        row.iloc[i] = squeezed_cells[i]
    
    return row

# define function to extract and clean cholera outbreaks
def extract_and_clean_cholera_outbreaks(file):
    
    # get file name
    file_name = file.split('/')[-1]    
    print(f'    {file_name}')
    
    # set table areas
    year = int(file.split('/')[4])
    if year in [2010, 2011]:
        table_areas = ['80,600,425,0']
    elif year in [2012, 2013, 2014, 2015]:
        table_areas = ['80,600,450,0']
    elif year in [2016, 2017, 2018]:
        table_areas = ['180,600,550,0']
    
    # extract raw tables
    if (year == 2016 and int(file_name[:-11]) >= 14) or year in [2017, 2018]:
        tables_raw = camelot.read_pdf(file,
                                      pages='3-end', # skip title page and summary page
                                      process_background=True,
                                      table_areas=table_areas,
                                      strip_text='\n',
                                      line_scale=40)
    else:
        tables_raw = camelot.read_pdf(file,
                                      pages='2-end', # skip title page
                                      process_background=True,
                                      table_areas=table_areas,
                                      strip_text='\n',
                                      line_scale=40)
    
    # clean raw tables
    tables_clean = pd.DataFrame()
    for i in range(0, len(tables_raw)):
        
        # extract raw table as dataframe
        table_raw = tables_raw[i].df
        
        # drop first column because it doens't contain relevant data
        table_raw = table_raw.drop(table_raw.columns[0], axis=1)
        
        # tag cholera outbreak rows with missing district
        table_raw.iloc[:, 0] = table_raw.apply(lambda x: 'district missing' if (x.iloc[0] == '') & ('cholera' in x.iloc[1].lower()) else x.iloc[0], axis=1)
        
        # squeeze empty cells
        table_raw = table_raw.apply(squeeze_empty_cells, axis=1)
        
        # fill nan values
        table_raw = table_raw.fillna('')
        
        # drop empty columns
        for col in table_raw.columns:
            if table_raw[col].nunique() == 1:
                table_raw = table_raw.drop(col, axis=1)
        
        # keep only relevant columns
        if year <= 2011:
            table_raw = table_raw.iloc[:, :4]
        else:
            table_raw = table_raw.iloc[:, :5]            
        
        # add empty extra column where necessary
        if year <= 2011:
            table_raw.insert(loc=3, column='temp', value='')
        
        # harmonize column names
        table_raw.columns = range(0,5)
        
        # drop almost empty rows
        for row in range(0, len(table_raw)):
            if table_raw.loc[[row]].iloc[0].nunique() <= 2:
                table_raw = table_raw.drop(row, axis=0)
        
        # split cases and deaths where necessary
        if year <= 2011:
            table_raw.iloc[:, 3] = table_raw.iloc[:, 2].apply(lambda x: x.split('/')[1] if len(x.split('/')) > 1 else '')
            table_raw.iloc[:, 2] = table_raw.iloc[:, 2].apply(lambda x: x.split('/')[0] if len(x.split('/')) > 1 else x)
        
        # keep only rows containing cholera outbreaks
        table_raw = table_raw[table_raw.apply(lambda x: x.str.contains('cholera', case=False).any(), axis=1)]
        
        # make all columns lower case
        table_raw = table_raw.apply(lambda x: x.astype(str).str.lower())
        
        # remove unwanted characters in disease column
        table_raw.iloc[:, 1] = table_raw.iloc[:, 1].apply(lambda x: x.replace('i', '').replace('x', '').replace('v', '').replace('.', '').strip())
        
        # concat extracted and cleaned cholera outbreaks
        tables_clean = pd.concat([tables_clean, table_raw], ignore_index=True)
    
    # rename columns
    tables_clean.columns = ['district', 'disease', 'cases', 'deaths', 'start_date']
    
    # add file name
    tables_clean['file_name'] = file_name

    return tables_clean

# make list of desired years
years = list(np.arange(2010, 2019))

# set path for reading outbreaks
path = '../../data/outbreaks'

# create empty dataframe
cholera_outbreaks = pd.DataFrame(columns=['file_name'])

# loop through years
for year in years:
    
    print(f'Processing {year}...')
    
    # get all PDF files in directory
    files = glob.glob(os.path.join(path, str(year), '*.pdf'))
    
    # loop through files
    for file in files:
        
        # extract and clean cholera outbreaks
        extracted_cleaned_cholera_outbreaks = extract_and_clean_cholera_outbreaks(file)
        
        # append all extracted and cleaned cholera outbreaks to previously created dataframe
        cholera_outbreaks = pd.concat([cholera_outbreaks, extracted_cleaned_cholera_outbreaks], ignore_index=True)

# write extracted and cleaned cholera outbreaks to csv
cholera_outbreaks.to_csv(os.path.join(path, 'cholera_outbreaks.csv'), index=False)

print('Extract and clean cholera outbreaks complete.')