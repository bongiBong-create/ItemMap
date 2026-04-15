import uuid
from datetime import datetime


def create_id():
    return str(uuid.uuid4())


def get_datetime():
    now = datetime.now()

    return now.strftime("%d.%m.%Y %H:%M:%S")
