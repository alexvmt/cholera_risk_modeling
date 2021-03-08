# Cholera risk modeling using essential climate variables and machine learning

In this project I replicate parts of Campbell et al. (2020), relating cholera risk and essential climate variables (ECV) and using a random forest classifier.

I focus on the years 2010 to 2018 and only on the most predictive ECV (i. e. sea surface salinity, chlorophyll-a concentration and land surface temperature), as indicated by Campbell et al. (2020), to keep the amount of data manageable (~50 GB at the moment).

First, the outbreaks and ECV data need to be downloaded using the following scripts (they can be executed directly from the subsequent notebooks):
- Cholera outbreaks: download_cholera_outbreaks_data.py
- Sea surface salinity: download_sea_surface_salinity_data.sh
- Chlorophyll-a concentration: download_chlorophyll_a_concentration_data.sh
- Land surface temperature: download_land_surface_temperature_data.sh

Second, the outbreaks and ECV data need to be preprocessed using the following notebooks:
- Cholera outbreaks: preprocess_cholera_outbreaks.ipynb
- ECV data: preprocess_essential_climate_variables.ipynb

Third, the data need to be processed to create a train and test set on district and month level using the following notebook:
- create_train_and_test_set.ipynb

Finally, the train and test set can be used to train a random forest classifier that trys to predict cholera outbreaks:
- modeling.ipynb

#### TODO

- validate outbreaks and ecv data
- add more comments
- exploratory data analysis, create static and interactive maps of outbreaks
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
Reul, N.; Grodsky, S.; Arias, M.; Boutin, J.; Catany, R.; Chapron, B.; D’Amico, F.; Dinnat, E.; Donlon, C.; Fore, A.; et al. Sea surface salinity estimates from spaceborne L-band radiometers: An overview of the first decade of observation (2010–2019). Remote Sens. Environ. 2020, 242, 111769.

### Chlorophyll-a concentration
Sathyendranath, S.; Brewin, R.J.W.; Brockmann, C.; Brotas, V.; Calton, B.; Chuprin, A.; Cipollini, P.; Couto, A.B.; Dingle, J.; Doerffer, R.; et al. An Ocean-Colour Time Series for Use in Climate Studies: The Experience of the Ocean-Colour Climate Change Initiative (OC-CCI). Sensors 2019, 19, 4285.

### Land surface temperature
Ghent, D.; Veal, K.; Trent, T.; Dodd, E.; Sembhi, H.; Remedios, J. A New Approach to Defining Uncertainties for MODIS Land Surface Temperature. Remote Sens. 2019, 11, 1021.

Most data on essential climate variables is available at the ESA Climate Change Initiative's [Open Data Portal](https://climate.esa.int/en/odp/#/dashboard)
