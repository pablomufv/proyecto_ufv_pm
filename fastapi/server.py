"""
Define las clases que contienen los datos del .csv y establece el servicio que devuelve los datos
"""

import shutil

import io
from fastapi.responses import JSONResponse
from fastapi import FastAPI, File, UploadFile,Form
import pandas as pd
from typing import  List

from pydantic import BaseModel as PydanticBaseModel

#la clase base para definir modelos en Pydantic. Al heredar de esta clase, 
# BaseModel tendrá toda la funcionalidad de validación, conversión de tipos, etc que provee Pydantic
class BaseModel(PydanticBaseModel):
	
    #La clase interna Config sirve para configurar el comportamiento del modelo Pydantic
    class Config:
    
    #indica que el modelo permitirá tipos de datos arbitrarios, no sólo tipos nativos de Python como ints, strings, etc.
    # Esto es útil cuando se desean guardar objetos custom o de otros paquetes como tipos de datos
        arbitrary_types_allowed=True

#Esta clase define los atributos y sus respectivos tipos de datos para un worker
class worker(BaseModel):
    #titulo:str
    work_year:int
    experience_level:str
    employment_type:str
    job_title:str
    salary:int
    salary_currency:str
    salary_in_usd:int
    employee_residence:str
    remote_ratio:int
    company_location:str
    company_size:str

#Define una clase Listadoworkers que hereda de la clase BaseModel
class Listadoworkers(BaseModel):

#Define un atributo workers con el tipo List de la librería typing
    workers=List[worker]

#Inicializa la aplicación FastAPI con la descripción y la versión del servidor
app=FastAPI(
    title="Servidor de datos", #Establece el título del servidor de datos
    description="""Servimos datos de workers, pero podríamos hacer muchas otras cosas, la la la.""",
    version="0.1.0", #Establece la versión del servidor de datos
)

#Define un endpoint en la aplicación FastAPI que utiliza el método HTTP GET para acceder a la URL /retrieve_data/
@app.get("/retrieve_data/")

#Esta línea define una función para implementar el endpoint de recuperación de datos
def retrieve_data ():
    
    #Esta línea lee el archivo CSV utilizando la biblioteca pandas y almacena los datos en una variable todosmisdatos
    todosmisdatos=pd.read_csv('./data_science_jobs_salaries.csv',sep=',')

    #Esta línea reemplaza todos los valores nulos en el DataFrame todosmisdatos con el valor 0
    todosmisdatos=todosmisdatos.fillna(0)
    
    #Esta línea convierte el DataFrame en un diccionario, donde cada clave es el índice del DataFrame y cada valor es una lista de datos para esa fila.
    todosmisdatosdict=todosmisdatos.to_dict(orient='records')
    
    #Esta línea crea un objeto Listadoworkers instanciando la clase Listadoworkers
    listado=Listadoworkers()
    
    #Esta línea asigna el diccionario todosmisdatosdict como el atributo
    listado.workers=todosmisdatosdict
    return listado
    
    
    
    
    
    
