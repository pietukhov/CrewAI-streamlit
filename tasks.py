from crewai import Task
class ResearchCrewTasks:


    def research_task(self, agent, inputs):
      return Task(
          agent=agent,
          description=f"Recopilar y documentar sistemáticamente noticias y artículos actuales y relevantes de diversas fuentes sobre {inputs}. Utilizar todas las herramientas digitales disponibles para asegurar una cobertura exhaustiva.",
          expected_output=f"""
  Informe de Investigación Detallado sobre {inputs}
  1. **Resumen Ejecutivo**: Un resumen conciso de los resultados de la investigación, destacando los hallazgos más críticos e importantes y las conclusiones extraídas de los datos recopilados.
  2. **Introducción**: Información de fondo sobre por qué la investigación sobre {inputs} es crucial en este momento. Incluya el alcance de la investigación y los objetivos principales.
  
  # Sección de Metodología
  3. **Metodología**:
    - **Fuentes Utilizadas**: Liste todas las fuentes utilizadas, incluyendo bases de datos digitales, sitios web de noticias y cualquier suscripción o herramienta especializada.
    - **Criterios de Búsqueda**: Describa los criterios de búsqueda y palabras clave utilizadas para recopilar la información relevante.
    - **Proceso de Recopilación de Datos**: Describa los pasos seguidos en el proceso de recopilación de datos, incluyendo cualquier herramienta de automatización o software utilizada.
  
  # Sección de Hallazgos
  4. **Hallazgos**:
    - **Información Clave Recopilada**: Resume la información clave recopilada de cada fuente, categorizada por relevancia e impacto en el tema.
    - **Tendencias Identificadas**: Discuta cualquier tendencia o similitud encontrada en diferentes fuentes.
  
  # Sección de Análisis
  5. **Análisis**:
    - **Relación con Tendencias Actuales**: Analiza cómo los hallazgos se relacionan con tendencias o desarrollos actuales en el campo.
    - **Gaps de Información**: Destaque cualquier vacío en la información que requiera investigación adicional.
  
  # Sección de Conclusión
  6. **Conclusión**:
    - **Resumen de Hallazgos**: Repita brevemente los hallazgos más importantes y sus implicaciones.
    - **Recomendaciones para Investigación Adicional**: Sugiera áreas donde la investigación adicional podría ser beneficiosa basándose en vacíos o tendencias emergentes notadas durante la investigación.
  
  # Sección de Referencias
  7. **Referencias**:
    - **Citaciones Completas**: Proporciona citas completas para todas las fuentes utilizadas, formateadas según un estándar académico reconocido.
          """
      )



    def analysis_task(self, agent, context):
      return Task(
        agent=agent,
        context=context,
        description="Evaluar críticamente la precisión, relevancia y profundidad de la información recopilada. Emplear metodologías avanzadas de análisis de datos para aumentar el valor de la información, asegurando que cumpla con los estándares exigentes requeridos para la evaluación experta.",
        expected_output=f"""
  Informe de Análisis Integral:
  1. **Resumen Ejecutivo**: Un resumen que resume los principales hallazgos, incluyendo la precisión, relevancia y profundidad de la información analizada.

  # Sección de Evaluación de Precisión
  2. **Evaluación de Precisión**:
    - **Verificación de Datos**: Evaluar la veracidad y corrección de los datos recopilados, identificando cualquier discrepancia o inconsistencia.
    - **Confiabilidad de Fuentes**: Evaluar la confiabilidad de las fuentes utilizadas, proporcionando una puntuación de credibilidad para cada una.

  # Sección de Análisis de Relevancia
  3. **Análisis de Relevancia**:
    - **Alineación Contextual**: Analizar cómo la información se alinea con las preguntas de investigación actuales y objetivos.
    - **Actualidad**: Verificar que la información esté actualizada y discutir su significado en el contexto actual.

  # Sección de Evaluación de Profundidad
  4. **Evaluación de Profundidad**:
    - **Ampliación**: Evaluar el alcance de la información y si cubre todos los aspectos necesarios del tema.
    - **Insightfulness**: Evaluar la profundidad de las ideas proporcionadas por la información, incluyendo cualquier implicación subyacente o patrones ocultos.

  # Sección de Revisión Metodológica
  5. **Revisión Metodológica**:
    - **Técnicas Utilizadas**: Enumerar y criticar las metodologías de análisis de datos empleadas, sugiriendo mejoras o alternativas si fuera necesario.
    - **Manipulación de Datos**: Discutir cómo se procesó y analizó la información, incluyendo cualquier herramienta o software utilizada.

  # Sección de Recomendaciones
  6. **Recomendaciones**:
    - **Investigación Adicional**: Sugiera áreas donde se necesita información adicional y proponga métodos para recopilar estos datos.
    - **Aplicaciones Prácticas**: Proporcionar recomendaciones sobre cómo los hallazgos pueden ser utilizados prácticamente por partes interesadas o en futuras investigaciones.

  # Sección de Conclusión
  7. **Conclusión**:
    - **Resumen de Puntos Clave**: Reiterar brevemente los hallazgos más importantes y sus implicaciones para el proyecto de investigación.
    - **Direcciones Futuras**: Sugerir cómo los hallazgos pueden informar futuras investigaciones y procesos de toma de decisiones en el campo relevante.

  # Sección de Apéndices
  8. **Apéndices**:
    - **Tablas y Figuras**: Incluir tablas, gráficos y diagramas exhaustivos que se utilizaron en el análisis.
    - **Documentación de Fuentes**: Proporcionar citas detalladas y referencias para todas las fuentes y datos utilizados en el informe.
          """
    )



    def writing_task(self, agent, context):
        return Task(
            agent=agent,
            context=context,
            description="Sintetizar la información proporcionada por el Investigador y mejorada por el Analista en un resumen claro, bien estructurado y persuasivo. Incluir los principales hallazgos y cite adecuadamente todas las fuentes para asegurar la credibilidad y trazabilidad.",
            expected_output=f"""
    Informe de Resumen Integral:
    1. **Introducción**:
      - **Antecedentes**: Proporcionar una breve introducción al tema, esbozando el alcance y propósito de la investigación inicial.
      - **Objetivos**: Reiterar los objetivos principales de la investigación para establecer el contexto para los hallazgos.

    # Sección de Síntesis de Investigación y Análisis
    2. **Síntesis de Investigación y Análisis**:
      - **Principales Hallazgos**: Presentar los principales hallazgos de la fase de investigación, enfatizando puntos de datos significativos, tendencias e ideas.
      - **Mejoras Analíticas**: Discutir cómo la fase de análisis agregó valor a los hallazgos iniciales, incluyendo cualquier nuevo conocimiento o comprensión derivada de la examinación más profunda.

    # Sección de Discusión
    3. **Discusión**:
      - **Implicaciones**: Explorar las implicaciones de los hallazgos en un contexto más amplio, discutiendo posibles impactos en el campo, la industria o la sociedad.
      - **Evaluación Crítica**: Evaluar críticamente los hallazgos, destacando fortalezas, debilidades y cualquier punto controvertido que surgió durante las fases de investigación y análisis.

    # Sección de Recomendaciones
    4. **Recomendaciones**:
      - **Pasos Accionables**: Proporcionar recomendaciones claras y prácticas basadas en los hallazgos y discusiones. Estas deben ser prácticas y adaptadas a partes interesadas específicas o implicaciones políticas.
      - **Investigación Futura**: Sugerir áreas para futuras investigaciones que podrían construir sobre los hallazgos actuales, abordando cualquier brecha o pregunta sin resolver.

    # Sección de Conclusión
    5. **Conclusión**:
      - **Resumen de Hallazgos**: Resumir los principales puntos del informe, reforzando la significación y fiabilidad de la investigación realizada.
      - **Pensamientos Finales**: Ofrecer pensamientos finales que subrayen la importancia de los hallazgos y el potencial para trabajo futuro en este área.

    # Sección de Referencias
    6. **Referencias**:
      - **Citaciones**: Incluir una lista detallada de todas las fuentes citadas en el documento, formateadas según un estándar académico o profesional reconocido.
      - **Anotaciones de Fuentes**: Opcionalmente, proporcionar anotaciones para fuentes clave, explicando su relevancia y fiabilidad.

    # Sección de Apéndices (si corresponde)
    7. **Apéndices**:
      - **Documentos de Apoyo**: Adjuntar cualquier documento de apoyo, tabla de datos o material suplementario mencionado en el informe.
      - **Glosario de Términos**: Incluir un glosario de términos clave y definiciones utilizadas en todo el informe para claridad.
            """
        )





