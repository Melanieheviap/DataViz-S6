import os

import streamlit as st
import pandas as pd

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from crea_db import CargasBip

# Esto solo para hacer referencia a una base de datos SQLlite local:
ruta_mi_bd = os.path.abspath("./cargas.db")
mi_bd = f"sqlite:///{ruta_mi_bd}"

# Crear conexión a BD
# Se quita el parámetro "future=True", por compatibilidad con Pandas 1.x
engine = create_engine(mi_bd)
# Crear sesión a BD
session = Session(engine)

# Selección de comunas
sel_comunas = ["PROVIDENCIA", "SANTIAGO", "LA FLORIDA"]

# Obtener los nombres de las Comunas
sql_comuna = select(CargasBip.COMUNA).where(CargasBip.COMUNA.in_(sel_comunas) )
sql_comuna = sql_comuna.distinct()
sql_comuna = sql_comuna.order_by(CargasBip.COMUNA)


# Consultar registros directo desde Pandas
datos_comunas = pd.read_sql_query(sql=sql_comuna, con=engine)

# Configurar Aplicación
st.set_page_config(
  layout="wide"
)

# Mostrar datos en la Aplicación
st.header("Información desde Base de Datos")

st.info("Puntos de Carga")
st.write(datos_comunas)
