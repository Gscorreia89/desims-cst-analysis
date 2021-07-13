# desims-cst-analysis

This repository contains data and scripts to replicate the analyses in the manuscript "Direct on-swab metabolic profiling of vaginal microbiome:host interactions during pregnancy and preterm birth".

All scripts are organized in the "Code" folder. There are R markdown notebooks (.Rmd), Jupyter Notebooks (.ipynb), and supplementary .py files with separate definition of functions. There are sub-directories for specific analyses, and the purpose of each file and the main script files which should be ran for each section are described in the accompanying 'readme.md' files.

The Data folder contains all the datasets required to replicate the analysis. These contain pre-processed metabolomics and 
16s sequencing data matrices, clinical and demographical variables, and immune marker abundances. 

Recommended software versions:
* Python version 3.8 or above (Anaconda Python is recommended) 
* R version 4.0.2 or above
* Specific packages used in each script are mentioned in the first cells of Jupyter or R notebooks.

Apart from installing R, Python, and the required packages, no other specific steps are needed to run the 
scripts. Some analyses use cross-validation and resampling, and therefore are computationally more demanding and might take
a few hours to complete. We recommend running on a multicore (16 or more CPU) workstation with 32GB RAM.
