from flask_restful import Resource
from markupsafe import escape
from flask import request


class Hello(Resource):
    def get(self):
        return {'message': 'Hello sir'}

    def post(self):
        # json_data = request.get_json(force=True)
        # if not json_data:
        #     return {'message': 'The data has send should be json'}, 400
        result = {'key one': 'val one', 'key two': 'val two'}
        error = None

        return {'msg': self.__p_method()}, 201

        # return {'status': 'success', 'error': error, 'data': result}, 201

    def __p_method(self):
        return 'this a private method'
