from flask import request
from flask_restx import Resource, Namespace

from dao.model.director import DirectorSchema
from helpers.decorators import auth_required, admin_required
from implemented import director_service

director_ns = Namespace('directors')

"""Вью для отображения всех режиссеров"""


@director_ns.route('/')
class DirectorsView(Resource):
    @auth_required
    def get(self):
        rs = director_service.get_all()
        res = DirectorSchema(many=True).dump(rs)
        return res, 200

    @admin_required
    def post(self):
        req_json = request.json
        user = director_service.create(req_json)
        return "", 201, {"location": f"/users/{user.id}"}


"""Вью для отображения определенного режиссера и работы с ним по его id"""


@director_ns.route('/<int:rid>')
class DirectorView(Resource):
    @auth_required
    def get(self, rid):
        r = director_service.get_one(rid)
        sm_d = DirectorSchema().dump(r)
        return sm_d, 200

    @admin_required
    def put(self, uid):
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = uid
        director_service.update(req_json)
        return "", 204

    @admin_required
    def delete(self, uid):
        director_service.delete(uid)
        return "", 204
