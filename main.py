import os
import logging
import random
import httpx
import sqlite3

from ics import Calendar, Event
from datetime import datetime, timedelta

from models import PrayerTime
from utils import (CREATE_PRAYER_TIMES_TABLE, EZANVAKTI_MAINZ_URL, CALENDAR_FILE, PRAYER_TIMES_DB,
                   INSERT_PRAYER_TIMES_TABLE, SELECT_PRAYER_TIMES_TABLE, SELECT_ALL_PRAYER_TIMES_TABLE,
                   IMAME)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info('Application started!')

conn = sqlite3.connect(PRAYER_TIMES_DB)
cursor = conn.cursor()
cursor.execute(CREATE_PRAYER_TIMES_TABLE)
conn.commit()


def create_event(datetime_string: str):
    start = datetime.strptime(datetime_string, "%d.%m.%Y %H:%M")
    end = start + timedelta(minutes=15)
    return {
        "title": f"({random.choice(IMAME)})",
        "start": start,
        "end": end
    }


def run():
    logger.info("Runner started!")

    today = datetime.now()
    formatted_date = today.strftime("%d.%m.%Y")
    formatted_today_date = datetime.strptime(formatted_date, "%d.%m.%Y").date()
    logger.info(f"{formatted_date}")

    cursor.execute(SELECT_PRAYER_TIMES_TABLE, (formatted_date,))

    today_prayer_time = cursor.fetchone()

    if today_prayer_time:
        columns = [column[0] for column in cursor.description]
        prayer_time_data = dict(zip(columns, today_prayer_time))
        prayer_time = PrayerTime(**prayer_time_data)
        logger.info(prayer_time.MiladiTarihKisa)
    else:
        logger.info("No prayer times found for today.")
        try:
            prayer_times_response = httpx.get(EZANVAKTI_MAINZ_URL)
            logger.info(f"{prayer_times_response.status_code}")
            if prayer_times_response.status_code == 200:
                for item in prayer_times_response.json():
                    prayer_time = PrayerTime(**item)
                    logger.info(f"Prayer time: {prayer_time.MiladiTarihKisa}")
                    cursor.execute(INSERT_PRAYER_TIMES_TABLE(prayer_time))
                conn.commit()
        except Exception as e:
            logger.error(e)

    events = []
    cursor.execute(SELECT_ALL_PRAYER_TIMES_TABLE)
    prayer_times = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    for prayer_time in prayer_times:
        prayer_time_data = dict(zip(columns, prayer_time))
        prayer_time = PrayerTime(**prayer_time_data)

        prayer_date = datetime.strptime(prayer_time.MiladiTarihKisa, "%d.%m.%Y").date()
        if prayer_date >= formatted_today_date:
            events.append(create_event(f"{prayer_time.MiladiTarihKisa} {prayer_time.Imsak}"))
            events.append(create_event(f"{prayer_time.MiladiTarihKisa} {prayer_time.Ogle}"))
            events.append(create_event(f"{prayer_time.MiladiTarihKisa} {prayer_time.Ikindi}"))
            events.append(create_event(f"{prayer_time.MiladiTarihKisa} {prayer_time.Aksam}"))
            events.append(create_event(f"{prayer_time.MiladiTarihKisa} {prayer_time.Yatsi}"))

    if os.path.exists(CALENDAR_FILE):
        os.remove(CALENDAR_FILE)
        logger.info(f"Removed existing file: {CALENDAR_FILE}")

    calendar = Calendar()

    for ev in events:
        e = Event()
        e.name = ev["title"]
        e.begin = ev["start"]
        e.end = ev["end"]
        calendar.events.add(e)

    with open(CALENDAR_FILE, "w") as f:
        f.writelines(calendar)

    logger.info(f"Created new calendar file: {CALENDAR_FILE}")


if __name__ == "__main__":
    run()
