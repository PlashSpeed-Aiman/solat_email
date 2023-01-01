from calendar import day_abbr
from dataclasses import dataclass

@dataclass
class Times(object):
    hijri   : str = ""
    date    : str = ""
    day     : str = ""
    zone    : str = ""
    imsak   : str = ""
    fajr    : str = ""
    syuruk  : str = "" 
    dhuhr   : str = ""
    asr     : str = ""
    maghrib : str = ""
    isha    : str = ""

    def to_string(self):
        return f"""  
        HIJRI  : {self.hijri}
        DATE   : {self.date}
        DAY    : {self.day}
        ZONE   : {self.zone}
        IMSAK  : {self.imsak}
        FAJR   : {self.fajr}
        SYURUK : {self.syuruk}
        ZOHOR  : {self.dhuhr}
        ASAR   : {self.asr}
        MAGHRIB : {self.maghrib}
        ISHA    : {self.isha}
        """
class SolatZone(object):
    """
    JOHOR :
    JHR01 - Pulau Aur dan Pulau Pemanggil
    JHR02 - Johor Bahru, Kota Tinggi, Mersing, Kulai
    JHR03 - Kluang, Pontian
    JHR04 - Batu Pahat, Muar, Segamat, Gemas Johor, Tangkak

    SELANGOR :
    SGR01 - Gombak, Petaling, Sepang, Hulu Langat, Hulu Selangor, S.Alam
    SGR02 - Kuala Selangor, Sabak Bernam
    SGR03 - Klang, Kuala Langat
    """
    JOHOR01 = "JHR01"
    JOHOR02 = "JHR02"
    JOHOR03 = "JHR03"
    JOHOR04 = "JHR04"
    SELANGOR01 = "SGR01"
    SELANGOR02 = "SGR02"
    SELANGOR03 = "SGR03"