"""
Feature Engineering Pipeline Diagram
Shows the detailed feature transformation and encoding process
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.generic.storage import Storage
from diagrams.generic.compute import Rack
from diagrams.programming.language import Python
from diagrams.onprem.analytics import Tableau
from diagrams.generic.database import SQL

with Diagram("Feature Engineering Pipeline", 
             filename="diagrams/06_feature_engineering_pipeline", 
             show=False,
             direction="TB"):
    
    # Raw Features Input
    raw_features = Storage("Raw Features (37)\n• 36 predictors\n• 1 target variable\n• Mixed data types")
    
    # Categorical Features Processing
    with Cluster("Categorical Feature Processing"):
        categorical_features = Rack("Categorical Features\n• Marital status\n• Application mode\n• Course\n• Nationality\n• Mother's/Father's qualification\n• Mother's/Father's occupation\n• Displaced\n• Educational special needs\n• Debtor\n• Tuition fees up to date\n• Gender\n• Scholarship holder\n• International")
        
        label_encoding = Python("Label Encoding\n• Target variable\n• Dropout = 0\n• Enrolled = 1\n• Graduate = 2")
        
        one_hot_encoding = Python("One-Hot Encoding\n• Categorical predictors\n• Binary columns creation\n• Feature expansion")
    
    # Numerical Features Processing
    with Cluster("Numerical Feature Processing"):
        numerical_features = Rack("Numerical Features\n• Application order\n• Previous qualification grade\n• Admission grade\n• Age at enrollment\n• Curricular units (1st & 2nd sem)\n• Unemployment rate\n• Inflation rate\n• GDP")
        
        feature_validation = Python("Feature Validation\n• Range checks\n• Outlier detection\n• Data type validation")
        
        feature_scaling = Python("Feature Scaling\n• Optional for tree models\n• Standardization available\n• Normalization available")
    
    # Feature Engineering Output
    with Cluster("Engineered Features"):
        encoded_features = Storage("Encoded Features (~105)\n• Original numerical (14)\n• One-hot encoded categorical (90+)\n• Label encoded target (1)")
        
        feature_mapping = SQL("Feature Mapping\n• Original → Encoded names\n• Category mappings\n• Reverse mappings")
        
        preprocessing_metadata = SQL("Preprocessing Metadata\n• Encoding schemes\n• Feature names\n• Transformation info")
    
    # Quality Assurance
    with Cluster("Quality Assurance"):
        feature_consistency = Rack("Feature Consistency\n• Column order preservation\n• Missing feature handling\n• Shape validation")
        
        data_validation = Rack("Data Validation\n• No missing values\n• Consistent data types\n• Feature alignment")
        
        pipeline_testing = Tableau("Pipeline Testing\n• Train/test consistency\n• Transformation verification\n• Edge case handling")
    
    # Data Flow
    raw_features >> categorical_features >> one_hot_encoding
    raw_features >> numerical_features >> feature_validation
    
    categorical_features >> label_encoding
    numerical_features >> feature_scaling
    
    one_hot_encoding >> encoded_features
    label_encoding >> encoded_features
    feature_validation >> encoded_features
    feature_scaling >> encoded_features
    
    encoded_features >> feature_mapping
    encoded_features >> preprocessing_metadata
    
    encoded_features >> feature_consistency
    feature_consistency >> data_validation
    data_validation >> pipeline_testing