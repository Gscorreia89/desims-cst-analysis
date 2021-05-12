# Description of 16S Data Analysis scripts

Scripts used to filter the 16s rRNA count matrices and perform Community State Type (CST) assignment.

**aggregateOTUs.py**: Python script containing the steps performed to do basic filtering of the VMET2 and VMET 16S rRNA dataset. 
Used to generate the data matrices used in VMET2 16S Analysis.ipynb and VMET 16S Analysis.ipynb notebooks.

The following two Jupyter Notebooks contain the steps to perform hierarchical clustering and assign each 16s rRNA profile to a Community 
State Type, or CST:

**VMET2 16S Analysis - Community State Type analysis.ipynb**: Notebook containing the HCA of the VMET2 16S dataset and definition of Community State Types

**VMET 16S Analysis - Community State Type analysis.ipynb**: Notebook containing the HCA of the VMET 16S dataset and definition of Community State Types

**16S data CLR Transform.rmd**: R notebook with steps used to generate centred-log-ratio transform of the 16S data matrices.

**CST_Clustering.py**: Python functions for performing Community state type clustering from a 16S data matrix. 
Used in the CST analysis Jupyter notebooks.

**Analysis Figures**: Default directory used to export figures generated from running the scripts above.

