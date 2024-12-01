import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Datos simulados del KPI
data_cultura = {
    "Periodo": ["Q1", "Q2", "Q3", "Q4"],
    "Proyectos Colaborativos": [5, 7, 10, 12],  # Progreso actual
    "Meta Proyectos": [6, 8, 11, 14]  # Metas establecidas
}

# Crear un DataFrame
df_cultura = pd.DataFrame(data_cultura)

# Visualización en Streamlit
st.write("### Evolución de Proyectos Colaborativos")
st.write("Este gráfico muestra el progreso actual y las metas establecidas para el número de proyectos colaborativos lanzados por trimestre.")

# Gráfico de líneas
fig_cultura, ax_cultura = plt.subplots(figsize=(8, 5))
ax_cultura.plot(df_cultura["Periodo"], df_cultura["Proyectos Colaborativos"], marker='o', label="Proyectos Colaborativos", color="blue")
ax_cultura.plot(df_cultura["Periodo"], df_cultura["Meta Proyectos"], marker='x', label="Meta Proyectos", color="orange", linestyle="--")
ax_cultura.set_title("Evolución de Proyectos Colaborativos", fontsize=14)
ax_cultura.set_xlabel("Periodo", fontsize=12)
ax_cultura.set_ylabel("Número de Proyectos", fontsize=12)
ax_cultura.legend()
ax_cultura.grid(True, linestyle="--", alpha=0.6)

# Mostrar el gráfico
st.pyplot(fig_cultura)
