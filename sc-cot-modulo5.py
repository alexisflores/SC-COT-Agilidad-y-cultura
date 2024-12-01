import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Datos simulados
data = {
    "Trimestre": ["T1 2024", "T2 2024", "T3 2024", "T4 2024"],
    "Proyectos Lanzados": [5, 8, 12, 15],
    "Objetivo OKR": [10, 10, 10, 10],  # Objetivo establecido
    "Colaboradores (Dept. A)": [3, 4, 6, 8],
    "Colaboradores (Dept. B)": [2, 4, 6, 7],
}

df = pd.DataFrame(data)

# Configuración del gráfico
fig, ax = plt.subplots(figsize=(10, 6))

# Crear las barras apiladas
ax.bar(df["Trimestre"], df["Colaboradores (Dept. A)"], label="Dept. A", color="skyblue")
ax.bar(
    df["Trimestre"],
    df["Colaboradores (Dept. B)"],
    bottom=df["Colaboradores (Dept. A)"],
    label="Dept. B",
    color="lightgreen",
)

# Agregar línea para Proyectos Lanzados
ax.plot(df["Trimestre"], df["Proyectos Lanzados"], marker="o", label="Proyectos Lanzados", color="blue", linewidth=2)

# Línea del Objetivo OKR
ax.axhline(y=10, color="red", linestyle="--", label="Objetivo OKR (10 proyectos)")

# Etiquetas adicionales para contexto
for idx, value in enumerate(df["Proyectos Lanzados"]):
    ax.text(idx, value + 0.5, str(value), ha="center", fontsize=10, color="blue")

# Título y etiquetas
ax.set_title("Progreso Trimestral de Proyectos Colaborativos Interdisciplinarios", fontsize=14)
ax.set_xlabel("Trimestre", fontsize=12)
ax.set_ylabel("Número de Proyectos / Colaboradores", fontsize=12)

# Añadir descripción del OKR y KPI en el gráfico
description = (
    "OKR: Incrementar proyectos colaborativos interdisciplinarios.\n"
    "KPI: Número de proyectos colaborativos lanzados por trimestre.\n"
    "Interpretación: Muestra el progreso respecto al objetivo y la participación de diferentes departamentos."
)
ax.text(0, -2, description, fontsize=10, color="gray", ha="left", wrap=True)

# Mostrar la leyenda
ax.legend()

# Mostrar el gráfico en Streamlit
st.pyplot(fig)

# Información adicional sobre el OKR y KPI
st.markdown("""
### Información Adicional
- **OKR:** Incrementar proyectos colaborativos interdisciplinarios para fomentar la innovación.
- **KPI:** Número de proyectos colaborativos lanzados por trimestre.
- **Interpretación:** El gráfico ilustra el progreso hacia el objetivo trimestral, mostrando también la colaboración interdisciplinaria mediante barras apiladas por departamento.
""")
