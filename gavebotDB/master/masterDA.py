from colorama import Cursor
import mysql.connector

import gavebotConstants as gb

mydb = mysql.connector.connect(
   
)


cursor = mydb.cursor()


def getUserIDs():

    rtList=[]
    cursor.execute(gb.sql_GET_USER_IDS)
    userids = cursor.fetchall()

    if userids.__len__() < 1:
        return rtList


    for x in userids:
        
        rtList.insert(0, x[0])

    return rtList


def getUserNames():

    rtList=[]
    cursor.execute(gb.sql_GET_USERNAMES)
    usernames = cursor.fetchall()

    if usernames.__len__() < 1:
        return rtList


    for x in usernames:
        
        rtList.insert(0, x[0])

    return rtList


def getNickNames():

    rtList=[]
    cursor.execute(gb.sql_GET_NICKNAMES)
    nicknames = cursor.fetchall()

    if nicknames.__len__() < 1:
        return rtList


    for x in nicknames:
        
        rtList.insert(0, x[0])

    return rtList





def addUserID(userid, username):
    try:
            cursor.execute(gb.sql_INSERT_USER.format(userid, username))
            mydb.commit()

    except mysql.connector.Error as error:
            print(error)
            return

    finally:
        print("new user spotted and added")
        return



def getMarkets():
    rtList=[]


    cursor.execute(gb.sql_GET_MARKETNICKNAME)
    markets = cursor.fetchall()

    if markets.__len__() < 1:
        return rtList


    for x in markets:
        
        rtList.insert(0, x[0])

    return rtList


def getEventIds():
    rtList=[]


    cursor.execute(gb.sql_GET_EVENTIDS)
    eventids = cursor.fetchall()

    if eventids.__len__() < 1:
        return rtList


    for x in eventids:
        
        rtList.insert(0, x[0])

    return rtList



def getUsername(userid):
    response = ""
    cursor.execute(gb.sql_GET_USERNAME_FROM_USERID.format(userid))
    username = cursor.fetchall()

    response = username[0][0]

    return response


def getUserIDByUsername(username):
    response = ""
    cursor.execute(gb.sql_GET_USERID_BY_USERNAME.format(username))
    userid = cursor.fetchall()

    response = userid[0][0]

    return response



def getUserIDByNickName(nickname):
    response = ""
    cursor.execute(gb.sql_GET_USERID_BY_NICKNAME.format(nickname))
    nickname = cursor.fetchall()

    response = nickname[0][0]

    return response



def getUsersInfo():
    rtDict = {}

    cursor.execute(gb.sql_GET_USERS)

    users = cursor.fetchall()

    if users.__len__() < 1:
        rtDict["names"] = 'False'
        rtDict["users"] = 'False'
    else:
        rtDict["names"] = cursor.column_names
        rtDict["users"] = users

    return rtDict


def getMarkets():
    rtDict = {}

    cursor.execute(gb.sql_GET_MARKETS)

    markets = cursor.fetchall()

    if markets.__len__() < 1:
        rtDict["names"] = 'False'
        rtDict["markets"] = 'False'
    else:
        rtDict["names"] = cursor.column_names
        rtDict["markets"] = markets

    return rtDict





def getContestIds():
    rtList=[]


    cursor.execute(gb.sql_GET_CONTESTIDS)
    contestids = cursor.fetchall()

    if contestids.__len__() < 1:
        return rtList


    for x in contestids:
        
        rtList.insert(0, x[0])

    return rtList



def addUserToTracker(userid, contestid, bankroll):
    try:
            cursor.execute(gb.sql_ADD_USER_TO_TRACKER.format(userid, contestid, bankroll, bankroll))
            mydb.commit()

    except mysql.connector.Error as error:
            print(error)
            return

    finally:
        print("new user added to tracker for default")
        return
    



def setNickname(userid, nickname):
    response = ""
    try:

        cursor.execute(gb.sql_SET_USERNICKNAME.format(nickname, userid))
        mydb.commit()
    except mysql.connector.Error as error:
        print(error)
        response = "FALSE"
        return response

    finally:
        response = "TRUE"

    return response