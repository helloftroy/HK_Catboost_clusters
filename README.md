# HK_Catboost_clusters

# 1) Jupyter Notebooks
#### beta_diversity.ipynb
* beta diversity, cluster richness, and sensor fraction
#### catboost_IMG_clusters.ipynb
* catboost training
* feature importance with SHAP values
* grid search
* all for classification models (biome model, and disease class model)
#### catboost_regression.ipynb
* catboost training
* feature importance with SHAP values
* grid search
* all for regression model with marine dataset
#### heatmaps_tree_enrichment.ipynb
* heatmaps for full biome dataset
#### hk_mmseq2.ipynb
* preparation of sensory and HK proteins for mmseq2
* analysis of mmseq2 results using % pfam identity (graphs not in manuscript)
* creation of cluster matrix from mmseq2 results
#### tSNE_heatmap_disease.ipynb
* tSNE for human centered biomes and tSNE exploration
* heatmaps for human centeres biomes and other biome exploration
#### Feature_Selection_Mgnify.ipynb
* feature selection methods on Mgnify dataset
#### exploring_specific_clusters.ipynb
* explore specific clusters of high feature importance
* annotation file creation
* figures for histogram, pfam domain vs. cluster count figures
* analysis on vick

# 2) Scripts
#### make_matrix.py
* used to create matrix by pulling all >20,000 pfam tables and grouping by cluster
* broke into multiple files to avoid crashing kernel
#### condence_matrix.py
* grouped matrix from make_matrix.py script
#### pearson_correlaction_coefficient.py
* feature selection method for PCC, ran in script as very long process
#### annotate.py
* pull from uniprot using expasy ID, using Bio SwissProt and ExPASy

# 3) Data
#### IMG Table S3 - Accessory Table
* accessory data after cleaning. Note: not all biomes have accessory data therefore the table is shorter than full dataset size
* Can filter the GOLD identifiers to Human:Large Intestine, or Marine in order to find the accessory data used for CatBoost Disease State Classifier and CatBoost Regressor, respectively
* contains disease class states for gut biomes
* contains physical parameters used for CatBoost regression on Marine bacteria
### GOLD Analysis Project ID
* A list of all GOLD identifiers used in this study
### other datasets can be found in manuscript or in the extra link containing full CatBoost abundance matrix

