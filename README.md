# The Intelligence Platform. Unlock the chemical DNA of scent.

[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Open%20in%20Spaces-blue)](https://huggingface.co/spaces/Baphomert/ScentSational-Fragrantica-LFS2)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://scentsational-zbznjhgc4xv7faddappdc2b.streamlit.app/)

---

---

### 💎 Project Overview

**ScentSational AI Core** is a machine learning service designed for semantic perfume search. Unlike traditional filters that rely solely on checkboxes, this engine uses **Semantic Search** and **Natural Language Processing (NLP)** to understand the *vibe* of a scent (e.g., *"dark, woody notes with a luxury feel"*).

This repository acts as a dedicated computation engine, isolating complex data processing from the user interface.

---

This repository acts as a dedicated computation engine, isolating complex data processing from the user interface.

---
# ✨ SCENTSATIONAL | AI CORE

### The Intelligence Platform. Unlock the chemical DNA of scent.

[![Open in Spaces](https://huggingface.co/datasets/huggingface/badges/raw/main/open-in-hf-spaces-md-dark.svg)](https://huggingface.co/spaces/Baphomert/ScentSational-Fragrantica-LFS2)
&nbsp;
[![Visit Atelier Dashboard](https://img.shields.io/badge/VISIT_MAIN_ATELIER-000000?style=for-the-badge&logo=github&logoColor=D4AF37&color=1a1a1a)](https://github.com/MagdalenaRomaniecka/ScentSational)

</div>

---

## 💎 Project Overview

**ScentSational AI Core** is a machine learning service designed for semantic perfume search. Unlike traditional filters that rely solely on checkboxes, this engine uses **Semantic Search** and **Natural Language Processing (NLP)** to understand the *vibe* of a scent (e.g., *"dark, woody notes with a luxury feel"*).
This repository acts as a dedicated computation engine, isolating complex data processing from the user interface.
---

## 📐 Architecture & Ecosystem

This project is part of a dual-repository architecture designed for scalability and clean code separation.

| **PART A: THE FACE (Frontend)** | **PART B: THE BRAIN (Backend)** |
| :--- | :--- |
| [**ScentSational Atelier**](https://github.com/MagdalenaRomaniecka/ScentSational) | **ScentSational AI Core (This Repo)** |
| 🎨 Interactive Streamlit Dashboard | 🧠 Hugging Face Space & LFS Storage |
| **Presentation Layer** | **Computation Layer** |

---

## ⚙️ Key Features & Tech Stack

This engine translates abstract concepts into mathematical vectors using state-of-the-art ML libraries.

* **Sentence-Transformers (SBERT):** Transforms perfume note descriptions into semantic vectors, preserving their context.
* **Cosine Similarity:** Measures the alignment between scent profiles to identify the most relevant matches.
* **Git LFS (Large File Storage):** Handles the storage of large model files essential for generating recommendations.
* **Stack**: Python 3.9+, Streamlit, Pandas, Numpy, Scikit-Learn.

---

## 💻 Installation & Usage

To run this backend engine locally:

```bash
# 1. Clone the repository (ensure Git LFS is installed)
git clone [https://github.com/MagdalenaRomaniecka/ScentSational-Fragrantica-LFS.git](https://github.com/MagdalenaRomaniecka/ScentSational-Fragrantica-LFS.git)

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the application
streamlit run app.py

---
```
## 📂 Data Source & LFS Structure

Due to GitHub's file size limits, this repository uses **Git LFS** to host artifacts.

| File Name | Description | Role |
| :--- | :--- | :--- |
| `scent_embeddings.pkl` | Vectorized representation of 40k+ perfumes | **Semantic Database** |
| `scentsational_data.csv` | Raw metadata (Brand, Notes, Ratings) | **Source Data** |

> **Data Source:** This project utilizes the [Fragrantica Perfumes Dataset](https://www.kaggle.com/datasets/olgagmiufana1/fragrantica-com-fragrance-dataset) sourced from Kaggle.

---

<div align="center">

### 👩‍💻 Author

**Created by Magdalena Romaniecka**
<br>
*Data Analyst & Web Analytics Enthusiast*

<br>

© 2026 | Built with 💚 and Python

</div>