import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Datos simulados
data = {
    "Trimestre": ["T1 2024", "T2 2024", "T3 2024", "T4 2024"],
    "Proyectos Lanzados": [5, 8, 12, 15],
    "Objetivo OKR": [10, 10, 10, 10],  # Objetivo establecido
    "Colaboradores (Dept. A)": [3, 4, 6, 8],
    "Colaboradores (Dept. B)": [2, 3, 4, 5],
}

df = pd.DataFrame(data)

# Configuración del gráfico
fig, ax = plt.subplots(figsize=(10, 6))

# Barras apiladas
ax.bar(df["Trimestre"], df["Colaboradores (Dept. A)"], label="Dept. A", color="skyblue")
ax.bar(
    df["Trimestre"],
    df["Colaboradores (Dept. B)"],
    bottom=df["Colaboradores (Dept. A)"],
    label="Dept. B",
    color="lightgreen",
)

# Línea de progreso de proyectos
ax.plot(df["Trimestre"], df["Proyectos Lanzados"], marker="o", label="Proyectos Lanzados", color="blue")

# Línea del objetivo
ax.axhline(y=10, color="red", linestyle="--", label="Objetivo OKR (10 proyectos)")

# Configuración del gráfico
ax.set_title("Progreso Trimestral de Proyectos Colaborativos Interdisciplinarios", fontsize=14)
ax.set_xlabel("Trimestre", fontsize=12)
ax.set_ylabel("Número de Proyectos / Colaboradores", fontsize=12)
ax.legend()

# Mostrar el gráfico en Streamlit
st.pyplot(fig)

# Información descriptiva del OKR y KPI
st.markdown("""
### Información del OKR y KPI
- **OKR:** Incrementar proyectos colaborativos interdisciplinarios para fomentar la innovación.
- **KPI:** Número de proyectos colaborativos lanzados por trimestre.
- **Interpretación:** El gráfico muestra el número de proyectos lanzados y su comparación con el objetivo establecido. Las barras apiladas indican la distribución de colaboradores de diferentes departamentos, reflejando el nivel de interdisciplinariedad alcanzado en cada trimestre.
""")
