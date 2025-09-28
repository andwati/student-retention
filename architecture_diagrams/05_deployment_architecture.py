"""
Deployment Architecture Diagram
Shows the deployment options and infrastructure for the application
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.client import Users
from diagrams.saas.cdn import Cloudflare
from diagrams.programming.framework import Django
from diagrams.onprem.container import Docker
from diagrams.k8s.compute import Pod
from diagrams.generic.storage import Storage
from diagrams.generic.network import Internet
from diagrams.aws.compute import EC2
from diagrams.gcp.compute import GKE

with Diagram("Deployment Architecture Options", 
             filename="diagrams/05_deployment_architecture", 
             show=False,
             direction="TB"):
    
    # Users
    users = Users("Global Users")
    internet = Internet("Internet")
    
    # Deployment Option 1: Streamlit Cloud
    with Cluster("Option 1: Streamlit Cloud (Recommended)"):
        streamlit_cloud = Django("Streamlit Cloud\n• Automatic deployment\n• GitHub integration\n• SSL/HTTPS\n• Global CDN")
        github_repo = Storage("GitHub Repository\n• Source code\n• Model artifacts\n• Configuration")
        
        # Cloud features
        cloud_features = [
            Storage("Automatic Scaling"),
            Storage("Monitoring & Logs"),
            Storage("Custom Domain Support")
        ]
    
    # Deployment Option 2: Docker Container
    with Cluster("Option 2: Docker Deployment"):
        docker_container = Docker("Docker Container\n• Streamlit app\n• Python runtime\n• Dependencies")
        container_registry = Storage("Container Registry\n• Docker Hub\n• AWS ECR\n• GCR")
        
        # Container orchestration options
        with Cluster("Orchestration Options"):
            kubernetes = Pod("Kubernetes\n• Pod management\n• Auto-scaling\n• Load balancing")
            cloud_run = GKE("Cloud Run/Fargate\n• Serverless containers\n• Pay-per-use\n• Auto-scaling")
    
    # Deployment Option 3: Traditional Server
    with Cluster("Option 3: Traditional Server"):
        web_server = EC2("Web Server\n• EC2/Compute Engine\n• Nginx reverse proxy\n• SSL certificate")
        app_server = Django("Application Server\n• Streamlit process\n• PM2/Supervisor\n• Process management")
    
    # Shared Resources
    with Cluster("Shared Resources"):
        model_storage = Storage("Model Storage\n• Trained models\n• Preprocessing info\n• Version control")
        monitoring = Storage("Monitoring\n• Application logs\n• Performance metrics\n• Error tracking")
        backup = Storage("Backup & Recovery\n• Model versioning\n• Configuration backup\n• Disaster recovery")
    
    # Data Flow
    users >> internet
    
    # Streamlit Cloud flow
    internet >> streamlit_cloud
    github_repo >> streamlit_cloud
    streamlit_cloud >> cloud_features[0]
    streamlit_cloud >> cloud_features[1]
    streamlit_cloud >> cloud_features[2]
    
    # Docker flow
    internet >> docker_container
    container_registry >> docker_container
    docker_container >> kubernetes
    docker_container >> cloud_run
    
    # Traditional server flow
    internet >> web_server >> app_server
    
    # Shared resources connections
    streamlit_cloud >> model_storage
    docker_container >> model_storage
    app_server >> model_storage
    
    streamlit_cloud >> monitoring
    kubernetes >> monitoring
    app_server >> monitoring
    
    model_storage >> backup