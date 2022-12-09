from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from databases import Database
import pandas as pd

database = Database("sqlite:///basedata.sqbpro")
app= FastAPI ()

@app.get("/get_count_plataform/")
async def count_plataforma(plataforma:str):
    url ='file:///home/guille/Escritorio/docker/Analisis/df_plataformas_concatenadas'
    df = pd.read_csv(url)
    df_plataforma = df.query("plataforma == @plataforma")
    contador = df_plataforma.type.value_counts(sort=True)
    return {plataforma,str(contador[0]),contador[1]}