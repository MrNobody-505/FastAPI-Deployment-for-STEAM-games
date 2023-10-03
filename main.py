from fastapi import FastAPI
import pandas as pd
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI()
df_merged = pd.read_csv("df_merged.csv")
df_sample = pd.read_csv("sample_df.csv")

#http://127.0.0.1:8000

@app.get("/")
def index():
    return {"Hola! soy César Forero", 
            "e-mail: cesarjf18@hotmail.com"
            "GitHub: MrNobody-505" }


@app.get('/PlayTimeGenre/{genero}')
def PlayTimeGenre(genero: str):
    df_merged = pd.read_csv("df_merged.csv")
    filtro_genero = df_merged[df_merged[genero] == True]
    grouped_df = filtro_genero.groupby('year')['playtime_forever'].max().reset_index()
    max_playtime_year = grouped_df.loc[grouped_df['playtime_forever'].idxmax()]
    Anio = max_playtime_year['year']
    tiempo = max_playtime_year['playtime_forever']
    return {'Genero': genero, 'Anio': Anio, 'Tiempo': tiempo}


@app.get('/UserForGenre/{genero}')
def UserForGenre(genero: str):
    filtro_genero = df_merged[df_merged[genero] == True]
    grouped_df = filtro_genero.groupby('user_id')['playtime_forever'].sum().reset_index()
    max_playtime_user = grouped_df.loc[grouped_df['playtime_forever'].idxmax(), 'user_id']

    playtime_per_year = filtro_genero.groupby('year')['playtime_forever'].sum().reset_index().values.tolist()
    
    return {'Genero': genero, 'Usuario con más horas jugadas': max_playtime_user, 'Acumulación de tiempo jugado por año': playtime_per_year}


@app.get('/recomendacion_juego/{id_de_producto}')

def recomendacion_juego(id_de_producto):
    item_profiles = df_sample.groupby('item_id').agg({'sentiment_score': 'mean', 'item_name': 'first'}).reset_index()
    if item_profiles.empty:
    print("No se encontró un juego similar")
    else:
    similarity_matrix = cosine_similarity(item_profiles[['sentiment_score']])
    item_index = item_profiles[item_profiles['item_id'] == id_de_producto].index
    if item_index.empty:
    print("No existe este juego.")
    return [], []
    item_index = item_index[0]
    similar_items_indices = similarity_matrix[item_index].argsort()[::-1][1:6]
    recommendations = sample_df.loc[similar_items_indices, 'item_id'].tolist()
    recommendation_names = sample_df.loc[similar_items_indices, 'item_name'].tolist()
    return recommendations, recommendation_names