import streamlit as st
import plotly.express as px
from utils.loader import load_data
from utils.stats import get_goalkeeper_stats

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
st.title("👤 Players")

# Filters
col1, col2, col3, col4 = st.columns(4)

with col1:
    team_filter = st.selectbox("Filter by Team", ["All"] + list(players["team"].unique()))

with col2:
    position_filter = st.selectbox("Filter by Position", ["All"] + list(players["position"].unique()))

with col3:
    nationality_filter = st.selectbox("Filter by Nationality", ["All"] + list(players["nationality"].unique()))

with col4:
    # Get unique ages and sort them
    unique_ages = sorted([int(age) for age in players["age"].dropna().unique() if str(age).replace('.', '').isdigit()])
    age_filter = st.selectbox("Filter by Age", ["All"] + unique_ages)

# Apply filters
filtered_players = players.copy()

if team_filter != "All":
    filtered_players = filtered_players[filtered_players["team"] == team_filter]

if position_filter != "All":
    filtered_players = filtered_players[filtered_players["position"] == position_filter]

if nationality_filter != "All":
    filtered_players = filtered_players[filtered_players["nationality"] == nationality_filter]

if age_filter != "All":
    filtered_players = filtered_players[filtered_players["age"] == age_filter]

# Display player stats
st.subheader("Player Statistics")
display_players = filtered_players[[
    "name", "team", "position", "nationality", "goals", "assists", "minutes"
]].copy()
display_players.columns = ["Player", "Team", "Position", "Nationality", "Goals", "Assists", "Minutes"]

st.dataframe(display_players, use_container_width=True, hide_index=True)

st.markdown("---")

st.subheader("Top Scorers")

top = filtered_players.sort_values(by="goals", ascending=False).head(10)

if len(top) > 0:
    fig = px.bar(top, x="name", y="goals", color="team", title="Top Scorers (Filtered)")
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

st.subheader("Top Assist Providers")

top_assists = filtered_players.sort_values(by="assists", ascending=False).head(10)

if len(top_assists) > 0:
    fig = px.bar(top_assists, x="name", y="assists", color="team", title="Top Assist Providers (Filtered)")
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

st.subheader("🧤 Goalkeeper Statistics")

# Get goalkeeper stats
gk_stats = get_goalkeeper_stats(players, matches, teams)

if len(gk_stats) > 0:
    col1, col2 = st.columns(2)
    
    with col1:
        # Best clean sheet records
        best_clean_sheets = gk_stats.nlargest(10, "Clean Sheets")[["name", "Clean Sheets", "team", "Matches"]]
        fig = px.bar(best_clean_sheets, x="name", y="Clean Sheets", color="team", title="Goalkeepers with Most Clean Sheets")
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Best goal conceded records (fewest)
        best_defense = gk_stats.nsmallest(10, "Goals Conceded")[["name", "Goals Conceded", "team", "Matches"]]
        fig = px.bar(best_defense, x="name", y="Goals Conceded", color="team", title="Goalkeepers with Fewest Goals Conceded")
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # Display full goalkeeper stats table
    st.write("**Complete Goalkeeper Statistics**")
    display_gk = gk_stats.sort_values("Clean Sheets", ascending=False)
    st.dataframe(display_gk, use_container_width=True, hide_index=True)
else:
    st.info("No goalkeeper data available")


