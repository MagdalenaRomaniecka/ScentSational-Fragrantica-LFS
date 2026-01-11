import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import re

# -----------------------------------------------------------------------------
# 1. UI CONFIGURATION
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="ScentSational | Atelier", 
    page_icon="👑",
    layout="wide"
)
# Clear cache to ensure CSS updates are applied immediately
st.cache_data.clear()

# -----------------------------------------------------------------------------
# 2. SHARED LUXURY CSS (MATCHING AI CORE)
# -----------------------------------------------------------------------------
st.markdown("""
    <style>
    /* IMPORT FONTS */
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,400&family=Montserrat:wght@300;400;500;600;700&display=swap');

    /* GLOBAL FONT ENFORCEMENT */
    html, body, [class*="css"], .stMarkdown, .stRadio, .stSelectbox, .stTextInput, .stMultiSelect, div, span, p {
        font-family: 'Montserrat', sans-serif !important;
        font-weight: 400 !important; 
        color: #E0E0E0 !important;
        font-size: 0.9rem !important;
    }
    
    /* TITLES (Golden Luxury) */
    h1, h2, h3 {
        font-family: 'Cormorant Garamond', serif !important;
        color: #D4AF37 !important;
        text-transform: uppercase;
        letter-spacing: 1.5px;
    }

    /* APP BACKGROUND */
    .stApp {
        background-color: #050505;
        background-image: radial-gradient(circle at 50% 50%, #1a1a1a 0%, #000000 100%);
    }

    /* ------------------------------------------------------ */
    /* FIX: FORCE BLACK BACKGROUND ON DROPDOWNS & POPOVERS    */
    /* ------------------------------------------------------ */
    div[data-baseweb="popover"],
    div[data-baseweb="popover"] > div,
    div[data-baseweb="menu"],
    div[data-baseweb="select"] > div {
        background-color: #050505 !important;
        border-color: #333 !important;
    }
    
    /* Dropdown Options Text Color */
    li[role="option"] {
        color: #E0E0E0 !important;
    }
    
    /* Hover/Selected State (Gold Highlight) */
    li[role="option"][aria-selected="true"] {
        background-color: #1a1a1a !important;
        color: #D4AF37 !important;
    }

    /* INPUT FIELDS STYLING */
    .stTextInput input, .stSelectbox div[data-baseweb="select"] {
        background-color: #0a0a0a !important;
        color: #D4AF37 !important;
        border: 1px solid #333 !important;
        border-radius: 0px !important;
    }

    /* CUSTOM CARDS */
    .perfume-card {
        background: rgba(20, 20, 20, 0.8);
        border: 1px solid #333;
        padding: 20px;
        margin-bottom: 15px;
        border-radius: 2px;
        transition: transform 0.3s ease, border-color 0.3s ease;
        display: flex;
        align-items: center;
        gap: 20px;
    }
    .perfume-card:hover {
        transform: translateY(-2px);
        border-color: #D4AF37;
    }
    .brand-emblem {
        width: 60px;
        height: 60px;
        background: #111;
        border: 1px solid #D4AF37;
        color: #D4AF37;
        display: flex;
        align-items: center;
        justify-content: center;
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.5rem;
        font-weight: 600;
        border-radius: 50%;
    }
    .row-brand {
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 2px;
        color: #888;
    }
    .row-name {
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.4rem;
        color: #E0E0E0;
        margin: 2px 0;
    }
    .row-meta {
        font-size: 0.8rem;
        color: #666;
        font-style: italic;
    }
    .row-rating {
        color: #D4AF37;
        font-size: 0.9rem;
        margin-top: 5px;
    }
    .row-notes {
        font-size: 0.85rem;
        color: #aaa;
        margin-top: 8px;
        line-height: 1.4;
    }

    /* BUTTONS */
    .gold-btn {
        display: inline-block;
        padding: 8px 20px;
        border: 1px solid #D4AF37;
        color: #D4AF37 !important;
        text-decoration: none;
        font-size: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: all 0.3s ease;
        margin-left: auto;
    }
    .gold-btn:hover {
        background-color: #D4AF37;
        color: #000 !important;
    }
    
    /* FOOTER */
    .custom-footer {
        text-align: center;
        padding: 40px 0;
        border-top: 1px solid #333;
        margin-top: 50px;
        color: #666;
        font-size: 0.8rem;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 3. HELPER FUNCTIONS
# -----------------------------------------------------------------------------
def get_initials(brand_name):
    """Extracts initials for the emblem (e.g., 'Giorgio Armani' -> 'GA')"""
    if not brand_name: return "?"
    parts = brand_name.split()
    if len(parts) >= 2:
        return (parts[0][0] + parts[1][0]).upper()
    return brand_name[:2].upper()

# -----------------------------------------------------------------------------
# 4. LOAD DATA
# -----------------------------------------------------------------------------
@st.cache_data
def load_data():
    """Loads the main CSV dataset."""
    try:
        # FIX: Added encoding='latin1' to handle special characters (e.g. accents)
        df = pd.read_csv("scentsational_data.csv", encoding='latin1') 
        return df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()

df = load_data()

# -----------------------------------------------------------------------------
# 5. MAIN LAYOUT
# -----------------------------------------------------------------------------
# Header
st.markdown("""
    <div style="text-align: center; padding-bottom: 40px;">
        <h1 style="font-size: 3rem; margin-bottom: 0;">SCENTSATIONAL</h1>
        <div style="font-family: 'Montserrat'; font-size: 0.9rem; letter-spacing: 3px; color: #888;">THE ATELIER</div>
    </div>
""", unsafe_allow_html=True)

if not df.empty:
    # --- Sidebar / Top Filter ---
    col1, col2 = st.columns([1, 3])
    
    with col1:
        st.markdown("### FILTER BY BRAND")
        # Get unique brands, sorted
        brands = sorted(df['Brand'].dropna().unique().tolist())
        # Insert a default 'All' option
        brands.insert(0, "All Brands")
        
        selected_brand = st.selectbox("Select a House", brands, label_visibility="collapsed")

    # --- Filtering Logic ---
    if selected_brand != "All Brands":
        filtered_df = df[df['Brand'] == selected_brand]
    else:
        filtered_df = df.head(50) # Show top 50 if no brand selected to improve performance

    # --- Display Results ---
    with col2:
        st.markdown(f"### COLLECTION ({len(filtered_df)} found)")
        
        for index, row in filtered_df.iterrows():
            brand = str(row.get('Brand', 'Unknown'))
            name = str(row.get('Name', 'Unknown Scent'))
            rating = row.get('Rating', 0.0)
            notes = str(row.get('Notes', 'Notes not available'))
            link = str(row.get('Image URL', '#')) # Using Image URL or specific link column
            
            # Emblem Initials
            initials = get_initials(brand)
            
            # Meta (Gender • Year)
            gender = str(row.get('Gender', 'Unisex')).capitalize()
            year = str(row.get('Year', ''))
            meta_info = f"{gender}"
            if year and year != 'nan': meta_info += f" &bull; {year}"

            # HTML Card
            st.markdown(f"""
                <div class="perfume-card">
                    <div class="brand-emblem">{initials}</div>
                    <div style="width:100%">
                        <div class="row-brand">{brand}</div>
                        <div class="row-name">{name}</div>
                        <div class="row-meta">{meta_info}</div>
                        <div class="row-rating">★ {rating:.2f}</div>
                        <div class="row-notes">{notes}</div>
                    </div>
                    <a href="{link}" target="_blank" class="gold-btn">FRAGRANTICA</a>
                </div>
            """, unsafe_allow_html=True)

    # --- 6. DISCREET FOOTER ---
    st.markdown("""
    <div class="custom-footer">
        ScentSational Atelier v3.0 &bull; Developed by Magdalena Romaniecka &bull; 2026<br>
        Data Source: <a href="https://www.kaggle.com/datasets/olgagmiufana1/fragrantica-com-fragrance-dataset" style="color: #888; text-decoration: none;">Fragrantica Dataset (Kaggle)</a>
    </div>
    """, unsafe_allow_html=True)
else:
    st.warning("Dataset not found or empty.")