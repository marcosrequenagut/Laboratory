'''Este código implementa una API REST utilizando FastAPI que interactúa con una base de datos SQLite para gestionar proyectos.
Los proyectos están representados por su nombre y un tiempo asociado.'''

import sqlite3
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from src.models import Project
from src.utils import check_if_project_exists

'''Un contexto asíncrono que se encarga de abrir y cerrar la conexión con la 
base de datos al inicio y al final del ciclo de vida de la aplicación FastAPI. 
Dentro de este contexto se asegura que la tabla Project existe, creando la tabla si no lo hace.'''

@asynccontextmanager
async def sqlite_lifespan(app: FastAPI):
    global DB_CONNECTION
    # Load the ML model
    with sqlite3.connect("project_database.db") as connection:
        print("[DB] Starting connection")
        DB_CONNECTION = connection
        cursor = connection.cursor()

        cursor.execute("""
CREATE TABLE IF NOT EXISTS Project (
    name TEXT PRIMARY KEY,
    time INTEGER
)
""") 
        connection.commit()
        yield
        # Clean DB connection
    print("[DB] Closing connection")


DB_CONNECTION = None

#  lo que garantiza que la conexión a la base de datos se abra al iniciar la app y se cierre al terminar.
app = FastAPI(
    lifespan=sqlite_lifespan
)

# Crea un proyecto en la base de datos si no existe previamente 
# Si el proyecto no existe, crea uno nuevo con tiempo igual a 0
@app.post("/api/v1/project/{project_name}")
def create_project(project_name: str):
    "Create a project, if it already exists returns a 4XX error"
    if check_if_project_exists(project_name):
        raise HTTPException(status_code=418,detail="The project already exists")
    
    with sqlite3.connect("project_database.db") as connection:
        cursor = connection.cursor()
        print(cursor.execute("""SELECT sql
FROM sqlite_schema
WHERE name = 'Project';""").fetchall())
        cursor.execute("INSERT INTO Project (name, time) VALUES ( ?, ?)", (project_name, 0))
        print("Project created succesfully")
        connection.commit()


# Recupera todos los proyectos de la base de datos
@app.get("/api/v1/project")
def list_all_projects() -> list[Project]:

    with sqlite3.connect("project_database.db") as connection:
        cursor = connection.cursor()
        results = cursor.execute("Select * from Project ").fetchall()

        projects = []
        for name, time in results:
            projects.append({"name": name, "time": time})
    
    return projects

# Permite registrar un tiempo para un proyecto concreto
@app.post("/api/v1/project/{project_name}/log")
def log_time(project_name: str, time_to_log: int):

    if not check_if_project_exists(project_name):
        raise HTTPException(status_code=404, detail="Project not found")
    # Ideally, all this should be done on a single transaction
    with sqlite3.connect("project_database.db") as connection:
        cursor = connection.cursor()

        result = cursor.execute("SELECT name, time from Project p where p.name = ?", (project_name,)).fetchone()

        project = Project(name=result[0], time=result[1])

        project.time += time_to_log

        cursor.execute("UPDATE Project set time = ?  where name = ?", (project.time, project.name))

        connection.commit()

    return {"message": "Time updated succesfully"}


# Borramos proyecto
@app.delete("/api/v1/project/{project_name}")
def delete_project(project_name: str):
    if not check_if_project_exists(project_name):
        raise HTTPException(status_code=404, detail="Project not found")

    with sqlite3.connect("project_database.db") as connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM Project WHERE name = ?", (project_name,))
        connection.commit()
        return {"message": "Project deleted successfully"}
# TODO: snapshot

@app.get("/api/v1/project/{project_name}/snapshot")
def create_snapshot(project_name: str):
    pass
