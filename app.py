import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')

st.header('Datos de venta de coches')

hist_button = st.button('Construir histograma')

if hist_button:

    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    fig = px.histogram(car_data, x="odometer")

    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:

    st.write(
        'Creación de un gráfico de dispersion para el conjunto de datos de anuncios de venta de coches')

    fig = px.scatter(car_data, x="days_listed", y="price")

    st.plotly_chart(fig, use_container_width=True)

show_hist = st.checkbox('Mostrar histograma')
show_scatter = st.checkbox('Mostrar gráfico de dispersión')

if show_hist:
    st.write('Construir un histograma para la columna odómetro')

    fig = px.histogram(car_data, x="odometer")

    st.plotly_chart(fig, use_container_width=True)

if show_scatter:
    st.write(
        'Construir de un gráfico de dispersion que compare los dias listado de los vehiculos vs el precio')

    fig = px.scatter(car_data, x="days_listed", y="price")

    st.plotly_chart(fig, use_container_width=True)
