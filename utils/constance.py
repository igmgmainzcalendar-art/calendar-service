PRAYER_TIMES_DB = "prayer_times.db"
EZANVAKTI_MAINZ_URL = "https://ezanvakti.emushaf.net/vakitler/11020"
CALENDAR_FILE = "calendar.ics"
IMAME = ["Safa", "Yasin"]

CREATE_PRAYER_TIMES_TABLE = '''
CREATE TABLE IF NOT EXISTS prayer_times (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    HicriTarihKisa TEXT,
    HicriTarihKisaIso8601 TEXT,
    HicriTarihUzun TEXT,
    HicriTarihUzunIso8601 TEXT,
    AyinSekliURL TEXT,
    MiladiTarihKisa TEXT,
    MiladiTarihKisaIso8601 TEXT,
    MiladiTarihUzun TEXT,
    MiladiTarihUzunIso8601 TEXT,
    GreenwichOrtalamaZamani REAL,
    Aksam TEXT,
    Gunes TEXT,
    GunesBatis TEXT,
    GunesDogus TEXT,
    Ikindi TEXT,
    Imsak TEXT,
    KibleSaati TEXT,
    Ogle TEXT,
    Yatsi TEXT
)
'''

SELECT_ALL_PRAYER_TIMES_TABLE = '''
SELECT *
FROM prayer_times
'''

SELECT_PRAYER_TIMES_TABLE = '''
SELECT *
FROM prayer_times
WHERE MiladiTarihKisa = ?
'''

def INSERT_PRAYER_TIMES_TABLE(prayer_time):
    return f"""
            INSERT INTO prayer_times (
    HicriTarihKisa,
    HicriTarihKisaIso8601,
    HicriTarihUzun,
    HicriTarihUzunIso8601,
    AyinSekliURL,
    MiladiTarihKisa,
    MiladiTarihKisaIso8601,
    MiladiTarihUzun,
    MiladiTarihUzunIso8601,
    GreenwichOrtalamaZamani,
    Aksam,
    Gunes,
    GunesBatis,
    GunesDogus,
    Ikindi,
    Imsak,
    KibleSaati,
    Ogle,
    Yatsi
) VALUES (
    '{prayer_time.HicriTarihKisa}',
    '{prayer_time.HicriTarihKisaIso8601}',
    '{prayer_time.HicriTarihUzun}',
    '{prayer_time.HicriTarihUzunIso8601}',
    '{prayer_time.AyinSekliURL}',
    '{prayer_time.MiladiTarihKisa}',
    '{prayer_time.MiladiTarihKisaIso8601}',
    '{prayer_time.MiladiTarihUzun}',
    '{prayer_time.MiladiTarihUzunIso8601}',
    {prayer_time.GreenwichOrtalamaZamani},
    '{prayer_time.Aksam}',
    '{prayer_time.Gunes}',
    '{prayer_time.GunesBatis}',
    '{prayer_time.GunesDogus}',
    '{prayer_time.Ikindi}',
    '{prayer_time.Imsak}',
    '{prayer_time.KibleSaati}',
    '{prayer_time.Ogle}',
    '{prayer_time.Yatsi}'
);"""

