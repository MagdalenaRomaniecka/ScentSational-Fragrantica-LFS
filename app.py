import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

# -----------------------------------------------------------------------------
# 1. UI CONFIGURATION
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="ScentSational | Atelier", 
    page_icon="👑",
    layout="wide"
)
st.cache_data.clear()

# -----------------------------------------------------------------------------
# 2. SHARED LUXURY CSS (To co działało dobrze)
# -----------------------------------------------------------------------------
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,400&family=Montserrat:wght@300;400;500;600;700&display=swap');

    html, body, [class*="css"], .stMarkdown, .stRadio, .stSelectbox, .stTextInput, .stMultiSelect, div, span, p {
        font-family: 'Montserrat', sans-serif !important;
        font-weight: 400 !important; 
        color: #E0E0E0 !important;
        font-size: 0.9rem !important;
    }
    
    h1, h2, h3 {
        font-family: 'Cormorant Garamond', serif !important;
        color: #D4AF37 !important;
        text-transform: uppercase;
        letter-spacing: 1.5px;
    }

    .stApp {
        background-color: #050505;
        background-image: radial-gradient(circle at 50% 50%, #1a1a1a 0%, #000000 100%);
    }

    /* FIX: CZARNE TŁO MENU (To co naprawiliśmy wcześniej) */
    div[data-baseweb="popover"],
    div[data-baseweb="menu"],
    div[data-baseweb="select"] > div {
        background-color: #050505 !important;
        border: 1px solid #333 !important;
    }
    
    div[data-baseweb="menu"] li, 
    div[data-baseweb="popover"] div {
        color: #E0E0E0 !important;
    }
    
    div[data-baseweb="menu"] li[aria-selected="true"],
    div[data-baseweb="menu"] li:hover {
        background-color: #1a1a1a !important;
        color: #D4AF37 !important;
    }

    /* KARTY PERFUM */
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
    if not brand_name: return "?"
    parts = str(brand_name).split()
    if len(parts) >= 2:
        return (parts[0][0] + parts[1][0]).upper()
    return str(brand_name)[:2].upper()

# -----------------------------------------------------------------------------
# 4. LOAD DATA (JEDYNA ZMIANA TUTAJ - FIX DLA DANYCH)
# -----------------------------------------------------------------------------
@st.cache_data
def load_data():
    try:
        # Wczytujemy z ignorowaniem błędów i kodowaniem latin1
        df = pd.read_csv("scentsational_data.csv", encoding='latin1', on_bad_lines='skip')
        
        # --- KLUCZOWA POPRAWKA ---
        # Usuwamy spacje z nazw kolumn (np. "Brand " -> "Brand")
        df.columns = df.columns.str.strip()
        
        # Jeśli kolumna nazywa się 'brand' (mała litera), zmieniamy na 'Brand'
        df.rename(columns={'brand': 'Brand', 'name': 'Name', 'notes': 'Notes', 'image': 'Image URL'}, inplace=True)
        
        return df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()

df = load_data()

# -----------------------------------------------------------------------------
# 5. MAIN LAYOUT
# -----------------------------------------------------------------------------
st.markdown("""
    <div style="text-align: center; padding-bottom: 40px;">
        <h1 style="font-size: 3rem; margin-bottom: 0;">SCENTSATIONAL</h1>
        <div style="font-family: 'Montserrat'; font-size: 0.9rem; letter-spacing: 3px; color: #888;">THE ATELIER</div>
    </div>
""", unsafe_allow_html=True)

if not df.empty and 'Brand' in df.columns:
    # --- Sidebar / Top Filter ---
    col1, col2 = st.columns([1, 3])
    
    with col1:
        st.markdown("### FILTER BY BRAND")
        # Teraz bezpiecznie bierzemy Brand
        brands = sorted(df['Brand'].astype(str).unique().tolist())
        brands.insert(0, "All Brands")
        
        selected_brand = st.selectbox("Select a House", brands, label_visibility="collapsed")

    # --- Filtering Logic ---
    if selected_brand != "All Brands":
        filtered_df = df[df['Brand'] == selected_brand]
    else:
        filtered_df = df.head(50) 

    # --- Display Results ---
    with col2:
        st.markdown(f"### COLLECTION ({len(filtered_df)} found)")
        
        for index, row in filtered_df.iterrows():
            # Używamy .get() dla bezpieczeństwa
            brand = str(row.get('Brand', 'Unknown'))
            name = str(row.get('Name', 'Unknown Scent'))
            rating = row.get('Rating', 0.0)
            notes = str(row.get('Notes', 'Notes not available'))
            link = str(row.get('Image URL', '#'))
            
            initials = get_initials(brand)
            
            # Karty (Ten sam ładny HTML co wcześniej)
            st.markdown(f"""
                <div class="perfume-card">
                    <div class="brand-emblem">{initials}</div>
                    <div style="width:100%">
                        <div style="font-size: 0.75rem; text-transform: uppercase; letter-spacing: 2px; color: #888;">{brand}</div>
                        <div style="font-family: 'Cormorant Garamond', serif; font-size: 1.4rem; color: #E0E0E0; margin: 2px 0;">{name}</div>
                        <div style="color: #D4AF37; font-size: 0.9rem; margin-top: 5px;">★ {rating}</div>
                        <div style="font-size: 0.85rem; color: #aaa; margin-top: 8px; line-height: 1.4;">{notes[:150]}...</div>
                    </div>
                    <a href="{link}" target="_blank" class="gold-btn">FRAGRANTICA</a>
                </div>
            """, unsafe_allow_html=True)

    # --- FOOTER ---
    st.markdown("""
    <div class="custom-footer">
        ScentSational Atelier v3.0 &bull; Developed by Magdalena Romaniecka &bull; 2026<br>
        Data Source: <a href="https://www.kaggle.com/datasets/olgagmiufana1/fragrantica-com-fragrance-dataset" style="color: #888; text-decoration: none;">Fragrantica Dataset (Kaggle)</a>
    </div>
    """, unsafe_allow_html=True)
else:
    if df.empty:
        st.warning("Dataset failed to load properly.")
    else:
        st.error(f"Dataset loaded but 'Brand' column is missing. Available columns: {list(df.columns)}")