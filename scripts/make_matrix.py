import pandas as pd
import datetime
import os

def make_matrix_py(main_dir, output_dir):
    parent_list = os.listdir(main_dir)
    my_columns = pd.Series(['GOLD Analysis Project ID', #'gene_oid',
                            'gene_copy', 'pfam_id'])
    all_studies = pd.DataFrame()
 #   cluster_labels = pd.read_csv('/global/cfs/cdirs/kbase/KE-Catboost/HK/mode_0/mode_0_clustered_11k_for_df.csv')
 #   GOLD = pd.read_csv('/global/cfs/cdirs/kbase/KE-Catboost/HK/study_gold_list.csv')
    
 #   cluster_labels['gene_oid'] = cluster_labels.gene
    count = 0
    
    for child in parent_list:
        if count < 20000: #20,000 total
            if 'pfam-hits_table.tsv' in child:
                
                # read in file and extract the biome info
                metagenome = pd.read_csv(os.path.join(main_dir,child), delimiter="\t", usecols=my_columns)
  #              f=metagenome.loc[0,'GOLD Analysis Project ID']
  #              if sum(GOLD['GOLD Analysis Project ID'].str.contains(f)) > 0:
    
                names = metagenome.loc[0:1,['GOLD Analysis Project ID']]
                        # remove non-sensory, non-conserved domains
                metagenome = metagenome[~metagenome.pfam_id.str.contains("pfam02895|pfam18947|pfam00672|pfam01627|pfam07536|pfam00072|pfam00512|pfam02518")]
                        # filter to just proteins in cluster
           #         just_clustered = metagenome.merge(cluster_labels, on='gene_oid', how='left')
           #         just_clustered = just_clustered[just_clustered.is_cluster == True]
                        # transpose / sum matrix
                transposed = (metagenome[['pfam_id','gene_copy']].groupby(by=['pfam_id']).sum()).transpose().reset_index()

                new_study = pd.concat([names, transposed], axis=1)
             #       new_study = new_study.loc[~(new_study.drop('GOLD Analysis Project ID',axis=1).sum(axis=1) == 0)]
                all_studies = pd.concat([all_studies, new_study])
        else:
            break
        if count%99 == 1:
            print(count)
            print(datetime.datetime.now())
        count = count+1

    all_studies = all_studies.fillna(0)
    all_studies.to_csv(output_dir)

if __name__ == '__main__':
        # done
    make_matrix_py(main_dir = "/global/cfs/cdirs/kbase/jungbluth/HK_sensors/run2/" ,  
        output_dir="/global/cfs/cdirs/kbase/KE-Catboost/HK/pfam_matrix/copy_matrix_ready_1.csv")
    
    make_matrix_py(main_dir = "/global/cfs/cdirs/kbase/jungbluth/HK_sensors/run2/run/",
        output_dir="/global/cfs/cdirs/kbase/KE-Catboost/HK/pfam_matrix/copy_matrix_ready_2.csv")
    
    make_matrix_py(main_dir = "/global/cfs/cdirs/kbase/jungbluth/HK_sensors/run2/run4/",
        output_dir="/global/cfs/cdirs/kbase/KE-Catboost/HK/pfam_matrix/copy_matrix_ready_3.csv")
    """
    make_matrix_py(main_dir = "/global/cfs/cdirs/kbase/jungbluth/HK_sensors/run2/run5/",
        output_dir="/global/cfs/cdirs/kbase/KE-Catboost/HK/all_clusters_113k/copy_matrix_ready_4.csv")
    
    make_matrix_py(main_dir = "/global/cfs/cdirs/kbase/jungbluth/HK_sensors/run2/run6/",
        output_dir="/global/cfs/cdirs/kbase/KE-Catboost/HK/all_clusters_113k/copy_matrix_ready_5.csv")
    
    make_matrix_py(main_dir = "/global/cfs/cdirs/kbase/jungbluth/HK_sensors/run2/run7/" ,  
        output_dir="/global/cfs/cdirs/kbase/KE-Catboost/HK/all_clusters_113k/copy_matrix_ready_6.csv")
    
    make_matrix_py(main_dir = "/global/cfs/cdirs/kbase/jungbluth/HK_sensors/run2/run8",
        output_dir="/global/cfs/cdirs/kbase/KE-Catboost/HK/all_clusters_113k/copy_matrix_ready_7.csv")
    
    make_matrix_py(main_dir = "/global/cfs/cdirs/kbase/jungbluth/HK_sensors/run2/run9",
        output_dir="/global/cfs/cdirs/kbase/KE-Catboost/HK/all_clusters_113k/copy_matrix_ready_8.csv")
    
    
    
    
    make_matrix_py(main_dir = "/global/cfs/cdirs/kbase/jungbluth/HK_sensors/run2/run2/",
        output_dir="/global/cfs/cdirs/kbase/KE-Catboost/HK/all_clusters_113k/copy_matrix_ready_9.csv")
    
    make_matrix_py(main_dir = "/global/cfs/cdirs/kbase/jungbluth/HK_sensors/run2/run2/run/",
        output_dir="/global/cfs/cdirs/kbase/KE-Catboost/HK/all_clusters_113k/copy_matrix_ready_10.csv")
    
    make_matrix_py(main_dir = "/global/cfs/cdirs/kbase/jungbluth/HK_sensors/run2/run2/run3",
        output_dir="/global/cfs/cdirs/kbase/KE-Catboost/HK/all_clusters_113k/copy_matrix_ready_11.csv")
    
    make_matrix_py(main_dir = "/global/cfs/cdirs/kbase/jungbluth/HK_sensors/run2/run2/run4" ,  
        output_dir="/global/cfs/cdirs/kbase/KE-Catboost/HK/all_clusters_113k/copy_matrix_ready_12.csv")
    
    make_matrix_py(main_dir = "/global/cfs/cdirs/kbase/jungbluth/HK_sensors/run2/run2/run5",
        output_dir="/global/cfs/cdirs/kbase/KE-Catboost/HK/all_clusters_113k/copy_matrix_ready_13.csv")
    
    make_matrix_py(main_dir = "/global/cfs/cdirs/kbase/jungbluth/HK_sensors/run2/run2/run6",
        output_dir="/global/cfs/cdirs/kbase/KE-Catboost/HK/all_clusters_113k/copy_matrix_ready_14.csv")
    
    make_matrix_py(main_dir = "/global/cfs/cdirs/kbase/jungbluth/HK_sensors/run2/run2/run7",
        output_dir="/global/cfs/cdirs/kbase/KE-Catboost/HK/all_clusters_113k/copy_matrix_ready_15.csv")
    
    make_matrix_py(main_dir = "/global/cfs/cdirs/kbase/jungbluth/HK_sensors/run2/run2/run8",
        output_dir="/global/cfs/cdirs/kbase/KE-Catboost/HK/all_clusters_113k/copy_matrix_ready_16.csv")
    
    make_matrix_py(main_dir = "/global/cfs/cdirs/kbase/jungbluth/HK_sensors/run2/run2/run9",
        output_dir="/global/cfs/cdirs/kbase/KE-Catboost/HK/all_clusters_113k/copy_matrix_ready_17.csv")
    
    make_matrix_py(main_dir = "/global/cfs/cdirs/kbase/jungbluth/HK_sensors/run2/run2/run10",
        output_dir="/global/cfs/cdirs/kbase/KE-Catboost/HK/all_clusters_113k/copy_matrix_ready_18.csv")
    
    make_matrix_py(main_dir = "/global/cfs/cdirs/kbase/jungbluth/HK_sensors/run2/run2/run11",
        output_dir="/global/cfs/cdirs/kbase/KE-Catboost/HK/all_clusters_113k/copy_matrix_ready_19.csv")
    
    make_matrix_py(main_dir = "/global/cfs/cdirs/kbase/jungbluth/HK_sensors/run2/run2/run12",
        output_dir="/global/cfs/cdirs/kbase/KE-Catboost/HK/all_clusters_113k/copy_matrix_ready_20.csv")
    
    make_matrix_py(main_dir = "/global/cfs/cdirs/kbase/jungbluth/HK_sensors/run2/run2/run13",
        output_dir="/global/cfs/cdirs/kbase/KE-Catboost/HK/all_clusters_113k/copy_matrix_ready_21.csv")
    
    make_matrix_py(main_dir = "/global/cfs/cdirs/kbase/jungbluth/HK_sensors/run2/run2/run2/",
        output_dir="/global/cfs/cdirs/kbase/KE-Catboost/HK/all_clusters_113k/copy_matrix_ready_22.csv")
    
    make_matrix_py(main_dir = "/global/cfs/cdirs/kbase/jungbluth/HK_sensors/run2/run2/run2/run2",
        output_dir="/global/cfs/cdirs/kbase/KE-Catboost/HK/all_clusters_113k/copy_matrix_ready_23.csv")
    
    make_matrix_py(main_dir = "/global/cfs/cdirs/kbase/jungbluth/HK_sensors/run2/run2/run2/run3",
        output_dir="/global/cfs/cdirs/kbase/KE-Catboost/HK/all_clusters_113k/copy_matrix_ready_24.csv")
    
    make_matrix_py(main_dir = "/global/cfs/cdirs/kbase/jungbluth/HK_sensors/run2/run2/run2/run4",
        output_dir="/global/cfs/cdirs/kbase/KE-Catboost/HK/all_clusters_113k/copy_matrix_ready_25.csv")
    
    make_matrix_py(main_dir = "/global/cfs/cdirs/kbase/jungbluth/HK_sensors/run2/run2/run2/run5",
        output_dir="/global/cfs/cdirs/kbase/KE-Catboost/HK/all_clusters_113k/copy_matrix_ready_26.csv")
    
    make_matrix_py(main_dir = "/global/cfs/cdirs/kbase/jungbluth/HK_sensors/run2/run2/run2/run6",
        output_dir="/global/cfs/cdirs/kbase/KE-Catboost/HK/all_clusters_113k/copy_matrix_ready_27.csv")
    
    make_matrix_py(main_dir = "/global/cfs/cdirs/kbase/jungbluth/HK_sensors/run2/run2/run2/run7",
        output_dir="/global/cfs/cdirs/kbase/KE-Catboost/HK/all_clusters_113k/copy_matrix_ready_28.csv")
    
    make_matrix_py(main_dir = "/global/cfs/cdirs/kbase/jungbluth/HK_sensors/run2/run2/run2/run8",
        output_dir="/global/cfs/cdirs/kbase/KE-Catboost/HK/all_clusters_113k/copy_matrix_ready_29.csv")
    
    make_matrix_py(main_dir = "/global/cfs/cdirs/kbase/jungbluth/HK_sensors/run2/run2/run2/run9",
        output_dir="/global/cfs/cdirs/kbase/KE-Catboost/HK/all_clusters_113k/copy_matrix_ready_30.csv")
    
    make_matrix_py(main_dir = "/global/cfs/cdirs/kbase/jungbluth/HK_sensors/run2/run2/run2/run/",
        output_dir="/global/cfs/cdirs/kbase/KE-Catboost/HK/all_clusters_113k/copy_matrix_ready_31.csv")
    
    make_matrix_py(main_dir = "/global/cfs/cdirs/kbase/jungbluth/HK_sensors/run2/run2/run2/run/run",
        output_dir="/global/cfs/cdirs/kbase/KE-Catboost/HK/all_clusters_113k/copy_matrix_ready_32.csv")
        
    make_matrix_py(main_dir = "/global/cfs/cdirs/kbase/jungbluth/HK_sensors/run2/run2/run2/run/run1/",
        output_dir="/global/cfs/cdirs/kbase/KE-Catboost/HK/all_clusters_113k/copy_matrix_ready_33.csv")
    
    make_matrix_py(main_dir = "/global/cfs/cdirs/kbase/jungbluth/HK_sensors/run2/run2/run2/run/run2/",
        output_dir="/global/cfs/cdirs/kbase/KE-Catboost/HK/all_clusters_113k/copy_matrix_ready_34.csv")
    
    make_matrix_py(main_dir = "/global/cfs/cdirs/kbase/jungbluth/HK_sensors/run2/run2/run2/run/run1/run",
        output_dir="/global/cfs/cdirs/kbase/KE-Catboost/HK/all_clusters_113k/copy_matrix_ready_35.csv")
    
    make_matrix_py(main_dir = "/global/cfs/cdirs/kbase/jungbluth/HK_sensors/run2/run2/run2/run/run/run2",
        output_dir="/global/cfs/cdirs/kbase/KE-Catboost/HK/all_clusters_113k/copy_matrix_ready_36.csv")
    
    make_matrix_py(main_dir = "/global/cfs/cdirs/kbase/jungbluth/HK_sensors/run2/run2/run2/run/run/run",
        output_dir="/global/cfs/cdirs/kbase/KE-Catboost/HK/all_clusters_113k/copy_matrix_ready_37.csv")
    
    make_matrix_py(main_dir = "/global/cfs/cdirs/kbase/jungbluth/HK_sensors/run2/run2/run2/run/run/oops",
        output_dir="/global/cfs/cdirs/kbase/KE-Catboost/HK/all_clusters_113k/copy_matrix_ready_38.csv")
    
    
    make_matrix_py(main_dir = "/global/cfs/cdirs/kbase/jungbluth/HK_sensors/run2/run3/",
        output_dir="/global/cfs/cdirs/kbase/KE-Catboost/HK/all_clusters_113k/copy_matrix_ready_39.csv")
    make_matrix_py(main_dir = "/global/cfs/cdirs/kbase/jungbluth/HK_sensors/run2/run3/run",
        output_dir="/global/cfs/cdirs/kbase/KE-Catboost/HK/all_clusters_113k/copy_matrix_ready_40.csv")
    make_matrix_py(main_dir = "/global/cfs/cdirs/kbase/jungbluth/HK_sensors/run2/run3/run10",
        output_dir="/global/cfs/cdirs/kbase/KE-Catboost/HK/all_clusters_113k/copy_matrix_ready_41.csv")
    make_matrix_py(main_dir = "/global/cfs/cdirs/kbase/jungbluth/HK_sensors/run2/run3/run2",
        output_dir="/global/cfs/cdirs/kbase/KE-Catboost/HK/all_clusters_113k/copy_matrix_ready_42.csv")
    make_matrix_py(main_dir = "/global/cfs/cdirs/kbase/jungbluth/HK_sensors/run2/run3/run3",
        output_dir="/global/cfs/cdirs/kbase/KE-Catboost/HK/all_clusters_113k/copy_matrix_ready_43.csv")
    make_matrix_py(main_dir = "/global/cfs/cdirs/kbase/jungbluth/HK_sensors/run2/run3/run4",
        output_dir="/global/cfs/cdirs/kbase/KE-Catboost/HK/all_clusters_113k/copy_matrix_ready_44.csv")
    make_matrix_py(main_dir = "/global/cfs/cdirs/kbase/jungbluth/HK_sensors/run2/run3/run5",
        output_dir="/global/cfs/cdirs/kbase/KE-Catboost/HK/all_clusters_113k/copy_matrix_ready_45.csv")
    make_matrix_py(main_dir = "/global/cfs/cdirs/kbase/jungbluth/HK_sensors/run2/run3/run6",
        output_dir="/global/cfs/cdirs/kbase/KE-Catboost/HK/all_clusters_113k/copy_matrix_ready_46.csv")
    make_matrix_py(main_dir = "/global/cfs/cdirs/kbase/jungbluth/HK_sensors/run2/run3/run7",
        output_dir="/global/cfs/cdirs/kbase/KE-Catboost/HK/all_clusters_113k/copy_matrix_ready_47.csv")
    make_matrix_py(main_dir = "/global/cfs/cdirs/kbase/jungbluth/HK_sensors/run2/run3/run8",
        output_dir="/global/cfs/cdirs/kbase/KE-Catboost/HK/all_clusters_113k/copy_matrix_ready_48.csv")
    make_matrix_py(main_dir = "/global/cfs/cdirs/kbase/jungbluth/HK_sensors/run2/run3/run9",
        output_dir="/global/cfs/cdirs/kbase/KE-Catboost/HK/all_clusters_113k/copy_matrix_ready_49.csv")
    """

    
