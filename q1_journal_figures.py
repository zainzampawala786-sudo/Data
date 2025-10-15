import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import scipy
from sklearn import metrics
import shap

# FINAL_COLORS Palette
FINAL_COLORS = {
    'primary': '#1f77b4',
    'secondary': '#ff7f0e',
    'tertiary': '#2ca02c',
    'quaternary': '#d62728',
    'fifth': '#9467bd',
    'sixth': '#8c564b',
    'seventh': '#e377c2',
    'eighth': '#7f7f7f',
    'ninth': '#bcbd22',
    'tenth': '#17becf'
}

# Typography Settings
TYPOGRAPHY = {
    'font.family': 'serif',
    'font.serif': 'Times New Roman'
}

# Figure Settings
FIGURE_SETTINGS = {
    'fig.figsize': (10, 6),
    'axes.titlesize': 14,
    'axes.labelsize': 12
}

# Axis Settings
AXIS_SETTINGS = {
    'xtick.labelsize': 10,
    'ytick.labelsize': 10
}

# Legend Settings
LEGEND_SETTINGS = {
    'legend.fontsize': 10
}

# Set up matplotlib rcParams
plt.rcParams.update({**TYPOGRAPHY, **FIGURE_SETTINGS, **AXIS_SETTINGS, **LEGEND_SETTINGS})

# Paths for data loading
INTERNAL_PATH = r"C:\Users\zainz\Desktop\Second Analysis\ZZTongji Dataset AMI Internal Validation One_Year.xlsx"
EXTERNAL_PATH = r"C:\Users\zainz\Desktop\Second Analysis\ZZMimic Dataset AMI External Validation One_Year.xlsx"
RESULTS_DIR = r"C:\Users\zainz\Desktop\Second Analysis\TRIPOD_Q1_Results\FIGS"

# Create output directories
import os

subdirs = ['figures', 'tables', 'supplementary']
for subdir in subdirs:
    os.makedirs(os.path.join(RESULTS_DIR, subdir), exist_ok=True)

# Helper functions

def save_figure(filename, dpi=600):
    plt.savefig(filename + '.pdf', dpi=dpi)
    plt.savefig(filename + '.png', dpi=dpi)
    plt.savefig(filename + '.svg')


def format_pvalue(p):
    if p < 0.001:
        return '< 0.001'
    elif p < 0.01:
        return f'{p:.3f} *'
    elif p < 0.05:
        return f'{p:.3f} **'
    else:
        return f'{p:.3f}'


def format_ci(lower, upper):
    return f'[{lower:.2f}, {upper:.2f}]'


def calculate_smd(group1, group2):
    mean1, mean2 = np.mean(group1), np.mean(group2)
    sd1, sd2 = np.std(group1), np.std(group2)
    smd = (mean1 - mean2) / np.sqrt((sd1 ** 2 + sd2 ** 2) / 2)
    return smd

# Main function to generate all figures and tables

def main():
    # Call all figure and table creation functions sequentially
    create_figure1_cohort_flowchart()
    create_figure2_feature_selection()
    create_figure3_feature_set_performance()
    create_figure4_roc_pr_curves()
    create_figure5_external_validation()
    create_figure6_confusion_matrices()
    create_figure7_population_forest_plot()
    create_figure8_feature_scaling()
    create_figure9_rf_shap_summary()
    create_figure10_rf_shap_dependence()
    create_figure11_lr_shap_summary()
    create_figure12_lr_shap_dependence()
    create_figure13_missing_data_heatmap()
    create_figure14_correlation_heatmap()

    create_table1_baseline_characteristics()
    create_table2_boruta_summary()
    create_table3_feature_selection_summary()
    create_table4_bootstrap_stability()
    create_table5_rfe_ranking()
    create_table6_multi_method_consensus()
    create_table7_optimal_hyperparameters()
    create_table8_gridsearch_results()
    create_table9_model_performance()
    create_table10_cv_results()
    create_table11_stacked_ensemble()
    create_table12_threshold_calibration()
    create_table13_feature_set_metrics()
    create_table14_lr_coefficients()


if __name__ == '__main__':
    main()