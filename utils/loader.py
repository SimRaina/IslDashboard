import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    """Load all data from CSV files with caching."""
    teams = pd.read_csv("data/teams.csv", encoding="latin-1")
    players = pd.read_csv("data/players.csv", encoding="latin-1")
    matches = pd.read_csv("data/matches.csv", encoding="latin-1")
    seasons = pd.read_csv("data/seasons.csv", encoding="latin-1")
    teams_socials = pd.read_csv("data/teams_socials.csv", encoding="latin-1")

    return teams, players, matches, seasons, teams_socials


def get_current_season():
    """Get the current season from environment or default."""
    return "2025-26"


@st.cache_data
def get_available_seasons(matches_df):
    """Get list of available seasons from matches data."""
    return sorted(matches_df["season"].unique().tolist())
