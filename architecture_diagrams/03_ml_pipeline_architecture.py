"""
Machine Learning Pipeline Architecture
Shows the complete ML workflow from preprocessing to model deployment
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.generic.storage import Storage
from diagrams.generic.compute import Rack
from diagrams.programming.language import Python
from diagrams.aws.ml import SagemakerModel
from diagrams.onprem.monitoring import Grafana
from diagrams.generic.database import SQL

with Diagram("Machine Learning Pipeline Architecture", 
             filename="diagrams/03_ml_pipeline_architecture", 
             show=False,
             direction="TB"):
    
    # Input Data
    clean_data = Storage("Cleaned Dataset\n• 4,424 samples\n• 36 features\n• 3 target classes")
    
    # Preprocessing Pipeline
    with Cluster("Data Preprocessing"):
        feature_encoding = Rack("Feature Encoding\n• Label encoding (target)\n• One-hot encoding (categorical)")
        data_splitting = Rack("Data Splitting\n• Train: 75%\n• Test: 25%\n• Stratified split")
        feature_alignment = Rack("Feature Alignment\n• Consistent column order\n• Missing feature handling")
    
    # Model Training
    with Cluster("Model Training & Validation"):
        model_training = Python("Random Forest Training\n• n_estimators=100\n• random_state=42")
        cross_validation = Grafana("Cross Validation\n• 5-fold CV\n• Performance metrics")
        hyperparameter_tuning = Grafana("Hyperparameter Tuning\n• Grid search\n• Best parameters")
    
    # Model Evaluation
    with Cluster("Model Evaluation"):
        performance_metrics = Grafana("Performance Metrics\n• Accuracy: 93.84%\n• Precision/Recall\n• F1-Score")
        confusion_matrix = Grafana("Confusion Matrix\n• Class-wise performance\n• Error analysis")
        feature_importance = Grafana("Feature Importance\n• Top predictors\n• Impact analysis")
    
    # Model Persistence
    with Cluster("Model Artifacts"):
        model_pickle = Storage("Model Pickle\nrandom_forest_model.pkl")
        preprocessing_info = SQL("Preprocessing Info\npreprocessing_info.json\n• Feature names\n• Encodings\n• Mappings")
    
    # Model Validation Results
    with Cluster("Validation Results"):
        accuracy_report = Rack("Accuracy Report\n• Training: 100%\n• Testing: 93.84%\n• Generalization: Good")
        class_performance = Rack("Class Performance\n• Graduate: 95% F1\n• Dropout: 92% F1\n• Enrolled: 88% F1")
    
    # Data Flow
    clean_data >> feature_encoding >> data_splitting
    data_splitting >> model_training >> cross_validation
    cross_validation >> hyperparameter_tuning >> performance_metrics
    
    performance_metrics >> confusion_matrix
    performance_metrics >> feature_importance
    
    model_training >> model_pickle
    feature_encoding >> preprocessing_info
    feature_alignment >> preprocessing_info
    
    performance_metrics >> accuracy_report
    confusion_matrix >> class_performance