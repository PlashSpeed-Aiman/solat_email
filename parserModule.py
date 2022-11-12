from datetime import date, datetime
import json
from typing import Dict, Optional
from zone import Times
import time
def parse_today(json_response : Dict)->Optional[Times]:
    
    if 'status' in json_response.keys():
        if json_response['status'] == "OK!":
            
           return parse_helper(json_response)

    elif json_response == {}:
        return None
    else :
        return None


def parse_helper(json_resp:Dict)-> Times:
    times = Times()
    times.hijri   = json_resp['prayerTime'][0] ['hijri']
    times.date    = json_resp['prayerTime'][0] ['date'].replace('-',' ')
    times.day     = json_resp['prayerTime'][0] ['day']
    times.zone    = json_resp['zone']
    times.imsak   = json_resp['prayerTime'][0] ['imsak']
    times.fajr    = json_resp['prayerTime'][0] ['fajr']
    times.syuruk  = json_resp['prayerTime'][0] ['syuruk']
    times.dhuhr   = json_resp['prayerTime'][0] ['dhuhr']
    times.asr     = json_resp['prayerTime'][0] ['asr']
    times.maghrib = json_resp['prayerTime'][0] ['maghrib']
    times.isha    = json_resp['prayerTime'][0] ['isha']
    return times
# print(time.strptime("14-Sep-2022", "%d-%b-%y")) 