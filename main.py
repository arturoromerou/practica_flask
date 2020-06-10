from flask import Flask

app = Flask(__name__) #nombre del app

@app.route("/") # ruta del entorno

def hola():
    return('hello world!')

if __name__ == '__main__': # se setea el main
    app.run()