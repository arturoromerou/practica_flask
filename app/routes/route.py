def routes(app):
    @app.route('/') # ruta del entorno
    def hello_world():
        return 'hola mundo!'