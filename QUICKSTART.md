# 🚀 Quick Start Guide - ISL Dashboard

## Installation & Setup (30 seconds)

### Step 1: Install Dependencies
```bash
pip install streamlit pandas plotly
```

### Step 2: Run the Dashboard
```bash
cd C:\Users\simra\PycharmProjects\IslDashboard
streamlit run app.py
```

### Step 3: Open in Browser
The dashboard will automatically open at `http://localhost:8501`

---

## 📱 Dashboard Navigation

The dashboard has 9 pages accessible from the left sidebar:

| Page | Purpose | Key Info |
|------|---------|----------|
| **1️⃣ Overview** | Dashboard summary | League standings, top scorer, recent matches |
| **2️⃣ Teams** | Team profiles | Squad, coach, home/away record |
| **3️⃣ Players** | Player stats | Top scorers, filters, visualizations |
| **4️⃣ Seasons** | Season data | Historical stats, season comparison |
| **5️⃣ Analytics** | Advanced stats | Goals analysis, team performance, trends |
| **6️⃣ Standings** | League table | Full standings, home/away splits |
| **7️⃣ Leaders** | Player rankings | Top scorers, assists, efficiency metrics |
| **8️⃣ Fixtures** | Match schedule | Results, upcoming matches, H2H |
| **9️⃣ Team Deep Dive** | Team analysis | Squad, form, comparisons, H2H |

---

## 💡 Quick Tips

### View League Standings
1. Go to **Standings** page
2. Select a season (default: 2025-26)
3. See full table with all metrics
4. Scroll down to see home/away breakdown

### Find Top Scorers
1. Go to **Leaders** page
2. Click "Top Scorers" tab
3. Sort by goals or view different metrics
4. Use "Player Comparison" tab to compare multiple players

### Check Upcoming Matches
1. Go to **Fixtures** page
2. Click "Upcoming Fixtures" tab
3. Select a gameweek
4. View all upcoming matches with dates

### Analyze a Specific Team
1. Go to **Team Deep Dive** page
2. Select a team from dropdown
3. View squad, recent form, stats
4. Compare with another team using "Comparisons" tab

### See Recent Results
1. Go to **Fixtures** page
2. Click "Results" tab
3. Select a gameweek
4. View all completed matches

---

## 📊 Current Season Data

**Season**: 2025-26

**Teams**: 14 ISL teams
- Mumbai City FC, Bengaluru FC, Mohun Bagan Super Giants, Goa FC
- ATK Mohun Bagan, FC Kochi, Odisha FC, Kerala Blasters FC
- Chennayin FC, Punjab FC, Jamshedpur FC, North East United
- Mohammedan SC, East Bengal FC

**Players**: 12 sample players (expand by adding to data/players.csv)

**Matches**: 14 matches (10 completed, 4 upcoming)

---

## 🔄 Adding New Data

### Add a New Match
1. Open `data/matches.csv`
2. Add a new row with match details
3. Dashboard updates automatically on refresh

### Add a Player
1. Open `data/players.csv`
2. Add a new row with player info
3. Player appears in all relevant sections

### Add a Team
1. Open `data/teams.csv`
2. Add a new row with team details
3. Team appears in team selector

---

## 🎯 Keyboard Shortcuts

| Action | Shortcut |
|--------|----------|
| Refresh | F5 or Ctrl+Shift+R |
| Clear cache | Ctrl+Shift+C |
| Switch page | Click in sidebar |
| Filter data | Use dropdown selectors |

---

## ⚠️ Common Issues & Solutions

### "No module named 'streamlit'"
**Solution**: Run `pip install streamlit pandas plotly`

### Dashboard doesn't update after data change
**Solution**: Press Ctrl+Shift+R to refresh and clear cache

### Charts not displaying
**Solution**: Ensure plotly is installed: `pip install plotly`

### Team not appearing in selectors
**Solution**: Check that team name matches exactly in teams.csv

---

## 📝 Data Format Requirements

When adding data, follow these formats:

### Date Format
- Must be: `YYYY-MM-DD` (e.g., 2025-11-15)

### Match Status
- Only: `completed` or `upcoming`

### Team Names
- Must match exactly across all CSV files
- Case-sensitive!

### Numbers
- Goals, assists, minutes: Integer values only
- No quotes or special characters

---

## 🎨 Customization

### Change Dashboard Title
Edit `app.py` line 6:
```python
st.title("⚽ Your Custom Title")
```

### Change Theme Colors
Edit the CSS section in any page (usually at top):
```python
st.markdown("""
    <style>
    body {
        background-color: #your-color;
    }
    </style>
""", unsafe_allow_html=True)
```

### Add Team Logos
1. Place PNG images in `assets/logos/` folder
2. Update `logo_path` in teams.csv
3. Images will display automatically

---

## 📞 Support

For detailed information, see:
- **README.md** - Complete feature documentation
- **IMPLEMENTATION_SUMMARY.md** - What was added
- Page comments in code for specific implementations

---

## ✨ Pro Tips

1. **Use Season Filter**: Select different seasons on multiple pages for historical comparison
2. **Export Data**: Click on dataframes to copy or export them
3. **Compare Players**: Use Players > Comparison tab to multi-select players
4. **H2H History**: Check Head-to-Head sections to see team matchups
5. **Recent Form**: Use Team Deep Dive > Recent Form for last 8 matches

---

**Last Updated**: March 2026
**Version**: 1.0
**Status**: ✅ Ready to Use

