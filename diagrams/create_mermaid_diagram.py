"""
Student Retention Predictor - Mermaid Architecture Diagram

This generates a beautiful Mermaid diagram that can be rendered as an image
using online tools or VS Code extensions.
"""

mermaid_diagram = """
graph TB
    %% Styling
    classDef userClass fill:#e8f4fd,stroke:#1e40af,stroke-width:2px,color:#1e40af
    classDef frontendClass fill:#fef3c7,stroke:#d97706,stroke-width:2px,color:#d97706  
    classDef authClass fill:#f3e8ff,stroke:#7c3aed,stroke-width:2px,color:#7c3aed
    classDef businessClass fill:#ecfdf5,stroke:#059669,stroke-width:2px,color:#059669
    classDef mlClass fill:#fee2e2,stroke:#dc2626,stroke-width:2px,color:#dc2626
    classDef dataClass fill:#f1f5f9,stroke:#475569,stroke-width:2px,color:#475569
    
    %% User Layer
    subgraph Users ["👥 User Layer"]
        Admin[👨‍💼 Admin<br/>Full Access]
        Educator[👨‍🏫 Educator<br/>Export Features]  
        Student[👨‍🎓 Student/User<br/>View Only]
    end
    
    %% Frontend Layer
    subgraph Frontend ["🎨 Presentation Layer"]
        StreamlitApp[🌐 Streamlit Web App<br/>app.py]
        UIComponents[📱 UI Components<br/>form_components.py<br/>prediction_components.py]
        Theme[🎨 Rose Pine Theme<br/>theme.py]
    end
    
    %% Authentication
    AuthLayer[🔐 Authentication<br/>& Session Management<br/>auth.py]
    
    %% Business Logic Layer  
    subgraph BusinessLogic ["⚙️ Business Logic Layer"]
        Validation[✅ Input Validation<br/>& Recommendations]
        Presets[📋 Preset Configurations<br/>mappings.py]
        DataMappings[🗂️ Data Dictionary<br/>Mappings]
    end
    
    %% ML Layer
    subgraph MLPipeline ["🤖 Machine Learning Layer"]
        MLModel[🧠 Random Forest Model<br/>36 Features]
        Preprocessing[🔄 Data Preprocessing<br/>& One-hot Encoding]
        ModelUtils[🔧 Model Utils<br/>models_utils.py]
    end
    
    %% Data Layer
    subgraph DataLayer ["💾 Data Layer"]
        Dataset[(📊 Student Dataset<br/>data.csv)]
        DataDict[(📚 Data Dictionary<br/>Excel)]
        ModelFiles[(💽 Serialized Models<br/>.pkl files)]
    end
    
    %% Training Pipeline
    Training[🏋️ Model Training<br/>train_and_save_model.py]
    
    %% Connections
    Admin --> StreamlitApp
    Educator --> StreamlitApp  
    Student --> StreamlitApp
    
    StreamlitApp --> AuthLayer
    AuthLayer --> UIComponents
    UIComponents --> Presets
    UIComponents --> DataMappings
    
    StreamlitApp --> Validation
    Validation --> Preprocessing
    Preprocessing --> MLModel
    
    MLModel --> ModelUtils
    ModelUtils --> StreamlitApp
    
    %% Data Flow
    Dataset --> Training
    DataDict --> DataMappings
    Training --> ModelFiles
    ModelFiles --> MLModel
    
    %% Styling connections
    StreamlitApp -.-> Theme
    
    %% Apply styles
    class Admin,Educator,Student userClass
    class StreamlitApp,UIComponents,Theme frontendClass
    class AuthLayer authClass
    class Validation,Presets,DataMappings businessClass
    class MLModel,Preprocessing,ModelUtils,Training mlClass
    class Dataset,DataDict,ModelFiles dataClass
"""

# Save the Mermaid diagram
with open("student_retention_architecture.mmd", "w", encoding="utf-8") as f:
    f.write(mermaid_diagram)

print("🎨 Mermaid architecture diagram created successfully!")
print("📁 File saved as: student_retention_architecture.mmd")
print()
print("🌐 To generate a beautiful image:")
print("   1. Copy the diagram content from the .mmd file")
print("   2. Paste it into https://mermaid.live/")
print("   3. Download as PNG/SVG")
print()
print("💡 Or use VS Code with Mermaid Preview extension")
print("📋 The diagram shows:")
print("   • 👥 User roles with different access levels")
print("   • 🎨 Streamlit frontend with modular components")
print("   • 🔐 Authentication and session management")
print("   • ⚙️ Business logic with validation and presets")
print("   • 🤖 ML pipeline with Random Forest model")
print("   • 💾 Data layer with preprocessing and storage")
print("   • 🏋️ Training pipeline for model updates")
