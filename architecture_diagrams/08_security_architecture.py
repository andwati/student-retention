"""
Security and Authentication Architecture Diagram
Shows the comprehensive security model and authentication flow
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.client import Users
from diagrams.onprem.security import Oauth
from diagrams.onprem.inmemory import Redis
from diagrams.programming.language import Python
from diagrams.generic.compute import Rack
from diagrams.generic.storage import Storage
from diagrams.onprem.network import Nginx
from diagrams.generic.database import SQL

with Diagram("Security and Authentication Architecture", 
             filename="diagrams/08_security_architecture", 
             show=False,
             direction="TB"):
    
    # External Users
    users = Users("External Users\n• Students\n• Educators\n• Administrators")
    
    # Security Perimeter
    with Cluster("Security Perimeter"):
        https_gateway = Nginx("HTTPS Gateway\n• SSL/TLS encryption\n• Certificate management\n• Secure headers")
        rate_limiting = Rack("Rate Limiting\n• Request throttling\n• DDoS protection\n• Abuse prevention")
    
    # Authentication Layer
    with Cluster("Authentication System"):
        login_handler = Oauth("Login Handler\n• Credential validation\n• Multi-factor support\n• Brute force protection")
        
        password_security = Python("Password Security\n• Hashing (bcrypt/scrypt)\n• Salt generation\n• Strength validation")
        
        session_store = Redis("Session Store\n• Secure session tokens\n• Expiration management\n• Cross-site protection")
    
    # Authorization Layer
    with Cluster("Authorization System"):
        role_manager = Python("Role Manager\n• Role definitions\n• Permission mapping\n• Access control")
        
        permission_engine = Rack("Permission Engine\n• Route protection\n• Resource access\n• Action authorization")
        
        with Cluster("User Roles & Permissions"):
            admin_permissions = Storage("Admin Permissions\n• Full system access\n• User management\n• Model updates\n• System configuration")
            
            educator_permissions = Storage("Educator Permissions\n• Student analytics\n• Batch predictions\n• Reporting tools\n• Limited admin")
            
            user_permissions = Storage("User Permissions\n• Personal predictions\n• Profile management\n• Basic analytics\n• Read-only access")
    
    # Security Middleware
    with Cluster("Security Middleware"):
        auth_decorator = Python("Auth Decorator\n• @require_auth\n• Route protection\n• Session validation")
        
        input_sanitization = Rack("Input Sanitization\n• XSS prevention\n• SQL injection protection\n• Data validation")
        
        csrf_protection = Rack("CSRF Protection\n• Token validation\n• State verification\n• Request authentication")
    
    # Application Security
    with Cluster("Application Security"):
        secure_storage = Storage("Secure Storage\n• Encrypted data\n• Access logs\n• Audit trails")
        
        error_handling = Rack("Error Handling\n• Secure error messages\n• Log sanitization\n• Information disclosure prevention")
        
        monitoring = SQL("Security Monitoring\n• Failed login attempts\n• Suspicious activity\n• Access pattern analysis")
    
    # Data Protection
    with Cluster("Data Protection"):
        data_encryption = Storage("Data Encryption\n• At-rest encryption\n• In-transit encryption\n• Key management")
        
        privacy_controls = Rack("Privacy Controls\n• Data anonymization\n• PII protection\n• Consent management")
        
        backup_security = Storage("Backup Security\n• Encrypted backups\n• Access controls\n• Recovery procedures")
    
    # Security Flow
    users >> https_gateway >> rate_limiting >> login_handler
    login_handler >> password_security >> session_store
    
    session_store >> role_manager >> permission_engine
    
    role_manager >> admin_permissions
    role_manager >> educator_permissions
    role_manager >> user_permissions
    
    permission_engine >> auth_decorator >> input_sanitization
    input_sanitization >> csrf_protection
    
    auth_decorator >> secure_storage
    csrf_protection >> error_handling
    error_handling >> monitoring
    
    secure_storage >> data_encryption
    data_encryption >> privacy_controls
    privacy_controls >> backup_security