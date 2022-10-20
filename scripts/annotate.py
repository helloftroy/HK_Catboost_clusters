# annotate.py

import pandas as pd
from Bio import ExPASy
from Bio import SwissProt
from urllib.request import urlopen

# change in each script
i=0
k=i
csv= '/global/cfs/cdirs/kbase/KE-Catboost/HK/mode_0/output_1.csv'

blasted_hk = pd.read_csv('/global/cfs/cdirs/kbase/KE-Catboost/HK/mmseqs/Blasted_sensory_proteins_70_identity.csv')

base_url = "https://rest.uniprot.org/uniprotkb/"
annotated_genes = pd.DataFrame()

for a in blasted_hk.expasy_id:
    if (k-i) < 10000:
        aa = blasted_hk.expasy_id[k]
        url = base_url + aa + '.txt'
        try:
            record = SwissProt.read(urlopen(url))
            annotated_genes = pd.concat([annotated_genes, 
                                 pd.DataFrame([record.entry_name, aa, 
                                               record.description,record.gene_name,
                                               record.comments]).transpose()])
        except IndexError:
            ID=''
            DE=''
            GN=''
            for line in urlopen("https://rest.uniprot.org/uniprotkb/E5KK10.txt"):
                line_2 = line.decode('utf-8')
                if line_2[0:2] == 'ID':
                    ID += line_2[3:]
                if line_2[0:2] == 'DE':
                    DE += line_2[3:]
                if line_2[0:2] == 'GN':
                    GN += line_2[3:]
            annotated_genes = pd.concat([annotated_genes, 
                                 pd.DataFrame([ID, aa,DE,GN,'google it']).transpose()])
    else:
        break
    k+=1
    if k%1000 == 0:
        print(k)
annotated_genes.columns = ['entry_name', 'accessions', 'description', 'gene_name', 'comments']
annotated_genes.to_csv(csv)