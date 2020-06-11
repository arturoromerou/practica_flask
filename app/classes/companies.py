from app.connection.database import Conexion
from app.helpers.helper import handler_response

class Companies:
    def __init__(self):
        self.name = ''
        self.ruc = ''
        self.status = ''

    def companies_all(self, app):
        try:
            conn = Conexion()
            query = f'''SELECT * FROM companies;'''
            result = conn.execute_query(query)
            company = result.fetchone()
            companies = {
                'id': company[0],
                'name': company[1],
                'ruc': company[2],
                'status': company[3]
            }
            
            result_json = companies
            return handler_response(app, 200, 'Data companies', True, result_json)
        except Exception as e:
            return handler_response(app, 501, str(e))

    def companies_get(self):
        conn = Conexion()
        query = f'''
            SELECT * FROM companies WHERE id = '1';
        '''
        result = conn.execute_query(query)
        for i in result:
            print(i)