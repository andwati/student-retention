"""
Master Script to Generate All Architecture Diagrams
Run this script to generate all diagram images at once
"""

import os
import sys
import subprocess
from pathlib import Path

def generate_diagram(script_name):
    """Generate a single diagram by running its Python script"""
    try:
        print(f"Generating {script_name}...")
        result = subprocess.run([sys.executable, script_name], 
                              capture_output=True, text=True, cwd="diagrams")
        
        if result.returncode == 0:
            print(f"✅ Successfully generated {script_name}")
        else:
            print(f"❌ Error generating {script_name}:")
            print(result.stderr)
            
    except Exception as e:
        print(f"❌ Exception while generating {script_name}: {e}")

def main():
    """Generate all architecture diagrams"""
    
    # Check if diagrams library is installed
    try:
        import diagrams
        print("✅ Diagrams library found")
    except ImportError:
        print("❌ Diagrams library not found. Installing...")
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "diagrams/requirements.txt"])
        print("✅ Diagrams library installed")
    
    # List of diagram scripts to generate
    diagram_scripts = [
        "00_system_overview.py",
        "01_data_flow_architecture.py",
        "02_eda_process_flow.py", 
        "03_ml_pipeline_architecture.py",
        "04_application_architecture.py",
        "05_deployment_architecture.py",
        "06_feature_engineering_pipeline.py",
        "07_user_journey_flow.py",
        "08_security_architecture.py"
    ]
    
    print("🚀 Starting diagram generation...")
    print("=" * 50)
    
    # Create diagrams directory if it doesn't exist
    Path("diagrams").mkdir(exist_ok=True)
    
    # Generate each diagram
    for script in diagram_scripts:
        if os.path.exists(f"diagrams/{script}"):
            generate_diagram(script)
        else:
            print(f"⚠️  Script not found: {script}")
    
    print("=" * 50)
    print("🎉 Diagram generation complete!")
    print("\nGenerated diagrams:")
    
    # List generated PNG files
    diagrams_dir = Path("diagrams")
    png_files = list(diagrams_dir.glob("*.png"))
    
    if png_files:
        for png_file in sorted(png_files):
            print(f"  📊 {png_file.name}")
    else:
        print("  ⚠️  No PNG files found. Check for errors above.")
    
    print(f"\nTotal diagrams generated: {len(png_files)}")

if __name__ == "__main__":
    main()