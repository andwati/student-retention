"""
System Overview Diagram
High-level view of the entire Student Success Prediction system
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.client import Users
from diagrams.generic.storage import Storage
from diagrams.programming.language import Python  
from diagrams.programming.framework import Django
from diagrams.onprem.analytics import Tableau
from diagrams.onprem.inmemory import Redis
from diagrams.aws.ml import SagemakerModel
from diagrams.generic.compute import Rack
from diagrams.onprem.monitoring import Grafana
from diagrams.onprem.network import Nginx

with Diagram("Student Success Prediction - System Overview", 
             filename="diagrams/00_system_overview", 
             show=False,
             direction="TB"):
    
    # System Title and Context
    title = Storage("Student Success Prediction System\n• 93.84% Accuracy Random Forest Model\n• 36 Features, 3 Outcomes\n• 4,424 Student Dataset")
    
    # Phase 1: Data Analysis & Model Development
    with Cluster("Phase 1: Data Analysis & Model Development"):
        raw_data = Storage("Raw Dataset\ndata.csv")
        eda_process = Tableau("Exploratory Data Analysis\n• Data quality assessment\n• Statistical analysis\n• Feature insights")
        ml_pipeline = Python("ML Pipeline\n• Feature engineering\n• Model training\n• Performance validation")
        model_artifacts = SagemakerModel("Model Artifacts\n• Random Forest (93.84%)\n• Preprocessing info\n• Feature mappings")
    
    # Phase 2: Application Development
    with Cluster("Phase 2: Application Development"):
        modular_architecture = Rack("Modular Architecture\n• Component separation\n• Configuration management\n• Utility services")
        
        auth_system = Redis("Authentication System\n• Role-based access\n• Session management\n• Security controls")
        
        ui_components = Django("UI Components\n• Rose Pine theme\n• Interactive forms\n• Responsive design")
        
        streamlit_app = Django("Streamlit Application\n• Main dashboard\n• User interface\n• API integration")
    
    # Phase 3: Production Deployment
    with Cluster("Phase 3: Production Deployment"):
        deployment_options = Rack("Deployment Options\n• Streamlit Cloud\n• Docker containers\n• Traditional servers")
        
        monitoring = Grafana("Monitoring & Analytics\n• Performance metrics\n• User analytics\n• System health")
        
        security = Redis("Security & Compliance\n• Data protection\n• Access control\n• Audit logging")
    
    # End Users and Outcomes
    with Cluster("Stakeholders & Users"):
        students = Users("Students\n• Academic planning\n• Risk assessment\n• Personal insights")
        educators = Users("Educators\n• Student analytics\n• Intervention planning\n• Performance tracking")
        administrators = Users("Administrators\n• System management\n• User oversight\n• Strategic planning")
    
    # Global Internet Access
    internet = Nginx("Global Access\nSecure HTTPS")
    
    # System Flow
    title >> raw_data >> eda_process >> ml_pipeline >> model_artifacts
    
    model_artifacts >> modular_architecture
    modular_architecture >> auth_system
    modular_architecture >> ui_components
    auth_system >> streamlit_app
    ui_components >> streamlit_app
    
    streamlit_app >> deployment_options
    deployment_options >> monitoring
    deployment_options >> security
    
    internet >> streamlit_app
    streamlit_app >> students
    streamlit_app >> educators
    streamlit_app >> administrators
    
    # Key Metrics and Features
    with Cluster("Key System Metrics"):
        accuracy_metric = Storage("Model Performance\n• 93.84% Test Accuracy\n• Balanced class performance\n• Robust generalization")
        
        feature_count = Storage("Feature Engineering\n• 36 input features\n• 105+ encoded features\n• Comprehensive preprocessing")
        
        user_experience = Storage("User Experience\n• 3 user roles\n• Intuitive interface\n• Real-time predictions")
        
        scalability = Storage("Scalability\n• Cloud deployment\n• Modular architecture\n• Production-ready")
    
    # Connect metrics to main system
    streamlit_app >> accuracy_metric
    ml_pipeline >> feature_count
    ui_components >> user_experience
    deployment_options >> scalability