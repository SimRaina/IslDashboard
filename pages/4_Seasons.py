import streamlit as st
import pandas as pd
import plotly.express as px
from utils.loader import load_data

teams, players, matches, seasons, teams_socials = load_data()
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
st.title("📅 Seasons")

# Season selector
season_selected = st.selectbox("Select Season", seasons["season"])

season_data = seasons[seasons["season"] == season_selected].iloc[0]

col1, col2, col3 = st.columns([1, 2, 1])
col1.metric("Season Winner", season_data["winner"])
col2.metric("Top Scorer", season_data["top_scorer"])
col3.metric("Top Goals", season_data["top_goals"])

st.markdown("---")

# Season comparison
st.subheader("Season Statistics Comparison")

# Prepare data for comparison
season_stats = []
for season_name in seasons["season"].unique():
    season_matches = matches[matches["season"] == season_name]
    completed = season_matches[season_matches["match_status"] == "completed"]
    
    total_goals = completed["home_goals"].sum() + completed["away_goals"].sum()
    total_matches = len(completed)
    
    season_stats.append({
        "Season": season_name,
        "Matches": total_matches,
        "Total Goals": total_goals,
        "Avg Goals/Match": total_goals / total_matches if total_matches > 0 else 0
    })

season_stats_df = pd.DataFrame(season_stats)

col1, col2 = st.columns(2)

with col1:
    fig1 = px.bar(season_stats_df, x="Season", y="Matches", title="Matches per Season")
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    fig2 = px.bar(season_stats_df, x="Season", y="Total Goals", title="Total Goals per Season")
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")

# All seasons table
st.subheader("Historical Seasons")
st.dataframe(seasons, use_container_width=True, hide_index=True)
