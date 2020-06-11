def routes(app):
    @app.route('/') # ruta del entorno
    def hello_world():
        return 'hola mundo!'

    @app.route('/employees')
    def employees():
        return 'Empleados'

    @app.route('/companies')
    def companies():
        return 'Empresas'

    @app.route('/employees/1')
    def employees_id():
        return 'Empleado 1'

    @app.route('/companies/1')
    def companies_id():
        return 'Empresa 1'
    
