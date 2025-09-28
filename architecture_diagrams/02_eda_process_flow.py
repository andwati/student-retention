"""
EDA Process Flow Diagram
Shows the exploratory data analysis workflow and key insights
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.generic.storage import Storage
from diagrams.generic.compute import Rack
from diagrams.programming.language import Python
from diagrams.onprem.analytics import Tableau
from diagrams.onprem.monitoring import Grafana

with Diagram("Exploratory Data Analysis Process Flow", 
             filename="diagrams/02_eda_process_flow", 
             show=False,
             direction="TB"):
    
    # Data Input
    raw_dataset = Storage("Raw Dataset\ndata.csv\n4,424 rows × 37 columns")
    
    # EDA Steps
    with Cluster("Data Quality Assessment"):
        data_info = Rack("Data Info\n• No missing values\n• No duplicates\n• Mixed data types")
        column_analysis = Rack("Column Analysis\n• 36 predictors\n• 1 target variable\n• Column name cleanup")
    
    with Cluster("Statistical Analysis"):
        descriptive_stats = Grafana("Descriptive Statistics\n• Central tendencies\n• Distributions\n• Outlier detection")
        correlation_analysis = Grafana("Correlation Analysis\n• Feature relationships\n• Multicollinearity check")
    
    with Cluster("Visualization & Insights"):
        target_distribution = Tableau("Target Distribution\n• Graduate: 50%\n• Dropout: 32%\n• Enrolled: 17%")
        feature_plots = Tableau("Feature Analysis\n• Histograms\n• Box plots\n• Categorical counts")
        pattern_discovery = Tableau("Pattern Discovery\n• Key predictors\n• Risk factors\n• Success indicators")
    
    # Key Findings
    with Cluster("Key Findings"):
        class_imbalance = Rack("Class Imbalance\nIdentified for modeling")
        high_cardinality = Rack("High Cardinality\nCourse (51 values)\nApplication order (9 values)")
        data_quality = Rack("Data Quality\nClean dataset\nReady for modeling")
    
    # Data Flow
    raw_dataset >> data_info >> descriptive_stats
    raw_dataset >> column_analysis >> correlation_analysis
    descriptive_stats >> target_distribution
    correlation_analysis >> feature_plots
    target_distribution >> pattern_discovery
    
    pattern_discovery >> class_imbalance
    pattern_discovery >> high_cardinality
    pattern_discovery >> data_quality