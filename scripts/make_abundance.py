import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
import datetime

"""
main_dir = "/global/cfs/cdirs/kbase/jungbluth/HK_sensors/run2/"
parent_list = os.listdir(main_dir)
my_columns = pd.Series(['GOLD Analysis Project ID', 'gene_copy'], )
all_studies_aa = pd.DataFrame()
count = 0
for child in parent_list:
    if count < 30000000000: #20,000 total
        if 'pfam-hits_table.tsv' in child:
                # read in file and extract the biome info
            metagenome = pd.read_csv(os.path.join(main_dir,child), delimiter="\t", usecols=my_columns)

            summed = metagenome.groupby('GOLD Analysis Project ID').sum()
            summed['count'] = metagenome.groupby('GOLD Analysis Project ID').count()

            all_studies_aa = pd.concat([all_studies_aa, summed])
    else:
        break
    if count%500 == 1:
        print(count)
        print(datetime.datetime.now())
    count = count+1
"""
all_studies_aa = pd.read_csv("/global/cfs/cdirs/kbase/KE-Catboost/HK/protein_abundance_metagenomes.csv")
all_studies_aa['cpy_number_total'] = all_studies_aa.gene_copy
all_studies_aa = all_studies_aa.drop('gene_copy', axis=1)

catboost = pd.read_csv("/global/cfs/cdirs/kbase/KE-Catboost/HK/mode_0/catboost_matrix_copy_number_no_0.csv")
catboost = catboost.drop(['Unnamed: 0'], axis=1)
catboost = catboost.merge(all_studies_aa, how='left', on='GOLD Analysis Project ID')

df = catboost.drop(['biome','GOLD Analysis Project ID','Ecosystem Type','Specific Ecosystem'], axis=1)

i=0
for column in df.columns:
    df[column] = df[column].div(df["cpy_number_total"].values)
    i+=1
    if i%100==0:
        print(i)

df['biome'] = catboost.biome
df['GOLD Analysis Project ID']=catboost['GOLD Analysis Project ID']
print(df.head())

df.to_csv("/global/cfs/cdirs/kbase/KE-Catboost/HK/mode_0/copy_number_abundance.csv")