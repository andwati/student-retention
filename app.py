"""
Main Streamlit application for Student Success Predictor
"""

import streamlit as st

from src.components.form_components import (
    render_preset_selector,
    render_personal_info_section,
    render_academic_background_section,
    render_family_background_section,
    render_financial_social_section,
    render_academic_performance_section,
    render_economic_indicators_section
)
from src.components.prediction_components import (
    render_prediction_section,
    render_model_info_sidebar,
    render_export_section,
    render_footer
)
from src.config.mappings import create_feature_mappings
from src.config.theme import ROSE_PINE_THEME, PAGE_CONFIG, APP_TITLE, APP_SUBTITLE
from src.utils.auth import require_auth, check_role_permission, render_admin_panel, check_session_timeout
from src.utils.models_utils import load_model_and_info


def apply_theme():
    """Apply the Rose Pine dark theme"""
    st.markdown(ROSE_PINE_THEME, unsafe_allow_html=True)


def render_header():
    """Render the main application header"""
    st.markdown(f'<h1 class="main-header">{APP_TITLE}</h1>', unsafe_allow_html=True)
    st.markdown(f'<p class="subtitle">{APP_SUBTITLE}</p>', unsafe_allow_html=True)


def collect_user_input():
    """Collect all user input from the sidebar form"""
    feature_maps = create_feature_mappings()

    with st.sidebar:
        # Preset selector
        preset = render_preset_selector()

        # Personal information
        personal_info = render_personal_info_section(preset, feature_maps)

        # Academic background
        academic_bg = render_academic_background_section(preset, feature_maps)

        # Family background
        family_bg = render_family_background_section(feature_maps)

        # Financial and social factors
        financial_social = render_financial_social_section()

        # Academic performance
        academic_performance = render_academic_performance_section(preset)

        # Economic indicators
        economic_indicators = render_economic_indicators_section()

    # Combine all input data
    user_input = {
        **personal_info,
        **academic_bg,
        **family_bg,
        **financial_social,
        **academic_performance,
        **economic_indicators
    }

    return user_input


@require_auth
def main():
    """Main Streamlit application"""
    # Check session timeout (30 minutes)
    check_session_timeout(30)

    # Apply theme
    apply_theme()

    # Load model and preprocessing info
    model, preprocessing_info, feature_names = load_model_and_info()

    # Render header with user context
    render_header()

    # Add admin panel if user is admin
    if check_role_permission("admin"):
        with st.sidebar:
            render_admin_panel()

    # Collect user input
    user_input = collect_user_input()

    # Main content area
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown('<h2 class="sub-header">Prediction Results</h2>', unsafe_allow_html=True)

        if check_role_permission("educator"):
            st.markdown(
                '<div class="info-box">🎓 <strong>Educator Access:</strong> You have full access to prediction features and student data analysis.</div>',
                unsafe_allow_html=True)

        # Render prediction section
        render_prediction_section(model, preprocessing_info, user_input)

    with col2:
        # Render model info and validation
        render_model_info_sidebar(user_input)

        # Render export section (role-based access)
        if check_role_permission("educator"):
            render_export_section(user_input)
        else:
            st.markdown(
                '<div class="warning-box">📊 <strong>Export Feature:</strong> Available for educators and administrators only.</div>',
                unsafe_allow_html=True)

    # Render footer
    render_footer()


if __name__ == "__main__":
    # Configure page before authentication
    st.set_page_config(**PAGE_CONFIG)
    main()