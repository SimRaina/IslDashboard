# 🔍 Scouting Report - Quick Start Guide

## ⚡ 60-Second Setup

1. **Run dashboard**: `streamlit run app.py`
2. **Navigate**: Click "Scouting Report" in sidebar
3. **Select**: Choose player and match
4. **Rate**: Score competencies 1-10
5. **Write**: Add scout name and notes
6. **Download**: Generate and save PDF

## 🎯 Step-by-Step

### Step 1: Select Player
```
Option A (Direct)
├─ Select "Player"
└─ Choose player name

Option B (Team-First)
├─ Select "Team & Player"
├─ Choose team
└─ Choose player from team
```

### Step 2: Choose Match
- Automatically shows recent completed matches
- Select from dropdown
- See match details (score, venue, date)

### Step 3: Competencies
- Appears based on player position
- Rate each 1-10 using slider
- 8 competencies per position

### Step 4: Scout Assessment
```
Fill in:
├─ Scout Name
├─ Key Strengths
├─ Areas for Improvement
├─ Overall Rating (1-10)
├─ Recommendation (dropdown)
└─ Detailed Comments
```

### Step 5: Generate PDF
- Click "Generate & Download PDF"
- File downloads automatically
- Named: `Scouting_Report_[Name]_[Date].pdf`

## 📊 Competencies by Position

| Position | Count | Examples |
|----------|-------|----------|
| Forward | 8 | Finishing, Positioning, Movement in Box |
| Winger | 8 | Pace, Dribbling, Crossing |
| Midfielder | 8 | Passing, Vision, Ball Control |
| Defender | 8 | Marking, Tackling, Positioning |

## 🎓 Best Practices

✅ **Do:**
- Scout immediately after match
- Use specific comments
- Rate honestly (1-10)
- Archive PDFs for comparison
- Update recommendations over time

❌ **Don't:**
- Scout from memory days later
- Use vague descriptions
- Skip any assessment fields
- Lose PDF files
- Use inconsistent rating scale

## 💾 PDF Contents

```
✅ Report Metadata
   ├─ Scout name
   ├─ Report date
   └─ Generation time

✅ Match Information
   ├─ Teams and score
   ├─ Venue
   ├─ Date
   └─ Gameweek

✅ Player Profile
   ├─ Name and position
   ├─ Team and nationality
   ├─ Shirt number
   └─ Career stats

✅ Competency Assessment
   ├─ Position-specific competencies
   ├─ Individual ratings (1-10)
   └─ Professional table format

✅ Evaluation
   ├─ Overall rating
   ├─ Recommendation
   ├─ Strengths
   ├─ Improvements
   └─ Detailed comments
```

## 🔗 Quick Links

**Dashboard**: `streamlit run app.py`

**Scouting Page**: Sidebar → "Scouting Report"

**Full Documentation**: See `SCOUTING_REPORT_COMPLETE.md`

## ❓ FAQ

**Q: Can I edit a downloaded PDF report?**
A: No, PDFs are locked. Create a new report to update.

**Q: What if player hasn't played in any match?**
A: Select a team first, only showing players with matches.

**Q: Can I compare multiple scout reports?**
A: Yes, download multiple PDFs and compare manually.

**Q: How do I rate the competencies?**
A: Use the sliders (1=Poor, 5=Average, 10=Excellent).

**Q: Can I change the recommendation?**
A: Yes, the dropdown has 4 options to choose from.

**Q: How long is a scouting report?**
A: Usually 1 page PDF with all details.

## 🎯 Recommendations Guide

| Option | Meaning | When to Use |
|--------|---------|-----------|
| **Target** | High interest player | Clear candidate for signing |
| **Monitor** | Watch for development | Potential, needs more time |
| **Pass** | Not suitable | Doesn't fit requirements |
| **Follow-up Required** | Needs more evaluation | Inconclusive, need more info |

## 📞 Support

- Check page displays correctly? ✅
- Can't generate PDF? Check reportlab installed
- Missing matches? Player's team needs matches
- Competencies wrong? Check player position

---

**Ready to scout?** 🔍 Navigate to "Scouting Report" now!

