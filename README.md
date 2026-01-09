---
title: ScentSational AI Core
emoji: 🧠
colorFrom: yellow
colorTo: gray
sdk: streamlit
sdk_version: 1.39.0
app_file: app.py
pinned: false
---

<div align="center">

# SCENTSATIONAL | AI CORE (LFS)

### 🧠 The Neural Engine Behind the Atelier

*Machine Learning Backend • Large File Storage • Hugging Face Integration*

---

### 📐 System Architecture

This repository serves as the **Computation Backend** for the [ScentSational Atelier](https://github.com/MagdalenaRomaniecka/ScentSational) ecosystem. While the main dashboard handles visualization and user experience, this Core handles the heavy lifting: vector embeddings and similarity calculations.

| **PROJECT PART A: THE FACE** | **PROJECT PART B: THE BRAIN (You are here)** |
| :---: | :---: |
| [**ScentSational Atelier**](https://github.com/MagdalenaRomaniecka/ScentSational) | **ScentSational AI Core** |
| Interactive Streamlit Dashboard | Hugging Face Space & LFS Storage |
| **Presentation Layer** | **Computation Layer** |

---

### ⚙️ Technical Specifications

This engine utilizes **Natural Language Processing (NLP)** to analyze olfactory profiles, translating abstract concepts (e.g., "woody notes", "luxury vibe") into mathematical vectors.

**Core Technologies:**
`Python` • `Git LFS` • `Hugging Face Spaces`

**Machine Learning Stack:**
* **Sentence-Transformers (SBERT):** For generating dense vector representations of perfume notes.
* **Cosine Similarity:** For calculating the mathematical distance between scent profiles.
* **Numpy:** For efficient storage of pre-computed matrices.

---

### 📂 LFS Data Structure

Due to GitHub's file size limits, this repository uses **Git LFS** (Large File Storage) to host heavy model artifacts required for AI inference.

| File Name | Description | Role |
| :--- | :--- | :--- |
| `scent_embeddings.pkl` | Vectorized representation of 40,000+ perfumes | **Semantic Database** |
| `hybrid_similarity.npy` | Pre-computed similarity matrix | **Instant Search Cache** |
| `perfumes_dataset.csv` | Raw metadata (Brand, Notes, Ratings) | **Source Data** |

---

### 🚀 Deployment & Integration

This core is deployed as a microservice on **Hugging Face Spaces**, exposing an interface that the main dashboard interacts with.

[🔗 Visit Main Dashboard (Atelier)](https://github.com/MagdalenaRomaniecka/ScentSational)

<br>

<div align="center">
    <img src="https://via.placeholder.com/800x20/D4AF37/000000?text=+" alt="Footer Line" width="100%">
    <p style="color:#666; font-size: 10px;">ENGINEERED BY MAGDALENA ROMANIECKA • 2026</p>
</div>

</div>