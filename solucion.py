# Importación de librerías.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Lectura de los archivos.
dfDatos = pd.read_csv(
    "C:\\Users\\alexa\\Documents\\Alexa\\Escuela\\ITAM\\Desarrollo de Aplicaciones Informáticas\\Proyecto2\\P_Data_Extract_From_Health_Nutrition_and_Population_Statistics\\361d8e4b-91be-4bc2-bdca-fbbf19126345_Data.csv",
    encoding="Latin-1",
)
dfDescr = pd.read_csv(
    "C:\\Users\\alexa\\Documents\\Alexa\\Escuela\\ITAM\\Desarrollo de Aplicaciones Informáticas\\Proyecto2\\P_Data_Extract_From_Health_Nutrition_and_Population_Statistics\\361d8e4b-91be-4bc2-bdca-fbbf19126345_Series - Metadata.csv",
    encoding="Latin-1",
)

# Países: Estados Unidos, China, México, Guatemala y Alemania.
# Indicadores: Población (masculina, feminia, total), tasa de mortalidad, gasto de salud privado, gasto de salud gubernamental, tasa de suicidio y población mayor a los 80 años.
# Años: 2000-2019.

paises = ["United States", "China", "Mexico", "Guatemala", "Germany"]
indicadores = [
    "SP.POP.TOTL",
    "SP.POP.TOTL.MA.IN",
    "SP.POP.TOTL.FE.IN",
    "SP.DYN.CDRT.IN",
    "SH.XPD.PVTD.CH.ZS",
    "SH.XPD.GHED.PC.CD",
    "SH.STA.SUIC.P5",
    "SP.POP.80UP.FE.5Y",
    "SP.POP.80UP.MA.5Y",
]
years = [
    "2000",
    "2001",
    "2002",
    "2003",
    "2004",
    "2005",
    "2006",
    "2007",
    "2008",
    "2009",
    "2010",
    "2011",
    "2012",
    "2013",
    "2014",
    "2015",
    "2016",
    "2017",
    "2018",
    "2019",
]

# Filtrado de los datos.
dfDatosFil = dfDatos[
    (dfDatos["Country Name"].isin(paises)) & (dfDatos["Series Code"].isin(indicadores))
]
dfDescrFil = dfDescr[
    (dfDescr["Country Name"].isin(paises)) & (dfDescr["Series Code"].isin(indicadores))
]

# 3) Indicadores en una única gráfica por país.
for pais in paises:
    datos_pais = dfDatosFil[dfDatosFil["Country Name"] == pais]  # filtrar por país.
    descr_pais = dfDescrFil[dfDescrFil["Country Name"] == pais]  # filtrar por país.

    plt.figure(figsize=(12, 8))  # tamaño de la gráfica.
    plt.title(f"Indicadores {pais}")  # título de la gráfica.

    for indicador in indicadores:
        datos_indicador = (
            datos_pais[datos_pais["Series Code"] == indicador]
            .iloc[:, 44:64]
            .values.flatten()
        )  # filtrar por indicador.
        descr_indicador = descr_pais[descr_pais["Series Code"] == indicador][
            "Series Code"
        ].values[
            0
        ]  # filtrar por indicador.

        plt.plot(years, datos_indicador)  # graficar los datos.

    plt.xlabel("Año")  # etiqueta del eje x.
    plt.ylabel("Valor")  # etiqueta del eje y.
    plt.grid()  # agregar cuadrícula.
    plt.legend(loc="upper left")  # agregar leyenda.
    plt.show()  # mostrar gráfica.


# 4) Países en una gráfica por indicador.
for indicador in indicadores:
    plt.figure(figsize=(12, 8))  # tamaño de la gráfica.
    plt.title(f"Países {indicador}")  # título de la gráfica.

    for pais in paises:
        datosP_indicador = (
            dfDatosFil[
                (dfDatosFil["Country Name"] == pais)
                & (dfDatosFil["Series Code"] == indicador)
            ]
            .iloc[:, 44:64]
            .values.flatten()
        )  # filtrar por indicador.
        descrP_indicador = dfDescrFil[
            (dfDescrFil["Country Name"] == pais)
            & (dfDescrFil["Series Code"] == indicador)
        ]["Series Code"].values[
            0
        ]  # filtrar por indicador.
        plt.plot(years, datosP_indicador)  # graficar los datos.

    plt.xlabel("Año")  # etiqueta del eje x.
    plt.ylabel("Valor")  # etiqueta del eje y.
    plt.legend(loc="upper left")  # agregar leyenda.
    plt.grid(True)  # agregar cuadrícula.
    plt.show()  # mostrar gráfica.
