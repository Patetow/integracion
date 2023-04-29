import json
from flask import Flask, render_template


app=Flask(__name__)

@app.route('/products')
def mostrar_productos():
    # Abrir el archivo JSON
    with open('productos.json') as archivo:
        # Cargar los datos del archivo en un objeto Python
        datos = json.load(archivo)
    # Obtener la lista de productos del objeto JSON
    productos = datos['productos']
    # Pasar la lista de productos a la plantilla Jinja2
    return render_template('products.html', productos=productos)



@app.route('/')
def index():
    data={
        'titulo':'index',
        'bienbenida':'saludos'
    }
    return render_template('index.html', data=data)

@app.route('/productos')
def productos():
    return render_template('productos.html')

if __name__ == '__main__':
    app.run(debug=True,port=5000)
