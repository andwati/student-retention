#!/usr/bin/env python3
"""
Student Retention Predictor - Architecture Diagram Generator

This script creates a beautiful system architecture diagram using the diagrams library.
The diagram illustrates the complete flow from user interaction to prediction results.
"""

from diagrams import Diagram
from diagrams.generic.blank import Blank
from diagrams.onprem.client import User
from diagrams.onprem.compute import Server
from diagrams.onprem.database import Postgresql
from diagrams.programming.framework import Fastapi
from diagrams.programming.language import Python
from diagrams.aws.ml import SagemakerModel
from diagrams.onprem.analytics import Spark
from diagrams.generic.storage import Storage
from diagrams.generic.device import Mobile
from diagrams.onprem.security import Vault
from diagrams.programming.flowchart import Decision

# Set diagram attributes for better appearance
graph_attr = {
    "fontsize": "45",
    "bgcolor": "transparent",
    "dpi": "300",
    "margin": "0.5",
    "rankdir": "TB",
}

node_attr = {
    "fontsize": "14",
    "fontcolor": "#2d3748",
    "style": "rounded,filled",
    "fillcolor": "#f7fafc",
    "color": "#4a5568",
}

edge_attr = {"fontsize": "12", "fontcolor": "#4a5568", "color": "#4a5568"}

with Diagram(
    "Student Retention Predictor Architecture",
    filename="student_retention_architecture",
    show=False,
    direction="TB",
    graph_attr=graph_attr,
    node_attr=node_attr,
    edge_attr=edge_attr,
):
    # User Layer
    with Diagram(
        "Users", show=False, graph_attr={"label": "User Layer", "style": "dotted"}
    ):
        admin = User("Admin")
        educator = User("Educator")
        student = User("Student/User")

    # Frontend Layer
    with Diagram(
        "Frontend",
        show=False,
        graph_attr={"label": "Presentation Layer", "style": "dotted"},
    ):
        streamlit_app = Server("Streamlit Web App\n(app.py)")
        ui_components = Mobile("UI Components\n(form_components.py)")
        theme = Blank("Rose Pine Theme\n(theme.py)")

    # Authentication & Security
    auth_layer = Vault("Authentication\n& Session Management\n(auth.py)")

    # Business Logic Layer
    with Diagram(
        "Business Logic",
        show=False,
        graph_attr={"label": "Business Logic Layer", "style": "dotted"},
    ):
        validation = Decision("Input Validation\n& Recommendations")
        presets = Storage("Preset Configurations\n(mappings.py)")
        data_mappings = Storage("Data Dictionary\nMappings")

    # ML Layer
    with Diagram(
        "ML Pipeline",
        show=False,
        graph_attr={"label": "Machine Learning Layer", "style": "dotted"},
    ):
        ml_model = SagemakerModel("Random Forest\nModel (36 features)")
        preprocessing = Spark("Data Preprocessing\n& One-hot Encoding")
        model_utils = Python("Model Utils\n(models_utils.py)")

    # Data Layer
    with Diagram(
        "Data", show=False, graph_attr={"label": "Data Layer", "style": "dotted"}
    ):
        dataset = Postgresql("Student Dataset\n(data.csv)")
        data_dict = Storage("Data Dictionary\n(Excel)")
        model_files = Storage("Serialized Models\n(.pkl files)")

    # Training Pipeline
    training = Fastapi("Model Training\n(train_and_save_model.py)")

    # Define connections with labels
    [admin, educator, student] >> streamlit_app

    streamlit_app >> auth_layer
    auth_layer >> ui_components
    ui_components >> [presets, data_mappings]

    streamlit_app >> validation
    validation >> preprocessing
    preprocessing >> ml_model

    ml_model >> model_utils
    model_utils >> streamlit_app

    # Data flow
    dataset >> training
    data_dict >> data_mappings
    training >> model_files
    model_files >> ml_model

    # Theme styling
    streamlit_app - theme

print("🎨 Architecture diagram generated successfully!")
print("📁 Check 'student_retention_architecture.png' in the diagrams folder")
print("🔍 The diagram shows the complete system architecture with:")
print("   • User roles and authentication flow")
print("   • Streamlit frontend with modular components")
print("   • ML pipeline with Random Forest model")
print("   • Data layer with preprocessing and mappings")
print("   • Training pipeline and model serialization")
