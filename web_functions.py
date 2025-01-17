# import modul yang digunakan
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import streamlit as st

@st.cache_data()
def load_data():

    # load dataset
    data = pd.read_csv('datamiskinsidorejo400.csv')

    df = data.drop(['nama'], axis = 1)
    ind_col = [col for col in df.columns if col != 'keputusan']
    dep_col = 'keputusan'
    mapping = {
    'kelamin': {'pria': 1, 'wanita': 2},
    'pendidikan': {'perguruan tinggi': 1, 'sma': 2, 'smp': 3, 'sd': 4, 'tidak sekolah':5},
    'pekerjaan': {'pegawai': 1, 'swasta':2, 'pedagang': 2, 'petani': 2, 'pedagang/petani': 2,'buruh': 3, 'tidak bekerja': 4},
    'jumlah_tanggungan': {'0': 1, '1':2, '2': 3, '3': 4, '4': 4, '5': 4},
    'lantai_rumah': {'keramik': 1, 'tegel/tembok': 2, 'tanah/bambu': 3},
    'dinding_rumah': {'tembok': 1, 'semi-tembok': 2, 'kayu/bambu': 3},
    'daya_listrik': {'900 va': 1, '450 va': 2},
    'sumber_air': {'pam': 1, 'sumur': 2},
    'keputusan': {'tidak miskin': 0, 'miskin': 1}
    }

    df = df.replace(mapping)

    x = df[ind_col] #feature
    y = df[dep_col] #label

    # x = df[["kelamin","pendidikan","pekerjaan","jumlah_tanggungan",
    #         "lantai_rumah","dinding_rumah","daya_listrik","sumber_air"]]
    # y = df[['keputusan']]

    return data, df, x, y

@st.cache_data()
def train_model(x,y):
    model = DecisionTreeClassifier(
            ccp_alpha=0.0, class_weight=None, criterion='entropy',
            max_depth=4, max_features=None, max_leaf_nodes=None,
            min_impurity_decrease=0.0, min_samples_leaf=1,
            min_samples_split=2, min_weight_fraction_leaf=0.0, 
            random_state=42, splitter='best'
        )
    
    model.fit(x,y)

    score = model.score(x,y)

    return model, score

def predict(x,y, features):
    model, score = train_model(x,y)

    prediction = model.predict(np.array(features).reshape(1,-1))

    return prediction, score


