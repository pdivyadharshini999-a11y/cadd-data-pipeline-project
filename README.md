# CADD Data Pipeline Project

This repository contains a step-by-step development of a molecular data pipeline for AI and data engineering, progressing from raw molecular data to machine learning-based prediction.

---

##  Project 1: Data Cleaner Tool

### Description

Cleans messy molecular dataset by handling missing values and removing unrealistic data.

### Features

* Handles missing values
* Filters invalid numerical data
* Prepares dataset for further processing

### Tools Used

* Python
* Pandas

### Output

Cleaned CSV file ready for next pipeline stage

---

##  Project 2: SMILES Validator

### Description

Validates molecular SMILES strings using RDKit and removes invalid molecules from dataset.

### Features

* Identifies valid and invalid SMILES
* Removes invalid molecular data
* Prepares dataset for feature extraction

### Tools Used

* Python
* Pandas
* RDKit

### Output

Valid SMILES dataset ready for next pipeline stage

---

##  Project 3: Descriptor Generator

### Description

Generates molecular descriptors from valid SMILES strings using RDKit.

### Features

* Converts SMILES into molecule objects
* Calculates molecular weight
* Calculates number of atoms
* Calculates number of bonds
* Calculates MolLogP
* Calculates TPSA
* Calculates hydrogen bond donors
* Calculates hydrogen bond acceptors
* Creates ML-ready dataset

### Tools Used

* Python
* Pandas
* RDKit

### Output

Descriptor dataset ready for machine learning

---

##  Project 4: Molecular Property Prediction using Machine Learning

### Description

Builds machine learning models to predict molecular bioactivity (pIC50) using generated molecular descriptors.

### Features

* Uses cleaned and validated SMILES dataset
* Utilizes molecular descriptors as features
* Splits data into training and testing sets
* Trains multiple machine learning models
* Compares model performance

### Models Used

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor

### Results

- **Final Model Selection:** Random Forest Regressor achieved the best and most reliable performance.

- **Final R² Score:** ~0.76 (Generalization Optimized).

- **Overfitting Correction:** Successfully identified an initial overfitting issue where the model had a 0.97 Train score vs a 0.79 Test score.

- **Hyperparameter Tuning:** Optimized the model using `max_depth=15` and `min_samples_leaf=5` to reduce variance and prevent the model from memorizing noise.

- **Model Robustness:** Reduced the gap between Training (0.86) and Testing (0.76) performance to ~10%, improving real-world prediction reliability.

- **Feature Importance Analysis:** Identified `Num_Bonds` as the most influential feature, contributing approximately 51.6% importance toward bioactivity prediction.

- **Key Achievement:** Improved the model’s ability to generalize on unseen molecular data while maintaining strong predictive performance.

### Features Used

* Molecular Weight
* Number of Atoms
* Number of Bonds
* MolLogP
* TPSA
* Hydrogen Bond Donors
* Hydrogen Bond Acceptors

### Outcome

Selected Random Forest as the final model for prediction

---

##  Project 5: Data Pipeline Automation

### Description

Automates the entire molecular data processing workflow from raw SMILES input to machine learning model evaluation.

### Features

* Integrates data cleaning, SMILES validation, and descriptor generation
* Automates feature engineering and model training
* Executes full pipeline with a single function call
* Reduces manual effort and improves workflow efficiency

### Workflow

Input CSV → Data Cleaning → SMILES Validation → Descriptor Generation → Model Training & Evaluation

### Tools Used

* Python
* Pandas
* RDKit
* Scikit-learn

### Outcome

Built a fully automated end-to-end molecular data pipeline for machine learning applications

##  Project 6: Data Engineering Pipeline

### Description

Implements data engineering concepts for scalable molecular data processing using SQL, PySpark, and Airflow workflow orchestration concepts.

### Features

* Stores molecular datasets using SQLite
* Executes SQL queries for filtering and analysis
* Processes large-scale molecular data using PySpark
* Performs Spark transformations and aggregations
* Exports processed data in Parquet format
* Simulates Airflow DAG workflow orchestration
* Demonstrates automated pipeline architecture concepts

### Technologies Used

* Python
* Pandas
* SQLite3
* PySpark
* Apache Airflow
* Scikit-learn

### Workflow

Raw Molecular Data → SQL Storage → PySpark Processing → Feature Engineering → Machine Learning → Airflow Workflow Scheduling

### Outcome

Built a beginner-friendly data engineering pipeline integrating SQL, PySpark, and Airflow concepts for scalable molecular machine learning workflows.

---

## Project 7: Cloud Deployment & Interactive Web App (LIVE)
### Description
Took the entire CADD pipeline to the cloud, transforming the machine learning model into a user-friendly, interactive web application for researchers.

### Live Application
**Try it here:** [CADD Molecular Property Predictor](https://cadd-data-pipeline-project-94czis6rlgjgeoaetjbnwk.streamlit.app/)

### Features
- **Instant SMILES Prediction:** Enter any molecular string (like Aspirin or Caffeine) to get pIC50 bioactivity results.
- **Automated Feature Engineering:** Real-time calculation of LogP, TPSA, and Molecular Weight using RDKit.
- **Model Deployment:** Successfully hosted a Scikit-Learn Random Forest model via Streamlit Cloud.
- **User-Centric Design:** Professional dark-mode UI designed for computational chemists.

### Tools Used
- **Python / Streamlit**
- **Scikit-Learn**
- **RDKit**
- **GitHub Actions**

---

## 🛠 Project 8: Upcoming - CADD AI Assistant (RAG System)
### Goal
Building a Retrieval-Augmented Generation (RAG) system using LLMs to allow researchers to "chat" with their molecular datasets and research papers.

---

##  Overall Pipeline Flow

Raw Data
   ->
Data Cleaning
   ->
SMILES Validation
   ->
Descriptor Generation
   ->
SQL Storage
   ->
PySpark Processing
   ->
Machine Learning Model
   ->
Airflow Workflow Automation
   ->
Prediction Output

The pipeline processes molecular data through multiple stages:

* Raw SMILES data is cleaned and preprocessed
* Invalid molecular structures are removed
* Molecular descriptors are generated using RDKit
* Molecular data is stored and queried using SQL
* PySpark processes scalable molecular datasets
* Airflow concepts are used for workflow orchestration
* Machine learning models generate final molecular predictions
