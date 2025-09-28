"""
Prediction and results display components
"""

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import time
import json
from typing import Dict, Any, Tuple, List

from src.utils.models_utils import preprocess_input, generate_recommendations, validate_input


def render_prediction_section(model, preprocessing_info, user_input: Dict[str, Any]) -> None:
    """Render the prediction section with enhanced animations"""


    # Prediction button with enhanced styling
    predict_button = st.button("🔬 Analyze Student Data", type="primary", use_container_width=True)

    if predict_button:
        # Enhanced loading animation
        progress_bar = st.progress(0)
        status_text = st.empty()

        # Simulate processing steps
        steps = [
            ("Loading student data...", 20),
            ("Preprocessing features...", 40),
            ("Running machine learning model...", 70),
            ("Calculating prediction confidence...", 90),
            ("Finalizing results...", 100)
        ]

        for step, progress in steps:
            status_text.text(step)
            progress_bar.progress(progress)
            time.sleep(0.3)

        # Clear progress indicators
        progress_bar.empty()
        status_text.empty()

        # Preprocess input
        processed_input = preprocess_input(user_input, preprocessing_info)

        # Make prediction
        prediction = model.predict(processed_input)[0]
        prediction_proba = model.predict_proba(processed_input)[0]

        # Get prediction label
        target_reverse_mapping = preprocessing_info['target_reverse_mapping']
        predicted_outcome = target_reverse_mapping[prediction]

        # Store in session state for export
        st.session_state['last_prediction'] = {
            'outcome': predicted_outcome,
            'probabilities': prediction_proba,
            'timestamp': time.time()
        }

        # Enhanced prediction display with confidence indicators
        confidence_level = max(prediction_proba)
        confidence_text = "High" if confidence_level > 0.7 else "Medium" if confidence_level > 0.5 else "Low"

        # Display prediction with enhanced styling and confidence
        if predicted_outcome == "Graduate":
            st.markdown(f'''<div class="prediction-box graduate-box fade-in">
                🎓 GRADUATE
                <br><small style="font-size: 1rem; opacity: 0.9;">Confidence: {confidence_level:.1%} ({confidence_text})</small>
            </div>''', unsafe_allow_html=True)
            st.balloons()
        elif predicted_outcome == "Dropout":
            st.markdown(f'''<div class="prediction-box dropout-box fade-in">
                ⚠️ AT RISK OF DROPOUT
                <br><small style="font-size: 1rem; opacity: 0.9;">Confidence: {confidence_level:.1%} ({confidence_text})</small>
            </div>''', unsafe_allow_html=True)
        else:
            st.markdown(f'''<div class="prediction-box enrolled-box fade-in">
                📚 LIKELY TO STAY ENROLLED  
                <br><small style="font-size: 1rem; opacity: 0.9;">Confidence: {confidence_level:.1%} ({confidence_text})</small>
            </div>''', unsafe_allow_html=True)

        # Add personalized recommendations
        render_recommendations(predicted_outcome, user_input)

        # Display probability charts
        render_probability_charts(prediction_proba)


def render_recommendations(predicted_outcome: str, user_input: Dict[str, Any]) -> None:
    """Render personalized recommendations section"""


    st.markdown("### 💡 Personalized Recommendations")

    recommendations = generate_recommendations(predicted_outcome, user_input)

    if predicted_outcome == "Graduate":
        st.markdown(
            '<div class="success-box">🎯 <strong>Success Indicators:</strong> This student shows strong potential for graduation. Continue supporting their academic journey.</div>',
            unsafe_allow_html=True)
    elif predicted_outcome == "Dropout":
        if recommendations:
            rec_text = '<br>'.join(recommendations)
            st.markdown(f'<div class="warning-box">🎯 <strong>Intervention Strategies:</strong><br>{rec_text}</div>',
                        unsafe_allow_html=True)
    else:
        st.markdown(
            '<div class="info-box">📈 <strong>Monitoring Needed:</strong> This student may benefit from regular check-ins and academic support.</div>',
            unsafe_allow_html=True)


def render_probability_charts(prediction_proba: List[float]) -> None:
    """Render prediction probability charts and metrics"""
    st.markdown("### 📊 Prediction Confidence")

    # Create probability dataframe
    import pandas as pd
    prob_df = pd.DataFrame({
        'Outcome': ['Dropout', 'Enrolled', 'Graduate'],
        'Probability': prediction_proba
    })

    # Create probability chart
    fig = px.bar(
        prob_df,
        x='Outcome',
        y='Probability',
        color='Outcome',
        color_discrete_map={
            'Graduate': '#9ccfd8',  # Rose Pine foam
            'Dropout': '#eb6f92',  # Rose Pine love
            'Enrolled': '#f6c177'  # Rose Pine gold
        },
        title="Prediction Probabilities"
    )
    fig.update_layout(
        showlegend=False,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    st.plotly_chart(fig, use_container_width=True)

    # Display detailed probabilities in cards
    col_a, col_b, col_c = st.columns(3)

    with col_a:
        st.markdown(f"""
        <div class="metric-card">
            <h4>Graduate</h4>
            <h2>{prediction_proba[2]:.1%}</h2>
        </div>
        """, unsafe_allow_html=True)

    with col_b:
        st.markdown(f"""
        <div class="metric-card">
            <h4>Dropout</h4>
            <h2>{prediction_proba[0]:.1%}</h2>
        </div>
        """, unsafe_allow_html=True)

    with col_c:
        st.markdown(f"""
        <div class="metric-card">
            <h4>Enrolled</h4>
            <h2>{prediction_proba[1]:.1%}</h2>
        </div>
        """, unsafe_allow_html=True)


def render_model_info_sidebar(user_input: Dict[str, Any]) -> None:
    """Render model information and validation in sidebar"""
    from ..config.theme import MODEL_METRICS

    st.markdown('<h2 class="sub-header">📊 Model Insights</h2>', unsafe_allow_html=True)

    # Model information
    st.markdown('<div class="info-box">', unsafe_allow_html=True)
    st.markdown(f"""
    **🤖 Model Details:**
    - **Algorithm:** Random Forest Classifier
    - **Features:** 36 student characteristics  
    - **Training Accuracy:** 100%
    - **Test Accuracy:** {MODEL_METRICS['accuracy']}%
    - **Classes:** Graduate, Dropout, Enrolled
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    # Input validation feedback
    st.markdown("### 🔍 Input Validation")
    validation_issues = validate_input(user_input)

    if validation_issues:
        for issue in validation_issues:
            st.warning(issue)
    else:
        st.success("✅ All inputs look valid!")

    # Model performance visualization
    st.markdown("### Model Performance")

    metrics = ['Accuracy', 'Precision', 'Recall', 'F1-Score']
    values = [MODEL_METRICS['accuracy'], MODEL_METRICS['precision'],
              MODEL_METRICS['recall'], MODEL_METRICS['f1_score']]

    fig_perf = go.Figure(data=go.Scatterpolar(
        r=values,
        theta=metrics,
        fill='toself',
        line_color='#c4a7e7'  # Rose Pine iris
    ))

    fig_perf.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )),
        showlegend=False,
        title="Model Performance Metrics",
        height=300,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )

    st.plotly_chart(fig_perf, use_container_width=True)


def render_export_section(user_input: Dict[str, Any]) -> None:
    """Render export functionality"""
    st.markdown("### 📥 Export Results")

    if st.session_state.get('last_prediction'):
        export_data = {
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
            'prediction': st.session_state['last_prediction']['outcome'],
            'confidence': f"{max(st.session_state['last_prediction']['probabilities']):.1%}",
            'student_data': user_input
        }

        # Convert to JSON for download
        json_str = json.dumps(export_data, indent=2, ensure_ascii=False)

        st.download_button(
            label="📁 Download Prediction Report",
            data=json_str,
            file_name=f"student_prediction_{time.strftime('%Y%m%d_%H%M%S')}.json",
            mime="application/json"
        )


def render_footer() -> None:
    """Render enhanced footer with project information"""
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("**📊 Data Source**")
        st.caption("UCI ML Repository - Student Academic Success")

    with col2:
        st.markdown("**🔬 Model Info**")
        st.caption("Random Forest with 93.84% accuracy")

    with col3:
        st.markdown("**🛠️ Built With**")
        st.caption("Streamlit • scikit-learn • Plotly")

    st.markdown("---")
    st.markdown(
        '<p style="text-align: center; color: #6c757d; font-size: 0.9rem;">🎓 Empowering educational institutions with data-driven insights for student success</p>',
        unsafe_allow_html=True)