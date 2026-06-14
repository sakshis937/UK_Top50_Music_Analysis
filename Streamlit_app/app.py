import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(
    page_title="UK Top 50 Music Analysis",
    page_icon="🎵",
    layout="wide"
)

st.title("🎵 UK Top 50 Music Analysis Dashboard")
st.markdown("Analyze Spotify UK Top 50 Playlist Data")

# ---------------------------
# Load Data
# ---------------------------
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("Dataset/Atlantic_United_Kingdom (1).csv")
        return df
    except FileNotFoundError:
        st.error("Dataset file not found. Please check the file path.")
        return pd.DataFrame()

df = load_data()

if df.empty:
    st.stop()

# ---------------------------
# Data Cleaning
# ---------------------------
df.columns = df.columns.str.lower()

if 'date' in df.columns:
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

if 'duration_ms' in df.columns:
    df['duration_min'] = round(df['duration_ms'] / 60000, 2)

# ---------------------------
# Sidebar Filters
# ---------------------------
st.sidebar.header("Filters")

artist = st.sidebar.selectbox(
    "Select Artist",
    ["All"] + sorted(df['artist'].dropna().unique().tolist())
)

explicit = st.sidebar.selectbox(
    "Explicit Content",
    ["All", True, False]
)

filtered_df = df.copy()

if artist != "All":
    filtered_df = filtered_df[filtered_df['artist'] == artist]

if explicit != "All":
    filtered_df = filtered_df[
        filtered_df['is_explicit'] == explicit
    ]

# ---------------------------
# KPI Cards
# ---------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Songs", len(filtered_df))
col2.metric("Unique Artists", filtered_df['artist'].nunique())
col3.metric(
    "Avg Popularity",
    round(filtered_df['popularity'].mean(), 2)
)
col4.metric(
    "Avg Duration (min)",
    round(filtered_df['duration_min'].mean(), 2)
)

st.divider()

# ---------------------------
# Top Artists
# ---------------------------
st.subheader("🎤 Top Artists")

artist_count = (
    filtered_df['artist']
    .value_counts()
    .head(10)
    .reset_index()
)

artist_count.columns = ['artist', 'count']

fig1 = px.bar(
    artist_count,
    x='artist',
    y='count',
    title="Top 10 Artists"
)

st.plotly_chart(fig1, use_container_width=True)

# ---------------------------
# Popularity Distribution
# ---------------------------
st.subheader("⭐ Popularity Distribution")

fig2 = px.histogram(
    filtered_df,
    x='popularity',
    nbins=20,
    title="Popularity Distribution"
)

st.plotly_chart(fig2, use_container_width=True)

# ---------------------------
# Explicit Content Analysis
# ---------------------------
st.subheader("🔞 Explicit Content Analysis")

explicit_df = (
    filtered_df['is_explicit']
    .value_counts()
    .reset_index()
)

explicit_df.columns = ['Explicit', 'Count']

fig3 = px.pie(
    explicit_df,
    names='Explicit',
    values='Count',
    hole=0.4
)

st.plotly_chart(fig3, use_container_width=True)

# ---------------------------
# Album Type Analysis
# ---------------------------
st.subheader("💿 Album Type")

album_df = (
    filtered_df['album_type']
    .value_counts()
    .reset_index()
)

album_df.columns = ['Album Type', 'Count']

fig4 = px.bar(
    album_df,
    x='Album Type',
    y='Count'
)

st.plotly_chart(fig4, use_container_width=True)

# ---------------------------
# Top Songs Table
# ---------------------------
st.subheader("🎵 Top Songs")

display_cols = [
    'song',
    'artist',
    'popularity',
    'duration_min',
    'album_type'
]

available_cols = [
    col for col in display_cols
    if col in filtered_df.columns
]

st.dataframe(
    filtered_df[available_cols],
    use_container_width=True
)

# ---------------------------
# Album Covers
# ---------------------------
st.subheader("🖼 Album Covers")

if 'album_cover_url' in filtered_df.columns:
    sample = filtered_df.head(5)

    cols = st.columns(5)

    for i, (_, row) in enumerate(sample.iterrows()):
        with cols[i]:
            st.image(
                row['album_cover_url'],
                width=150
            )
            st.caption(row['song'])

# ---------------------------
# Footer
# ---------------------------
st.markdown("---")
st.markdown(
    "Developed using Streamlit | UK Top 50 Music Analysis"
)