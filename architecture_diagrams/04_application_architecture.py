"""
Application Architecture Diagram
Shows the modular Streamlit application structure and components
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.client import Users
from diagrams.onprem.inmemory import Redis
from diagrams.programming.framework import Django, React
from diagrams.programming.language import Python
from diagrams.generic.storage import Storage
from diagrams.generic.compute import Rack
from diagrams.onprem.network import Nginx

with Diagram("Streamlit Application Architecture", 
             filename="diagrams/04_application_architecture", 
             show=False,
             direction="TB"):
    
    # Users
    users = Users("End Users\n• Students\n• Educators\n• Administrators")
    
    # Web Interface
    streamlit_frontend = Django("Streamlit Frontend\n• Rose Pine Theme\n• Responsive UI\n• Interactive Forms")
    
    # Authentication Layer
    with Cluster("Authentication System"):
        auth_service = Redis("Authentication Service\n• Session management\n• Role-based access\n• Security validation")
        user_roles = Rack("User Roles\n• Admin (full access)\n• Educator (analytics)\n• User (predictions)")
    
    # Application Core
    with Cluster("Application Core (app.py)"):
        main_app = Python("Main Application\n• Request routing\n• Session handling\n• Error management")
        auth_decorator = Python("Auth Decorator\n• @require_auth\n• Permission checks\n• Session validation")
    
    # Configuration Layer
    with Cluster("Configuration (src/config/)"):
        theme_config = React("Theme Configuration\n• Rose Pine CSS\n• Color constants\n• UI styling")
        mappings_config = Storage("Feature Mappings\n• Human-readable labels\n• Preset templates\n• Validation rules")
    
    # Utility Services
    with Cluster("Utility Services (src/utils/)"):
        model_utils = Python("Model Utilities\n• Model loading\n• Preprocessing\n• Prediction logic")
        auth_utils = Python("Auth Utilities\n• User validation\n• Session management\n• Password hashing")
    
    # UI Components
    with Cluster("UI Components (src/components/)"):
        form_components = React("Form Components\n• Input sections\n• Validation feedback\n• Preset selection")
        prediction_display = React("Prediction Display\n• Results visualization\n• Confidence scores\n• Recommendations")
    
    # Model Layer
    with Cluster("Model Layer"):
        trained_model = Storage("Trained Model\nrandom_forest_model.pkl\n93.84% accuracy")
        preprocessing_pipeline = Storage("Preprocessing Pipeline\npreprocessing_info.json\nFeature transformations")
    
    # Data Flow
    users >> streamlit_frontend
    streamlit_frontend >> auth_service >> user_roles
    auth_service >> main_app >> auth_decorator
    
    main_app >> theme_config
    main_app >> mappings_config
    main_app >> form_components
    main_app >> prediction_display
    
    form_components >> model_utils
    model_utils >> trained_model
    model_utils >> preprocessing_pipeline
    model_utils >> prediction_display
    
    auth_decorator >> auth_utils