import pandas as pd
from sentence_transformers import SentenceTransformer
import pickle
import os

def generate_ai_brain():
    print("--- 1. Loading Dataset ---")
    try:
        # Load CSV with flexible separator handling
        df = pd.read_csv('scentsational_data.csv', sep=None, encoding='latin1', engine='python')
        
        # Clean column names (remove hidden spaces)
        df.columns = df.columns.str.strip()
        
        # Rename 'Perfume' to 'Name' if needed
        if 'Perfume' in df.columns:
            df = df.rename(columns={'Perfume': 'Name'})
            
        print(f"Data loaded successfully. Total perfumes: {len(df)}")
    except FileNotFoundError:
        print("Error: 'scentsational_data.csv' not found.")
        return
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return

    print("--- 2. Preprocessing & Merging Accords ---")
    # FIX: Combine individual accord columns into one 'Main Accords' column
    accord_cols = ['mainaccord1', 'mainaccord2', 'mainaccord3', 'mainaccord4', 'mainaccord5']
    # Check which of these columns actually exist in the file
    existing_cols = [c for c in accord_cols if c in df.columns]
    
    if existing_cols:
        # Join them with spaces
        df['Main Accords'] = df[existing_cols].apply(lambda x: ' '.join(x.dropna().astype(str)), axis=1)
    else:
        # Fallback if no accord columns found
        print("Warning: No accord columns found. Using empty string for accords.")
        df['Main Accords'] = ""

    print("--- 3. Creating Text Features (The Soup) ---")
    # Combining Brand, Name, and Notes into a single descriptive string
    df['text_features'] = (
        df['Brand'].astype(str) + " " + 
        df['Name'].astype(str) + " " + 
        df['Main Accords'].astype(str)
    )

    print("--- 4. Downloading AI Model ---")
    model = SentenceTransformer('all-MiniLM-L6-v2')

    print("--- 5. Generating Embeddings (Crunching numbers...) ---")
    embeddings = model.encode(df['text_features'].tolist(), show_progress_bar=True)

    print("--- 6. Saving the AI Brain (.pkl file) ---")
    output_filename = 'scent_embeddings.pkl'
    with open(output_filename, 'wb') as f:
        pickle.dump(embeddings, f)

    if os.path.exists(output_filename):
        file_size = os.path.getsize(output_filename) / (1024 * 1024)
        print(f"SUCCESS! '{output_filename}' created ({file_size:.2f} MB).")
    else:
        print("Error: File was not saved.")

if __name__ == "__main__":
    generate_ai_brain()