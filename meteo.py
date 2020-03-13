import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
# Función encargada de extraer los datos de una página que provee los datos del tiempo
def meteo():
    lista_datos=[] # vamos a cargar el diccionario con todos los datos
    url  = 'https://www.meteored.com.py/tiempo-en_Lambare-America+Sur-Paraguay-Central--1-22784.html'
    page=requests.get(url)
    soup= BeautifulSoup(page.content,'html.parser')
    ############## Aqui extraemos la temperatura
    temperatura= soup.find_all("span",class_="dato-temperatura changeUnitT")
    temperatura = temperatura[0].get_text() 
    temperatura=temperatura.replace("°","")
    ############### Aqui extraemos la velocidad del viento tanto min-max
    viento = soup.find_all("span", class_="changeUnitW")
    viento_min = viento[0].get_text()
    viento_max = viento[1].get_text()
    viento_max = viento_max.replace(" km/h","")
    ############## Aqui extraemos la ciudad en cuestión
    ciudad = soup.find_all("h1",class_="titulo")
    ciudad = ciudad[0].get_text()[10:]
    ############### Y por último extraemos la dirección del viento
    direccion_viento = soup.find_all("span",class_="datos-viento")
    direccion_viento = direccion_viento[0].get_text()[:5]
    direccion_viento=direccion_viento.replace(" ","")
    ################ todo esto guardamos en un diccionario datos
    datos={
        "ciudad" : ciudad,
        "temperatura": temperatura,
        "viento_min": viento_min,
        "viento_max": viento_max,
        "direccion": direccion_viento
    }
    lista_datos.append(datos)
    return lista_datos

