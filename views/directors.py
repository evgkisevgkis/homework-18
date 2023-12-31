from flask_restx import Resource, Namespace

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        return 'get', 200


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did: int):
        return 'get', 200
