from fastapi import FastAPI
import pandas as pd

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


