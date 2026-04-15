# Netflix Popularity Predictor - Sistema Desacoplado (API + Web)

Este proyecto implementa un sistema de aprendizaje automático para predecir la popularidad de contenidos en Netflix, utilizando una arquitectura de microservicios separando el **Backend** (Lógica y Modelo) del **Frontend** (Interfaz de Usuario).

## 🚀 Arquitectura del Proyecto
- **Backend:** Desarrollado con **FastAPI**. Procesa las peticiones y ejecuta el modelo XGBoost.
- **Frontend:** Desarrollado con **Streamlit**. Ofrece una interfaz intuitiva para el usuario.
- **Modelo:** XGBoost (seleccionado por su bajo MAE de 32.24 en la fase de pruebas).

## 🛠️ Instalación y Configuración

### 1. Clonar el repositorio y preparar el entorno
```bash
git clone <enlace_github>
cd Acif104_

### Instalación

```bash
python -m venv venv
```

### Windows
```bash
venv\Scripts\activate
```

### Linux / Mac
```bash
source venv/bin/activate
```

### Instalar dependencias:

```bash
pip install -r requirements.txt
```
Ejecutar:

```bash
uvicorn Backend.main:app --reload (ejecutar el backend)
streamlit run Frontend/app.py (ejecutar el frontend)
```

Abrir en el navegador:

```text
http://localhost:8501 (Streamlit)
```
