import streamlit as st
import pandas as pd
from utils.loader import load_data, get_current_season

st.set_page_config(page_title="ISL Fixtures", layout="wide")

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

st.title("🗓️ Fixtures & Results")

teams, players, matches, seasons, teams_socials = load_data()
current_season = get_current_season()

# Filter matches by season
season_matches = matches[matches["season"] == current_season].sort_values("date", ascending=False)

# Create tabs
tab1, tab2 = st.tabs(["Results", "Upcoming Fixtures"])

with tab1:
    st.subheader("📋 Match Results")
    
    # Completed matches
    completed = season_matches[season_matches["match_status"] == "completed"]
    
    if len(completed) > 0:
        # Group by gameweek
        gameweeks = sorted(completed["gameweek"].unique(), reverse=True)
        
        selected_gameweek = st.selectbox(
            "Select Gameweek",
            gameweeks,
            key="gw_results"
        )
        
        gw_matches = completed[completed["gameweek"] == selected_gameweek].sort_values("date", ascending=False)
        
        st.write(f"**Gameweek {selected_gameweek}**")
        
        for _, match in gw_matches.iterrows():
            col1, col2, col3, col4, col5 = st.columns([2, 1, 1, 1, 2])
            
            with col1:
                st.write(f"**{match['home_team']}**")
            with col2:
                st.write(f"{int(match['home_goals'])}")
            with col3:
                st.write("-")
            with col4:
                st.write(f"{int(match['away_goals'])}")
            with col5:
                st.write(f"**{match['away_team']}**")
            
            st.caption(f"{match['date']} at {match['venue']}")
            st.divider()
        
        # Show all results table
        st.subheader("All Results")
        all_results_display = completed[[
            "date", "gameweek", "home_team", "home_goals", "away_team", "away_goals", "venue"
        ]].copy()
        # Convert date to datetime for proper sorting
        all_results_display["date"] = pd.to_datetime(all_results_display["date"], format="%d-%m-%Y")
        all_results_display.columns = ["Date", "GW", "Home", "HG", "Away", "AG", "Venue"]
        all_results_display = all_results_display.sort_values("Date", ascending=False)
        # Format date back to readable format
        all_results_display["Date"] = all_results_display["Date"].dt.strftime("%d-%m-%Y")
        st.dataframe(all_results_display, use_container_width=True, hide_index=True)
    else:
        st.info("No completed matches yet.")

with tab2:
    st.subheader("📅 Upcoming Matches")
    
    # Upcoming matches
    upcoming = season_matches[season_matches["match_status"] == "upcoming"]
    
    if len(upcoming) > 0:
        # Group by gameweek
        gameweeks = sorted(upcoming["gameweek"].unique())
        
        selected_gameweek = st.selectbox(
            "Select Gameweek",
            gameweeks,
            key="gw_upcoming"
        )
        
        gw_matches = upcoming[upcoming["gameweek"] == selected_gameweek].sort_values("date")
        
        st.write(f"**Gameweek {selected_gameweek}**")
        
        for _, match in gw_matches.iterrows():
            col1, col2, col3 = st.columns([2, 1, 2])
            
            with col1:
                st.write(f"**{match['home_team']}**")
            with col2:
                st.write("vs")
            with col3:
                st.write(f"**{match['away_team']}**")
            
            st.caption(f"{match['date']} at {match['venue']}")
            st.divider()
        
        # Show fixture calendar
        st.subheader("Full Fixture List")
        fixture_display = upcoming[[
            "date", "gameweek", "home_team", "away_team", "venue"
        ]].copy()
        fixture_display.columns = ["Date", "GW", "Home", "Away", "Venue"]
        st.dataframe(fixture_display, use_container_width=True, hide_index=True)
    else:
        st.info("No upcoming matches scheduled.")

st.markdown("---")

# Head-to-head section
st.subheader("🏁 Head-to-Head Matchups")

col1, col2 = st.columns(2)
with col1:
    team1 = st.selectbox("Select First Team", teams["team_name"].unique(), key="h2h_1")

with col2:
    team2 = st.selectbox("Select Second Team", teams["team_name"].unique(), key="h2h_2")

if team1 != team2:
    h2h_matches = season_matches[
        ((season_matches["home_team"] == team1) & (season_matches["away_team"] == team2)) |
        ((season_matches["home_team"] == team2) & (season_matches["away_team"] == team1))
    ]
    
    if len(h2h_matches) > 0:
        st.write(f"**{team1} vs {team2}** - All Time Matches")
        
        h2h_display = h2h_matches[[
            "date", "home_team", "home_goals", "away_team", "away_goals", "venue"
        ]].copy()
        h2h_display.columns = ["Date", "Home", "HG", "Away", "AG", "Venue"]
        st.dataframe(h2h_display, use_container_width=True, hide_index=True)
    else:
        st.info(f"{team1} and {team2} haven't played each other yet this season.")
else:
    st.warning("Please select two different teams.")

