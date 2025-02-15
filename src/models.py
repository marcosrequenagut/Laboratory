from pydantic import BaseModel

'''Pydantic es especialmente popular cuando se trabaja con APIs (como con FastAPI) porque
facilita la validación de datos de entrada y salida, y convierte datos de entrada
(como los de un JSON) en objetos Python.'''

'''BaseModel es una clase base de Pydantic que se usa para crear modelos de datos que serán 
validados automáticamente.'''

class Project(BaseModel):
    name: str
    time: int