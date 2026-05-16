# Quick Optimization Reference

## 🎨 Apply Theme to Any Page
```python
from utils.styles import apply_dark_theme
apply_dark_theme()
```

## 📊 Get Season Data
```python
from utils.loader import get_current_season, get_completed_matches, get_upcoming_matches

current_season = get_current_season()
completed = get_completed_matches(matches, current_season)
upcoming = get_upcoming_matches(matches, current_season)
```

## 🏟️ Display Team Header
```python
from utils.components import display_team_header
display_team_header(team_info)
```

## ⚽ Display a Match
```python
from utils.components import display_match_result
for _, match in matches.iterrows():
    display_match_result(match)  # Shows: Home 2 - 1 Away | Date | GW | Venue
```

## 📋 Display Matches Table
```python
from utils.components import display_matches_table
display_matches_table(completed_matches, sort_by="date", ascending=False)
```

## 📈 Display Metrics Grid
```python
from utils.components import display_key_metrics
display_key_metrics({
    "Total Matches": 20,
    "Total Goals": 45,
    "Avg Goals/Match": 2.25
})
```

## 🎯 Theme Colors
```python
from utils.styles import THEME
bg_color = THEME["bg_dark"]        # #0e1117
card_color = THEME["bg_card"]      # #1c1f26
accent = THEME["accent_green"]     # #228B22
```

## ✅ Checklist When Adding New Page

- [ ] Import `apply_dark_theme` and call it first
- [ ] Use `get_completed_matches()` instead of manual filtering
- [ ] Use `display_match_result()` for match display
- [ ] Use `display_team_header()` for team info
- [ ] Import from `utils/` not duplicate code
- [ ] Test with `python -m py_compile pages/your_page.py`

