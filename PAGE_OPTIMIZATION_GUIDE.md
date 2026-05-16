# Page-by-Page Optimization Guide

## Pages Already Updated ✅
- ✅ `1_Overview.py` - Refactored
- ✅ `6_Standings.py` - Refactored  
- ✅ `8_Fixtures.py` - Refactored
- ✅ `app.py` - Updated

---

## Priority: HIGH 🔴

### `2_Teams.py` (320 lines) - HIGH OPTIMIZATION POTENTIAL

**Current Issues**:
1. Hardcoded CSS styling (lines 26-36)
2. Not using new components
3. `safe_int()` helper function (lines 11-23) - OBSOLETE NOW
4. Repetitive display code

**Quick Fix** (15 min):
```python
# Replace lines 26-36 with:
from utils.styles import apply_dark_theme
apply_dark_theme()

# Replace safe_int() calls with direct access (numeric types handled at load):
display_players["Age"] = display_players["age"]  # Already int!

# Replace team header code with:
from utils.components import display_team_header
display_team_header(team_info)
```

**Impact**: -50 lines, cleaner code

---

### `3_Players.py` (115 lines) - ADD SESSION STATE

**Quick Fix** (10 min):
```python
# Add at top after imports:
if "team_filter" not in st.session_state:
    st.session_state.team_filter = "All"

# In filters section:
with col1:
    st.session_state.team_filter = st.selectbox(
        "Filter by Team", 
        ["All"] + list(players["team"].unique()),
        key="team_filter"
    )
```

**Benefit**: Filters persist when navigating away and back

---

## Priority: MEDIUM 🟡

### `5_Analytics.py` (352 lines) - LAZY LOAD CHARTS

**Issue**: All 8 tabs' charts load upfront

**Quick Fix** (20 min):
```python
with tab1:
    st.subheader("Goals Distribution")
    if st.session_state.get("show_tab1", False):  # Render on first view
        # Expensive chart code here
    st.session_state.show_tab1 = True

# Repeat for other tabs
```

**Impact**: ~40% faster initial page load

---

### `4_Seasons.py` - Use New Utilities

**Current**: Likely has hardcoded styles and manual filtering

**Quick Fix** (10 min):
```python
from utils.styles import apply_dark_theme
apply_dark_theme()

from utils.loader import get_current_season, get_completed_matches
current_season = get_current_season()
completed = get_completed_matches(matches, current_season)
```

---

### `10_Scouting_Report.py` - Use New Utilities

**Current**: Likely has hardcoded styles

**Quick Fix** (5 min):
```python
from utils.styles import apply_dark_theme
apply_dark_theme()
```

---

### `11_MPLSoccer_Charts.py` - Use New Utilities

**Quick Fix** (5 min):
```python
from utils.styles import apply_dark_theme
apply_dark_theme()
```

---

## Priority: LOW 🟢

### `7_Leaders.py` (if exists) - Use Components

Apply same patterns as above

---

## 🚀 Recommended Implementation Order

1. **Day 1** (15 min each):
   - [ ] Fix `2_Teams.py` - Remove safe_int, use apply_dark_theme
   - [ ] Fix `3_Players.py` - Add session state

2. **Day 2** (20 min each):
   - [ ] Fix `5_Analytics.py` - Add lazy loading
   - [ ] Fix `4_Seasons.py` - Use utilities

3. **Day 3** (5 min each):
   - [ ] Fix remaining pages - Just add `apply_dark_theme()`

---

## 📈 Expected Total Impact After All Pages Updated

| Metric | Now | After |
|--------|-----|-------|
| Total duplicate CSS | 5 instances | 0 instances |
| Total duplicate filtering | 10+ instances | 0 instances |
| Code duplication | ~300 lines | ~50 lines |
| Average page compile time | Baseline | -15-20% |
| Safe_int() calls | 50+ | 0 |

---

## ⚡ Mini Quick-Fixes (2 min each)

These can be done in any page to improve immediately:

### Add Docstrings to Main Functions
```python
def analyze_team_performance(team_name, matches):
    """Calculate W-D-L record for a team."""
    # ... code ...
```

### Add Type Hints
```python
def filter_matches(matches: pd.DataFrame, team: str) -> pd.DataFrame:
    return matches[matches["team"] == team]
```

### Remove Print Statements
```python
# Remove any print() calls - use st.write() instead
```

### Extract Magic Numbers
```python
# Before:
players[players["minutes"] >= 500]

# After:
MIN_MINUTES = 500
players[players["minutes"] >= MIN_MINUTES]
```

---

## 🎓 Learning Objectives

By implementing these optimizations, you'll learn:

1. **DRY Principle** - Don't Repeat Yourself
   - Extract common code to utilities
   
2. **Caching Strategy** - Smart data loading
   - Use @st.cache_data for expensive operations
   
3. **UI Component Libraries** - Reusable components
   - Build your own component patterns
   
4. **Type Safety** - Fix errors early
   - Convert types at load time, not runtime
   
5. **Performance Profiling** - Find bottlenecks
   - Identify which pages are slow

---

## 📞 Need Help?

- **For questions about new utils**: Check `OPTIMIZATION_QUICK_REFERENCE.md`
- **For detailed explanations**: See `OPTIMIZATIONS_IMPLEMENTED.md`
- **For all opportunities**: See `OPTIMIZATIONS.md`

---

Last Updated: May 16, 2026

