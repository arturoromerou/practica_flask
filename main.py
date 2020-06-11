from flask import Flask
from app.routes.route import routes
from app.routes.route_error import error_handler

app = Flask(__name__) #nombre del app

routes(app)
error_handler(app)

if __name__ == '__main__': # se setea el main
    app.run()