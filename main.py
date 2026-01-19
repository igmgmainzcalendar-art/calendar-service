from ics import Calendar, Event
from datetime import datetime, timedelta

c = Calendar()

# Beispiel-Termine (hier kannst du DB / CSV / API nutzen)
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
    c.events.add(e)

with open("calendar.ics", "w") as f:
    f.writelines(c)

print("calendar.ics aktualisiert")

