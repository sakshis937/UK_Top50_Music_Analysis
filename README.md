# 🎵 United Kingdom Top 50 Music Analysis

## 📌 Project Overview

This project analyzes the structure of the UK Top 50 music playlist to understand artist dominance, collaboration trends, explicit content preferences, and release strategies in the UK music market.

The analysis provides insights for Atlantic Recording Corporation to support:
- Artist signing strategy
- UK-specific marketing decisions
- Release format optimization
- Cross-border promotion planning

---

## 📂 Dataset Description

The dataset contains daily snapshots of the UK Top 50 playlist.

### Features

| Column | Description |
|--------|-------------|
| date | Playlist snapshot date |
| position | Rank position (1–50) |
| song | Song title |
| artist | Artist name(s) |
| popularity | Popularity score |
| duration_ms | Track duration in milliseconds |
| album_type | Single or Album |
| total_tracks | Number of tracks in album |
| is_explicit | Explicit content flag |
| album_cover_url | Album artwork URL |

---

## 📊 Key Performance Indicators (KPIs)

- Artist Concentration Index
- Unique Artist Count
- Collaboration Ratio
- Explicit Content Share
- Single vs Album Ratio
- Diversity Score
- Content Variety Index
- Top 5 Artist Share

---

## 🔬 Methodology

### 1. Data Cleaning
- Missing value handling
- Duplicate removal
- Artist name standardization
- Date conversion

### 2. Artist Analysis
- Artist dominance
- Diversity measurement
- Concentration index

### 3. Collaboration Analysis
- Solo vs collaborative tracks
- Collaboration ratio
- Artist network graph

### 4. Content Analysis
- Explicit vs clean content
- Rank-based analysis

### 5. Album Strategy Analysis
- Single vs album comparison
- Album size impact

### 6. Duration Analysis
- Track duration distribution
- Duration vs popularity

---

## 💡 Key Insights

- UK charts show strong domestic artist representation.
- Collaborations increase chart visibility.
- Singles dominate playlist presence.
- Explicit content performs differently across rank groups.
- Artist concentration reveals market competitiveness.

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/sakshis937/UK_Top50_Music_Analysis.git
cd UK_Top50_Music_Analysis
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run Streamlit app:

```bash
streamlit run app.py
```

---

## 🚀 Streamlit Deployment

Deploy on Streamlit Cloud:

1. Push project to GitHub
2. Visit https://share.streamlit.io
3. Connect GitHub repository
4. Select `app.py`
5. Click Deploy

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- NetworkX
- Streamlit

---

## 👩‍💻 Author

**Sakshi Sharma**

GitHub: https://github.com/sakshis937
