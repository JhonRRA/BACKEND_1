# FastAPI es un FrameWork

from fastapi import FastAPI

app = FastAPI()


# Accediendo al contexto de FastAPI
@app.get("/") # Accediendo a un lugar que es una barra, todo lo que hacemos cuando entramos a un explorador y buscamos en la web

# Creando una operacion (funcion)
async def root(): #Tiene que ser asincrono (que haga lo que deba hacer cuando pueda)
    return 'Hola Mundo'