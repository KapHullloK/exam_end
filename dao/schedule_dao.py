from dao.models.schedule import Schedule


class ScheduleDAO:

    def __init__(self, session):
        self.session = session

    def get_one(self, sid):
        return self.session.query(Schedule).get(sid)

    def get_all(self):
        return self.session.query(Schedule).all()

    def create(self, data):
        schedule = Schedule(**data)

        self.session.add(schedule)
        self.session.commit()

        return schedule

    def update(self, schedule):

        self.session.add(schedule)
        self.session.commit()

        return schedule

    def delete(self, sid):
        schedule = self.get_one(sid)

        self.session.delete(schedule)
        self.session.commit()
