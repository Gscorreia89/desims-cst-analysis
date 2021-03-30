"""
This python script ript to aggregate raw counts, 
prepare the 16S data matrix and correct OTU assignments


"""
import pandas as pds
import numpy as np
import matplotlib.pyplot as plt

"""

VMET2 Dataset

"""

# Read the excel spreadsheet 
# Table with raw counts
otu_table_nr = pds.read_excel('../../Final Data for paper/16S Data/VMET2_16S_Not Subsampled Results-081019.xlsx', sheet_name='FULL TAXONOMY')

# We keep the Species/RDP assignment from RDP, but fetch the BVAB1 assignment from STIRRUPs
otu_table_nr.loc[otu_table_nr['STIRRUPs'] == 'Lachnospiraceae_BVAB1', 'Species/RDP'] = 'Lachnospiraceae_BVAB1'
otu_table_nr.loc[otu_table_nr['STIRRUPs'] == 'Clostridiales_BVAB2', 'Species/RDP'] = 'Clostridiales_BVAB2'
otu_table_nr.loc[otu_table_nr['STIRRUPs'] == 'Clostridiales_BVAB3', 'Species/RDP'] = 'Clostridiales_BVAB3'

# Rename L. fornicalis to L. jensenii 
otu_table_nr.loc[otu_table_nr['Species/RDP'] == 'Lactobacillus_fornicalis', 'Species/RDP'] = 'Lactobacillus_jensenii'

# set a multiIndex - hierarchical index to assist in aggregating the counts accross Species
otu_table_nr_multi = otu_table_nr.set_index(['Phylum', 'Class', 'Order', 'Family', 'Genera', 'Species/RDP', 'Group'], inplace=False)

# Sum all counts from OTUs accross a species
species = otu_table_nr_multi.sum(level='Species/RDP')
# Remove all unnassigned OTU counts
species.drop(index='_', inplace=True)

# Filtering the count matrices
# Remove any species or genera with less than 50 counts accross all samples
species_filtered = species.loc[species.sum(axis=1) >= 50, :]

species_filtered = species_filtered.T

# Remove the sequencing repeat samples
which_qc = [x for x in species_filtered.index if x[-1] == 'R']
species_filtered.drop(which_qc, inplace=True)

which_qc = [x for x in species_filtered.index if 'R' in x[-2:] and len(x) >3 ]
species_filtered.drop(which_qc, inplace=True)

which_qc = [x for x in species_filtered.index if 'C' in x]
species_filtered.drop(which_qc, inplace=True)

padded_index = [x[0] + x[1:].zfill(3) if 'G' in x else x for x in species_filtered.index]

species_filtered.index = padded_index

species_filtered.index.name = 'Seq_ID'

# Save the new data matrices
species_filtered.to_csv('../../Final Data for paper/16S Data/VMET2_16S_SpeciesMatrixFiltered.csv', index=True)



"""

VMET Dataset

"""

# Read the excel spreadsheet 
# Table with raw counts
otu_table_nr = pds.read_excel('../../Final Data for paper/16S Data/621_VMET_data_results.xlsx', sheet_name='Taxonomy_Full')

# Rename L. fornicalis to L. jensenii 
otu_table_nr.loc[otu_table_nr['Species(97%)'] == 'Lactobacillus_fornicalis', 'Species(97%)'] = 'Lactobacillus_jensenii'

# set a multiIndex - hierarchical index to assist in aggregating the counts accross Species
otu_table_nr_multi = otu_table_nr.set_index(['Phylum', 'Class', 'Order', 'Family', 'Genus', 'Species(95%)', 'Species(97%)', 'Group'], inplace=False)

# Sum all counts from OTUs accross a species
species = otu_table_nr_multi.sum(level='Species(97%)')
# Remove all unnassigned OTU counts
species.drop(index='_', inplace=True)

# Filtering the count matrices
# Remove any species or genera with less than 50 counts accross all samples
species_filtered = species.loc[species.sum(axis=1) >= 50, :]

species_filtered = species_filtered.T
species_filtered.index.name = 'Seq_ID'

# Save the new data matrices
species_filtered.to_csv('../../Final Data for paper/16S Data/VMET_16S_SpeciesMatrixFiltered.csv', index=True)

