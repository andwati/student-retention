
# Student Retention Predictor

A Streamlit-based ML app for predicting student academic outcomes (Graduate/Dropout/Enrolled) using a Random Forest model. Includes role-based authentication, modular UI, customizable presets, and human-readable field mappings.

---

## Usage Instructions

### 1. Launch the Application

```bash
streamlit run app.py
```

The app will open in your browser. If model files are missing, follow the Model Training steps below.

---

### 2. Authentication & Roles

- **Login Required:** Enter your username and password to access the app.
- **Default Admin:** Username: `admin`, Password: `admin123`
- **Roles:**
	- **Admin:** Full access, can manage users and export data
	- **Educator:** Can export predictions
	- **User:** Can view predictions only

---

### 3. Input Forms & Presets

- **Sidebar Forms:** Enter student details using dropdowns, sliders, and text fields.
- **Presets:** Use the preset selector to auto-fill fields for typical student profiles (e.g., "Typical Graduate Student").
	- Presets cover academic, family background, and financial/social fields.
- **Field Mappings:** All dropdowns show human-readable names (e.g., country names, not codes), powered by the integrated data dictionary.

---

### 4. Prediction Workflow

1. **Fill in Student Data:** Complete all required fields. Use presets for convenience or enter custom values.
2. **Submit:** Click the Predict button.
3. **View Results:**
	 - Prediction outcome (Graduate/Dropout/Enrolled)
	 - Confidence score
	 - Personalized recommendations based on input and prediction
4. **Validation:** If input is invalid (e.g., age out of range), warnings will be shown with guidance.

---

### 5. Export & Role-Based Features

- **Export Predictions:** Available to Educator/Admin roles. Export results for further analysis.
- **Session Management:** Sessions persist for extended periods, but re-login may be required after browser refresh or timeout.

---

### 6. Model Training (If Needed)

If model files are missing or you want to retrain:

```bash
cd models
python train_and_save_model.py
```

This generates:
- `random_forest_model.pkl`
- `preprocessing_info.pkl`
- `feature_names.pkl`

---

### 7. Customization & Advanced Usage

- **Feature Changes:** Update `src/config/mappings.py` and retrain the model.
- **Presets:** Edit `PRESET_CONFIGURATIONS` in `mappings.py` to add or modify student profiles.
- **Styling:** Adjust theme in `src/config/theme.py`.
- **Authentication:** Extend roles in `src/utils/auth.py`.

---

## Project Structure

- `app.py`: Main Streamlit app
- `src/components/`: UI components (forms, prediction display)
- `src/config/`: Mappings, theme, config
- `src/utils/`: Auth, model utils
- `models/`: ML model training, serialized files
- `data/`: CSV dataset, data dictionary
- `notebook/`: Data analysis notebook

---

## Troubleshooting

- **Model files missing:** Retrain using the steps above.
- **Authentication issues:** Check `users.json` for correct credentials.
- **Invalid input:** Review warnings and ensure all required fields are filled.

---

## License

MIT