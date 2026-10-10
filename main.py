from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Any, Optional

app = FastAPI()
origins = [
    "http://localhost:3000",      
]   

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,        # Lista de dominios permitidos.
    allow_credentials=True,       # Permite el envío de cookies o headers de autorización 
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"]
)

# -- Clases-- #

class AuthorModel(BaseModel):
    name : str
    contact : list[str]
    tel : str #telefono
    biography : str

class SkillModel(BaseModel): 
    hardware_skills : list[str] #skills de hardware
    software_skills : list[str] #skills de software
    soft_skills : Optional[list[str]] = None #habilidades blandas 

class EducationModel(BaseModel): 
    high_school : str
    university : str
    certifications : list[str]

class ProfileResponse(BaseModel):
    author : AuthorModel
    skills : SkillModel
    edu : EducationModel

class StandardResponse(BaseModel): 
    status: str
    message: str
    data: Any
    meta: Optional[dict] = None

class ProjectModel(BaseModel):
    project_name : str
    description : str
    status: str
    stack : Optional[list[str]] = None #Solo si es de programacion
    link : str
    demo : str

all_projects_hard: list[ProjectModel] = []
all_projects_soft: list[ProjectModel] = []

#--Metodos--#
#--Pagina inicial--# 
@app.get("/", response_model=StandardResponse)
def sobre_mi(): #pagina principal/inicial

    datos_autor = AuthorModel(
        name = "Gabriel Andres Cumes de León",
        contact =  ["github", "linkedin"],
        tel = "+502 3400-8702",
        biography =  "Especialista en la intersección del hardware y software. Diseñando arquitecturas robustas desde el silicio hasta la nube. Mi enfoque es la eficiencia, precisión y confiabilidad en sistemas complejos."
    )
    skills_list = SkillModel(
        hardware_skills =  ["Diseño de PCB.", "Microcontroladores","Simulacion de circuitos.","Procesamiento de señales."],
        software_skills = ["python.", "C/C++.","SQL.","FastAPI"]

    )
    education_list = EducationModel(
        high_school = "Perito En electronica",
        university =  "Estudiante de Ingenieria Electronica",
        certifications =  ["python", "html", "css", "SQL"]
    )

    profile = ProfileResponse(
        author = datos_autor,
        skills = skills_list,
        edu = education_list
    )

    return StandardResponse(
        status= "success",
        message= "Datos recuperados",
        data= profile,
    )

#--Proyectos Hardware/Electronica--#

@app.get("/hardware_projects", response_model=StandardResponse)
def list_hardw():
  
    return StandardResponse(
           status= "success",
           message= "Proyectos encontrados" if all_projects_hard else "No hay proyectos disponibles",
           data= all_projects_hard,
       )

#--Proyectos Software/Programacion--#

@app.get("/software_projects", response_model=StandardResponse)
def list_softw():
    return StandardResponse(
            status= "success",
            message= "Proyectos encontrados" if all_projects_soft else "No hay proyectos disponibles",
            data= all_projects_soft,
           )
