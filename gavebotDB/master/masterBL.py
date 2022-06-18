import master.masterDA as mda
import embed.errEMB as errEMB
import embed.usersEMB as usersEMB
import embed.marketEMB as marketEMB
def newUser(userid, username):
    
    userids = mda.getUserIDs()
    userid = str(userid)
    if userid not in userids:
        mda.addUserID(userid, username)
        contestid ='0'
        bankroll = 50
        mda.addUserToTracker(userid, contestid, bankroll)
        return

    return


def checkMarket(market):
    markets = mda.getMarkets()

    market = str(market)

    if market not in markets:
        return False
    else:
        return True

       
    
    
def checkEvent(eventid):
    eventids = mda.getEventIds()
    

    if eventid not in eventids:
        return False
    else:
        return True


def getUsers():
    resDict ={}
    resDict = mda.getUsersInfo()
    names = resDict["names"]
    users = resDict["users"]
    if names == 'False':
        response = "ERROR ERROR ERROR ERROR ERROR ERROR"
        embed = errEMB.getError(response)
        return embed
    else:
        embed = usersEMB.getUserEMB(users, names)
        return embed
   
def getMarkets():
    resDict ={}
    resDict = mda.getMarkets()
    name = resDict["names"]
    market = resDict["markets"]
    if name == 'False':
        response = "ERROR ERROR ERROR ERROR ERROR ERROR"
        embed = errEMB.getError(response)
        return embed
    else:
        embed = marketEMB.getMarkets(market, name)
        return embed



def checkContest(contestid):
    contestids = mda.getContestIds()

    if contestid not in contestids:
        return False
    else:
        return True



def setNickname(userid, nickname):
    usernicknames = mda.getNickNames()

    if nickname in usernicknames:
        response = "nickname already in use try again"
        return response

    response = mda.setNickname(userid, nickname)
    
    if response == "FALSE":
        rtRes = "Nickname did not get set fail"
        return rtRes
    else:
        rtRes = "{0} set for userid: {1}".format(nickname, userid)

    return rtRes