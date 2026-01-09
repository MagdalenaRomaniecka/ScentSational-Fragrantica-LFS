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

# ✨ SCENTSATIONAL | AI CORE

### The Intelligence Platform. Unlock the chemical DNA of scent.

[![Open in Spaces](https://huggingface.co/datasets/huggingface/badges/raw/main/open-in-hf-spaces-md-dark.svg)](https://huggingface.co/spaces/Baphomert/ScentSational-Fragrantica-LFS2)
&nbsp;
[![Visit Atelier Dashboard](https://img.shields.io/badge/VISIT_MAIN_ATELIER-000000?style=for-the-badge&logo=github&logoColor=D4AF37&color=1a1a1a)](https://github.com/MagdalenaRomaniecka/ScentSational)

</div>

---

## 💎 Project Overview

**ScentSational AI Core** is the backend intelligence engine designed to revolutionize fragrance discovery. Unlike traditional filters that rely solely on checkboxes, this engine uses **Semantic Search** and **Natural Language Processing (NLP)** to understand the *vibe* of a scent.

This repository serves as the computational brain, separating heavy logic from the visual presentation layer.

---

## 📐 Architecture & Ecosystem

This project is part of a dual-repository architecture designed for scalability and clean code separation.

| **PART A: THE FACE (Frontend)** | **PART B: THE BRAIN (Backend)** |
| :--- | :--- |
| [**ScentSational Atelier**](https://github.com/MagdalenaRomaniecka/ScentSational) | **ScentSational AI Core (This Repo)** |
| 🎨 Interactive Streamlit Dashboard | 🧠 Hugging Face Space & LFS Storage |
| **Presentation Layer** | **Computation Layer** |

---

## 🛠️ Key Features & Tech Stack

This engine translates abstract concepts (e.g., *"woody notes with a luxury vibe"*) into mathematical vectors using state-of-the-art ML libraries.

* **Python 3.9+** & **Streamlit**: Core framework.
* **Sentence-Transformers (SBERT)**:
    * *Role:* Generates dense vector representations of perfume notes.
* **Cosine Similarity**:
    * *Role:* Calculates mathematical distance between scent profiles.
* **Numpy & Pickle**:
    * *Role:* Efficient storage of pre-computed similarity matrices (~500MB+ data).
* **Git LFS (Large File Storage)**:
    * *Role:* Hosting heavy model artifacts required for inference.

---

## 📂 Data Source & LFS Structure

Due to GitHub's file size limits, this repository uses **Git LFS** to host artifacts.

| File Name | Description | Role |
| :--- | :--- | :--- |
| `scent_embeddings.pkl` | Vectorized representation of 40k+ perfumes | **Semantic Database** |
| `scentsational_data.csv` | Raw metadata (Brand, Notes, Ratings) | **Source Data** |

> **Note:** This project utilizes the Fragrantica Dataset sourced from Kaggle.

---

<div align="center">

### 👩‍💻 Author

**Created by Magdalena Romaniecka**
<br>
*Data Analyst & Web Analytics Enthusiast*

<br>

© 2026 | Built with 💚 and Python

</div>