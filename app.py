import meteo
from flask import Flask, render_template

app= Flask(__name__) # crea el objeto del tipo flask, instancia la clase flas y crea el objeto app

@app.route('/' ) # este es el index

def indice():
    datos = meteo.meteo() # esto devuelve los datos escrapeados
    return render_template('index.html', datos=datos) # esta es la respuesta del servidor 

if __name__ == "__main__":
    app.run()
