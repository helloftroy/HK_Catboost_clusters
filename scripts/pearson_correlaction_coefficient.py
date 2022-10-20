import pandas as pd
#import ipywidgets
from sklearn import decomposition
#import altair as alt
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from catboost import CatBoostClassifier, Pool, cv
from sklearn.metrics import plot_confusion_matrix
from pathlib import Path
import os
import matplotlib.pyplot as plt
import numpy as np
from catboost import CatBoost
from sklearn import preprocessing
from catboost.utils import eval_metric
from catboost import EShapCalcType, EFeaturesSelectionAlgorithm
from sklearn.model_selection import StratifiedKFold
from sklearn.feature_selection import SelectKBest, f_classif, chi2, mutual_info_classif

def read_in_data_filter_integer_labels(grouped = 30, abundance=False,
                        csv = "/global/cfs/cdirs/kbase/KE-Catboost/HK/matrix_copy_number/catboost_matrix_copy_number_normalize_abundance_2.csv"):
    df = pd.read_csv(csv)
    df = df.drop('Unnamed: 0', axis=1)
    df = df.fillna(0)

    grouped_df = df.groupby('biome').filter(lambda x : len(x) > grouped)
    grouped_df = grouped_df.reset_index(drop=True)
    print(grouped_df['biome'].nunique())
    if abundance==True:
        print('abundance')
        grouped_df = grouped_df.drop(['cpy_number_total', 'count'],axis=1)

    le = preprocessing.LabelEncoder()
    le.fit(grouped_df.biome)
    #list(le.classes_)
    le.transform(grouped_df.biome)
    
    return grouped_df, le

# copies from ziming https://github.com/Yzm1234/KE/blob/master/lib/ plot and data_prepare
def pearson_correlation_coefficient(X):
    """
    calculate pearson correlation coefficient of matrix X
    X: numpy array (MxN)
    return pcc: numpy array (MxM)
    """
    M, N = X.shape[0], X.shape[1]  # number of features, number of data points
    X_mean = np.mean(X, axis=1).values.reshape(X.shape[0], 1)
    print('1')
    X_std = np.std(X, axis=1).values.reshape(X.shape[0], 1)
    print('2')
    X_tilde = (X-X_mean)/X_std
    print('3')
    pcc = X_tilde@X_tilde.T/N
    print('4')
    np.fill_diagonal(pcc.values, 1, wrap=False)
    return pcc
def feature_extraction(pcc_mat, cutoff):
    """
    AKA: feature_selection_method_4 in notebooks
    select features from full pearson correlation coefficient (PCC) matrix whose correlation is below cutoff
    pcc_mat:
    cutoff: pcc value threshold
    return: a list of feature mask, True means selected, False means not selected
    """
    M = pcc_mat.shape[0]  # number of features
    feature_mask = [True] * M
    print(M)
    pcc_mat_abs = np.abs(pcc_mat)
    for i in range(M):
        for j in range(i):
            if pcc_mat_abs[i][j] >= cutoff:
                pcc_mat_abs.values[i, :] = 0
                pcc_mat_abs.values[:, i] = 0
                feature_mask[i] = False
        if i%16845 == 0:
            print(i)
    return feature_mask
def feature_selection(df, cutoff=0.9):
    """
    This method takes features table and filters out features util correlation of any pair is below the cutoff
    :param df: feature table, N x (M + 1) M: number of features plus one label column ('biome')
    :type df: pandas dataframe
    :param cutoff:  when a pair of features correlation coefficient number is above this threshold, the feature
                    with smaller index will be removed
    :type cutoff: float
    :return: feature table after removing highly correlated features
    :rtype: pandas dataframe work
    """
    df = df.set_index('biome')
    feature_mat = pd.DataFrame(df.to_numpy().transpose())
    print('feature matrix made')
    pcc_mat = pearson_correlation_coefficient(feature_mat)
    print('pcc_matrix complete')
    feature_mask = feature_extraction(pcc_mat, cutoff)
    print('matrix mask complete')
    selected_features = df.columns[feature_mask]
    df = df[selected_features]
    df.insert(0, 'biome', df.index, True)
    df = df.reset_index(drop=True)
    return df


grouped_df, le = read_in_data_filter_integer_labels(csv="/global/cfs/cdirs/kbase/KE-Catboost/HK/matrix_read/catboost_matrix_normalize_abundance_2.csv")
#grouped_df = grouped_df.drop('GOLD Analysis Project ID', axis=1)
X = feature_selection(grouped_df, cutoff=0.5)
pd.DataFrame(X).to_csv("/global/cfs/cdirs/kbase/KE-Catboost/HK/matrix_copy_number/eliminated_features_df_50.csv")