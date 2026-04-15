import streamlit as st
import requests

st.set_page_config(page_title="Netflix AI Finder", page_icon="🎬")
st.title("🎬 Netflix AI Recommendation")

# BARRA LATERAL PARA FILTROS
st.sidebar.header("Filtros de Búsqueda")

generos_reales = ['Action', 'Adventure', 'Animation', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy', 'Horror', 'Romance', 'Science Fiction', 'Thriller']
seleccion_gen = st.sidebar.multiselect("Géneros", generos_reales, default=['Drama'])

# Filtros de Año y Rating
rango_anio = st.sidebar.slider("Rango de Años", 1990, 2025, (2015, 2025))
min_rating = st.sidebar.slider("Rating Mínimo", 0.0, 10.0, 5.0)

if st.button("¡Encontrar mi Top 10!"):
    if not seleccion_gen:
        st.warning("Selecciona al menos un género en la barra lateral.")
    else:
        with st.spinner('La IA está analizando el catálogo...'):
            try:
                payload = {
                    "generos": seleccion_gen,
                    "anio_min": rango_anio[0],
                    "anio_max": rango_anio[1],
                    "rating_min": min_rating
                }
                res = requests.post("http://127.0.0.1:8000/recommend", json=payload)
                datos = res.json()

                if "error" in datos:
                    st.error(datos["error"])
                else:
                    st.write(f"### 🏆 Top 10 Recomendaciones ({rango_anio[0]}-{rango_anio[1]})")
                    for peli in datos:
                        with st.expander(f"⭐ {peli['title']}"):
                            st.write(f"**Año:** {peli['release_year']}")
                            st.write(f"**Rating Original:** {peli['rating']}")
                            st.write(f"**Popularidad IA:** {peli['score_ia']:.2f}")
            except Exception as e:
                st.error(f"Error de conexión: {e}")