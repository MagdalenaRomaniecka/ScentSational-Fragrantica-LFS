import streamlit as st
import pandas as pd
import pickle
from sentence_transformers import SentenceTransformer, util

# --- 1. CONFIGURATION ---
st.set_page_config(page_title="ScentSational AI Core", page_icon="🧠", layout="centered")

# --- 2. CACHED RESOURCE LOADER ---
@st.cache_resource
def load_ai_engine():
    try:
        # Load Raw Data (Using robust separator and encoding settings)
        df = pd.read_csv('scentsational_data.csv', sep=None, encoding='latin1', engine='python')
        
        # Load Pre-computed Embeddings (The "Brain")
        with open('scent_embeddings.pkl', 'rb') as f:
            embeddings = pickle.load(f)
            
        # Load Model (Only for encoding user queries)
        model = SentenceTransformer('all-MiniLM-L6-v2')
        
        return df, embeddings, model
    except Exception as e:
        return None, None, None

# Load resources
df, embeddings, model = load_ai_engine()

# --- 3. UI LAYOUT ---
st.title("🧠 ScentSational | AI Core")
st.markdown("### Deep Learning Semantic Search")
st.markdown("Powered by *Sentence-Transformers* & *Neural Networks*")

# Error Handling
if df is None or embeddings is None:
    st.error("System Error: AI Models or Data not found. Please verify Git LFS setup.")
    st.stop()

# --- 4. SEARCH INTERFACE ---
query = st.text_input("Describe your dream fragrance:", placeholder="e.g. dark woody scent with vanilla and tobacco...")

if query:
    with st.spinner("Analyzing olfactory DNA..."):
        # 1. Convert user text to vector
        query_embedding = model.encode(query, convert_to_tensor=True)
        
        # 2. Perform Cosine Similarity Search (Top 5 matches)
        hits = util.semantic_search(query_embedding, embeddings, top_k=5)
        
        st.success("Analysis Complete. Top matches found:")
        st.markdown("---")

        # 3. Display Results
        for hit in hits[0]:
            idx = hit['corpus_id']
            score = hit['score']
            row = df.iloc[idx]
            
            # Clean Card Layout
            col1, col2 = st.columns([1, 4])
            with col1:
                st.metric(label="Match", value=f"{int(score*100)}%")
            with col2:
                st.markdown(f"**{row['Brand']}**")
                st.subheader(f"{row['Name']}")
                # Handle cases where 'Main Accords' might be missing in display
                accords = row.get('Main Accords', 'N/A')
                st.caption(f"Notes: {accords}")
            
            st.markdown("---")