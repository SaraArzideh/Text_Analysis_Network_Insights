# Network Analysis with Python 🔗

This repository contains a Python script for performing network analysis on co-occurrence data. It visualizes relationships between keywords and identifies clusters using community detection algorithms.

---

## 📂 File Overview
- **`NetworkAnalysis.py`:**  
  A Python script that:
  - Reads co-occurrence data from a CSV file.
  - Creates and visualizes a network graph of keyword relationships.
  - Detects and visualizes communities within the network.
  - Maps keywords to specific categories and exports the results to a CSV file.

---

##  📜  Features
- **Data Visualization:** Interactive network graph using `networkx` and `matplotlib`.
- **Community Detection:** Cluster identification with the Louvain algorithm.
- **Keyword Categorization:** Assigns categories to keywords and saves the mapping.

---

## 🛠️ Tools and Libraries
- `networkx`
- `pandas`
- `matplotlib`
- `nltk`
- `community_louvain`

---

## 🔧 How to Use
1. Place your co-occurrence data in a file named `filtered_co_occurrence_data.csv`.
2. Run the script:
   ```bash
   python NetworkAnalysis.py
