from dao.schedule_dao import ScheduleDAO
from services.schedule_service import ScheduleService
from setup_db import db

schedule_dao = ScheduleDAO(db.session)
schedule_service = ScheduleService(dao=schedule_dao)
