import tracker.trackerDA as tda
import master.masterDA as mda
import embed.errEMB as errEMB
import embed.statsEMB as statsEMB
import embed.leaderboardEMB as leaderboardEMB
def updateUserTacker(userid, contestid, wager, newbankroll, isABet):
    
    amtWagered = tda.getAmountWageredByUserIdContestId(userid, contestid)
    newamtWagered = amtWagered + float(wager)
    if isABet == "False":
        tailsAmt = tda.getTailsAmt(userid, contestid)
        newtailsAmt = int(tailsAmt) + 1
        tda.updateUserTrackerTail(userid, contestid, newamtWagered, newbankroll, newtailsAmt)
    else:
        betAmt = tda.getBetAmt(userid, contestid)
        newbetAmt = int(betAmt) + 1
        tda.updateUserTrackerBet(userid, contestid, amtWagered, newbankroll, newbetAmt)

    return



def getStats(userid, contestid, option):
    resDict= {}
    if option == 'ME':
        resDict = tda.getStatsByUserIdContestId(userid, contestid)
        names = resDict["names"]
        stats = resDict["stats"]
        if names == 'False':
            response = "ERROR ERROR ERROR ERROR ERROR ERROR"
            embed = errEMB.getError(response)
            return embed
    else:
        usernames = mda.getUserNames()
        usernicknames = mda.getNickNames()

        if option in usernames:
            userid = mda.getUserIDByUsername(option)
            resDict = tda.getStatsByUserIdContestId(userid, contestid)
            names = resDict["names"]
            stats = resDict["stats"]
            if names == 'False':
                response = "ERROR ERROR ERROR ERROR ERROR ERROR"
                embed = errEMB.getError(response)
                return embed
        elif option in usernicknames:
            userid = mda.getUserIDByNickName(option)
            resDict = tda.getStatsByUserIdContestId(userid, contestid)
            names = resDict["names"]
            stats = resDict["stats"]
            if names == 'False':
                response = "ERROR ERROR ERROR ERROR ERROR ERROR"
                embed = errEMB.getError(response)
                return embed
        else: 
            response = "ERROR CHECK COMMAND FORMAT"
            embed = errEMB.getError(response)
            return embed

    userstats = dict(zip(names, stats[0]))
    embed = statsEMB.getStats(userstats)
    
    return embed


def getLeaderboard(contestid):
    rtDict={}

    rtDict = tda.getLeaderboard(contestid)
    names = rtDict["names"]
    content = rtDict["content"]
    if names == 'False':
        response = "ERROR ERROR ERROR ERROR ERROR ERROR"
        embed = errEMB.getError(response)
        return embed

    embed = leaderboardEMB.getLeaderboard(content, names)
    
    return embed

