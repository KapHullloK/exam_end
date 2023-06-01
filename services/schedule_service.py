from dao.schedule_dao import ScheduleDAO


class ScheduleService:

    def __init__(self, dao: ScheduleDAO):
        self.dao = dao

    def get_one(self, sid):
        return self.dao.get_one(sid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        return self.dao.create(data)

    def update(self, data, sid):
        schedule = self.dao.get_one(sid)

        schedule.school_subject = data.get("school_subject")
        schedule.date_subject = data.get("date_subject")
        schedule.fio = data.get("fio")
        schedule.office = data.get("office")

        self.dao.update(schedule)

    def update_partial(self, data, sid):
        schedule = self.get_one(sid)

        if "school_subject" in data:
            schedule.school_subject = data.get("school_subject")

        if "date_subject" in data:
            schedule.date = data.get("date_subject")

        if "fio" in data:
            schedule.fio = data.get("fio")

        if "office" in data:
            schedule.office = data.get("office")

        self.dao.update(schedule)

    def delete(self, sid):
        return self.dao.delete(sid)
