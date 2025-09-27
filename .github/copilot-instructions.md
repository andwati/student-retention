# Predictive Analysis - Student Success Classification

## Project Overview
This is a comprehensive data science project analyzing student academic success using a dataset with 37 features and 4,424 instances. The goal is to predict whether students will **Dropout**, **Graduate**, or remain **Enrolled** based on academic, demographic, and economic factors.

## Data Architecture
- **Source**: `./data/data.csv` - Student academic success dataset from UCI ML Repository
- **Target Variable**: 3-class categorical (`Dropout`, `Graduate`, `Enrolled`) with class imbalance (~50% Graduate, 32% Dropout, 17% Enrolled)
- **Features**: 36 predictors including academic performance, demographics, socioeconomic factors, and macroeconomic indicators
- **Data Quality**: No missing values, no duplicates, clean dataset

## Key Data Processing Patterns

### Column Naming Conventions
- Remove apostrophes from column names: `Mother's qualification` → `Mothers qualification`
- Fix typos consistently: `Nacionality` → `Nationality`
- Use snake_case or maintain original spacing for display purposes

### Feature Engineering Workflow
1. **Categorical Encoding**: Label encode target variable (Dropout=0, Enrolled=1, Graduate=2)
2. **High Cardinality Handling**: One-hot encode categorical features but consider binning for `Course` and `Application order` columns
3. **Outlier Detection**: Pay attention to curricular units and age at enrollment for extreme values
4. **Class Imbalance**: Address using resampling techniques before modeling

## Notebook Structure & Workflow
The main analysis follows this sequential pattern:

### 1. Data Loading & Initial EDA
```python
# Standard data loading pattern
dataFileNamePath = "./data/data.csv"
masterRawData = pd.read_csv(dataFileNamePath)
data = masterRawData.copy()  # Always work with a copy
```

### 2. Data Cleaning & Preprocessing
- Column name standardization (remove apostrophes, fix typos)
- Null/duplicate checks (this dataset has none)
- Feature type identification and conversion

### 3. Exploratory Data Analysis
- Distribution analysis with histograms for numeric features
- Categorical variable analysis with count plots
- Target variable distribution and class balance assessment
- Feature correlation analysis and outlier detection

### 4. Feature Engineering
- One-hot encoding for categorical variables (results in ~105 features after encoding)
- Label encoding for target variable
- Feature scaling considerations for ML models

### 5. Modeling Approach
- Train/test split (75/25 split standard)
- Baseline logistic regression model
- Handle class imbalance before final modeling
- Multiple algorithm comparison

## Development Patterns

### Display & Visualization Setup
Always include this setup for proper notebook display:
```python
# Expand jupyter display width
from IPython.display import display, HTML
display(HTML("<style>.container { width:100% !important; }</style>"))

# Standard display options
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 150)

# Standard imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
%matplotlib inline
```

### Data Exploration Best Practices
- Use `data.nunique().sort_values()` to identify categorical vs numeric features
- Apply `.describe().T` for transposed statistical summaries
- Use `.filter(like='pattern')` to examine related columns (e.g., `Curricular`)
- Print statements with controlled display width for viewing all columns

### Feature Analysis Patterns
- **High Cardinality Features**: `Course` (51 unique), `Application order` (9 unique) - consider binning
- **Binary Features**: Most encoded as 0/1 (Gender, Scholarship holder, etc.)
- **Continuous Features**: Academic grades, age, curricular units, economic indicators
- **Ordinal Features**: Application order, qualification grades

## Code Quality Standards
- Always create a copy of raw data before manipulation
- Use descriptive variable names: `masterRawData`, `dataFileNamePath`
- Include shape and info statements after major transformations
- Comment data quality observations directly in markdown cells
- Use `.sample()` for quick data inspection rather than `.head()` when exploring patterns

## Performance Considerations
- Dataset size is manageable (4,424 rows) - no special memory handling needed
- One-hot encoding creates ~105 features - monitor for overfitting
- Class imbalance requires resampling strategies
- Consider feature selection techniques for high-dimensional encoded data

## Domain Knowledge
This is an **educational/academic success prediction** problem where:
- Students are classified into 3 outcomes based on their academic journey
- Economic factors (GDP, inflation, unemployment) are included as external influences
- Academic performance metrics are key predictors
- Demographic and socioeconomic factors provide additional context
- The prediction can help institutions identify at-risk students early for intervention