import streamlit as st
from main import ResearchCrew  # Import the ResearchCrew class from main.py
import os

st.title('Configuración del equipo de investigación')

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

# Crear la sección de entrada de usuario en la barra lateral
with st.sidebar:
    # Título para la sección de entrada de usuario
    st.header('Introduce detalles de la investigación')
    
    # Campos de entrada para la investigación
    topic = st.text_input("Tema principal de la investigación:")
    detailed_questions = st.text_area("Preguntas específicas o subtemas que se desean explorar:")
    key_points = st.text_area("Puntos clave o información específica necesaria:")

# Botón para ejecutar la investigación
if st.button('Ejecutar investigación'):
    # Verificar si todos los campos están llenos
    if not topic or not detailed_questions or not key_points:
        st.error("Por favor, complete todos los campos.")
    else:
        # Procesar la investigación
        inputs = f"Investigación: {topic}\nPreguntas detalladas: {detailed_questions}\nPuntos clave: {key_points}"
        research_crew = ResearchCrew(inputs)
        result = research_crew.run()
        
        # Mostrar los resultados de la investigación
        st.subheader("Resultados del proyecto de investigación:")
        st.write(result)
