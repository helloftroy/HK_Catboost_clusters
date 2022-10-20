import pandas as pd
import datetime
import os

def make_one_matrix(main_dir, output_df, output_df_0):
    catboost_matrix = pd.DataFrame()
    parent_list = os.listdir(main_dir)
    for child in parent_list:
        if 'copy_matrix_ready' in child:
            print(child)
            metagenome = pd.read_csv(os.path.join(main_dir,child))
            metagenome = metagenome.drop('Unnamed: 0', axis=1)
            metagenome = metagenome.reset_index(drop = True)

            catboost_matrix = pd.concat([catboost_matrix, metagenome])

    catboost_matrix = catboost_matrix.fillna(0)
    catboost_matrix = catboost_matrix.reset_index(drop=True)
    # add biome label and reorder columns
   # catboost_matrix['biome'] = catboost_matrix['Ecosystem']+":"+catboost_matrix['Ecosystem Category']+":"+catboost_matrix['Ecosystem Subtype']
   # catboost_matrix = catboost_matrix.drop(['Ecosystem', 'Ecosystem Category', 'Ecosystem Subtype', 'index'], axis=1)
    
    catboost_matrix.to_csv(output_df, index='False')
    print("final number of metagenomes: ", catboost_matrix['GOLD Analysis Project ID'].nunique())
    #print("final number of biomes: ", catboost_matrix['biome'].nunique())
    
    df = catboost_matrix.loc[~(catboost_matrix.sum(axis=1) == 0), ~(catboost_matrix.drop('GOLD Analysis Project ID',axis=1).sum(axis=1) == 0)]
    df = df.reset_index(drop=True)
    df.to_csv(output_df_0, index='False')
    print("final number of metagenomes after drop 0: ", df['GOLD Analysis Project ID'].nunique())
    print("final number of biomes after drop 0: ", df['biome'].nunique())
    
    

if __name__ == '__main__': 
    
    
    
    
    main_dir = "/global/cfs/cdirs/kbase/KE-Catboost/HK/pfam_matrix/"
    
    output_df = "/global/cfs/cdirs/kbase/KE-Catboost/HK/pfam_matrix/pfam_copy_number.csv"
    output_df_0 = "/global/cfs/cdirs/kbase/KE-Catboost/HK/pfam_matrix/pfam_copy_number_no_0.csv"
    
    make_one_matrix(main_dir, output_df, output_df_0)
    
