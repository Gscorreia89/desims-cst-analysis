# Description of analysis scripts

The scripts in this folder contain the main analysis relating the vaginal microbiome community state type (CST) and related
with the

**DESI-MS Data QC.Rmd**: R notebook containing with some basic quality control checks of the DESI-MS spectra. This script 
should be run before all other analyses, since it will generate a list of low quality spectra to exclude.

**DESI-MS CST Typing - Lactobacillus Depleted Detection.Rmd**: R notebook with the random forest classifier discrimination 
of Lactobacillus dominant from Lactobacillus depleted cases using DESI-MS metabolic profiles. Used to generate part of the results shown 
in Figure 2 and Supplementary Material Figures 3, 4, and Table 3.

**DESI-MS CST Typing - CST Comparisons.Rmd**: R notebook with random forest classifier analysis to discriminate 
samples from CST type I, III, IV and V from DESI-MS spectra. Used to generate part of the 
results shown in Figure 2 and Supplementary Material Figures 3, 4, and Table 3.

**LC-MS CST Typing - Lactobacillus Depleted Detection.Rmd**: R notebook with the random forest classifier discrimination 
of Lactobacillus dominant from Lactobacillus depleted cases using liquid chromatography-mass spectrometry data. 
Used to generate part of the results shown in Figure 2 and Supplementary Material Figures 3, 4, and Table 3.

**LC-MS CST Typing - CST Comparisons.Rmd**: R notebook with random forest classifier analysis to discriminate 
samples from CST type I, III, IV and V from LC-MS data. Used to generate part of the 
results shown in Figure 2 and Supplementary Material Figures 3, 4, and Table 3.

**Bacterial Culture Library.ipynb**: Jupyter Notebook with the analysis of the bacterial culture library data. 
Contains the steps required to obtain Figure 3 from the main manuscript.
