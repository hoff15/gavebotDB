from email.headerregistry import ContentDispositionHeader
import mysql.connector
import datetime
import gavebotConstants as gb
from datetime import date
mydb = mysql.connector.connect(
   
)


cursor = mydb.cursor()
tailCursor = mydb.cursor()

def insertBet(odds, wager, market, bet, event, userid, contestid):
    ct = datetime.datetime.now()
    rtDict={}
    try:
            cursor.execute(gb.sql_INSERT_BET_NT_NF.format(event, ct, userid, market, bet, odds, wager, contestid))
            mydb.commit()

    except mysql.connector.Error as error:
            print(error)
            rtDict["response"] = 'False'
            rtDict["rownum"] = 'False'
            return rtDict

    finally:
        print("Bet inserted ...........")
        rtDict["response"] = 'True'
        rtDict["rownum"] = cursor.lastrowid
        return rtDict



def getMarketID(market):
    cursor.execute(gb.sql_GET_MARKET_ID.format(market))

    rtID =""

    marketid = cursor.fetchall()

    rtID = marketid[0][0]

    return rtID


def getBetIds():

    rtList=[]
    cursor.execute(gb.sql_GET_BET_IDS)
    betids = cursor.fetchall()

    if betids.__len__() < 1:
        return rtList


    for x in betids:
        rtList.insert(0, x[0])

    return rtList


def getBet(betid):
    cursor.execute(gb.sql_GET_BET.format(betid))
    rtDict = {}
    bet = cursor.fetchall()


    if bet.__len__() < 1:
        rtDict["names"] = 'False'
        rtDict["bet"] = 'False'
    else:
        rtDict["names"] = cursor.column_names
        rtDict["bet"] = bet

    return rtDict 



def getTodayBets():
    today = date.today()
    rtDict ={}
    cursor.execute(gb.sql_GET_BETS_BY_DATE.format(today))

    bets = cursor.fetchall()

    if bets.__len__() < 1:
        rtDict["names"] = 'False'
        rtDict["bets"] = 'False'
    else:
        rtDict["names"] = cursor.column_names
        rtDict["bets"] = bets

    return rtDict



def getBetsByUserId(userid):
    userid = str(userid)
    print(userid)
    cursor.execute(gb.sql_GET_UPCOMING_BETS_BY_USERID.format(userid))
    rtDict = {}
    bets = cursor.fetchall()

    print(bets)

    if bets.__len__() < 1:
        rtDict["names"] = 'False'
        rtDict["bets"] = 'False'
    else:
        rtDict["names"] = cursor.column_names
        rtDict["bets"] = bets

    return rtDict



def insertTail(odds, wager, market, bet, event, userid, tailedid, contestid):
    ct = datetime.datetime.now()
    rtDict={}
    try:
        print(odds)
        print(wager)
        print(market)
        print(bet)
        print(event)
        print(userid)
        print(tailedid)
        print(ct)
        print(gb.sql_INSERT_TAIL.format(event, ct, userid, market, bet, odds, wager, tailedid))
        tailCursor.execute(gb.sql_INSERT_TAIL.format(event, ct, userid, market, bet, odds, wager, tailedid, contestid))
        mydb.commit()

    except mysql.connector.Error as error:
        print(error)
        rtDict["response"] = 'False'
        rtDict["rownum"] = 'False'
        return rtDict

    finally:
        print("Bet inserted ...........")
        rtDict["response"] = 'True'
        rtDict["rownum"] = tailCursor.lastrowid
        print(rtDict["rownum"])
        return rtDict



def getTails(betid):
    cursor.execute(gb.sql_GET_TAILS_BY_BETID.format(betid))
    tails = cursor.fetchall()
    numOfTails = ""

    numOfTails = tails[0][0]

    return numOfTails


def updateTails(betid, tails):
    rtDict = {}
    try:
        
        tailCursor.execute(gb.sql_UPDATE_TAILS.format(tails, betid))
        mydb.commit()

    except mysql.connector.Error as error:
        print(error)
        rtDict["response"] = 'False'
        rtDict["rownum"] = 'False'
        return rtDict

    finally:
        print("Bet inserted ...........")
        rtDict["response"] = 'True'
        rtDict["rownum"] = tailCursor.lastrowid
        print(rtDict["rownum"])
        return rtDict