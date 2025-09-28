# Student Retention Predictor - AI Developer Guide

## Architecture Overview

This is a **Streamlit-based ML application** that predicts student academic outcomes (Graduate/Dropout/Enrolled) using a Random Forest model trained on 36 features. The app uses role-based authentication and a clean modular architecture.

### Core Components
- **`app.py`**: Main Streamlit application with auth decorators and component orchestration
- **`src/components/`**: UI components split into form and prediction modules
- **`src/config/`**: Theme, mappings, and configuration constants
- **`src/utils/`**: Authentication, model utilities, and business logic
- **`models/`**: ML model training and serialized model files
- **`data/`**: CSV dataset and preprocessing pipeline

## Development Patterns

### Authentication System
Uses **decorator-based auth** with role hierarchy (admin > educator > user):
```python
@require_auth
def main():
    # Auth required for entire app
    
# Role-based features
if check_role_permission("educator"):
    render_export_section()
```

User credentials stored in `users.json` with SHA-256 hashing. Default admin: `admin`/`admin123`.

### Component Architecture
Components follow **separation of concerns**:
- `form_components.py`: All input forms and sidebar widgets
- `prediction_components.py`: Results display and model interaction
- All components accept preprocessed data and return structured dictionaries

### Configuration Pattern
**Centralized config** in `src/config/`:
- `mappings.py`: Feature mappings, presets, validation rules
- `theme.py`: Rose Pine color scheme with CSS-in-Python
- Use `create_feature_mappings()` for all dropdowns/selects

### Model Integration
**Cached model loading** with preprocessing pipeline:
```python
@st.cache_data
def load_model_and_info():
    # Returns model, preprocessing_info, feature_names
```

Features undergo **one-hot encoding** to match training format. Missing columns auto-filled with zeros.

## Development Workflows

### Running the Application
```bash
streamlit run app.py
```

### Model Training
```bash
cd models
python train_and_save_model.py
```
Generates: `random_forest_model.pkl`, `preprocessing_info.pkl`, `feature_names.pkl`

### Data Pipeline
1. CSV data in `data/data.csv` 
2. Notebook analysis in `notebook/predictive_analysis.ipynb`
3. Model training script recreates notebook preprocessing
4. Streamlit app loads serialized models

## Project-Specific Conventions

### Form State Management
Use **preset configurations** from `mappings.py`:
- `PRESET_CONFIGURATIONS`: Default values for different student types
- `ACADEMIC_DEFAULTS`: Semester performance presets
- All forms accept `preset` parameter for consistent state

### Validation & Recommendations
- `validate_input()`: Business rule validation (age limits, unit consistency)
- `generate_recommendations()`: Personalized advice based on prediction + input
- Validation messages use emoji prefixes: ⚠️ 🚫 ✅

### Styling System
**Rose Pine theme** with CSS variables defined in `theme.py`. Prediction boxes use gradient styling with hover effects. All UI follows dark theme with custom CSS injected via `st.markdown()`.

### Error Handling
- Model files missing → `st.error()` + `st.stop()`
- Authentication failure → login form re-render
- Invalid input → warning boxes with specific guidance

## Key Files for Modifications

- **Feature changes**: Update `mappings.py` constants and `train_and_save_model.py`
- **UI/UX changes**: Modify components in `src/components/`
- **Authentication**: Extend `src/utils/auth.py` role system
- **Model updates**: Retrain via `models/train_and_save_model.py`
- **Styling**: Adjust `theme.py` CSS variables

## Data Flow
1. User input collected via sidebar forms
2. Input validated and preprocessed to match training features
3. Model prediction with confidence scores
4. Results displayed with personalized recommendations
5. Role-based export functionality for educators/admins