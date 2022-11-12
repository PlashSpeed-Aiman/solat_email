import sqlite3
from zone import Times
from typing import Optional
def create_db():
    # Create a database and open the database.
    # If the database already exists just opens the database
    conn = sqlite3.connect('salatdb.db')
    c = conn.cursor()
    # Create a users table if the table does not exists
    c.execute('''CREATE TABLE IF NOT EXISTS salat
    (hijri TEXT, date TEXT, day TEXT,zone TEXT,imsak TEXT, fajr TEXT, syuruk TEXT, dhuhr TEXT, asr TEXT, maghrib TEXT, isha TEXT)
    ''')
    # commit changes and close database connect
    conn.commit()
    conn.close()

def search_db(date_today,zone,db_name) -> Optional[Times]:
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    print(date_today)
    # WHERE CLAUSE TO RETRIEVE DATA
    cursor.execute(f"SELECT * FROM SALAT WHERE date = '{date_today}' AND zone = '{zone}'")
    
    # printing the cursor data
    record = cursor.fetchone()
    print(record)
    if record is not None:
        times = Times()
        times.hijri = record[0]
        times.date = record[1]
        times.day = record[2]
        times.zone = record[3]
        times.imsak = record[4]
        times.fajr = record[5]
        times.syuruk = record[6]
        times.dhuhr = record[7]
        times.asr = record[8]
        times.maghrib = record[9]
        times.isha = record[10]
        return times

    times = None
    return times
    
    
def insert_to_db(db_name,times:Times):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    insert_param = """
    INSERT INTO SALAT
    (hijri , date , day ,zone,imsak , fajr , syuruk , dhuhr , asr , maghrib , isha )
    VALUES
    (?,?,?,?,?,?,?,?,?,?,?)
    """
    data_tuple = (times.hijri,times.date,times.day,times.zone,times.imsak,times.fajr,times.syuruk,times.dhuhr,times.asr,times.maghrib,times.isha)
    cursor.execute(insert_param, data_tuple)
    connection.commit()
    connection.close()




