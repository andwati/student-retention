"""
Form input components for the Student Success Predictor
"""

import streamlit as st
from typing import Dict, Any, Tuple
from ..config.mappings import create_feature_mappings, PRESET_CONFIGURATIONS, ACADEMIC_DEFAULTS


def render_preset_selector() -> str:
    """Render the preset selector section"""
    st.markdown('<div class="sidebar-section">', unsafe_allow_html=True)
    st.markdown("### 🚀 Quick Start")
    preset = st.selectbox(
        "Load Sample Data",
        ["Custom Entry", "Typical Graduate Student", "At-Risk Student", "International Student"],
        help="Choose a preset to quickly fill common scenarios"
    )
    st.markdown('</div>', unsafe_allow_html=True)

    if preset != "Custom Entry":
        st.markdown(
            f'<div class="success-box">✅ Loading <strong>{preset}</strong> preset values. You can modify any field below.</div>',
            unsafe_allow_html=True)

    return preset


def render_personal_info_section(preset: str, feature_maps: Dict) -> Dict[str, Any]:
    """Render personal information input section"""
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    st.markdown("### 👤 Personal Information")
    st.markdown('<div class="info-box">Basic demographic information about the student</div>', unsafe_allow_html=True)

    defaults = PRESET_CONFIGURATIONS[preset]

    marital_status = st.selectbox(
        "Marital Status",
        options=list(feature_maps['marital_status'].keys()),
        format_func=lambda x: feature_maps['marital_status'][x],
        index=list(feature_maps['marital_status'].keys()).index(defaults["marital"])
    )

    gender = st.selectbox(
        "Gender",
        [0, 1],
        format_func=lambda x: "Female" if x == 0 else "Male",
        index=defaults["gender"]
    )

    age_at_enrollment = st.number_input(
        "Age at Enrollment",
        min_value=17,
        max_value=70,
        value=defaults["age"],
        step=1
    )

    nationality = st.selectbox(
        "Nationality",
        options=list(feature_maps['nationality'].keys()),
        format_func=lambda x: feature_maps['nationality'][x],
        index=0
    )

    return {
        'Marital status': marital_status,
        'Gender': gender,
        'Age at enrollment': age_at_enrollment,
        'Nationality': nationality
    }


def render_academic_background_section(preset: str, feature_maps: Dict) -> Dict[str, Any]:
    """Render academic background input section"""
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    st.markdown("### 🎓 Academic Background")
    st.markdown('<div class="info-box">Information about the student\'s application and academic history</div>',
                unsafe_allow_html=True)

    defaults = PRESET_CONFIGURATIONS[preset]

    application_mode = st.selectbox(
        "Application Mode",
        options=list(feature_maps['application_mode'].keys()),
        format_func=lambda x: feature_maps['application_mode'].get(x, f"Mode {x}"),
        index=list(feature_maps['application_mode'].keys()).index(defaults["app_mode"]) if defaults["app_mode"] in
                                                                                           feature_maps[
                                                                                               'application_mode'] else 0
    )

    application_order = st.selectbox(
        "Application Order (1st choice, 2nd choice, etc.)",
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        index=0
    )

    course = st.selectbox(
        "Course",
        options=list(feature_maps['course'].keys()),
        format_func=lambda x: feature_maps['course'].get(x, f"Course {x}"),
        index=list(feature_maps['course'].keys()).index(defaults["course"]) if defaults["course"] in feature_maps[
            'course'] else 0
    )

    daytime_evening = st.selectbox(
        "Attendance",
        [0, 1],
        format_func=lambda x: "Evening" if x == 0 else "Daytime"
    )

    previous_qualification = st.selectbox(
        "Previous Qualification",
        options=list(feature_maps['qualification'].keys()),
        format_func=lambda x: feature_maps['qualification'].get(x, f"Qualification {x}")
    )

    col1, col2 = st.columns(2)
    with col1:
        previous_qualification_grade = st.number_input(
            "Previous Qualification Grade",
            min_value=95,
            max_value=190,
            value=defaults["prev_grade"],
            step=1
        )
    with col2:
        admission_grade = st.number_input(
            "Admission Grade",
            min_value=95,
            max_value=190,
            value=defaults["adm_grade"],
            step=1
        )

    return {
        'Application mode': application_mode,
        'Application order': application_order,
        'Course': course,
        'Daytime/evening attendance': daytime_evening,
        'Previous qualification': previous_qualification,
        'Previous qualification (grade)': previous_qualification_grade,
        'Admission grade': admission_grade
    }


def render_family_background_section(preset: str, feature_maps: Dict) -> Dict[str, Any]:
    """Render family background input section"""
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    st.markdown("### 👨‍👩‍👧‍👦 Family Background")
    st.markdown('<div class="info-box">Parent education and occupation information</div>', unsafe_allow_html=True)

    defaults = PRESET_CONFIGURATIONS[preset]

    mothers_qualification = st.selectbox(
        "Mother's Qualification",
        options=list(feature_maps['qualification'].keys()),
        format_func=lambda x: feature_maps['qualification'].get(x, f"Qualification {x}"),
        index=list(feature_maps['qualification'].keys()).index(defaults["mothers_qualification"]) if defaults["mothers_qualification"] in feature_maps['qualification'] else 0
    )

    fathers_qualification = st.selectbox(
        "Father's Qualification",
        options=list(feature_maps['qualification'].keys()),
        format_func=lambda x: feature_maps['qualification'].get(x, f"Qualification {x}"),
        index=list(feature_maps['qualification'].keys()).index(defaults["fathers_qualification"]) if defaults["fathers_qualification"] in feature_maps['qualification'] else 0
    )

    mothers_occupation = st.selectbox(
        "Mother's Occupation",
        options=list(feature_maps['occupation'].keys()),
        format_func=lambda x: feature_maps['occupation'].get(x, f"Occupation {x}"),
        index=list(feature_maps['occupation'].keys()).index(defaults["mothers_occupation"]) if defaults["mothers_occupation"] in feature_maps['occupation'] else 0
    )

    fathers_occupation = st.selectbox(
        "Father's Occupation",
        options=list(feature_maps['occupation'].keys()),
        format_func=lambda x: feature_maps['occupation'].get(x, f"Occupation {x}"),
        index=list(feature_maps['occupation'].keys()).index(defaults["fathers_occupation"]) if defaults["fathers_occupation"] in feature_maps['occupation'] else 0
    )

    return {
        'Mothers qualification': mothers_qualification,
        'Fathers qualification': fathers_qualification,
        'Mothers occupation': mothers_occupation,
        'Fathers occupation': fathers_occupation
    }


def render_financial_social_section(preset: str) -> Dict[str, Any]:
    """Render financial and social factors input section"""
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    st.markdown("### 💰 Financial & Social")
    st.markdown('<div class="info-box">Student financial status and special circumstances</div>',
                unsafe_allow_html=True)

    defaults = PRESET_CONFIGURATIONS[preset]

    col1, col2 = st.columns(2)
    with col1:
        displaced = st.radio(
            "Displaced Student",
            [0, 1],
            format_func=lambda x: "No" if x == 0 else "Yes",
            index=defaults["displaced"],
            horizontal=True
        )
        educational_special_needs = st.radio(
            "Educational Special Needs",
            [0, 1],
            format_func=lambda x: "No" if x == 0 else "Yes",
            index=defaults["educational_special_needs"],
            horizontal=True
        )
        debtor = st.radio(
            "Has Outstanding Debts",
            [0, 1],
            format_func=lambda x: "No" if x == 0 else "Yes",
            index=defaults["debtor"],
            horizontal=True
        )
    with col2:
        tuition_fees_up_to_date = st.radio(
            "Tuition Fees Up to Date",
            [0, 1],
            format_func=lambda x: "No" if x == 0 else "Yes",
            index=defaults["tuition_fees_up_to_date"],
            horizontal=True
        )
        scholarship_holder = st.radio(
            "Scholarship Holder",
            [0, 1],
            format_func=lambda x: "No" if x == 0 else "Yes",
            index=defaults["scholarship_holder"],
            horizontal=True
        )
        international = st.radio(
            "International Student",
            [0, 1],
            format_func=lambda x: "No" if x == 0 else "Yes",
            index=defaults["international"],
            horizontal=True
        )

    return {
        'Displaced': displaced,
        'Educational special needs': educational_special_needs,
        'Debtor': debtor,
        'Tuition fees up to date': tuition_fees_up_to_date,
        'Scholarship holder': scholarship_holder,
        'International': international
    }


def render_academic_performance_section(preset: str) -> Dict[str, Any]:
    """Render academic performance input sections"""
    academic_defaults = ACADEMIC_DEFAULTS[preset]

    # 1st Semester
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    st.markdown("### 📚 1st Semester Performance")
    st.markdown(
        '<div class="warning-box">⚠️ <strong>Important:</strong> Academic performance is a key predictor of student success</div>',
        unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        curricular_units_1st_sem_enrolled = st.number_input(
            "Enrolled Units", min_value=0, max_value=26,
            value=academic_defaults["1st_sem"]["enrolled"], step=1,
            key="1st_enrolled", help="Number of courses registered for"
        )
        curricular_units_1st_sem_approved = st.number_input(
            "Approved Units", min_value=0, max_value=26,
            value=academic_defaults["1st_sem"]["approved"], step=1,
            key="1st_approved", help="Number of courses passed"
        )
        curricular_units_1st_sem_credited = st.number_input(
            "Credited Units", min_value=0, max_value=26,
            value=academic_defaults["1st_sem"]["credited"], step=1,
            key="1st_credited", help="Credits from previous education"
        )
    with col2:
        curricular_units_1st_sem_evaluations = st.number_input(
            "Evaluations", min_value=0, max_value=45,
            value=academic_defaults["1st_sem"]["evaluations"], step=1,
            key="1st_evaluations", help="Number of exams taken"
        )
        curricular_units_1st_sem_grade = st.number_input(
            "Average Grade (0-20)", min_value=0, max_value=20,
            value=academic_defaults["1st_sem"]["grade"], step=1,
            key="1st_grade", help="Average grade on 0-20 scale"
        )
        curricular_units_1st_sem_without_evaluations = st.number_input(
            "Without Evaluations", min_value=0, max_value=14,
            value=academic_defaults["1st_sem"]["without"], step=1,
            key="1st_without", help="Courses registered but not evaluated"
        )

    # 2nd Semester
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    st.markdown("### 📖 2nd Semester Performance")
    st.markdown('<div class="info-box">Second semester data helps improve prediction accuracy</div>',
                unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        curricular_units_2nd_sem_enrolled = st.number_input(
            "Enrolled Units", min_value=0, max_value=23,
            value=academic_defaults["2nd_sem"]["enrolled"], step=1,
            key="2nd_enrolled", help="Number of courses registered for"
        )
        curricular_units_2nd_sem_approved = st.number_input(
            "Approved Units", min_value=0, max_value=20,
            value=academic_defaults["2nd_sem"]["approved"], step=1,
            key="2nd_approved", help="Number of courses passed"
        )
        curricular_units_2nd_sem_credited = st.number_input(
            "Credited Units", min_value=0, max_value=20,
            value=academic_defaults["2nd_sem"]["credited"], step=1,
            key="2nd_credited", help="Credits from previous education"
        )
    with col2:
        curricular_units_2nd_sem_evaluations = st.number_input(
            "Evaluations", min_value=0, max_value=33,
            value=academic_defaults["2nd_sem"]["evaluations"], step=1,
            key="2nd_evaluations", help="Number of exams taken"
        )
        curricular_units_2nd_sem_grade = st.number_input(
            "Average Grade (0-20)", min_value=0, max_value=20,
            value=academic_defaults["2nd_sem"]["grade"], step=1,
            key="2nd_grade", help="Average grade on 0-20 scale"
        )
        curricular_units_2nd_sem_without_evaluations = st.number_input(
            "Without Evaluations", min_value=0, max_value=12,
            value=academic_defaults["2nd_sem"]["without"], step=1,
            key="2nd_without", help="Courses registered but not evaluated"
        )

    return {
        'Curricular units 1st sem (credited)': curricular_units_1st_sem_credited,
        'Curricular units 1st sem (enrolled)': curricular_units_1st_sem_enrolled,
        'Curricular units 1st sem (evaluations)': curricular_units_1st_sem_evaluations,
        'Curricular units 1st sem (approved)': curricular_units_1st_sem_approved,
        'Curricular units 1st sem (grade)': curricular_units_1st_sem_grade,
        'Curricular units 1st sem (without evaluations)': curricular_units_1st_sem_without_evaluations,
        'Curricular units 2nd sem (credited)': curricular_units_2nd_sem_credited,
        'Curricular units 2nd sem (enrolled)': curricular_units_2nd_sem_enrolled,
        'Curricular units 2nd sem (evaluations)': curricular_units_2nd_sem_evaluations,
        'Curricular units 2nd sem (approved)': curricular_units_2nd_sem_approved,
        'Curricular units 2nd sem (grade)': curricular_units_2nd_sem_grade,
        'Curricular units 2nd sem (without evaluations)': curricular_units_2nd_sem_without_evaluations
    }


def render_economic_indicators_section() -> Dict[str, Any]:
    """Render economic indicators input section"""
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    st.markdown("### 📊 Economic Indicators")
    st.markdown(
        '<div class="info-box">📈 Economic context data - typically set by institution based on current conditions</div>',
        unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        unemployment_rate = st.number_input(
            "Unemployment Rate (%)",
            min_value=7.0, max_value=16.2, value=10.8, step=0.1, format="%.1f"
        )
    with col2:
        inflation_rate = st.number_input(
            "Inflation Rate (%)",
            min_value=-0.8, max_value=3.7, value=1.4, step=0.1, format="%.1f"
        )
    with col3:
        gdp = st.number_input(
            "GDP Growth",
            min_value=-4.06, max_value=3.51, value=1.74, step=0.1, format="%.2f"
        )

    return {
        'Unemployment rate': unemployment_rate,
        'Inflation rate': inflation_rate,
        'GDP': gdp
    }