import streamlit as st
import pandas as pd
from utils.loader import load_data, get_current_season, get_available_seasons
from utils.standings import calculate_standings

st.set_page_config(page_title="ISL Standings", layout="wide")

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

st.title("🏆 League Standings")

teams, players, matches, seasons, teams_socials = load_data()

# Season selector
available_seasons = get_available_seasons(matches)
current_season = get_current_season()

selected_season = st.selectbox(
    "Select Season",
    available_seasons,
    index=available_seasons.index(current_season) if current_season in available_seasons else 0
)

# Calculate and display standings
standings = calculate_standings(matches, teams, selected_season)

st.subheader(f"2025-26 Season Standings")

# Format standings for display
display_standings = standings.copy()
display_standings = display_standings[[
    "position", "team_name", "matches_played", "wins", "draws", "losses",
    "goals_for", "goals_against", "goal_difference", "points"
]]
display_standings.columns = ["Pos", "Team", "P", "W", "D", "L", "GF", "GA", "GD", "Pts"]

# Color-code positions
def style_standings(row):
    styles = [''] * len(row)
    pos = row['Pos']
    if pos <= 4:
        return [f'background-color: rgba(34, 139, 34, 0.2)'] * len(row)
    return styles

st.dataframe(display_standings, use_container_width=True, hide_index=True)

st.markdown("---")

# Additional stats
col1, col2, col3 = st.columns(3)

total_goals = matches[matches["season"] == selected_season]["home_goals"].sum() + \
              matches[matches["season"] == selected_season]["away_goals"].sum()
total_matches = len(matches[(matches["season"] == selected_season) & (matches["match_status"] == "completed")])

col1.metric("Total Matches Played", total_matches)
col2.metric("Total Goals Scored", int(total_goals))
col3.metric("Avg Goals per Match", f"{total_goals / total_matches:.2f}" if total_matches > 0 else "0")

st.markdown("---")
st.subheader("Home vs Away Performance")

home_away_stats = []
for team in standings["team_name"]:
    team_matches = matches[(matches["season"] == selected_season) & (matches["match_status"] == "completed")]
    
    home = team_matches[team_matches["home_team"] == team]
    away = team_matches[team_matches["away_team"] == team]
    
    home_wins = len(home[home["home_goals"] > home["away_goals"]])
    away_wins = len(away[away["away_goals"] > away["home_goals"]])
    
    home_away_stats.append({
        "Team": team,
        "Home P": len(home),
        "Home W": home_wins,
        "Away P": len(away),
        "Away W": away_wins,
    })

home_away_df = pd.DataFrame(home_away_stats)
st.dataframe(home_away_df, use_container_width=True, hide_index=True)

