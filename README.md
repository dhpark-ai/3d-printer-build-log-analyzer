# 3D Printer Build Log Analyzer

## 📌 Overview
This project analyzes build log text files from industrial 3D printers,
extracts key parameters, and visualizes them for process monitoring and analysis.

## 🔍 Problem Statement
In production environments, build logs are stored as raw text files,
making it difficult for engineers to quickly understand process behavior
or identify anomalies.

## 🛠️ What This Project Does
- Parses build log text files
- Extracts key parameters (temperature, speed, etc.)
- Ignores data after "At the end of the build job"
- Generates plots automatically
- Exports results as a PDF report

## ⚙️ Tech Stack
- Python
- pandas
- matplotlib
- PyQt5

## 📌 Version comparison

| Version | Graphs | warnings.txt | minmax.txt | PDF |
|---------|--------|--------------|------------|-----|
| v1.0 | ✅ | ✅ | — | — |
| v1.1 | ✅ | ✅ | ✅ | — |
| v1.2 | ✅ | ✅ | ✅ | ✅ (folder per Build name) |

## 🚀 How to Run
```bash
pip install -r requirements.txt
python main.py
```

1. Click **Select log file**
2. Choose the protocol `.txt` file to analyze
3. Results are saved under `output/<Build job name>/`


## 🧠 What I Learned
 - Log parsing in real production systems
 - Building executable tools for non-Python environments
 - Automating analysis workflows for engineers
