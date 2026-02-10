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
- Extracts key parameters (temperature, time, etc.)
- Ignores data after "At the end of the build job"
- Generates plots automatically
- Exports results as a PDF report

## ⚙️ Tech Stack
- Python
- pandas
- matplotlib
- PyQt5

## 🚀 How to Run
```bash
python main.py


