import streamlit as st
import pandas as pd
from utils.loader import load_data, get_current_season
from utils.standings import calculate_standings
from utils.styles import apply_dark_theme
from utils.components import display_match_result

teams, players, matches, seasons, teams_socials = load_data()
current_season = get_current_season()

apply_dark_theme()

st.title("⚽ Indian Super League Dashboard 2026")
st.markdown("**Explore teams, players, seasons, and analytics in one place.**")

# Key metrics
season_matches = matches[matches["season"] == current_season]
completed_matches = season_matches[season_matches["match_status"] == "completed"]
total_goals = completed_matches["home_goals"].sum() + completed_matches["away_goals"].sum()
total_matches = len(completed_matches)
top_scorer = players.sort_values(by="goals", ascending=False).iloc[0]

st.markdown("---")
st.subheader("📊 Key Metrics")

col1, col2, col3, col4 = st.columns([1, 1, 2.5, 0.75])

col1.metric("Total Matches", total_matches)
col2.metric("Total Goals", int(total_goals))
col3.metric("Top Scorer", top_scorer["name"])
col4.metric("Goals", int(top_scorer['goals']))

st.markdown("---")

# Current standings widget
st.subheader("⚡ Current League Standings")
standings = calculate_standings(completed_matches, teams, current_season)
display_standings = standings[["position", "team_name", "matches_played", "points", "goal_difference"]]
display_standings.columns = ["Pos", "Team", "P", "Pts", "GD"]
st.dataframe(display_standings, use_container_width=True, hide_index=True)

col1, col2 = st.columns(2)

with col1:
    st.caption(f"📍 Top team: **{standings.iloc[0]['team_name']}** with {int(standings.iloc[0]['points'])} points")

with col2:
    st.caption(f"🏆 Teams in competition: **{len(standings)}** teams")

st.markdown("---")

st.subheader("📋 Recent Matches")
recent_matches = completed_matches.copy()
recent_matches["date"] = pd.to_datetime(recent_matches["date"], format="%d-%m-%Y")
recent_matches = recent_matches.sort_values("date", ascending=False).head(7)

if len(recent_matches) > 0:
    for _, match in recent_matches.iterrows():
        display_match_result(match)
else:
    st.info("No matches played yet.")
