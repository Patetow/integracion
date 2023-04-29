from flask import Flask, render_template


app=Flask(__name__)

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
