"""
Model loading and data preprocessing utilities
"""

import streamlit as st
import pandas as pd
import pickle
from typing import Dict, Any, List


@st.cache_data
def load_model_and_info():
    """Load the trained model and preprocessing information"""
    try:
        with open('random_forest_model.pkl', 'rb') as f:
            model = pickle.load(f)

        with open('preprocessing_info.pkl', 'rb') as f:
            preprocessing_info = pickle.load(f)

        with open('feature_names.pkl', 'rb') as f:
            feature_names = pickle.load(f)

        return model, preprocessing_info, feature_names
    except FileNotFoundError:
        st.error("❌ Model files not found! Please run 'train_and_save_model.py' first.")
        st.stop()


def preprocess_input(user_input: Dict[str, Any], preprocessing_info: Dict[str, Any]) -> pd.DataFrame:
    """Preprocess user input to match the training data format"""

    # Create a DataFrame with the user input
    input_df = pd.DataFrame([user_input])

    # Get categorical columns that need one-hot encoding
    categorical_columns = [
        'Marital status', 'Application mode', 'Course', 'Daytime/evening attendance',
        'Previous qualification', 'Nationality', 'Mothers qualification',
        'Fathers qualification', 'Mothers occupation', 'Fathers occupation',
        'Gender', 'Displaced', 'Educational special needs', 'Debtor',
        'Tuition fees up to date', 'Scholarship holder', 'International',
        'Application order'
    ]

    # Perform one-hot encoding for categorical columns
    for column in categorical_columns:
        if column in input_df.columns:
            # Get dummies with prefix
            dummies = pd.get_dummies(input_df[column], prefix=column)
            # Concatenate with original data
            input_df = pd.concat([input_df, dummies], axis=1)
            # Drop original column
            input_df.drop(columns=[column], inplace=True)

    # Ensure all training features are present
    feature_names = preprocessing_info['feature_names']

    # Add missing columns with 0 values
    for feature in feature_names:
        if feature not in input_df.columns:
            input_df[feature] = 0

    # Select only the features used in training and in the same order
    input_df = input_df[feature_names]

    return input_df


def validate_input(user_input: Dict[str, Any]) -> List[str]:
    """Validate user input and return list of issues"""
    validation_issues = []

    # Check for unrealistic combinations
    if user_input['Age at enrollment'] < 17:
        validation_issues.append("⚠️ Age seems too low for enrollment")

    if user_input['Curricular units 1st sem (approved)'] > user_input['Curricular units 1st sem (enrolled)']:
        validation_issues.append("⚠️ Approved units exceed enrolled units (1st sem)")

    if user_input['Curricular units 2nd sem (approved)'] > user_input['Curricular units 2nd sem (enrolled)']:
        validation_issues.append("⚠️ Approved units exceed enrolled units (2nd sem)")

    return validation_issues


def generate_recommendations(predicted_outcome: str, user_input: Dict[str, Any]) -> List[str]:
    """Generate personalized recommendations based on prediction and input"""
    recommendations = []

    if predicted_outcome == "Dropout":
        if user_input['Curricular units 1st sem (approved)'] == 0:
            recommendations.append("📚 **Academic Support:** Provide tutoring for struggling courses")

        if user_input['Scholarship holder'] == 0:
            recommendations.append("💰 **Financial Aid:** Consider scholarship opportunities")

        if user_input['Age at enrollment'] > 25:
            recommendations.append("🕐 **Flexible Scheduling:** Offer evening or part-time options")

        if user_input['Debtor'] == 1:
            recommendations.append("💳 **Financial Counseling:** Address outstanding debts")

    elif predicted_outcome == "Graduate":
        recommendations.append("🎯 **Success Indicators:** This student shows strong potential for graduation")
        recommendations.append("🔄 **Continue Support:** Maintain current academic support systems")

    else:  # Enrolled
        recommendations.append("📈 **Regular Monitoring:** Schedule periodic academic check-ins")
        recommendations.append("🎯 **Goal Setting:** Help establish clear academic objectives")

    return recommendations