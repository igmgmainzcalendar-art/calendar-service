from pydantic import BaseModel
from typing import Optional

class PrayerTime(BaseModel):
    HicriTarihKisa: str
    HicriTarihKisaIso8601: Optional[str]
    HicriTarihUzun: str
    HicriTarihUzunIso8601: Optional[str]
    AyinSekliURL: str
    MiladiTarihKisa: str
    MiladiTarihKisaIso8601: str
    MiladiTarihUzun: str
    MiladiTarihUzunIso8601: str
    GreenwichOrtalamaZamani: float
    Aksam: str
    Gunes: str
    GunesBatis: str
    GunesDogus: str
    Ikindi: str
    Imsak: str
    KibleSaati: str
    Ogle: str
    Yatsi: str
