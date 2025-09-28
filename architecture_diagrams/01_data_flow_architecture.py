"""
Data Flow Architecture Diagram
Shows the complete data pipeline from raw data to model predictions
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.inmemory import Redis
from diagrams.programming.language import Python
from diagrams.onprem.analytics import Tableau
from diagrams.onprem.client import Users
from diagrams.onprem.workflow import Airflow
from diagrams.generic.storage import Storage
from diagrams.generic.compute import Rack
from diagrams.aws.ml import SagemakerModel
from diagrams.programming.framework import Django
from diagrams.onprem.monitoring import Grafana

with Diagram("Student Success Prediction - Data Flow Architecture", 
             filename="diagrams/01_data_flow_architecture", 
             show=False,
             direction="TB"):
    
    # Data Sources
    with Cluster("Data Sources"):
        raw_data = Storage("Raw Dataset\n(data.csv)\n4,424 students\n37 features")
    
    # Data Processing Pipeline
    with Cluster("Data Processing Pipeline"):
        eda_notebook = Python("Exploratory Data Analysis\n(predictive_analysis.ipynb)")
        data_cleaning = Rack("Data Cleaning\n• Remove apostrophes\n• Fix typos\n• Handle duplicates")
        feature_eng = Rack("Feature Engineering\n• One-hot encoding\n• Label encoding\n• Scaling")
        
    # Model Development
    with Cluster("Model Development"):
        model_training = Python("Model Training\n(train_and_save_model.py)")
        model_validation = Grafana("Model Validation\n• Cross-validation\n• Performance metrics")
        model_storage = Storage("Model Artifacts\n• random_forest_model.pkl\n• preprocessing_info.json")
    
    # Production System
    with Cluster("Production Dashboard"):
        auth_system = Redis("Authentication\n• Session management\n• Role-based access")
        streamlit_app = Django("Streamlit App\n(app.py)")
        
        with Cluster("Modular Components"):
            theme_config = Python("Theme Config\n• Rose Pine CSS\n• UI constants")
            form_components = Python("Form Components\n• Input validation\n• User interface")
            model_utils = Python("Model Utils\n• Preprocessing\n• Inference")
    
    # End Users
    users = Users("End Users\n• Students\n• Educators\n• Administrators")
    
    # Data Flow
    raw_data >> eda_notebook >> data_cleaning >> feature_eng
    feature_eng >> model_training >> model_validation >> model_storage
    
    model_storage >> model_utils
    auth_system >> streamlit_app
    theme_config >> streamlit_app
    form_components >> streamlit_app
    model_utils >> streamlit_app
    
    streamlit_app >> users