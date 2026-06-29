🎵 UK Top 50 Music Analysis

> A data analytics web application that analyzes the structure of Spotify's UK Top 50 playlist — built to support smarter artist signing, release strategy, and marketing decisions for Atlantic Recording Corporation.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io)
![Python](https://img.shields.io/badge/Python-3.10-blue?style=flat-square)
![Analysis](https://img.shields.io/badge/Analysis-Spotify%20UK%20Top%2050-green?style=flat-square)
![UI](https://img.shields.io/badge/UI-Streamlit-red?style=flat-square)
![Type](https://img.shields.io/badge/Project-Individual%20Academic%20Project-lightgrey?style=flat-square)

🔗 **Live Demo:** https://uktop50musicanalysis-twzbytr8e7hiyt4blqjtpf.streamlit.app/


---

## 📌 Problem Statement

Record labels struggle to make data-driven decisions about which artists to sign, what format to release music in, and how to target the UK market specifically. Manual chart tracking misses patterns in collaboration trends, explicit content performance, and release timing.

This project analyzes **daily snapshots of the UK Spotify Top 50 playlist** and presents insights through an **interactive Streamlit dashboard** — designed for music industry executives and A&R teams at Atlantic Recording Corporation.

---

## 👩‍💻 My Contribution — Sakshi Sharma

This is an **individual academic project**. I handled the full pipeline end-to-end:

- **Data pipeline** — Collected, cleaned, and standardized daily UK Top 50 snapshot data including artist name normalization and date parsing
- **Streamlit dashboard** — Designed and built the complete frontend in `app.py` including sidebar filters, KPI cards, and chart sections
- **Artist analysis** — Built top artist bar chart, diversity score, and artist concentration index
- **Collaboration & content analysis** — Explicit vs clean donut chart, album type breakdown, and duration vs popularity scatter
- **KPI system** — 8 business KPIs tracking market competitiveness, content mix, and release format trends

---

## 📊 Project Stats

| Metric | Value |
|--------|-------|
| Playlist | Spotify UK Top 50 |
| Data Type | Daily chart snapshots |
| Chart Positions | 1 – 50 |
| KPIs Tracked | 8 |
| Visualizations | 5 interactive charts |
| Client | Atlantic Recording Corporation |

---

## 🖥️ Dashboard Sections

| Section | What It Shows |
|---------|--------------|
| 🎤 Artist Performance | Top 10 artists by chart appearances + popularity distribution |
| 📊 Content & Format | Explicit vs clean split + Single vs Album breakdown |
| ⏱️ Duration Analysis | Song length vs popularity scatter plot |
| 🎵 Top Songs Table | Filterable full dataset sorted by popularity |
| 🖼️ Album Covers | Visual preview of top charting tracks |

---

## 📈 Key Performance Indicators (KPIs)

| KPI | What It Measures |
|-----|-----------------|
| Artist Concentration Index | How much a few artists dominate the chart |
| Unique Artist Count | Total distinct artists on the playlist |
| Collaboration Ratio | % of tracks with featured artists |
| Explicit Content Share | % of explicit vs clean songs |
| Single vs Album Ratio | Release format distribution |
| Diversity Score | Overall chart variety index |
| Content Variety Index | Mix of content types across the chart |
| Top 5 Artist Share | Top 5 artists' combined % of total chart |

---

## 🛠️ Tech Stack

| Layer | Tools |
|-------|-------|
| Language | Python 3.10 |
| Data | Pandas, NumPy |
| Visualisation | Plotly, Matplotlib, Seaborn |
| Network Graph | NetworkX |
| Word Cloud | WordCloud |
| Dashboard | Streamlit |

---

## 📂 Input Features

| Column | Type | Description |
|--------|------|-------------|
| `date` | `datetime` | Playlist snapshot date |
| `position` | `int` | Chart rank position (1–50) |
| `song` | `str` | Song title |
| `artist` | `str` | Artist name(s) |
| `popularity` | `int` | Spotify popularity score (0–100) |
| `duration_ms` | `int` | Track duration in milliseconds |
| `album_type` | `str` | Single or Album |
| `total_tracks` | `int` | Number of tracks in the release |
| `is_explicit` | `bool` | Explicit content flag |
| `album_cover_url` | `str` | Album artwork URL |

---

## 📁 Project Structure

```
UK_Top50_Music_Analysis/
│
├── Streamlit_app/
│   └── app.py                           # Main Streamlit dashboard
│
├── Dataset/
│   └── cleaned_atlantic_uk_top50.csv    # Cleaned UK Top 50 playlist data
│
├── requirements.txt                     # Python dependencies
└── README.md                            # Project documentation
```

---

## 🚀 How to Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/sakshis937/UK_Top50_Music_Analysis.git
cd UK_Top50_Music_Analysis

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch the app
streamlit run Streamlit_app/app.py
```

---

## 💡 Key Insights

- 🇬🇧 UK charts show **strong domestic artist representation**, reflecting local listener preferences
- 🤝 **Collaborations significantly increase chart visibility** — featured tracks outperform solo releases
- 💿 **Singles dominate** playlist presence, indicating a shift toward shorter, accessible music formats
- 🔞 **Explicit content performs differently** across rank groups, reflecting UK cultural nuances
- 📊 **Artist concentration metrics** reveal the competitiveness and openness of the UK music market

---

## 💡 Key Learnings

- Chart data contains rich signals about listener behavior that go beyond just popularity scores
- Sidebar filters dramatically improve usability when presenting data to non-technical stakeholders
- Plotly's interactivity adds significant value over static Matplotlib charts for business dashboards

---

## 👩‍💻 Author

**Sakshi Sharma**
GitHub: [sakshis937](https://github.com/sakshis937)

---
