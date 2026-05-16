import pandas as pd
import streamlit as st

# Constant encoding for all CSV files
CSV_ENCODING = "latin-1"

@st.cache_data
def load_data():
    """Load all data from CSV files with caching and type optimization."""
    teams = pd.read_csv("data/teams.csv", encoding=CSV_ENCODING)
    players = pd.read_csv("data/players.csv", encoding=CSV_ENCODING)
    matches = pd.read_csv("data/matches.csv", encoding=CSV_ENCODING)
    seasons = pd.read_csv("data/seasons.csv", encoding=CSV_ENCODING)
    teams_socials = pd.read_csv("data/teams_socials.csv", encoding=CSV_ENCODING)
    
    # Optimize numeric columns in matches
    numeric_match_cols = ["home_goals", "away_goals", "gameweek"]
    for col in numeric_match_cols:
        if col in matches.columns:
            matches[col] = pd.to_numeric(matches[col], errors='coerce').fillna(0).astype(int)
    
    # Optimize numeric columns in players
    numeric_player_cols = ["goals", "assists", "age", "minutes"]
    for col in numeric_player_cols:
        if col in players.columns:
            players[col] = pd.to_numeric(players[col], errors='coerce').fillna(0)
            if col != "minutes":  # minutes can be float for per-90 calculations
                players[col] = players[col].astype(int)

    return teams, players, matches, seasons, teams_socials


def get_current_season():
    """Get the current season from environment or default."""
    return "2025-26"


@st.cache_data
def get_available_seasons(matches_df):
    """Get list of available seasons from matches data."""
    return sorted(matches_df["season"].unique().tolist())


@st.cache_data
def get_season_matches(matches_df, season):
    """Get matches for a specific season (cached)."""
    return matches_df[matches_df["season"] == season].copy()


@st.cache_data
def get_completed_matches(matches_df, season):
    """Get completed matches for a specific season (cached)."""
    matches = matches_df[matches_df["season"] == season]
    return matches[matches["match_status"] == "completed"].copy()


@st.cache_data
def get_upcoming_matches(matches_df, season):
    """Get upcoming matches for a specific season (cached)."""
    matches = matches_df[matches_df["season"] == season]
    return matches[matches["match_status"] == "upcoming"].copy()

