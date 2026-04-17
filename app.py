import streamlit as st

st.set_page_config(
    page_title="ISL Dashboard",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
    <style>
    body {
        background-color: #0e1117;
        color: white;
    }
    .stMetric {
        background-color: #1c1f26;
        padding: 10px;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("⚽ Indian Super League Dashboard 2026")
st.markdown("**Your complete platform for ISL data analysis, team evaluation, and professional scouting.**")

st.markdown("---")

st.subheader("🎯 Dashboard Features")

# Feature columns
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### 📊 **Analytics & Insights**
    - **Standings** - Live league table with all statistics
    - **Leaders** - Top scorers, assists, and player efficiency
    - **Analytics** - Advanced statistics and trends
    - **Seasons** - Historical data and comparisons
    """)

with col2:
    st.markdown("""
    ### 🔍 **Scouting & Evaluation**
    - **Scouting Report** - Professional player evaluation
    - **Team Deep Dive** - Detailed team analysis
    - **Fixtures** - Match schedule and results
    - **Head-to-Head** - Team comparisons
    """)

st.markdown("---")

st.subheader("📖 Quick Navigation Guide")

# Main navigation
with st.expander("📱 **All Pages** (Click to expand)", expanded=True):
    st.markdown("""
    #### **Data & Statistics**
    - **Overview** - Dashboard summary with key metrics and current standings
    - **Teams** - View team profiles, squads, and performance records
    - **Players** - Explore player statistics with advanced filtering
    - **Standings** - Complete league table with detailed metrics
    - **Analytics & Statistics** - Advanced statistics, trends, and performance analysis
    
    #### **Analysis & Insights**
    - **Seasons** - Historical season data and yearly comparisons
    - **Fixtures** - Match schedule, results, and head-to-head history
    
    #### **Professional Scouting**
    - **Scouting Report** - Generate professional player evaluation reports
        - Select any player and match
        - Rate position-specific competencies
        - Add detailed assessment notes
        - Download as professional PDF report
    """)

st.markdown("---")

st.subheader("🔍 Scouting Report - Professional Player Evaluation")

with st.expander("📋 **How to Use Scouting Report**", expanded=False):
    st.markdown("""
    The **Scouting Report** tool allows you to create professional player evaluations:
    
    **Step-by-Step Guide:**
    1. Navigate to "Scouting Report" in the sidebar
    2. Select a player from the dropdown
    3. Choose a recent match for evaluation
    4. Review auto-populated match and player details
    5. Rate position-specific competencies (1-10)
    6. Enter your assessment:
       - Scout name
       - Key strengths
       - Areas for improvement
       - Overall rating
       - Recommendation (Target/Monitor/Pass/Follow-up)
       - Detailed comments
    7. Click "Generate & Download PDF"
    8. Save the professional report
    
    **Position-Specific Competencies:**
    - **Forward:** Finishing, Positioning, Movement, First Touch, Physical Strength, Game Intelligence, Work Rate, Heading
    - **Winger:** Pace, Dribbling, Crossing, Shooting, Work Rate, Defensive Work Rate, Decision Making, Physical Strength
    - **Midfielder:** Passing Accuracy, Vision, Ball Control, Positioning, Work Rate, Tackling, Game Intelligence, Physical Strength
    - **Defender:** Marking, Tackling, Positioning, Heading, Physical Strength, Passing Accuracy, Concentration, Game Reading
    
    **PDF Report Includes:**
    - Report metadata (date, scout name, timestamp)
    - Complete match information
    - Full player profile
    - Competency assessment table
    - Detailed evaluation section
    - Professional formatting for documentation
    """)

st.markdown("---")

st.subheader("🎯 Common Tasks")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    **📊 Analytics**
    
    - View league standings
    - Check top scorers
    - Compare seasons
    - Analyze trends
    """)

with col2:
    st.markdown("""
    **🏟️ Team Analysis**
    
    - Team profiles & squads
    - Team comparisons
    - Deep dive analytics
    - Performance metrics
    """)

with col3:
    st.markdown("""
    **🔍 Scouting**
    
    - Create scout reports
    - Evaluate players
    - Generate PDFs
    - Document assessments
    """)

st.markdown("---")

st.info("""
💡 **Tip:** Use the sidebar to navigate between different pages. Each page provides specific insights and analysis tools for your ISL data exploration and scouting needs.
""")

