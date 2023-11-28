# Importación de librerías.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Lectura de los archivos.
dfDatos = pd.read_csv(
    "C:\\Users\\alexa\\Documents\\Alexa\\Escuela\\ITAM\\Desarrollo de Aplicaciones Informáticas\\Proyecto2\\Analisis_Paises_Indicadores\\P_Data_Extract_From_Health_Nutrition_and_Population_Statistics\\361d8e4b-91be-4bc2-bdca-fbbf19126345_Data.csv",
    encoding="Latin-1",
)
dfDescr = pd.read_csv(
    "\\Users\\alexa\\Documents\\Alexa\\Escuela\\ITAM\\Desarrollo de Aplicaciones Informáticas\\Proyecto2\\Analisis_Paises_Indicadores\\P_Data_Extract_From_Health_Nutrition_and_Population_Statistics\\361d8e4b-91be-4bc2-bdca-fbbf19126345_Series - Metadata.csv",
    encoding="Latin-1",
)

# Países: Estados Unidos, China, México, Guatemala y Alemania.
# Indicadores: Población (masculina, feminia, total), tasa de mortalidad, gasto de salud privado, gasto de salud gubernamental, tasa de suicidio y población mayor a los 80 años.
# Años: 2000-2019.

paises = ["United States", "China", "Mexico", "Guatemala", "Germany"]
indicadores = [
    "Population, total",
    "Population, male",
    "Population, female",
    "Death rate, crude (per 1,000 people)",
    "Domestic private health expenditure (% of current health expenditure)",
    "Domestic general government health expenditure per capita (current US$)",
    "Suicide mortality rate (per 100,000 population)",
    "Population ages 80 and older, female (% of female population)",
    "Population ages 80 and above, male (% of male population)",
]

# Años
nomcolumn = [
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
    (dfDatos["Country Name"].isin(paises)) & (dfDatos["Series Name"].isin(indicadores))
]
dfDescrFil = dfDescr[
    (dfDescr["Country Name"].isin(paises)) & (dfDescr["Series Name"].isin(indicadores))
]

# 1) Gráficas por indicador por país
for pais in paises:
    for indicador in indicadores:
        datos_pais = pd.to_numeric(
            dfDatosFil[
                (dfDatosFil["Country Name"] == pais)
                & (dfDatosFil["Series Name"] == indicador)
            ]
            .iloc[:, 44:64]
            .values.flatten()
        )
        plt.figure(figsize=(12, 8))
        plt.title(f"{indicador} {pais}")
        plt.plot(nomcolumn, datos_pais)
        plt.xlabel("Año")  # etiqueta del eje x.
        plt.ylabel("Valor")  # etiqueta del eje y.
        plt.grid()  # agregar cuadrícula.
        plt.show()

# 2) Maxímo y mínimo de cada indicador y país
for pais in paises:
    print("País :", pais)
    for indicador in indicadores:
        datos_pais_nump = np.array(
            dfDatosFil[
                (dfDatosFil["Country Name"] == pais)
                & (dfDatosFil["Series Name"] == indicador)
            ]
            .iloc[:, 44:64]
            .values.flatten()
        )
        print("Indicador :", indicador)
        print("Mínimo :", datos_pais_nump.min())
        print("Máximo :", datos_pais_nump.max())
        print()


# 3) Indicadores en una única gráfica por país.
for pais in paises:
    datos_pais = dfDatosFil[dfDatosFil["Country Name"] == pais]  # filtrar por país.
    descr_pais = dfDescrFil[dfDescrFil["Country Name"] == pais]  # filtrar por país.

    plt.figure(figsize=(12, 8))  # tamaño de la gráfica.
    plt.title(f"Indicadores {pais}")  # título de la gráfica.
    
    poblacionTotal = pd.to_numeric(datos_pais[datos_pais["Series Name"] == "Population, total"].iloc[:,44:64].values.flatten())

    for indicador in indicadores:
        datos_indicador = pd.to_numeric(
            (
                datos_pais[datos_pais["Series Name"] == indicador]
                .iloc[:, 44:64]
                .values.flatten()
            )
        )  # filtrar por indicador.
        descr_indicador = descr_pais[descr_pais["Series Name"] == indicador][
            "Series Name"
        ].values[
            0
        ]  # filtrar por indicador.
            
        datos_normalizados = datos_indicador / poblacionTotal # normalizar los datos.
            
        # 5) El país con el mínimo y el máximo de cada indicador junto con el año, a partir de las gráficas del punto 3.
        min_value = datos_indicador.min()
        max_value = datos_indicador.max()
        year_min = nomcolumn[np.argmin(datos_indicador)]
        year_max = nomcolumn[np.argmax(datos_indicador)]

        plt.plot(
            nomcolumn, datos_normalizados, label=f"{indicador}"
        )  # graficar los datos.

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
        datosP_indicador = pd.to_numeric(
            (
                dfDatosFil[
                    (dfDatosFil["Country Name"] == pais)
                    & (dfDatosFil["Series Name"] == indicador)
                ]
                .iloc[:, 44:64]
                .values.flatten()
            )
        )  # filtrar por indicador.
        descrP_indicador = dfDescrFil[
            (dfDescrFil["Country Name"] == pais)
            & (dfDescrFil["Series Name"] == indicador)
        ]["Series Name"].values[
            0
        ]  # filtrar por indicador.
        plt.plot(
            datosP_indicador, label=f"{pais} - {descrP_indicador}"
        )  # graficar los datos.

    plt.xlabel("Año")  # etiqueta del eje x.
    plt.ylabel("Valor")  # etiqueta del eje y.
    plt.legend(loc="upper left")  # agregar leyenda.
    plt.grid(True)  # agregar cuadrícula.
    plt.show()  # mostrar gráfica.
