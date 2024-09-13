from fastapi import FastAPI #importar fastAPI
from fastapi.responses import HTMLResponse
from movies_list import movies_list

app=FastAPI() #Crea un instancia de la clase fastAPI
app.title= "Mi primera aplicación de peliculas y análisis de datos"
app.version = "0.0.1"

@app.get('/', tags=['Home']) #Se define la ruta
def message(): #Definimos una funcion de la ruta
    return HTMLResponse('<h1> Hello World </h1>')

@app.get('/movies', tags=['Movies'])
def movies():
    return movies_list

@app.get('/movies/{_id}',tags=['Movies'])
def get_movie(id:int):
    for item in movies_list:
        if item['id']==id:
            return item
    return []
