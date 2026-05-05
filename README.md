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

* Random Forest achieved the best performance
* R² score ≈ 0.79
* Demonstrated ability to capture nonlinear relationships

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

##  Upcoming Projects

* Project 6: Advanced Feature Engineering
* Project 7: Deployment
* Project 8: CADD AI Assistant

---

##  Overall Pipeline Flow



Raw Data 
   ↓
Data Cleaning 
   ↓
SMILES Validation 
   ↓
Descriptor Generation (Feature Engineering)
   ↓
Machine Learning Model 
   ↓
Prediction Output


The pipeline processes molecular data through multiple stages:

* Raw SMILES data is cleaned and preprocessed
* Invalid molecular structures are removed
* Molecular descriptors are generated using RDKit
* Machine learning models are trained on engineered features
* Final predictions (pIC50) are generated





