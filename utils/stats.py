import pandas as pd
import streamlit as st

@st.cache_data
def get_top_scorers(players_df, limit=10):
    """Get top scorers ranked by goals."""
    return players_df.nlargest(limit, "goals")[["name", "team", "position", "goals", "minutes"]]


@st.cache_data
def get_top_assists(players_df, limit=10):
    """Get top assists providers ranked by assists."""
    return players_df.nlargest(limit, "assists")[["name", "team", "position", "assists", "minutes"]]


@st.cache_data
def get_efficiency_stats(players_df, limit=10):
    """Calculate goals per 90 minutes for players with sufficient minutes."""
    players = players_df.copy()
    
    # Filter players with at least 500 minutes
    players = players[players["minutes"] >= 500].copy()
    
    # Calculate goals per 90
    players["goals_per_90"] = (players["goals"] / (players["minutes"] / 90)).round(2)
    
    return players.nlargest(limit, "goals_per_90")[
        ["name", "team", "position", "goals", "minutes", "goals_per_90"]
    ]


@st.cache_data
def get_assists_per_90(players_df, limit=10):
    """Calculate assists per 90 minutes for players with sufficient minutes."""
    players = players_df.copy()
    
    # Filter players with at least 500 minutes
    players = players[players["minutes"] >= 500].copy()
    
    # Calculate assists per 90
    players["assists_per_90"] = (players["assists"] / (players["minutes"] / 90)).round(2)
    
    return players.nlargest(limit, "assists_per_90")[
        ["name", "team", "position", "assists", "minutes", "assists_per_90"]
    ]


@st.cache_data
def get_recent_form(matches_df, team_name, limit=5):
    """Get recent match results for a team."""
    matches = matches_df[matches_df["match_status"] == "completed"].copy()
    
    home_matches = matches[matches["home_team"] == team_name].copy()
    away_matches = matches[matches["away_team"] == team_name].copy()
    
    # Prepare home matches
    home_matches["opponent"] = home_matches["away_team"]
    home_matches["for"] = home_matches["home_goals"]
    home_matches["against"] = home_matches["away_goals"]
    home_matches["location"] = "Home"
    
    # Prepare away matches
    away_matches["opponent"] = away_matches["home_team"]
    away_matches["for"] = away_matches["away_goals"]
    away_matches["against"] = away_matches["home_goals"]
    away_matches["location"] = "Away"
    
    # Combine and sort by date
    recent = pd.concat([home_matches, away_matches], ignore_index=True)
    recent = recent.sort_values("date", ascending=False).head(limit)
    
    # Determine result
    recent["result"] = recent.apply(
        lambda row: "W" if row["for"] > row["against"] else ("D" if row["for"] == row["against"] else "L"),
        axis=1
    )
    
    return recent[["date", "opponent", "location", "for", "against", "result"]]


@st.cache_data
def get_head_to_head(matches_df, team1, team2):
    """Get head-to-head stats between two teams."""
    matches = matches_df[matches_df["match_status"] == "completed"].copy()
    
    h2h = matches[
        ((matches["home_team"] == team1) & (matches["away_team"] == team2)) |
        ((matches["home_team"] == team2) & (matches["away_team"] == team1))
    ].copy()
    
    if len(h2h) == 0:
        return None, "No matches played between these teams yet."
    
    team1_wins = 0
    team2_wins = 0
    draws = 0
    team1_goals = 0
    team2_goals = 0
    
    for _, match in h2h.iterrows():
        if match["home_team"] == team1:
            team1_goals += match["home_goals"]
            team2_goals += match["away_goals"]
            if match["home_goals"] > match["away_goals"]:
                team1_wins += 1
            elif match["home_goals"] < match["away_goals"]:
                team2_wins += 1
            else:
                draws += 1
        else:
            team1_goals += match["away_goals"]
            team2_goals += match["home_goals"]
            if match["away_goals"] > match["home_goals"]:
                team1_wins += 1
            elif match["away_goals"] < match["home_goals"]:
                team2_wins += 1
            else:
                draws += 1
    
    stats = {
        "matches_played": len(h2h),
        f"{team1}_wins": team1_wins,
        f"{team2}_wins": team2_wins,
        "draws": draws,
        f"{team1}_goals": team1_goals,
        f"{team2}_goals": team2_goals,
    }
    
    return h2h.sort_values("date", ascending=False), stats


@st.cache_data
def get_goalkeeper_stats(players_df, matches_df, teams_df):
    """Calculate goalkeeper stats including goals conceded and clean sheets."""
    goalkeepers = players_df[players_df["position"] == "Goalkeeper"].copy()
    
    # Get completed matches
    completed_matches = matches_df[matches_df["match_status"] == "completed"]
    
    gk_stats = []
    
    for _, gk in goalkeepers.iterrows():
        gk_team = gk["team"]
        
        # Get all matches where this goalkeeper's team played
        home_matches = completed_matches[completed_matches["home_team"] == gk_team]
        away_matches = completed_matches[completed_matches["away_team"] == gk_team]
        
        total_goals_conceded = 0
        clean_sheets = 0
        matches_played = 0
        
        # Home matches
        for _, match in home_matches.iterrows():
            goals_conceded = match["away_goals"]
            total_goals_conceded += goals_conceded
            if goals_conceded == 0:
                clean_sheets += 1
            matches_played += 1
        
        # Away matches
        for _, match in away_matches.iterrows():
            goals_conceded = match["home_goals"]
            total_goals_conceded += goals_conceded
            if goals_conceded == 0:
                clean_sheets += 1
            matches_played += 1
        
        if matches_played > 0:
            avg_goals_conceded = round(total_goals_conceded / matches_played, 2)
            gk_stats.append({
                "name": gk["name"],
                "team": gk_team,
                "Matches": matches_played,
                "Goals Conceded": total_goals_conceded,
                "Clean Sheets": clean_sheets,
                "Avg Goals/Match": avg_goals_conceded
            })
    
    return pd.DataFrame(gk_stats) if gk_stats else pd.DataFrame()
