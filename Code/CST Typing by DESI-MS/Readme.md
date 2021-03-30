# Description of analysis scripts

The scripts in this folder contain a series of analyses correlating DESI-MS or LC-MS metabolic profiles with the 
vaginal microbiome status.

**DESI-MS Data QC.Rmd**: R notebook containing with some basic quality control checks of the DESI-MS spectra. This script 
should be run before all other analyses, since it will generate a list of low quality spectra to exclude.

**DESI-MS CST Typing - Lactobacillus Depleted Detection.Rmd**: R notebook with the random forest discrimination 
of Lactobacillus dominant from Lactobacillus depleted cases, based on their DESI-MS metabolic profiles. 
Used to generate part of the results shown in Figure 2 and Supplementary Data Figures 3, 4, 5, and Table 3.

**DESI-MS CST Typing - CST Comparisons.Rmd**: R notebook with the random forest classifier analysis used to discriminate 
between individual CST with the DESI-MS data. Used to generate part of the 
results shown in Figure 2 and Supplementary Data Figures 3, 4, and Table 3.

**LC-MS CST Typing - Lactobacillus Depleted Detection.Rmd**: R notebook with the random forest discrimination 
of Lactobacillus dominant from Lactobacillus depleted cases, based on their LC-MS metabolic profiles. 
Used to generate part of the results shown in Supplementary Data Figures 3, 4, 5, and Table 3.

**LC-MS CST Typing - CST Comparisons.Rmd**: R notebook with the random forest classifier analysis used to discriminate 
between individual CST with the LC-MS data. Used to generate part of the 
results shown in Supplementary Material Figures 2 and Table 3.

**Bacterial Culture Library.ipynb**: Jupyter Notebook with the analysis of the bacterial culture library data. 
Contains the steps required to obtain Figure 3 from the main manuscript.
