import streamlit as st
from rdkit import Chem
from rdkit.Chem import Descriptors
import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score

st.title("Cadd_Data_Pipeline")
st.write("Predict molecular bioactivity using machine learning.")
st.info("Enter valid molecular SMILES for prediction")

model = joblib.load("random_forest_regressor.joblib")

smiles = st.text_input("Enter smiles :")
predict_button = st.button("Predict")

if predict_button:
  mol = Chem.MolFromSmiles(smiles)
  if smiles == "":
    st.warning("No input entered")
  elif mol is None:
    st.error("Invalid SMILES string. Please enter a valid SMILES.")
  else:
    weight = Descriptors.MolWt(mol)
    bonds = mol.GetNumBonds()
    atoms = mol.GetNumAtoms()
    tpsa = Descriptors.TPSA(mol)
    logp = Descriptors.MolLogP(mol)
    numhdonors = Descriptors.NumHDonors(mol)
    numhacceptors = Descriptors.NumHAcceptors(mol)

    st.subheader("Molecular properties :")
    st.write("You entered:",smiles)
    st.write("Molecular weight:", weight)
    st.write("Number of bonds:",bonds)
    st.write("Number of atoms:",atoms)
    st.write("Topological Polar Surface Area (TPSA):", tpsa) 
    st.write("LogP:", logp)
    st.write("Number of Hydrogen Donors:",numhdonors)
    st.write("Number of Hydrogen Acceptors:",numhacceptors)

    data = pd.DataFrame({
    "num_atoms":[atoms],
    "logP":[logp],
    "Molecular_Weight":[weight],
    "Num_Bonds":[bonds],
    "TPSA":[tpsa],
    "NumHDoner":[numhdonors],
    "NumHAcceptor":[numhacceptors]
    })

    
    predicted_pIC50  = model.predict(data)
    st.subheader("Predicted pIC50 value:")
    st.success(f"Predicted pIC50 value : {predicted_pIC50[0]:.4f}")

    st.subheader("Molecular properties in tabular form")
    st.dataframe(data)

