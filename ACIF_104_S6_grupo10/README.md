# Netflix Popularity Predictor 🎬📊

Sistema de aprendizaje automático orientado a la predicción de popularidad de contenidos de Netflix utilizando técnicas de Machine Learning y una arquitectura desacoplada basada en microservicios.

El proyecto integra un modelo predictivo desarrollado con XGBoost, una API REST construida con FastAPI y una interfaz interactiva implementada con Streamlit.

---

# 📌 Objetivo del Proyecto

El objetivo principal del proyecto es predecir la popularidad de películas y series de Netflix a partir de metadatos estructurados, permitiendo apoyar decisiones relacionadas con:

- análisis de contenido,
- priorización de catálogo,
- recomendaciones,
- posicionamiento de contenido,
- análisis de patrones de popularidad.

El sistema busca transformar datos estructurados en información útil mediante modelos de aprendizaje automático supervisado.

---

# 🎯 Problema a Resolver

Las plataformas de streaming operan en un entorno altamente competitivo, donde comprender qué factores influyen en la popularidad de un contenido resulta fundamental para mejorar la experiencia del usuario y optimizar decisiones de negocio.

La popularidad de películas y series depende de múltiples factores, por lo que este proyecto busca modelar parcialmente este fenómeno utilizando variables estructuradas disponibles en datasets públicos.

---

# 📂 Dataset Utilizado

Se utilizó el dataset:

**Netflix Movies and TV Shows till 2025**

El dataset contiene información relacionada con:
- películas,
- series,
- géneros,
- países,
- ratings,
- popularidad,
- años de lanzamiento.

## Características principales

- ~32.000 registros
- Datos de películas y series
- Variables numéricas y categóricas
- Dataset integrado y preprocesado

## Variables utilizadas en el modelo

### Variables de entrada
- `release_year`
- `rating`
- `main_country`
- `main_genre`

### Variable objetivo
- `popularity`

---

# 🧠 Modelos Evaluados

Durante el desarrollo se evaluaron múltiples técnicas de Machine Learning y Deep Learning:

| Modelo | Tipo |
|---|---|
| Regresión Lineal | Machine Learning |
| Random Forest | Machine Learning |
| XGBoost | Boosting |
| CatBoost | Boosting |
| MLP Base | Deep Learning |
| MLP Deep | Deep Learning |
| MLP Regularizada | Deep Learning |

---

# 📈 Métricas Utilizadas

El desempeño de los modelos fue evaluado mediante métricas de regresión:

| Métrica | Descripción |
|---|---|
| MAE | Error absoluto promedio |
| RMSE | Penaliza errores grandes |
| R² | Capacidad explicativa del modelo |

---

# 🏆 Modelo Seleccionado

## XGBoost Regressor

El modelo final seleccionado fue XGBoost debido a que presentó el mejor desempeño relativo durante las pruebas experimentales.

## Resultados principales

| Métrica | Resultado |
|---|---|
| MAE | 32.24 |
| RMSE | 112.13 |
| R² | 0.082 |

## Justificación de selección

XGBoost fue seleccionado porque:
- obtuvo el menor MAE,
- presentó mejor RMSE,
- mostró mejor capacidad de generalización,
- capturó mejor relaciones no lineales,
- tuvo mejor desempeño sobre datos tabulares.

---

# 🚀 Arquitectura del Proyecto

El sistema utiliza una arquitectura desacoplada compuesta por frontend y backend separados.

## 🔹 Backend
Desarrollado con FastAPI.

Responsabilidades:
- cargar modelo entrenado,
- procesar solicitudes,
- ejecutar predicciones,
- retornar resultados al frontend.

## 🔹 Frontend
Desarrollado con Streamlit.

Responsabilidades:
- interfaz gráfica de usuario,
- selección de filtros,
- visualización de resultados,
- interacción con la API.

---

# 🛠️ Tecnologías Utilizadas

## Backend
- FastAPI
- Uvicorn
- Joblib
- Pandas
- NumPy
- Scikit-learn
- XGBoost

## Frontend
- Streamlit

## Machine Learning
- Scikit-learn
- XGBoost
- CatBoost
- TensorFlow / Keras
- SHAP

## Desarrollo
- Python 3
- Google Colab
- GitHub

---

# 📂 Estructura del Repositorio

```text
Acif104/
│
├── Backend/
│   ├── main.py
│
├── Frontend/
│   └── app.py
│
├── notebooks/
│   └── Semana_9_Sumativa_2_fase3.ipynb
│
├── data/
│   └── netflix_movies_detailed_up_to_2025.csv
    └── netflix_tv_shows_detailed_up_to_2025.csv
│
├── docs/
│   └── acif104_s9_BCastillo_SHerrera_RGarrote.pdf
    
 ── models/
│     └── modelo_final_netflix-2.pkl

├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Instalación y Configuración

## 1️⃣ Clonar el repositorio

```bash
git clone <ENLACE_GITHUB>
cd Acif104
```

---

## 2️⃣ Crear entorno virtual

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# ▶️ Ejecución del Proyecto

## 🔹 Ejecutar Backend (FastAPI)

```bash
uvicorn Backend.main:app --reload
```

Backend disponible en:

```text
http://127.0.0.1:8000
```

Documentación Swagger:

```text
http://127.0.0.1:8000/docs
```

---

## 🔹 Ejecutar Frontend (Streamlit)

En otra terminal:

```bash
streamlit run Frontend/app.py
```

Frontend disponible en:

```text
http://localhost:8501
```

---

# 🔄 Flujo del Sistema

1. El usuario ingresa parámetros desde Streamlit.
2. El frontend envía la solicitud al backend.
3. FastAPI procesa la información.
4. El modelo XGBoost genera la predicción.
5. El backend retorna el resultado.
6. Streamlit muestra la recomendación al usuario.

---

# 📌 Ejemplo de Uso

## Entrada del usuario

- Género: Drama
- Año: 2020
- Rating mínimo: 7

## Resultado esperado

El sistema retorna:
- contenidos recomendados,
- popularidad estimada,
- ranking de resultados.

---

# 📡 Ejemplo de Uso API

## Endpoint

```text
POST /predict
```

## Ejemplo JSON

```json
{
  "release_year": 2020,
  "rating": 7,
  "main_country": "United States",
  "main_genre": "Drama"
}
```

---


# 🔍 Interpretabilidad del Modelo

Durante el desarrollo del proyecto se exploraron técnicas de interpretabilidad como SHAP (SHapley Additive Explanations) con el objetivo de analizar la influencia de las variables sobre las predicciones.

Sin embargo, debido al alcance académico y restricciones de las propias bases de datos del proyecto, estas técnicas no fueron integradas en la versión final del sistema. En su lugar, se priorizó el análisis del desempeño mediante métricas de regresión y estrategias de ponderación de muestras (`sample_weight`) para mejorar la sensibilidad del modelo frente a contenidos de alta popularidad.

---

# 📈 Características del Sistema

✅ Arquitectura desacoplada  
✅ API REST con FastAPI  
✅ Interfaz interactiva con Streamlit  
✅ Modelo de Machine Learning integrado  
✅ Sistema reproducible  
✅ Escalable para futuras mejoras  
✅ Estrategias de ponderación mediante sample_weight


---

# 🔮 Mejoras Futuras

- Incorporación de NLP sobre descripciones
- Optimización avanzada de hiperparámetros
- Validación cruzada
- Despliegue en la nube
- Integración con bases de datos
- Recomendaciones personalizadas
- Monitoreo del modelo

---

# 👥 Integrantes

- Beatriz Castillo
- Sofia Herrera
- Rosa Garrote

---

# 📚 Referencias

- Scikit-learn Documentation
- XGBoost Documentation
- FastAPI Documentation
- Streamlit Documentation

---

# 📄 Licencia

Proyecto desarrollado con fines académicos para la asignatura ACIF104.