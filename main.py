import pickle
import pandas as pd 
from fastapi import FastAPI
from unidecode import unidecode

app = FastAPI()



def encoder(names):
    alphabet = "abcdefghijklmnopqrstuvwxyz-"

    features = pd.DataFrame()
    for letter in alphabet:
        features[letter] = (
            names.apply(unidecode).str.lower().str.count(letter).astype(int)
        )
        
    return features



    
@app.get("/")
def read_root():
    return {"Hello World"}



@app.get("/predict/name={name}")
def pred(name: str):   
    model = pickle.load(open('finalized_model.sav','rb'))  
    res = model.predict(encoder(pd.Series([name]))) 
    return {"Sexe": int(res)}
