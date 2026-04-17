import streamlit as st
import pandas as pd
from utils.loader import load_data, get_current_season
from utils.standings import calculate_standings

teams, players, matches, seasons, teams_socials = load_data()
current_season = get_current_season()

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
st.markdown("**Explore teams, players, seasons, and analytics in one place.**")

# Key metrics
season_matches = matches[matches["season"] == current_season]
total_goals = season_matches["home_goals"].sum() + season_matches["away_goals"].sum()
total_matches = len(season_matches[season_matches["match_status"] == "completed"])
top_scorer = players.sort_values(by="goals", ascending=False).iloc[0]

st.markdown("---")
st.subheader("📊 Key Metrics")

col1, col2, col3, col4 = st.columns([1, 1, 1.5, 1])

col1.metric("Total Matches", total_matches)
col2.metric("Total Goals", int(total_goals))
col3.metric("Top Scorer", top_scorer["name"])
col4.metric("Goals", int(top_scorer['goals']))

st.markdown("---")

# Current standings widget
st.subheader("⚡ Current League Standings")
standings = calculate_standings(season_matches, teams, current_season)
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
completed_matches = season_matches[season_matches["match_status"] == "completed"].copy()
completed_matches["date"] = pd.to_datetime(completed_matches["date"], format="%d-%m-%Y")
completed_matches = completed_matches.sort_values("date", ascending=False).head(7)

if len(completed_matches) > 0:
    for _, match in completed_matches.iterrows():
        result = "Won" if match["home_goals"] > match["away_goals"] else ("Drew" if match["home_goals"] == match["away_goals"] else "Lost")
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(f"**{match['home_team']}** {int(match['home_goals'])} - {int(match['away_goals'])} **{match['away_team']}**")
            st.caption(f"{match['date'].strftime('%d-%m-%Y')} | GW {int(match['gameweek'])} | {match['venue']}")
        st.divider()
else:
    st.info("No matches played yet.")
