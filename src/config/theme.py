ROSE_PINE_THEME = """
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Rose Pine Color Palette */
    :root {
        --rp-base: #191724;
        --rp-surface: #1f1d2e;
        --rp-overlay: #26233a;
        --rp-muted: #6e6a86;
        --rp-subtle: #908caa;
        --rp-text: #e0def4;
        --rp-love: #eb6f92;
        --rp-gold: #f6c177;
        --rp-rose: #ebbcba;
        --rp-pine: #31748f;
        --rp-foam: #9ccfd8;
        --rp-iris: #c4a7e7;
    }
    
    /* Global Styles */
    .stApp {
        font-family: 'Inter', sans-serif;
        background-color: var(--rp-base);
        color: var(--rp-text);
    }
    
    /* Override Streamlit's default colors */
    .main .block-container {
        background-color: var(--rp-base);
        color: var(--rp-text);
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background-color: var(--rp-surface);
    }
    
    .css-1lcbmhc {
        background-color: var(--rp-surface);
    }
    
    /* Header Styles */
    .main-header {
        font-size: 3.5rem;
        background: linear-gradient(135deg, var(--rp-iris), var(--rp-foam));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-align: center;
        margin-bottom: 1rem;
        font-weight: 700;
        letter-spacing: -1px;
    }
    
    .subtitle {
        text-align: center;
        font-size: 1.2rem;
        color: var(--rp-subtle);
        margin-bottom: 3rem;
        font-weight: 400;
    }
    
    .sub-header {
        font-size: 1.4rem;
        color: var(--rp-text);
        margin-bottom: 1.5rem;
        font-weight: 600;
        border-bottom: 2px solid var(--rp-overlay);
        padding-bottom: 0.5rem;
    }
    
    /* Prediction Result Boxes */
    .prediction-box {
        padding: 2.5rem 2rem;
        border-radius: 16px;
        text-align: center;
        font-size: 1.8rem;
        font-weight: 700;
        margin: 2rem 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        transform: translateY(0);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        border: 2px solid;
    }
    
    .prediction-box:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 40px rgba(0,0,0,0.4);
    }
    
    .graduate-box {
        background: linear-gradient(135deg, var(--rp-foam), var(--rp-pine));
        color: var(--rp-base);
        border-color: var(--rp-foam);
    }
    
    .dropout-box {
        background: linear-gradient(135deg, var(--rp-love), #c74665);
        color: var(--rp-text);
        border-color: var(--rp-love);
    }
    
    .enrolled-box {
        background: linear-gradient(135deg, var(--rp-gold), #e6a85c);
        color: var(--rp-base);
        border-color: var(--rp-gold);
    }
    
    /* Metric Cards */
    .metric-card {
        background: linear-gradient(135deg, var(--rp-surface), var(--rp-overlay));
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 4px solid var(--rp-iris);
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        transition: transform 0.2s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.3);
    }
    
    .metric-card h4 {
        color: var(--rp-subtle);
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    
    .metric-card h2 {
        color: var(--rp-iris);
        font-weight: 700;
    }
    
    /* Sidebar Styling */
    .sidebar-section {
        background: var(--rp-overlay);
        padding: 1rem;
        border-radius: 8px;
        margin-bottom: 1rem;
        border-left: 3px solid var(--rp-iris);
    }
    
    /* Info boxes */
    .info-box {
        background: linear-gradient(135deg, var(--rp-overlay), var(--rp-surface));
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 4px solid var(--rp-foam);
        margin: 1rem 0;
        color: var(--rp-text);
    }
    
    .warning-box {
        background: linear-gradient(135deg, var(--rp-overlay), var(--rp-surface));
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 4px solid var(--rp-gold);
        margin: 1rem 0;
        color: var(--rp-text);
    }
    
    .success-box {
        background: linear-gradient(135deg, var(--rp-overlay), var(--rp-surface));
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 4px solid var(--rp-pine);
        margin: 1rem 0;
        color: var(--rp-text);
    }
    
    /* Button Styling */
    .stButton > button {
        background: linear-gradient(135deg, var(--rp-iris), var(--rp-love));
        color: var(--rp-text);
        border: none;
        border-radius: 25px;
        font-weight: 600;
        font-size: 1.1rem;
        padding: 0.75rem 2rem;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(196, 167, 231, 0.4);
    }
    
    /* Streamlit widget overrides */
    .stSelectbox > div > div {
        background-color: var(--rp-surface);
        color: var(--rp-text);
        border-color: var(--rp-overlay);
    }
    
    .stNumberInput > div > div > input {
        background-color: var(--rp-surface);
        color: var(--rp-text);
        border-color: var(--rp-overlay);
    }
    
    .stRadio > div {
        background-color: var(--rp-surface);
        border-radius: 8px;
        padding: 0.5rem;
    }
    
    /* Progress indicator */
    .progress-container {
        background: var(--rp-overlay);
        border-radius: 10px;
        height: 8px;
        margin: 1rem 0;
    }
    
    .progress-bar {
        background: linear-gradient(90deg, var(--rp-iris), var(--rp-foam));
        height: 100%;
        border-radius: 10px;
        transition: width 0.3s ease;
    }
    
    /* Section dividers */
    .section-divider {
        height: 2px;
        background: linear-gradient(90deg, transparent, var(--rp-iris), transparent);
        margin: 2rem 0;
    }
    
    /* Text color overrides */
    .markdown-text-container {
        color: var(--rp-text);
    }
    
    h1, h2, h3, h4, h5, h6 {
        color: var(--rp-text);
    }
    
    .stMarkdown {
        color: var(--rp-text);
    }
    
    /* Animations */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .fade-in {
        animation: fadeInUp 0.6s ease forwards;
    }
    
    /* Mobile responsiveness */
    @media (max-width: 768px) {
        .main-header {
            font-size: 2.5rem !important;
        }
        .prediction-box {
            font-size: 1.4rem !important;
            padding: 1.5rem 1rem !important;
        }
        .metric-card {
            padding: 1rem !important;
        }
    }
</style>
"""

PAGE_CONFIG = {
    "page_title": "Student Success Predictor",
    "page_icon": "📊",
    "layout": "wide",
    "initial_sidebar_state": "expanded",
}

APP_TITLE = "Student Success Predictor"
APP_SUBTITLE = "Predict whether a student will Graduate, Dropout, or remain Enrolled based on academic and demographic factors using advanced machine learning."

MODEL_FILES = {
    "model": "random_forest_model.pkl",
    "preprocessing": "preprocessing_info.pkl",
    "features": "feature_names.pkl",
}

MODEL_METRICS = {
    "accuracy": 93.84,
    "precision": 92.6,
    "recall": 94.02,
    "f1_score": 93.15,
}
