# Cholera risk modeling using essential climate variables and machine learning

In this project I replicate parts of Campbell et al. (2020), relating cholera risk and essential climate variables (ECV) and using a random forest classifier.

I focus on the years 2010 to 2018 and only on the most predictive ECV (i. e. sea surface salinity, chlorophyll-a concentration and land surface temperature), as indicated by Campbell et al. (2020), to keep the amount of raw data manageable (~44 GB at the moment).

First, the outbreaks and ECV data need to be downloaded using the following scripts:
- Cholera outbreaks: download_cholera_outbreaks_data.py
- Sea surface salinity: download_sea_surface_salinity_data.sh
- Chlorophyll-a concentration: download_chlorophyll_a_concentration_data.sh
- Land surface temperature: download_and_preprocess_land_surface_temperature_data.py

Second, the outbreaks and ECV data need to be preprocessed using the following notebooks:
- Cholera outbreaks: preprocess_cholera_outbreaks.ipynb
- ECV data: preprocess_essential_climate_variables.ipynb

Third, the data need to be processed to create a train and test set on district and month level using the following notebook:
- create_train_and_test_set.ipynb

Finally, the train and test set can be used to train a random forest classifier that trys to predict cholera outbreaks:
- modeling.ipynb

There is also a notebook that explores the created cholera outbreaks dataset and creates the map shown below:
- exploratory_data_analysis.ipynb

![Cholera outbreaks in India from 2010 to 2018](cholera_outbreaks_india_2010_2018.png 'Cholera outbreaks in India from 2010 to 2018')

#### TODO

- validate outbreaks and ecv data
- add more comments
- exploratory data analysis (e.g. create map of outbreaks)
- improve model

#### Open questions

- Which CRS is best to use in the present case (e.g. https://epsg.io/7755)?
- How is the buffering of geometries done in detail to calculate the areal means?
- Which of the lag variables are used in the final model, i. e. actual lag values, rate of change and/or binary features indicating the rate of change's direction?
- How is the number of non-outbreak data points of 8504 calculated? Intuitively I would calculate 9 years x 12 months x 40 coastal districts = 4320. I'm clearly missing something here.

## References

### Original paper
Campbell AM, Racault M-F, Goult S, Laurenson A. Cholera Risk: A Machine Learning Approach Applied to Essential Climate Variables. International Journal of Environmental Research and Public Health. 2020; 17(24):9378. https://doi.org/10.3390/ijerph17249378 

### Cholera outbreaks
National Centre for Disease Control, Directorate General of Health Services. Integrated Disease Surveillance Programme. Available online: http://idsp.nic.in/ (accessed on 28 February 2021).

### Level 2 administrative zones for India
University of California, Berkely. Global Administrative Areas. Digital Geospatial Data. 2020. Available online: http://www.gadm.org (accessed on 28 February 2021).

### Sea surface salinity
Boutin, J.; Vergely, J.-L.; Reul, N.; Catany, R.; Koehler, J.; Martin, A.; Rouffi, F.; Arias, M.; Chakroun, M.; Corato, G.; Estella-Perez, V.; Guimbard, S.; Hasson, A.; Josey, S.; Khvorostyanov, D.; Kolodziejczyk, N.; Mignot, J.; Olivier, L.; Reverdin, G.; Stammer, D.; Supply, A.; Thouvenin-Masson, C.; Turiel, A.; Vialard, J.; Cipollini, P.; Donlon, C. (2021): ESA Sea Surface Salinity Climate Change Initiative (Sea_Surface_Salinity_cci): Weekly sea surface salinity product, v03.21, for 2010 to 2020. NERC EDS Centre for Environmental Data Analysis, 8 October 2021. https://catalogue.ceda.ac.uk/uuid/fad2e982a59d44788eda09e3c67ed7d5

### Chlorophyll-a concentration
Sathyendranath, S.; Jackson, T.; Brockmann, C.; Brotas, V.; Calton, B.; Chuprin, A.; Clements, O.; Cipollini, P.; Danne, O.; Dingle, J.; Donlon, C.; Grant, M.; Groom, S.; Krasemann, H.; Lavender, S.; Mazeran, C.; Mélin, F.; Müller, D.; Steinmetz, F.; Valente, A.; Zühlke, M.; Feldman, G.; Franz, B.; Frouin, R.; Werdell, J.; Platt, T. (2021): ESA Ocean Colour Climate Change Initiative (Ocean_Colour_cci): Global chlorophyll-a data products gridded on a geographic projection, Version 5.0. NERC EDS Centre for Environmental Data Analysis, 12 May 2021. https://catalogue.ceda.ac.uk/uuid/e9f82908fd9c48138b31e5cfaa6d692b

### Land surface temperature
Ghent, D.; Veal, K.; Perry, M. (2022): ESA Land Surface Temperature Climate Change Initiative (LST_cci): Multisensor Infra-Red (IR) Low Earth Orbit (LEO) land surface temperature (LST) time series level 3 supercollated (L3S) global product (1995-2020), version 2.00. NERC EDS Centre for Environmental Data Analysis, 25 February 2022. doi:10.5285/ef8ce37b6af24469a2a4bdc31d3db27d. http://dx.doi.org/10.5285/ef8ce37b6af24469a2a4bdc31d3db27d

Data on essential climate variables is available at the ESA Climate Change Initiative's [Open Data Portal](https://climate.esa.int/en/odp/#/dashboard)