# Cholera risk modeling using essential climate variables and machine learning

In this project I replicate parts of Campbell et al. (2020), relating cholera risk and essential climate variables (ECVs) and using a random forest classifier.

I focus on the years 2010 to 2018 and only on the most predictive ECVs (i. e. sea surface salinity, chlorophyll-a concentration and land surface temperature), as indicated by Campbell et al. (2020), to keep the amount of raw data manageable.

**Contents**

- [Download the data](#download-the-data)
- [Preprocess the data](#preprocess-the-data)
- [Exploratory data analysis and validation](#exploratory-data-analysis-and-validation)
- [Create train and test set](#create-train-and-test-set)
- [Modeling](#modeling)
- [Open questions](#open-questions)
- [Requirements](#requirements)
- [References](#references)



## Download the data

First, outbreaks and ECVs need to be downloaded:
- Outbreaks: `download_outbreaks.py`
- Sea surface salinity: `download_sea_surface_salinity.sh`
- Chlorophyll-a concentration: `download_chlorophyll_a_concentration.sh`
- Land surface temperature: `download_and_preprocess_land_surface_temperature.py`

The land surface temperature data need some extra preprocessing due to their daily temporal resolution and the resulting extremely large amount of data.



## Preprocess the data

Second, downloaded outbreaks and ECVs need to be preprocessed:
- Outbreaks:  `extract_and_clean_cholera_outbreaks.py` and `preprocess_cholera_outbreaks.ipynb`
- ECVs: `preprocess_essential_climate_variables.ipynb`



## Exploratory data analysis and validation

Third, preprocessed cholera outbreaks and ECVs need to be explored and validated:
- `exploratory_data_analysis_and_validation.ipynb`

### Cholera outbreaks in India by district (2010 to 2018)
![Cholera outbreaks in India by district (2010 to 2018)](0_images/cholera_outbreaks_india_district_2010_2018.png 'Cholera outbreaks in India by district (2010 to 2018)')

### Mean sea surface salinity January, April, July and October 2018
![Mean sea surface salinity 2018](0_images/mean_sss_2018.png 'Mean sea surface salinity 2018')

### Mean chlorophyll-a concentration January, April, July and October 2018
![Mean chlorophyll-a concentration 2018](0_images/mean_chlora_2018.png 'Mean chlorophyll-a concentration 2018')

### Mean land surface temperature January, April, July and October 2018
![Mean land surface temperature 2018](0_images/mean_lst_2018.png 'Mean land surface temperature 2018')



## Create train and test set

Fourth, validated cholera outbreaks and ECVs need to be merged to create a train and a test set on district and month level:
- `create_train_and_test_set.ipynb`



## Modeling

Finally, a random forest classifier is trained to predict cholera outbreaks based on a range of ECV features:
- `modeling.ipynb`



## Open questions

- Which local CRS is best to use (e.g. https://epsg.io/7755)?
- How exactly is the buffering done?
- How exactly are the areal means of terrestrial and oceanic variables computed?
- How is the number of non-outbreak data points of 8504 calculated? Intuitively I would calculate 9 years x 12 months x 40 coastal districts = 4320. I'm clearly missing something here.
- Which of the lag variables are used in the final model, i. e. actual lag values, rate of change and/or binary features indicating the rate of change's direction?



## Requirements

Assuming `conda` is installed, run the following commands in your terminal to run the scripts and notebooks in this repository:

- create environment: `conda env create --file=cholera_risk_modeling.yaml`
- activate environment: `conda activate cholera_risk_modeling`
- you might need to do the following in addition: `pip install ghostscript`

Run the scripts and notebooks directly in their respective directory.



## References

### Original paper
Campbell AM, Racault M-F, Goult S, Laurenson A. Cholera Risk: A Machine Learning Approach Applied to Essential Climate Variables. International Journal of Environmental Research and Public Health. 2020; 17(24):9378. https://doi.org/10.3390/ijerph17249378 

### Outbreaks
National Centre for Disease Control, Directorate General of Health Services. Integrated Disease Surveillance Programme. Available online: http://idsp.nic.in/ (accessed on 28 February 2021).

### Level 2 administrative zones for India
University of California, Berkely. Global Administrative Areas. Digital Geospatial Data. 2020. Available online: http://www.gadm.org (accessed on 28 February 2021).

### Sea surface salinity
Boutin, J.; Vergely, J.-L.; Reul, N.; Catany, R.; Koehler, J.; Martin, A.; Rouffi, F.; Arias, M.; Chakroun, M.; Corato, G.; Estella-Perez, V.; Guimbard, S.; Hasson, A.; Josey, S.; Khvorostyanov, D.; Kolodziejczyk, N.; Mignot, J.; Olivier, L.; Reverdin, G.; Stammer, D.; Supply, A.; Thouvenin-Masson, C.; Turiel, A.; Vialard, J.; Cipollini, P.; Donlon, C. (2021): ESA Sea Surface Salinity Climate Change Initiative (Sea_Surface_Salinity_cci): Weekly sea surface salinity product, v03.21, for 2010 to 2020. NERC EDS Centre for Environmental Data Analysis, 8 October 2021. https://catalogue.ceda.ac.uk/uuid/fad2e982a59d44788eda09e3c67ed7d5

### Chlorophyll-a concentration
Sathyendranath, S.; Jackson, T.; Brockmann, C.; Brotas, V.; Calton, B.; Chuprin, A.; Clements, O.; Cipollini, P.; Danne, O.; Dingle, J.; Donlon, C.; Grant, M.; Groom, S.; Krasemann, H.; Lavender, S.; Mazeran, C.; Mélin, F.; Müller, D.; Steinmetz, F.; Valente, A.; Zühlke, M.; Feldman, G.; Franz, B.; Frouin, R.; Werdell, J.; Platt, T. (2021): ESA Ocean Colour Climate Change Initiative (Ocean_Colour_cci): Global chlorophyll-a data products gridded on a geographic projection, Version 5.0. NERC EDS Centre for Environmental Data Analysis, 12 May 2021. https://catalogue.ceda.ac.uk/uuid/e9f82908fd9c48138b31e5cfaa6d692b

### Land surface temperature
Ghent, D.; Veal, K.; Perry, M. (2022): ESA Land Surface Temperature Climate Change Initiative (LST_cci): Multisensor Infra-Red (IR) Low Earth Orbit (LEO) land surface temperature (LST) time series level 3 supercollated (L3S) global product (1995-2020), version 2.00. NERC EDS Centre for Environmental Data Analysis, 25 February 2022. doi:10.5285/ef8ce37b6af24469a2a4bdc31d3db27d. http://dx.doi.org/10.5285/ef8ce37b6af24469a2a4bdc31d3db27d

Data on essential climate variables is available in the ESA Climate Change Initiative's [Open Data Portal](https://climate.esa.int/en/odp/#/dashboard)