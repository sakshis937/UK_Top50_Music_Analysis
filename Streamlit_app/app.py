import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(
    page_title="UK Top 50 Music Analysis",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------
# Custom CSS
# ---------------------------
st.markdown("""
<style>
    /* Import Google Font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    /* Global */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* Background */
    .stApp {
        background: linear-gradient(135deg, #0d0d1a 0%, #111827 50%, #0d1117 100%);
        color: #e2e8f0;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #111827 0%, #0f172a 100%);
        border-right: 1px solid #1e293b;
    }
    [data-testid="stSidebar"] .stSelectbox label,
    [data-testid="stSidebar"] .stSlider label,
    [data-testid="stSidebar"] h1, h2, h3 {
        color: #94a3b8 !important;
        font-size: 12px !important;
        text-transform: uppercase;
        letter-spacing: 0.08em;
    }

    /* Hero Header */
    .hero-header {
        background: linear-gradient(135deg, #1e1b4b 0%, #312e81 50%, #4c1d95 100%);
        border-radius: 16px;
        padding: 36px 40px;
        margin-bottom: 28px;
        border: 1px solid #4338ca33;
        position: relative;
        overflow: hidden;
    }
    .hero-header::before {
        content: "🎵";
        position: absolute;
        right: 40px;
        top: 50%;
        transform: translateY(-50%);
        font-size: 80px;
        opacity: 0.15;
    }
    .hero-title {
        font-size: 32px;
        font-weight: 700;
        background: linear-gradient(90deg, #a78bfa, #818cf8, #60a5fa);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0 0 8px 0;
        letter-spacing: -0.5px;
    }
    .hero-sub {
        font-size: 15px;
        color: #94a3b8;
        margin: 0;
        font-weight: 400;
    }
    .hero-tag {
        display: inline-block;
        background: #4338ca44;
        border: 1px solid #6366f155;
        color: #a5b4fc;
        font-size: 11px;
        font-weight: 600;
        padding: 4px 10px;
        border-radius: 20px;
        margin-top: 14px;
        letter-spacing: 0.06em;
        text-transform: uppercase;
    }

    /* KPI Cards */
    .kpi-card {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        border: 1px solid #334155;
        border-radius: 14px;
        padding: 20px 22px;
        text-align: center;
        transition: border-color 0.2s;
    }
    .kpi-card:hover {
        border-color: #6366f1;
    }
    .kpi-icon {
        font-size: 22px;
        margin-bottom: 8px;
    }
    .kpi-value {
        font-size: 28px;
        font-weight: 700;
        color: #a78bfa;
        line-height: 1;
        margin-bottom: 6px;
    }
    .kpi-label {
        font-size: 12px;
        color: #64748b;
        text-transform: uppercase;
        letter-spacing: 0.07em;
        font-weight: 500;
    }

    /* Section Headers */
    .section-header {
        display: flex;
        align-items: center;
        gap: 10px;
        margin: 32px 0 16px 0;
        padding-bottom: 12px;
        border-bottom: 1px solid #1e293b;
    }
    .section-icon {
        font-size: 20px;
    }
    .section-title {
        font-size: 18px;
        font-weight: 600;
        color: #e2e8f0;
        margin: 0;
    }
    .section-badge {
        margin-left: auto;
        background: #1e293b;
        color: #64748b;
        font-size: 11px;
        padding: 3px 10px;
        border-radius: 20px;
        font-weight: 500;
    }

    /* Plotly chart container */
    .chart-container {
        background: #0f172a;
        border: 1px solid #1e293b;
        border-radius: 14px;
        padding: 4px;
        margin-bottom: 20px;
    }

    /* Data Table */
    .stDataFrame {
        background: #0f172a !important;
        border-radius: 12px !important;
        overflow: hidden;
    }

    /* Album cover captions */
    .album-card {
        background: #1e293b;
        border-radius: 12px;
        padding: 10px;
        text-align: center;
        border: 1px solid #334155;
        transition: border-color 0.2s;
    }
    .album-card:hover {
        border-color: #6366f1;
    }
    .album-song-name {
        font-size: 11px;
        color: #94a3b8;
        margin-top: 8px;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }

    /* Sidebar filter label */
    .filter-label {
        font-size: 11px;
        color: #475569;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        font-weight: 600;
        margin-bottom: 4px;
    }

    /* Divider */
    hr { border-color: #1e293b !important; }

    /* Footer */
    .footer {
        text-align: center;
        color: #334155;
        font-size: 12px;
        padding: 24px 0 8px;
        border-top: 1px solid #1e293b;
        margin-top: 40px;
    }

    /* Hide default streamlit elements */
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    .stDeployButton { display: none; }
</style>
""", unsafe_allow_html=True)

# ---------------------------
# Plotly dark theme config
# ---------------------------
CHART_THEME = {
    "paper_bgcolor": "#0f172a",
    "plot_bgcolor": "#0f172a",
    "font_color": "#94a3b8",
    "gridcolor": "#1e293b",
    "colorscale": px.colors.sequential.Purp,
}

ACCENT_COLORS = ["#a78bfa", "#818cf8", "#60a5fa", "#34d399", "#f472b6", "#fbbf24"]

def style_fig(fig, height=360):
    fig.update_layout(
        paper_bgcolor=CHART_THEME["paper_bgcolor"],
        plot_bgcolor=CHART_THEME["plot_bgcolor"],
        font=dict(color=CHART_THEME["font_color"], family="Inter"),
        height=height,
        margin=dict(l=16, r=16, t=40, b=16),
        title_font=dict(size=14, color="#e2e8f0"),
        legend=dict(bgcolor="#0f172a", bordercolor="#1e293b", borderwidth=1),
    )
    fig.update_xaxes(gridcolor=CHART_THEME["gridcolor"], zeroline=False)
    fig.update_yaxes(gridcolor=CHART_THEME["gridcolor"], zeroline=False)
    return fig

# ---------------------------
# Load Data
# ---------------------------
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("Dataset/cleaned_atlantic_uk_top50.csv")
        return df
    except FileNotFoundError:
        st.error("⚠️ Dataset not found. Please check: Dataset/cleaned_atlantic_uk_top50.csv")
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
# Sidebar
# ---------------------------
with st.sidebar:
    st.markdown("""
    <div style='padding: 16px 0 20px; border-bottom: 1px solid #1e293b; margin-bottom: 20px;'>
        <div style='font-size:20px; font-weight:700; color:#a78bfa; letter-spacing:-0.3px;'>🎵 UK Top 50</div>
        <div style='font-size:11px; color:#475569; margin-top:4px; text-transform:uppercase; letter-spacing:0.07em;'>Music Dashboard</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="filter-label">Artist</div>', unsafe_allow_html=True)
    artist = st.selectbox(
        "Artist",
        ["All"] + sorted(df['artist'].dropna().unique().tolist()),
        label_visibility="collapsed"
    )

    st.markdown('<div class="filter-label" style="margin-top:16px;">Explicit Content</div>', unsafe_allow_html=True)
    explicit = st.selectbox(
        "Explicit",
        ["All", True, False],
        label_visibility="collapsed"
    )

    if 'album_type' in df.columns:
        st.markdown('<div class="filter-label" style="margin-top:16px;">Album Type</div>', unsafe_allow_html=True)
        album_types = ["All"] + sorted(df['album_type'].dropna().unique().tolist())
        album_filter = st.selectbox("Album Type", album_types, label_visibility="collapsed")
    else:
        album_filter = "All"

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div style='background:#0f172a; border:1px solid #1e293b; border-radius:10px; padding:12px 14px;'>
        <div style='font-size:11px; color:#475569; text-transform:uppercase; letter-spacing:0.07em; margin-bottom:8px;'>About</div>
        <div style='font-size:12px; color:#64748b; line-height:1.6;'>Analyzing Spotify UK Top 50 playlist for Atlantic Recording Corporation's market insights.</div>
    </div>
    """, unsafe_allow_html=True)

# ---------------------------
# Apply Filters
# ---------------------------
filtered_df = df.copy()

if artist != "All":
    filtered_df = filtered_df[filtered_df['artist'] == artist]
if explicit != "All":
    filtered_df = filtered_df[filtered_df['is_explicit'] == explicit]
if album_filter != "All":
    filtered_df = filtered_df[filtered_df['album_type'] == album_filter]

# ---------------------------
# Hero Header
# ---------------------------
st.markdown("""
<div class="hero-header">
    <p class="hero-title">UK Top 50 Music Analysis</p>
    <p class="hero-sub">Spotify chart intelligence for Atlantic Recording Corporation</p>
    <span class="hero-tag">🇬🇧 United Kingdom Market</span>
</div>
""", unsafe_allow_html=True)

# ---------------------------
# KPI Cards
# ---------------------------
col1, col2, col3, col4 = st.columns(4)

kpis = [
    ("🎵", str(len(filtered_df)), "Total Songs", col1),
    ("🎤", str(filtered_df['artist'].nunique()), "Unique Artists", col2),
    ("⭐", str(round(filtered_df['popularity'].mean(), 1)) if not filtered_df.empty else "—", "Avg Popularity", col3),
    ("⏱️", str(round(filtered_df['duration_min'].mean(), 2)) + " min" if 'duration_min' in filtered_df.columns and not filtered_df.empty else "—", "Avg Duration", col4),
]

for icon, value, label, col in kpis:
    with col:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-icon">{icon}</div>
            <div class="kpi-value">{value}</div>
            <div class="kpi-label">{label}</div>
        </div>
        """, unsafe_allow_html=True)

# ---------------------------
# Top Artists + Popularity Distribution
# ---------------------------
st.markdown("""
<div class="section-header">
    <span class="section-icon">🎤</span>
    <p class="section-title">Artist Performance</p>
    <span class="section-badge">Top 10</span>
</div>
""", unsafe_allow_html=True)

c1, c2 = st.columns([3, 2])

with c1:
    artist_count = (
        filtered_df['artist']
        .value_counts()
        .head(10)
        .reset_index()
    )
    artist_count.columns = ['artist', 'count']

    fig1 = px.bar(
        artist_count,
        x='count',
        y='artist',
        orientation='h',
        color='count',
        color_continuous_scale=["#312e81", "#6366f1", "#a78bfa"],
        title="Top 10 Artists by Chart Appearances",
    )
    fig1.update_traces(showlegend=False)
    fig1.update_coloraxes(showscale=False)
    fig1.update_layout(yaxis=dict(autorange="reversed"))
    fig1 = style_fig(fig1, height=340)
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.plotly_chart(fig1, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with c2:
    fig2 = px.histogram(
        filtered_df,
        x='popularity',
        nbins=20,
        title="Popularity Distribution",
        color_discrete_sequence=["#818cf8"],
    )
    fig2 = style_fig(fig2, height=340)
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.plotly_chart(fig2, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------
# Explicit + Album Type
# ---------------------------
st.markdown("""
<div class="section-header">
    <span class="section-icon">📊</span>
    <p class="section-title">Content & Format Analysis</p>
</div>
""", unsafe_allow_html=True)

c3, c4 = st.columns(2)

with c3:
    explicit_df = (
        filtered_df['is_explicit']
        .map({True: "Explicit 🔞", False: "Clean ✅"})
        .value_counts()
        .reset_index()
    )
    explicit_df.columns = ['Type', 'Count']

    fig3 = px.pie(
        explicit_df,
        names='Type',
        values='Count',
        hole=0.55,
        title="Explicit vs Clean Content",
        color_discrete_sequence=["#f472b6", "#34d399"],
    )
    fig3.update_traces(textfont_size=13, textposition='outside')
    fig3 = style_fig(fig3, height=320)
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.plotly_chart(fig3, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with c4:
    if 'album_type' in filtered_df.columns:
        album_df = (
            filtered_df['album_type']
            .value_counts()
            .reset_index()
        )
        album_df.columns = ['Album Type', 'Count']

        fig4 = px.bar(
            album_df,
            x='Album Type',
            y='Count',
            title="Release Format Breakdown",
            color='Album Type',
            color_discrete_sequence=ACCENT_COLORS,
        )
        fig4.update_traces(showlegend=False)
        fig4 = style_fig(fig4, height=320)
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.plotly_chart(fig4, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------
# Duration vs Popularity Scatter
# ---------------------------
if 'duration_min' in filtered_df.columns:
    st.markdown("""
    <div class="section-header">
        <span class="section-icon">⏱️</span>
        <p class="section-title">Duration vs Popularity</p>
    </div>
    """, unsafe_allow_html=True)

    fig5 = px.scatter(
        filtered_df,
        x='duration_min',
        y='popularity',
        color='album_type' if 'album_type' in filtered_df.columns else None,
        hover_data=['song', 'artist'] if 'song' in filtered_df.columns else None,
        title="Does song length affect popularity?",
        color_discrete_sequence=ACCENT_COLORS,
    )
    fig5 = style_fig(fig5, height=360)
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.plotly_chart(fig5, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------
# Top Songs Table
# ---------------------------
st.markdown("""
<div class="section-header">
    <span class="section-icon">🎵</span>
    <p class="section-title">Top Songs</p>
    <span class="section-badge">Full Dataset</span>
</div>
""", unsafe_allow_html=True)

display_cols = ['song', 'artist', 'popularity', 'duration_min', 'album_type', 'is_explicit']
available_cols = [col for col in display_cols if col in filtered_df.columns]

st.dataframe(
    filtered_df[available_cols].sort_values('popularity', ascending=False).reset_index(drop=True),
    use_container_width=True,
    height=360,
)

# ---------------------------
# Album Covers
# ---------------------------
if 'album_cover_url' in filtered_df.columns:
    st.markdown("""
    <div class="section-header">
        <span class="section-icon">🖼️</span>
        <p class="section-title">Album Covers</p>
        <span class="section-badge">Top 5</span>
    </div>
    """, unsafe_allow_html=True)

    sample = filtered_df.dropna(subset=['album_cover_url']).head(5)
    cols = st.columns(5)

    for i, (_, row) in enumerate(sample.iterrows()):
        with cols[i]:
            st.image(row['album_cover_url'], use_container_width=True)
            st.markdown(f"""
            <div style='font-size:11px; color:#64748b; margin-top:6px; text-align:center;
                        white-space:nowrap; overflow:hidden; text-overflow:ellipsis;'>
                {row.get('song', '')}
            </div>
            """, unsafe_allow_html=True)

# ---------------------------
# Footer
# ---------------------------
st.markdown("""
<div class="footer">
    Built with Streamlit &nbsp;·&nbsp; UK Top 50 Music Analysis &nbsp;·&nbsp; Sakshi Sharma
</div>
""", unsafe_allow_html=True)
