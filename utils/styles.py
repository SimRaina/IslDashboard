"""
Centralized styling for ISL Dashboard
Provides consistent theming across all pages
"""
import streamlit as st

# Color constants
THEME = {
    "bg_dark": "#0e1117",
    "bg_card": "#1c1f26",
    "accent_green": "#228B22",
    "accent_green_light": "rgba(34, 139, 34, 0.2)",
    "text_white": "white",
    "text_light_gray": "#c9d1d9",
}

def apply_dark_theme():
    """Apply consistent dark theme styling across all pages."""
    st.markdown(f"""
        <style>
        body {{
            background-color: {THEME['bg_dark']};
            color: {THEME['text_white']};
        }}
        .stMetric {{
            background-color: {THEME['bg_card']};
            padding: 10px;
            border-radius: 10px;
        }}
        .stDataFrame {{
            background-color: {THEME['bg_dark']};
        }}
        </style>
    """, unsafe_allow_html=True)

def get_theme_color(key):
    """Get a specific theme color by key."""
    return THEME.get(key, "#FFFFFF")

