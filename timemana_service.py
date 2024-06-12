# Time-management software
import psycopg2
from psycopg2.extras import RealDictCursor
from config import config
import json
from datetime import datetime

# Helper function to convert datetime to string -Chat GPT
def datetime_converter(o):
    if isinstance(o, datetime):
        return o.isoformat()


# lisää uuden tuntisyöttö-entryn tableen hours
def db_add_hours(startTime, endTime, lunchBreak, consultantName, customerName):
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor(cursor_factory=RealDictCursor)
        SQL = 'INSERT INTO time_management (startTime, endTime, lunchBreak, consultantName, customerName) VALUES (%s, %s, %s, %s, %s);'
        cursor.execute(SQL, (startTime, endTime, lunchBreak, consultantName, customerName))
        con.commit()
        result = {"success": "added hours by: %s " % consultantName}
        cursor.close()
        return json.dumps(result)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

# palauttaa kirjatut rivit (testikäyttöön): azuressa on valmiina table jonne data insertataan
def db_get_hours():
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor(cursor_factory=RealDictCursor)
        SQL = 'SELECT * FROM time_management;'
        cursor.execute(SQL)
        data = cursor.fetchall()
        cursor.close()
        return json.dumps({"hours_list": data}, default=datetime_converter)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

#if __name__ == "__main__":
 #   print(db_get_hours())