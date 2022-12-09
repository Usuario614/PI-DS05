from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from databases import Database
import pandas as pd

database = Database("sqlite:///basedata.sqbpro")
app= FastAPI ()

@app.get("/get_count_plataform/")
async def count_plataforma(plataforma:str):
    url ='file:///'
    df = pd.read_csv(url)
    plataformas = df.query("plataforma == @plataforma")
    contador = plataformas.type.value_counts(sort=True)
    return {plataforma,str(contador[0]),contador[1]}