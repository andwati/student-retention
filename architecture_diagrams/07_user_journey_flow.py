"""
User Journey and Interaction Flow Diagram
Shows how different user types interact with the application
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.client import Users, User
from diagrams.programming.framework import Django
from diagrams.onprem.inmemory import Redis
from diagrams.generic.compute import Rack
from diagrams.onprem.analytics import Tableau
from diagrams.generic.storage import Storage

with Diagram("User Journey and Interaction Flow", 
             filename="diagrams/07_user_journey_flow", 
             show=False,
             direction="TB"):
    
    # User Types
    with Cluster("User Types"):
        student_user = User("Student\n• Personal predictions\n• Academic planning\n• Risk assessment")
        educator_user = User("Educator\n• Student analytics\n• Intervention planning\n• Batch predictions")
        admin_user = User("Administrator\n• System management\n• User oversight\n• Full access")
    
    # Authentication Flow
    with Cluster("Authentication Flow"):
        login_page = Django("Login Page\n• Credential input\n• Role selection\n• Security validation")
        auth_service = Redis("Authentication Service\n• Session creation\n• Role assignment\n• Access control")
        session_management = Redis("Session Management\n• Timeout handling\n• Security checks\n• State persistence")
    
    # Application Interface
    with Cluster("Application Interface"):
        main_dashboard = Django("Main Dashboard\n• Role-based UI\n• Feature access\n• Navigation menu")
        
        # Student workflow
        with Cluster("Student Workflow"):
            personal_form = Rack("Personal Information Form\n• Basic demographics\n• Academic history\n• Family background")
            academic_form = Rack("Academic Performance Form\n• Current grades\n• Curricular units\n• Progress tracking")
            prediction_results = Tableau("Prediction Results\n• Outcome probability\n• Confidence scores\n• Recommendations")
        
        # Educator workflow
        with Cluster("Educator Workflow"):
            student_management = Rack("Student Management\n• Batch input\n• Template selection\n• Data validation")
            analytics_dashboard = Tableau("Analytics Dashboard\n• Class performance\n• Risk indicators\n• Intervention alerts")
            reporting_tools = Tableau("Reporting Tools\n• Performance reports\n• Trend analysis\n• Export capabilities")
        
        # Admin workflow
        with Cluster("Admin Workflow"):
            user_management = Rack("User Management\n• Account creation\n• Role assignment\n• Access control")
            system_monitoring = Tableau("System Monitoring\n• Usage statistics\n• Performance metrics\n• Error logs")
            model_management = Storage("Model Management\n• Version control\n• Performance tracking\n• Updates")
    
    # Prediction Engine
    with Cluster("Prediction Engine"):
        input_validation = Rack("Input Validation\n• Data quality checks\n• Range validation\n• Required fields")
        feature_processing = Rack("Feature Processing\n• Encoding\n• Transformation\n• Alignment")
        model_inference = Storage("Model Inference\n• Random Forest prediction\n• Confidence calculation\n• Result formatting")
    
    # User Journey Flows
    
    # Student journey
    student_user >> login_page >> auth_service >> main_dashboard
    main_dashboard >> personal_form >> academic_form
    academic_form >> input_validation >> feature_processing >> model_inference
    model_inference >> prediction_results
    
    # Educator journey
    educator_user >> login_page >> auth_service >> main_dashboard
    main_dashboard >> student_management >> analytics_dashboard
    student_management >> input_validation >> feature_processing >> model_inference
    model_inference >> reporting_tools
    
    # Admin journey
    admin_user >> login_page >> auth_service >> main_dashboard
    main_dashboard >> user_management >> system_monitoring >> model_management
    
    # Session management connections
    auth_service >> session_management
    session_management >> main_dashboard