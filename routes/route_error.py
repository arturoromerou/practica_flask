def error_handler(app):
    @app.errorhandler(404)
    def page_not_found(error):
        return 'pagina no encontrada', 404