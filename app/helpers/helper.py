from flask import json

# estandarizacion de los endpoints
def handler_response(app, code_error, output, validate=True, payload=None):
    if payload is None:
        payload = {}

    response_object = {
        'response': {
            'message': output, # mensaje personalizado
            'api_response': payload, # bodyresponse
            'request_validate': validate, # falta un dato
            'status_code': code_error # codigo de estado
        }
    }

    response = app.response_class(
        response=json.dumps(response_object),
        status=code_error,
        mimetype='application/json'
    )

    return response