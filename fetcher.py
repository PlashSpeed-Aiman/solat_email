import json
import requests
from requests.exceptions import HTTPError

from zone import SolatZone
'''
{"prayerTime":[{"hijri":"1444-03-02","date":"29-Sep-2022","day":"Thursday","imsak":"05:44:00","fajr":"05:54:00","syuruk":"07:00:00","dhuhr":"13:06:00","asr":"16:16:00","maghrib":"19:08:00","isha":"20:17:00"}],"status":"OK!","serverTime":"2022-09-29 02:18:45","periodType":"today","lang":"ms_my","zone":"SGR01","bearing":"291&#176; 7&#8242; 23&#8243;"}
'''
API_LINK = "https://www.e-solat.gov.my/index.php?r=esolatApi/takwimsolat&period=today&zone="

def fetcher(zone:str):
    try:
        response = requests.get(API_LINK + zone)
        response.raise_for_status()
        jsonResponse = response.json()
        # print("Entire JSON response")
        # print(jsonResponse)
        if jsonResponse["status"] == "OK!":
            return jsonResponse
        else:
            return {}

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        return {}
    except Exception as err:
        print(f'Other error occurred: {err}')
        return {}

