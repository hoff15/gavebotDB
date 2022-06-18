
import mysql.connector
from datetime import date

import gavebotConstants as gb

mydb = mysql.connector.connect(
   
)

cursor = mydb.cursor()

# def checkEventID(eventid):
#     cursor.execute()



def getLeagues():
    rtList=[]
    cursor.execute(gb.sql_GET_LEAGUES)
    leagues = cursor.fetchall()

    if leagues.__len__() < 1:
        return rtList


    for x in leagues:
        
        rtList.insert(0, x[0])

    print(rtList)
    return rtList


def getLeagueLogo(league):
    rtLogo =""
    cursor.execute(gb.sql_GET_LEAGUE_LOGO.format(league))
    logo = cursor.fetchall()

    rtLogo = logo[0][0]

    return rtLogo

def getUpcomingEventsByLeague(league):
    rtDict={}
    cursor.execute(gb.sql_GET_UPCOMING_EVENTS_BY_LEAGUE.format(league))

    events = cursor.fetchall()


    if events.__len__() < 1:
        rtDict["names"] = 'False'
        rtDict["events"] = 'False'
    else:
        rtDict["names"] = cursor.column_names
        rtDict["events"] = events
    
    return rtDict



def getTodayEvents():
    today = date.today()
    rtDict = {}
    cursor.execute(gb.sql_GET_TODAYS_EVENTS.format(today))

    events = cursor.fetchall()

    if events.__len__() < 1:
        rtDict["names"] = 'False'
        rtDict["events"] = 'False'
    else:
        rtDict["names"] = cursor.column_names
        rtDict["events"] = events
    
    return rtDict


def getLiveEvents():
    rtDict = {}
    cursor.execute(gb.sql_GET_LIVE_EVENTS)

    events = cursor.fetchall()

    if events.__len__() < 1:
        rtDict["names"] = 'False'
        rtDict["events"] = 'False'
    else:
        rtDict["names"] = cursor.column_names
        rtDict["events"] = events
    
    return rtDict


def getEvent(eventid):
    rtDict = {}
    
    cursor.execute(gb.sql_GET_EVENT.format(eventid))

    event = cursor.fetchall()

    if event.__len__() < 1:
        rtDict["names"] = 'False'
        rtDict["event"] = 'False'
    else:
        rtDict["names"] = cursor.column_names
        rtDict["event"] = event
    
    return rtDict
        


