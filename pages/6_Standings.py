import streamlit as st
import pandas as pd
from utils.loader import load_data, get_current_season, get_available_seasons, get_completed_matches
from utils.standings import calculate_standings
from utils.styles import apply_dark_theme

st.set_page_config(page_title="ISL Standings", layout="wide")

apply_dark_theme()

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

# Calculate and display standings - only use completed matches
completed_matches = get_completed_matches(matches, selected_season)
standings = calculate_standings(completed_matches, teams, selected_season)

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

total_goals = completed_matches["home_goals"].sum() + completed_matches["away_goals"].sum()
total_matches_played = len(completed_matches)

col1.metric("Total Matches Played", total_matches_played)
col2.metric("Total Goals Scored", int(total_goals))
col3.metric("Avg Goals per Match", f"{total_goals / total_matches_played:.2f}" if total_matches_played > 0 else "0")

st.markdown("---")
st.subheader("Home vs Away Performance")

home_away_stats = []
for team in standings["team_name"]:
    home = completed_matches[completed_matches["home_team"] == team]
    away = completed_matches[completed_matches["away_team"] == team]
    
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

