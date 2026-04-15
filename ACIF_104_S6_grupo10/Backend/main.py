from fastapi import FastAPI
import joblib
import pandas as pd
import os
import numpy as np
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Cargar Modelo y CSV
base_path = os.path.dirname(__file__)
model = joblib.load(os.path.join(base_path, 'modelo_final_netflix.pkl'))
df = pd.read_csv(os.path.join(base_path, 'netflix_cleaned.csv'), sep=';')

class FilterQuery(BaseModel):
    generos: List[str]
    anio_min: int
    anio_max: int
    rating_min: float

@app.post("/recommend")
def recommend(data: FilterQuery):
    try:
        # 1. FILTRAR EL CSV (Nombres y datos base)
        mask = (
            (df['genre_1'].isin(data.generos)) & 
            (df['release_year'] >= data.anio_min) & 
            (df['release_year'] <= data.anio_max) & 
            (df['rating'] >= data.rating_min)
        )
        candidatos = df[mask].copy()
        
        if candidatos.empty:
            return {"error": "No hay películas que cumplan todos esos filtros. ¡Prueba bajando el rating o ampliando los años!"}

        # 2. PREPARAR PARA EL MODELO (Las 39 columnas)
        X = pd.DataFrame(0, index=np.arange(len(candidatos)), columns=model.feature_names_in_)
        X['release_year'] = candidatos['release_year'].values
        X['rating'] = candidatos['rating'].values
        
        # Llenar géneros y países para que el modelo no se pierda
        for i, (idx, row) in enumerate(candidatos.iterrows()):
            g_col = f"main_genre_{row['genre_1']}"
            c_col = f"main_country_{row['country_1']}"
            if g_col in X.columns: X.at[i, g_col] = 1
            if c_col in X.columns: X.at[i, c_col] = 1
            else: X.at[i, 'main_country_Other'] = 1

        # 3. EL MODELO PREDICE EL SCORE
        candidatos['score_ia'] = model.predict(X)
        
        # 4. DEVOLVER TOP 10 (Solo lo que el usuario quiere ver)
        top_10 = candidatos.sort_values(by='score_ia', ascending=False).head(10)
        return top_10[['title', 'release_year', 'rating', 'score_ia']].to_dict(orient='records')

    except Exception as e:
        return {"error": str(e)}