import pandas as pd
import streamlit as st

@st.cache_data
def calculate_standings(matches_df, teams_df, season=None):
    """
    Calculate league standings from matches data.
    
    Parameters:
    - matches_df: DataFrame with matches
    - teams_df: DataFrame with teams
    - season: Specific season to filter, if None use all
    
    Returns:
    - DataFrame with standings (position, team, P, W, D, L, GF, GA, GD, Pts)
    """
    if season:
        matches = matches_df[matches_df["season"] == season].copy()
    else:
        matches = matches_df.copy()
    
    # Filter only completed matches
    matches = matches[matches["match_status"] == "completed"]
    
    # Initialize standings dictionary
    standings_dict = {}
    
    for _, team in teams_df.iterrows():
        team_name = team["team_name"]
        standings_dict[team_name] = {
            "team_id": team["team_id"],
            "team_name": team_name,
            "city": team["city"],
            "matches_played": 0,
            "wins": 0,
            "draws": 0,
            "losses": 0,
            "goals_for": 0,
            "goals_against": 0,
            "points": 0
        }
    
    # Process each match
    for _, match in matches.iterrows():
        home_team = match["home_team"]
        away_team = match["away_team"]
        home_goals = match["home_goals"]
        away_goals = match["away_goals"]
        
        if home_team in standings_dict and away_team in standings_dict:
            # Update home team
            standings_dict[home_team]["matches_played"] += 1
            standings_dict[home_team]["goals_for"] += home_goals
            standings_dict[home_team]["goals_against"] += away_goals
            
            # Update away team
            standings_dict[away_team]["matches_played"] += 1
            standings_dict[away_team]["goals_for"] += away_goals
            standings_dict[away_team]["goals_against"] += home_goals
            
            # Determine result
            if home_goals > away_goals:
                standings_dict[home_team]["wins"] += 1
                standings_dict[home_team]["points"] += 3
                standings_dict[away_team]["losses"] += 1
            elif home_goals < away_goals:
                standings_dict[away_team]["wins"] += 1
                standings_dict[away_team]["points"] += 3
                standings_dict[home_team]["losses"] += 1
            else:
                standings_dict[home_team]["draws"] += 1
                standings_dict[home_team]["points"] += 1
                standings_dict[away_team]["draws"] += 1
                standings_dict[away_team]["points"] += 1
    
    # Convert to DataFrame
    standings_list = list(standings_dict.values())
    standings_df = pd.DataFrame(standings_list)
    
    # Calculate goal difference
    standings_df["goal_difference"] = standings_df["goals_for"] - standings_df["goals_against"]
    
    # Sort by points (descending), then goal difference (descending), then goals for (descending)
    standings_df = standings_df.sort_values(
        by=["points", "goal_difference", "goals_for"],
        ascending=[False, False, False]
    ).reset_index(drop=True)
    
    # Add position
    standings_df["position"] = range(1, len(standings_df) + 1)
    
    # Reorder columns
    column_order = [
        "position", "team_name", "city", "matches_played", "wins", "draws", "losses",
        "goals_for", "goals_against", "goal_difference", "points"
    ]
    
    return standings_df[column_order]


@st.cache_data
def get_team_stats(matches_df, teams_df, team_name, season=None):
    """Get detailed stats for a specific team."""
    if season:
        matches = matches_df[matches_df["season"] == season].copy()
    else:
        matches = matches_df.copy()
    
    matches = matches[matches["match_status"] == "completed"]
    
    home_matches = matches[matches["home_team"] == team_name]
    away_matches = matches[matches["away_team"] == team_name]
    
    home_wins = len(home_matches[home_matches["home_goals"] > home_matches["away_goals"]])
    away_wins = len(away_matches[away_matches["away_goals"] > away_matches["home_goals"]])
    
    home_losses = len(home_matches[home_matches["home_goals"] < home_matches["away_goals"]])
    away_losses = len(away_matches[away_matches["away_goals"] < away_matches["home_goals"]])
    
    home_draws = len(home_matches[home_matches["home_goals"] == home_matches["away_goals"]])
    away_draws = len(away_matches[away_matches["away_goals"] == away_matches["home_goals"]])
    
    return {
        "home_wins": home_wins,
        "away_wins": away_wins,
        "home_losses": home_losses,
        "away_losses": away_losses,
        "home_draws": home_draws,
        "away_draws": away_draws,
        "total_wins": home_wins + away_wins,
        "total_losses": home_losses + away_losses,
        "total_draws": home_draws + away_draws,
    }

