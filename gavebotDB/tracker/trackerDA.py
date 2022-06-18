import mysql.connector

import gavebotConstants as gb

mydb = mysql.connector.connect(

)


cursor = mydb.cursor()



def getUserBankRollByContestId(userid, contestid):
    response = ""
    cursor.execute(gb.sql_GET_USER_BANKROLL_BY_CONTESTID.format(userid, contestid))
    bankroll = cursor.fetchall()

    response = bankroll[0][0]

    return response


def getTailsAmt(userid, contestid):
    response = ""
    cursor.execute(gb.sql_GET_TAILSAMT_BY_USERID_CONTESTID.format(userid, contestid))
    tailsAmt = cursor.fetchall()

    response = tailsAmt[0][0]

    return response


def getBetAmt(userid, contestid):
    response = ""
    cursor.execute(gb.sql_GET_BETSAMT_BY_USERID_CONTESTID.format(userid, contestid))
    betsAmt = cursor.fetchall()

    response = betsAmt[0][0]

    return response


def getAmountWageredByUserIdContestId(userid, contestid):
    response = ""
    cursor.execute(gb.sql_GET_AMTWAGERED_BY_USERID_CONTESTID.format(userid, contestid))

    amountWagered = cursor.fetchall()
    
    response = amountWagered[0][0]

    return response


def updateUserTrackerTail(userid, contestid, amtWagered, newbankroll, tailsAmt):
    try:
            cursor.execute(gb.sql_UPDATE_USER_TRACKER_TAIL.format(newbankroll, tailsAmt, amtWagered, userid, contestid))
            mydb.commit()

    except mysql.connector.Error as error:
            print(error)
            return

    finally:
        print("user tracker updated")
        return

def updateUserTrackerBet(userid, contestid, amtWagered, newbankroll, betAmt):
    try:
            cursor.execute(gb.sql_UPDATE_USER_TRACKER_BET.format(newbankroll, betAmt, amtWagered, userid, contestid))
            mydb.commit()

    except mysql.connector.Error as error:
            print(error)
            return

    finally:
        print("user tracker updated")
        return





def getStatsByUserIdContestId(userid, contestid):
    userid = str(userid)
    cursor.execute(gb.sql_GET_STATS_BY_USERID_CONTESTID.format(userid, contestid))
    rtDict = {}
    stats = cursor.fetchall()

    if stats.__len__() < 1:
        rtDict["names"] = 'False'
        rtDict["stats"] = 'False'
    else:
        rtDict["names"] = cursor.column_names
        rtDict["stats"] = stats

    return rtDict

def getLeaderboard(contestid):
    cursor.execute(gb.sql_GET_LEADERBOARD_BY_CONTESTID.format(contestid))
    rtDict = {}
    leaderboard = cursor.fetchall()

    if leaderboard.__len__() < 1:
        rtDict["names"] = 'False'
        rtDict["content"] = 'False'
    else:
        rtDict["names"] = cursor.column_names
        rtDict["content"] = leaderboard

    return rtDict

