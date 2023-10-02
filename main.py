from fastapi import FastAPI

app = FastAPI()

#http://127.0.0.1:8000

@app.get("/")
def index():
    return {"Hola! soy César Forero", 
            "e-mail: cesarjf18@hotmail.com"
            "GitHub: MrNobody-505" }


@app.get('/PlayTimeGenre/{genero}')
def PlayTimeGenre(genero: str):
    import pandas as pd
    df_merged = pd.read_csv("df_merged.csv")
    filtro_genero = df_merged[df_merged[genero] == True]
    grouped_df = filtro_genero.groupby('year')['playtime_forever'].max().reset_index()
    max_playtime_year = grouped_df.loc[grouped_df['playtime_forever'].idxmax()].astype(int)
    texto_genero = f"El anio con más tiempo de juego para el género {genero} es {max_playtime_year['year']} con {max_playtime_year['playtime_forever']} unidades de tiempo jugadas."
    return texto_genero