import os
import logging

from ics import Calendar, Event
from datetime import datetime


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info('Application started!')


CALENDAR_FILE = "calendar.ics"


def run():
    logger.info("Runner started!")

    if os.path.exists(CALENDAR_FILE):
        os.remove(CALENDAR_FILE)
        logger.info(f"Removed existing file: {CALENDAR_FILE}")

    calendar = Calendar()

    events = [
        {
            "title": "Team Meeting",
            "start": datetime(2026, 1, 20, 10, 0),
            "end": datetime(2026, 1, 20, 11, 0),
        },
        {
            "title": "Review",
            "start": datetime(2026, 1, 22, 14, 0),
            "end": datetime(2026, 1, 22, 15, 0),
        },
    ]

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
