from flask import request
from flask_restx import Resource, Namespace
from dao.models.schedule import ScheduleSchema
from implemented import schedule_service


schedule_ns = Namespace('sch')

schedule_schema = ScheduleSchema()
schedules_schema = ScheduleSchema(many=True)


@schedule_ns.route('/')
class NotesView(Resource):

    def get(self):
        schedules = schedule_service.get_all()
        return schedules_schema.dump(schedules), 200
    def post(self):
        data = request.json
        schedule_service.create(data)

        return "OK", 201


@schedule_ns.route('/<int:sid>')
class NoteView(Resource):

    def get(self, sid):
        schedule = schedule_service.get_one(sid)
        return schedule_schema.dump(schedule), 200

    def put(self, sid):
        data = request.json
        schedule_service.update(data, sid)

        return "OK", 204

    def patch(self, sid):
        data = request.json
        schedule_service.update_partial(data, sid)

        return "OK", 204

    def delete(self, sid):
        schedule_service.delete(sid)
        return "OK", 204
