import os
from decouple import config
from crewai import Crew, Process
from textwrap import dedent
from agents import ResearchCrewAgents
from tasks import ResearchCrewTasks
import streamlit as st

# Configuración de variables de entorno
# Función para verificar si el archivo secrets.toml existe
def secrets_file_exists():
    secrets_path = os.path.join('.streamlit', 'secrets.toml')
    return os.path.isfile(secrets_path)

# Intentar obtener las claves de API desde st.secrets si el archivo secrets.toml existe
if secrets_file_exists():
    try:
        os.environ["OPENAI_API_KEY"] = st.secrets['OPENAI_API_KEY']
        os.environ["SERPER_API_KEY"] = st.secrets['SERPER_API_KEY']
    except KeyError:
        # Si las claves no están en secrets.toml, intentar obtenerlas de variables de entorno
        openai_api_key = os.environ.get('OPENAI_API_KEY')
        serper_api_key = os.environ.get('SERPER_API_KEY')
        
        if openai_api_key and serper_api_key:
            os.environ["OPENAI_API_KEY"] = openai_api_key
            os.environ["SERPER_API_KEY"] = serper_api_key
        else:
            # Si las claves no están en variables de entorno, pedirlas al usuario
            os.environ["OPENAI_API_KEY"] = st.sidebar.text_input('Introduce la clave de API de OpenAI', type='password')
            os.environ["SERPER_API_KEY"] = st.sidebar.text_input('Introduce la clave de API de Serper', type='password')
else:
    # Si el archivo secrets.toml no existe, intentar obtener las claves de variables de entorno
    openai_api_key = os.environ.get('OPENAI_API_KEY')
    serper_api_key = os.environ.get('SERPER_API_KEY')
    
    if openai_api_key and serper_api_key:
        os.environ["OPENAI_API_KEY"] = openai_api_key
        os.environ["SERPER_API_KEY"] = serper_api_key
    else:
        # Si las claves no están en variables de entorno, pedirlas al usuario
        os.environ["OPENAI_API_KEY"] = st.sidebar.text_input('Introduce la clave de API de OpenAI', type='password')
        os.environ["SERPER_API_KEY"] = st.sidebar.text_input('Introduce la clave de API de Serper', type='password')

# Verificar si las claves de API están disponibles
if not os.environ["OPENAI_API_KEY"] or not os.environ["SERPER_API_KEY"]:
    st.sidebar.error("Por favor, proporciona las claves de API necesarias.")
    st.stop()

class ResearchCrew:
    def __init__(self, inputs):
        # Inicializar la tripulación de investigación con entradas del usuario
        self.inputs = inputs
        self.agents = ResearchCrewAgents()
        self.tasks = ResearchCrewTasks()

    def run(self):
        # Inicializar agentes
        researcher = self.agents.researcher()
        analyst = self.agents.analyst()
        writer = self.agents.writer()

        # Inicializar tareas con agentes respectivos
        research_task = self.tasks.research_task(researcher, self.inputs)
        analysis_task = self.tasks.analysis_task(analyst, [research_task])
        writing_task = self.tasks.writing_task(writer, [analysis_task])

        # Formar la tripulación con agentes y tareas definidos
        crew = Crew(
            agents=[researcher, analyst, writer],
            tasks=[research_task, analysis_task, writing_task],
            process=Process.sequential
        )

        # Ejecutar la tripulación para llevar a cabo el proyecto de investigación
        return crew.kickoff()

if __name__ == "__main__":
    print("Bienvenida a la configuración de la tripulación de investigación")
    print("---------------------------------------")
    tema_principal = input("Por favor, ingresa el tema principal de tu investigación: ")
    preguntas_detalladas = input("¿Cuáles son las preguntas específicas o subtemas que deseas explorar? ")
    puntos_clave = input("¿Hay algún punto clave o información específica que deba incluirse en la investigación? ")

    inputs = f"Tema de investigación: {tema_principal}\nPreguntas detalladas: {preguntas_detalladas}\nPuntos clave: {puntos_clave}"
    research_crew = ResearchCrew(inputs)
    resultado = research_crew.run()

    print("\n\n##############################")
    print("## Aquí están los resultados de tu proyecto de investigación:")
    print("##############################\n")
    print(resultado)
