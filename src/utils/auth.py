"""
Authentication module for Student Success Predictor
Provides secure login/logout functionality with session management
"""

import streamlit as st
import hashlib
import json
import os
from typing import Dict, Optional, Tuple
from pathlib import Path

# Path to store user credentials (in production, use a proper database)
USERS_FILE = Path("users.json")

# Default admin user (change password in production!)
DEFAULT_USERS = {
    "admin": {
        "password_hash": "240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9",  # "admin123"
        "role": "admin",
        "name": "Administrator"
    },
}


def hash_password(password: str) -> str:
    """Hash a password using SHA-256"""
    return hashlib.sha256(password.encode()).hexdigest()


def load_users() -> Dict:
    """Load users from file or create default users"""
    if USERS_FILE.exists():
        try:
            with open(USERS_FILE, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            pass

    # Create default users file
    save_users(DEFAULT_USERS)
    return DEFAULT_USERS


def save_users(users: Dict) -> None:
    """Save users to file"""
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=2)


def verify_credentials(username: str, password: str) -> Tuple[bool, Optional[Dict]]:
    """Verify user credentials"""
    users = load_users()

    if username in users:
        stored_hash = users[username]["password_hash"]
        input_hash = hash_password(password)

        if stored_hash == input_hash:
            return True, users[username]

    return False, None


def init_session_state():
    """Initialize session state for authentication"""
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    if 'username' not in st.session_state:
        st.session_state.username = None
    if 'user_role' not in st.session_state:
        st.session_state.user_role = None
    if 'user_name' not in st.session_state:
        st.session_state.user_name = None


def login_form():
    """Render login form with Rose Pine styling"""
    st.markdown("""
    <style>
    .login-container {
        max-width: 400px;
        margin: 2rem auto;
        padding: 2rem;
        background: linear-gradient(135deg, var(--rp-surface), var(--rp-overlay));
        border-radius: 16px;
        border: 2px solid var(--rp-iris);
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }
    .login-header {
        text-align: center;
        color: var(--rp-text);
        font-size: 2rem;
        font-weight: 700;
        margin-bottom: 2rem;
        background: linear-gradient(135deg, var(--rp-iris), var(--rp-foam));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .login-info {
        background: linear-gradient(135deg, var(--rp-overlay), var(--rp-surface));
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid var(--rp-gold);
        margin-bottom: 1.5rem;
        color: var(--rp-text);
        font-size: 0.9rem;
    }
    </style>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="login-container">', unsafe_allow_html=True)

        st.markdown('<h1 class="login-header">🔐 Student Success Predictor</h1>', unsafe_allow_html=True)

        # Demo credentials info
        st.markdown("""
        <div class="login-info">
        <strong>Demo Credentials:</strong><br>
        👨‍💼 Admin: <code>admin</code> / <code>admin123</code><br>
        </div>
        """, unsafe_allow_html=True)

        with st.form("login_form"):
            username = st.text_input("Username", placeholder="Enter your username")
            password = st.text_input("Password", type="password", placeholder="Enter your password")

            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                login_button = st.form_submit_button("🚀 Login", use_container_width=True)

            if login_button:
                if username and password:
                    is_valid, user_info = verify_credentials(username, password)

                    if is_valid:
                        st.session_state.authenticated = True
                        st.session_state.username = username
                        st.session_state.user_role = user_info["role"]
                        st.session_state.user_name = user_info["name"]
                        st.success(f"Welcome back, {user_info['name']}!")
                        st.rerun()
                    else:
                        st.error("❌ Invalid username or password")
                else:
                    st.warning("⚠️ Please enter both username and password")

        st.markdown('</div>', unsafe_allow_html=True)


def logout():
    """Logout user and clear session"""
    st.session_state.authenticated = False
    st.session_state.username = None
    st.session_state.user_role = None
    st.session_state.user_name = None
    st.rerun()


def render_user_info():
    """Render user information in sidebar"""
    if st.session_state.authenticated:
        with st.sidebar:
            st.markdown("---")
            st.markdown("### 👤 User Information")

            # User info card
            st.markdown(f"""
            <div style="
                background: linear-gradient(135deg, var(--rp-surface), var(--rp-overlay));
                padding: 1rem;
                border-radius: 8px;
                border-left: 3px solid var(--rp-iris);
                margin-bottom: 1rem;
            ">
                <strong>👋 {st.session_state.user_name}</strong><br>
                <small>Role: {st.session_state.user_role.title()}</small><br>
                <small>User: @{st.session_state.username}</small>
            </div>
            """, unsafe_allow_html=True)

            # Logout button
            if st.button("🚪 Logout", type="secondary", use_container_width=True):
                logout()


def require_auth(func):
    """Decorator to require authentication for functions"""

    def wrapper(*args, **kwargs):
        init_session_state()

        if not st.session_state.authenticated:
            login_form()
            return None

        # Add user info to sidebar
        render_user_info()

        return func(*args, **kwargs)

    return wrapper


def check_role_permission(required_role: str = None) -> bool:
    """Check if current user has required role"""
    if not st.session_state.authenticated:
        return False

    if required_role is None:
        return True

    user_role = st.session_state.user_role

    # Define role hierarchy (admin > educator > user)
    role_hierarchy = {
        "admin": 3,
        "educator": 2,
        "user": 1
    }

    current_level = role_hierarchy.get(user_role, 0)
    required_level = role_hierarchy.get(required_role, 0)

    return current_level >= required_level


def add_user(username: str, password: str, name: str, role: str = "user") -> bool:
    """Add a new user (admin only)"""
    if not check_role_permission("admin"):
        return False

    users = load_users()

    if username in users:
        return False  # User already exists

    users[username] = {
        "password_hash": hash_password(password),
        "role": role,
        "name": name
    }

    save_users(users)
    return True


def render_admin_panel():
    """Render admin panel for user management"""
    if not check_role_permission("admin"):
        st.error("🚫 Access denied. Admin privileges required.")
        return

    st.markdown("### 👨‍💼 Admin Panel")

    with st.expander("👥 User Management"):
        st.markdown("#### Add New User")

        with st.form("add_user_form"):
            new_username = st.text_input("Username")
            new_password = st.text_input("Password", type="password")
            new_name = st.text_input("Full Name")
            new_role = st.selectbox("Role", ["user", "educator", "admin"])

            if st.form_submit_button("➕ Add User"):
                if all([new_username, new_password, new_name]):
                    if add_user(new_username, new_password, new_name, new_role):
                        st.success(f"✅ User '{new_username}' added successfully!")
                    else:
                        st.error("❌ User already exists or operation failed")
                else:
                    st.warning("⚠️ Please fill all fields")

        # Display existing users
        st.markdown("#### Existing Users")
        users = load_users()

        for username, info in users.items():
            col1, col2, col3 = st.columns([2, 1, 1])
            with col1:
                st.text(f"👤 {info['name']} (@{username})")
            with col2:
                st.text(f"🏷️ {info['role']}")
            with col3:
                if username != st.session_state.username:  # Can't delete self
                    if st.button("🗑️", key=f"del_{username}", help="Delete user"):
                        del users[username]
                        save_users(users)
                        st.rerun()


# Session timeout functionality
def check_session_timeout(timeout_minutes: int = 30):
    """Check if session has timed out"""
    import time

    if 'last_activity' not in st.session_state:
        st.session_state.last_activity = time.time()

    current_time = time.time()
    time_diff = (current_time - st.session_state.last_activity) / 60  # Convert to minutes

    if time_diff > timeout_minutes and st.session_state.authenticated:
        st.warning(f"⏰ Session expired after {timeout_minutes} minutes of inactivity")
        logout()
    else:
        st.session_state.last_activity = current_time