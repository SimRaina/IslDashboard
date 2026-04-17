# ⚽ Indian Super League Dashboard

A comprehensive Streamlit dashboard for exploring Indian Super League (ISL) tournament data for the 2025-26 season. View team standings, player statistics, match fixtures, and advanced analytics in one place.

## 📋 Features

### 1. **Overview** (1_Overview.py)
- Key metrics: Total matches, total goals, top scorer
- League standings widget (top 8 teams)
- Recent match results with dates, venues, and gameweek information

### 2. **Teams** (2_Teams.py)
- Team selector with detailed information
- Team logo placeholder and coach information
- Live team standings with position, points, and goal difference
- Squad information with player stats
- Home vs away match records

### 3. **Players** (3_Players.py)
- Player database with comprehensive filters
- Filter by team, position, and nationality
- Player statistics table with goals, assists, minutes played
- Top scorers visualization
- Top assist providers visualization

### 4. **Seasons** (4_Seasons.py)
- Season selector with season winner and top scorer info
- Historical season statistics
- Season comparison charts (matches per season, goals per season)
- All seasons data table

### 5. **Analytics** (5_Analytics.py)
- **Goals Analysis**: Team goals distribution, best defenses
- **Team Performance**: Home vs away records for all teams
- **Player Statistics**: Top scorers, assist providers, efficiency metrics
- **League Trends**: Goals per gameweek, matches per gameweek

### 6. **Standings** (6_Standings.py) ⭐ NEW
- Complete league table with sortable columns
- Position, matches played, wins, draws, losses
- Goals for, goals against, goal difference, points
- Home vs away performance breakdown for all teams
- Season statistics

### 7. **Leaders** (7_Leaders.py) ⭐ NEW
- **Top Scorers**: Ranked by goals with efficiency metrics
- **Top Assists**: Ranked by assists provided
- **Goals per 90**: Efficiency metric for scorers (min 500 mins)
- **Assists per 90**: Efficiency metric for playmakers (min 500 mins)
- **Player Comparison**: Multi-select comparison tool with visualizations

### 8. **Fixtures** (8_Fixtures.py) ⭐ NEW
- **Results Tab**: Completed matches grouped by gameweek
- **Upcoming Tab**: Upcoming matches with date and venue
- **Head-to-Head**: Match history between any two teams
- Interactive match calendar and fixture list

### 9. **Team Deep Dive** (9_Team_Deep_Dive.py) ⭐ NEW
- **Squad Tab**: Full player roster with detailed stats
- **Recent Form Tab**: Last 8 matches with form visualization
- **Statistics Tab**: Home/away splits, goals analysis, goal difference
- **Comparisons Tab**: Compare selected team vs other teams
- **H2H Tab**: Head-to-head history with stats

## 📂 Data Structure

### CSV Files

**teams.csv**
- `team_id`: Unique identifier
- `team_name`: Team name
- `city`: Home city
- `logo_path`: Path to team logo asset
- `founded_year`: Founding year
- `coach`: Current coach name

**players.csv**
- `player_id`: Unique identifier
- `name`: Player name
- `team`: Team name
- `position`: Playing position
- `goals`: Goals scored
- `assists`: Assists provided
- `minutes`: Total minutes played
- `shirt_number`: Jersey number
- `nationality`: Player nationality
- `dob`: Date of birth

**matches.csv**
- `match_id`: Unique identifier
- `season`: Season (e.g., "2025-26")
- `home_team`: Home team name
- `away_team`: Away team name
- `home_goals`: Goals by home team
- `away_goals`: Goals by away team
- `date`: Match date
- `venue`: Stadium name
- `gameweek`: Round number
- `match_status`: "completed" or "upcoming"

**seasons.csv**
- `season`: Season name
- `winner`: Season champion
- `top_scorer`: Top goal scorer
- `total_goals`: Total goals in season

## 🛠️ Utilities

### `utils/loader.py`
- `load_data()`: Load all CSV files with Streamlit caching
- `get_current_season()`: Get current season (2025-26)
- `get_available_seasons()`: Get list of available seasons

### `utils/standings.py`
- `calculate_standings()`: Generate league table from matches
- `get_team_stats()`: Get home/away statistics for a team

### `utils/stats.py`
- `get_top_scorers()`: Get ranked goal scorers
- `get_top_assists()`: Get ranked assist providers
- `get_efficiency_stats()`: Calculate goals per 90 minutes
- `get_assists_per_90()`: Calculate assists per 90 minutes
- `get_recent_form()`: Get team's recent matches
- `get_head_to_head()`: Get H2H stats between teams

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Streamlit
- Pandas
- Plotly

### Installation

```bash
pip install streamlit pandas plotly
```

### Running the Dashboard

```bash
streamlit run Home.py
```

The dashboard will open at `http://localhost:8501`

## 📊 Data Entry Guide

### Adding New Matches
Add rows to `data/matches.csv`:
```csv
match_id,season,home_team,away_team,home_goals,away_goals,date,venue,gameweek,match_status
```

### Adding New Players
Add rows to `data/players.csv`:
```csv
player_id,name,team,position,goals,assists,minutes,shirt_number,nationality,dob
```

### Adding New Teams
Add rows to `data/teams.csv`:
```csv
team_id,team_name,city,logo_path,founded_year,coach
```

## 🎯 Future Enhancements

- [ ] Live match updates (real-time data integration)
- [ ] Player photos and team logos
- [ ] Season archives with historical comparisons
- [ ] Player injury/suspension tracking
- [ ] Match predictor based on team form
- [ ] Multi-season player career statistics
- [ ] API integration for live data
- [ ] Advanced analytics (xG, possession %, etc.)

## 📁 Project Structure

```
IslDashboard/
├── Home.py                     # Main Streamlit app (entry point)
├── pages/
│   ├── 1_Overview.py          # Dashboard overview
│   ├── 2_Teams.py             # Team profiles
│   ├── 3_Players.py           # Player statistics
│   ├── 4_Seasons.py           # Season history
│   ├── 5_Analytics.py         # Advanced analytics
│   ├── 6_Standings.py         # League standings
│   ├── 7_Leaders.py           # Player leaderboards
│   ├── 8_Fixtures.py          # Match fixtures & results
│   └── 9_Team_Deep_Dive.py    # Team analysis
├── utils/
│   ├── loader.py              # Data loading & caching
│   ├── standings.py           # Standings calculations
│   └── stats.py               # Statistical functions
├── data/
│   ├── teams.csv
│   ├── players.csv
│   ├── matches.csv
│   └── seasons.csv
└── assets/
    ├── logos/                 # Team logos (placeholder)
    └── players/               # Player photos (placeholder)
```

## 🎨 Styling

The dashboard uses a dark theme with custom Streamlit CSS:
- Background: `#0e1117`
- Metric cards: `#1c1f26`
- Text: White

## 📝 Notes

- All dates should be in YYYY-MM-DD format
- Match status must be either "completed" or "upcoming"
- Empty cells in CSV should be left blank (not null)
- Team names must match exactly across all CSV files
- Minutes should be total minutes played in season

## 🤝 Contributing

To add new features or improve existing ones:

1. Create new utility functions in `utils/` folder
2. Add new pages in `pages/` folder following the naming convention
3. Update this README with feature descriptions
4. Test thoroughly before committing

## 📄 License

This project is open-source and available for educational purposes.

---

**Last Updated**: March 2026
**Current Season**: 2025-26
**Dashboard Version**: 1.0

