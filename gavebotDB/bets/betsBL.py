import bets.betsDA as bda
import embed.errEMB as errEMB
import embed.betsEMB as betsEMB
import master.masterDA as mda

def placeBet(odds, wager, market, bet, event, userid, contestid):
    marketId = bda.getMarketID(market)
    response = bda.insertBet(odds, wager, marketId, bet, event, userid, contestid)
    
    betId = response["rownum"]

    if betId == 'False':
        rtResponse = 'False'
        return rtResponse
        
    else:
        return betId


def checkBetId(betid):
    betids = bda.getBetIds()

    betid = str(betid)
    

    if betid not in betids:
        return False
    else:
        return True


def getPayout(odds, wager):
    convertedOdds = int(odds)
    if convertedOdds > 0:
        decimalOdds = (convertedOdds / 100) + 1
    else:
        decimalOdds = 1 - (100 / convertedOdds)

    payout = (wager * decimalOdds) - wager

    return payout





def getBets(option, userid):
    resDict= {}
    if option == 'TODAY':
        resDict = bda.getTodayBets()
        names = resDict["names"]
        bets = resDict["bets"]
        if names == 'False':
            response = "ERROR ERROR ERROR ERROR ERROR ERROR"
            embed = errEMB.getError(response)
            return embed
    elif option == 'ME':
        resDict = bda.getBetsByUserId(userid)
        names = resDict["names"]
        bets = resDict["bets"]
        if names == 'False':
            response = "ERROR ERROR ERROR ERROR ERROR ERROR"
            embed = errEMB.getError(response)
            return embed
    else:
        usernames = mda.getUserNames()
        usernicknames = mda.getNickNames()
        print(usernicknames)
        print(option)
        
        if option in usernames:
            userid = mda.getUserIDByUsername(option)
            resDict = bda.getBetsByUserId(userid)
            names = resDict["names"]
            bets = resDict["bets"]
            if names == 'False':
                response = "ERROR ERROR ERROR ERROR ERROR ERROR"
                embed = errEMB.getError(response)
                return embed
        elif option in usernicknames:
            userid = mda.getUserIDByNickName(option)
            resDict = bda.getBetsByUserId(userid)
            names = resDict["names"]
            bets = resDict["bets"]
            if names == 'False':
                response = "ERROR ERROR ERROR ERROR ERROR ERROR"
                embed = errEMB.getError(response)
                return embed
        else: 
            response = "ERROR CHECK COMMAND FORMAT"
            embed = errEMB.getError(response)
            return embed

    embed = betsEMB.getBets(bets, names, option, userid)
    
    return embed

        
    
def tailBet(betid, wager, userid):
    isValid = checkBetId(betid)
    success= {}
    if isValid == 'False':
        success["response"] = "BET ID DOES NOT EXSIST ERROR"
        success["rownum"] = "False"
        return success

    bet = bda.getBet(betid)

    tailing = dict(zip(bet["names"], bet["bet"][0]))
    odds = tailing.get("odds")
    eventid = tailing.get("eventid")
    tailbet = tailing.get("bet")
    marketid = tailing.get("marketid")
    tailedid = tailing.get("betid")
    bettorid = tailing.get("bettorid")
    userid = str(userid) 
    contestid = tailing.get("contestid")   
    if bettorid == userid:
        success["response"] = "FAIL cant tail ur own bet"
        success["rownum"] = "False"
        return success


    if tailing.get("tailedid") != None:
         success["response"] = " FAIL... Cant tail a tailor"
         success["rownum"] = "False"
         return success
    
    
    success = bda.insertTail(odds, wager, marketid, tailbet, eventid, userid, tailedid, contestid)

    return success

    

    
def increaseTails(betid):
    tails = bda.getTails(betid)

    tails = tails + 1

    success = bda.updateTails(betid)    

    if success["response"] == "False":
        print("failed to increase number of tails....")
        return

    print("tailed number successfully increased for betid '{0}'".format(betid))

    return