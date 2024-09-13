from fastapi import FastAPI #importar fastAPI

app=FastAPI() #Crea un instancia de la clase fastAPI
app.title= "Mi primera aplicación de peliculas y análisis de datos"
app.version = "0.0.1"

@app.get('/', tags=['Home']) #Se define la ruta
def message(): #Definimos una funcion de la ruta
    return "Hello World"

