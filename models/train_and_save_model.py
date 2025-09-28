"""
Model Training and Pickle Export Script
This script recreates the Random Forest model training process and saves the model and preprocessing pipeline.
"""

import pickle

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


def load_and_preprocess_data():
    """Load and preprocess the data exactly as done in the notebook"""
    # Load data
    data_file_name_path = "../../../data/data.csv"
    master_raw_data = pd.read_csv(data_file_name_path)
    data = master_raw_data.copy()

    # Fix column name typo
    data.rename(columns={'Nacionality': 'Nationality'}, inplace=True)

    # Remove apostrophes from column names
    for column_name in data.columns:
        if "'" in column_name:
            new_column_name = column_name.replace("'", "")
            data.rename(columns={column_name: new_column_name}, inplace=True)

    return data


def encode_target_variable(data):
    """Encode the target variable as done in the notebook"""
    # Label mapping from the notebook analysis
    target_mapping = {'Dropout': 0, 'Enrolled': 1, 'Graduate': 2}
    data['Target_encoded'] = data['Target'].map(target_mapping)
    return data


def prepare_features_for_modeling(data):
    """Prepare features exactly as done in the notebook"""
    # Get all categorical columns that need one-hot encoding
    categorical_columns = [
        'Marital status', 'Application mode', 'Course', 'Daytime/evening attendance',
        'Previous qualification', 'Nationality', 'Mothers qualification',
        'Fathers qualification', 'Mothers occupation', 'Fathers occupation',
        'Gender', 'Displaced', 'Educational special needs', 'Debtor',
        'Tuition fees up to date', 'Scholarship holder', 'International'
    ]

    # Additional columns that might be categorical (from notebook analysis)
    for col in data.columns:
        if col not in categorical_columns and col not in ['Target', 'Target_encoded']:
            unique_vals = data[col].nunique()
            # If low unique values, likely categorical
            if unique_vals <= 20 and col not in ['Age at enrollment']:
                categorical_columns.append(col)

    # Create a copy for processing
    processed_data = data.copy()

    # Perform one-hot encoding for categorical columns
    for column in categorical_columns:
        if column in processed_data.columns:
            # Get dummies with prefix
            dummies = pd.get_dummies(processed_data[column], prefix=column)
            # Concatenate with original data
            processed_data = pd.concat([processed_data, dummies], axis=1)
            # Drop original column
            processed_data.drop(columns=[column], inplace=True)

    # Drop the original Target column, keep Target_encoded
    processed_data.drop(columns=['Target'], inplace=True)

    return processed_data


def train_and_save_model():
    """Train the Random Forest model and save both model and preprocessing info"""

    # Load and preprocess data
    print("Loading and preprocessing data...")
    data = load_and_preprocess_data()

    # Encode target variable
    data = encode_target_variable(data)

    # Prepare features
    processed_data = prepare_features_for_modeling(data)

    # Separate features and target
    X = processed_data.drop('Target_encoded', axis=1)
    y = processed_data['Target_encoded']

    print(f"Final dataset shape: {X.shape}")
    print(f"Features: {X.columns.tolist()}")

    # Split data (using 30% test size as in the notebook)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

    # Train Random Forest model
    print("Training Random Forest model...")
    rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_classifier.fit(X_train, y_train)

    # Evaluate model
    train_accuracy = rf_classifier.score(X_train, y_train)
    test_accuracy = rf_classifier.score(X_test, y_test)

    print(f"Training Accuracy: {train_accuracy:.4f}")
    print(f"Test Accuracy: {test_accuracy:.4f}")

    # Save the trained model
    with open('random_forest_model.pkl', 'wb') as f:
        pickle.dump(rf_classifier, f)

    # Save feature names for consistency
    feature_names = X.columns.tolist()
    with open('feature_names.pkl', 'wb') as f:
        pickle.dump(feature_names, f)

    # Save preprocessing information
    preprocessing_info = {
        'target_mapping': {'Dropout': 0, 'Enrolled': 1, 'Graduate': 2},
        'target_reverse_mapping': {0: 'Dropout', 1: 'Enrolled', 2: 'Graduate'},
        'categorical_columns': [
            'Marital status', 'Application mode', 'Course', 'Daytime/evening attendance',
            'Previous qualification', 'Nationality', 'Mothers qualification',
            'Fathers qualification', 'Mothers occupation', 'Fathers occupation',
            'Gender', 'Displaced', 'Educational special needs', 'Debtor',
            'Tuition fees up to date', 'Scholarship holder', 'International',
            'Application order'  # Adding this based on notebook analysis
        ],
        'feature_names': feature_names,
        'original_columns': [
            'Marital status', 'Application mode', 'Application order', 'Course',
            'Daytime/evening attendance', 'Previous qualification',
            'Previous qualification (grade)', 'Nationality', 'Mothers qualification',
            'Fathers qualification', 'Mothers occupation', 'Fathers occupation',
            'Admission grade', 'Displaced', 'Educational special needs', 'Debtor',
            'Tuition fees up to date', 'Gender', 'Scholarship holder',
            'Age at enrollment', 'International', 'Curricular units 1st sem (credited)',
            'Curricular units 1st sem (enrolled)', 'Curricular units 1st sem (evaluations)',
            'Curricular units 1st sem (approved)', 'Curricular units 1st sem (grade)',
            'Curricular units 1st sem (without evaluations)',
            'Curricular units 2nd sem (credited)', 'Curricular units 2nd sem (enrolled)',
            'Curricular units 2nd sem (evaluations)', 'Curricular units 2nd sem (approved)',
            'Curricular units 2nd sem (grade)', 'Curricular units 2nd sem (without evaluations)',
            'Unemployment rate', 'Inflation rate', 'GDP'
        ]
    }

    with open('preprocessing_info.pkl', 'wb') as f:
        pickle.dump(preprocessing_info, f)

    print("Model and preprocessing info saved successfully!")
    print("Files created:")
    print("- random_forest_model.pkl")
    print("- feature_names.pkl")
    print("- preprocessing_info.pkl")

    return rf_classifier, preprocessing_info


if __name__ == "__main__":
    train_and_save_model()