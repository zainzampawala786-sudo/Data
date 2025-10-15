"""
════════════════════════════════════════════════════════════════════════════════
PULSE-IABP Study Configuration
════════════════════════════════════════════════════════════════════════════════
Date: 2025-10-15 19:17:45 UTC
Author: zainzampawala786-sudo
Study: One-Year Mortality Prediction in AMI Patients with IABP Support
TRIPOD Type: 2b (Development + External Validation)
════════════════════════════════════════════════════════════════════════════════
"""

from pathlib import Path
import numpy as np

# ════════════════════════════════════════════════════════════════════════════════
# FILE PATHS (⚠️ UPDATE THESE TO YOUR SYSTEM!)
# ════════════════════════════════════════════════════════════════════════════════

INTERNAL_PATH = r"C:\Users\zainz\Desktop\Second Analysis\ZZTongji Dataset AMI Internal Validation One_Year.xlsx"
EXTERNAL_PATH = r"C:\Users\zainz\Desktop\Second Analysis\ZZMimic Dataset AMI External Validation One_Year.xlsx"
RESULTS_DIR = Path(r"C:\Users\zainz\Desktop\Second Analysis\TRIPOD_Q1_Results")

# ════════════════════════════════════════════════════════════════════════════════
# DIRECTORY STRUCTURE
# ════════════════════════════════════════════════════════════════════════════════

DIRS = {
    'figures': RESULTS_DIR / 'figures',
    'tables': RESULTS_DIR / 'tables',
    'models': RESULTS_DIR / 'models',
    'supplementary': RESULTS_DIR / 'supplementary',
    'data': RESULTS_DIR / 'data',
    'results': RESULTS_DIR / 'results',
    'transformers': RESULTS_DIR / 'transformers',  # NEW: For imputers/scalers
}

# ════════════════════════════════════════════════════════════════════════════════
# STUDY CONFIGURATION
# ════════════════════════════════════════════════════════════════════════════════

CONFIG = {
    # Study design
    'random_state': 42,
    'target_col': 'one_year_mortality',
    'test_size': 0.30,
    'cv_folds': 5,
    
    # Missing data (FIXED: Increased threshold to 40%)
    'missing_threshold': 40.0,  # CHANGED from 10.0 to 40.0
    'protected_features': ['lactate_min', 'lactate_max'],
    'imputation_strategy': 'iterative',  # NEW: 'iterative' (MICE) or 'simple'
    'imputation_n_iter': 10,  # NEW: For MICE
    
    # Feature selection
    'boruta_runs': 20,
    'boruta_vote_threshold': 0.60,
    'rfe_step': 1,
    'vif_threshold': 10.0,  # NEW: Variance Inflation Factor threshold
    
    # Class imbalance (NEW)
    'use_smote': False,  # Set to True for sensitivity analysis
    'class_weight_ratio': None,  # e.g., {0: 1, 1: 2} or None for balanced
    
    # Validation
    'n_bootstrap': 1000,
    'alpha': 0.05,
    
    # Figures
    'figure_dpi': 600,
    'figure_format': ['pdf', 'png', 'svg'],
    
    # External validation (NEW: Prevent data leakage)
    'fit_on_internal_only': True,  # CRITICAL: Always True
    'save_transformers': True,  # Save imputers/scalers for external validation
}

# Set random seed globally
np.random.seed(CONFIG['random_state'])

# ════════════════════════════════════════════════════════════════════════════════
# PLOTTING STANDARDS (Q1 JOURNALS)
# ════════════════════════════════════════════════════════════════════════════════

PLOT_CONFIG = {
    # Fonts
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'Helvetica', 'DejaVu Sans'],
    'font.size': 9,
    'axes.labelsize': 10,
    'axes.titlesize': 11,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'legend.fontsize': 8,
    
    # Quality
    'figure.dpi': 300,
    'savefig.dpi': 600,
    'pdf.fonttype': 42,  # TrueType for Illustrator
    'ps.fonttype': 42,
    'svg.fonttype': 'none',
    
    # Layout
    'figure.constrained_layout.use': False,
    'axes.linewidth': 0.8,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.grid': False,
}

# Figure sizes (inches)
FIGURE_SIZES = {
    'single': (3.5, 2.625),   # Single column
    'double': (7.2, 4.8),     # Double column
    'full': (7.2, 9.5),       # Full page
    'square': (4.5, 4.5),     # Square
    'wide': (7.2, 3.6),       # Wide panel
}

# Colorblind-safe palettes (Wong 2011 + Tol)
COLORS = {
    'models': {
        'Logistic Regression': '#0173B2',
        'Elastic Net': '#DE8F05',
        'Random Forest': '#029E73',
        'XGBoost': '#D55E00',
        'LightGBM': '#CC78BC',
        'SVM': '#949494',
        'CatBoost': '#56B4E9',
    },
    'outcome': {
        'survived': '#029E73',
        'died': '#D55E00',
    },
    'risk': {
        'low': '#029E73',
        'moderate': '#DE8F05',
        'high': '#D55E00',
    },
    'cohort': {
        'internal': '#0173B2',
        'external': '#DE8F05',
    },
}

# ════════════════════════════════════════════════════════════════════════════════
# TRIPOD METADATA
# ════════════════════════════════════════════════════════════════════════════════

TRIPOD_METADATA = {
    'title': 'PULSE-IABP: One-Year Mortality Prediction in AMI Patients with IABP Support',
    'type': 'Type 2b (Development + External Validation)',
    'date': '2025-10-15 19:17:45 UTC',
    'analyst': 'zainzampawala786-sudo',
    'version': '2.0',  # Refactored version
}