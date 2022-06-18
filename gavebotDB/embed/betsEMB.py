import discord

import bets.betsDA as bda
import bets.betsBL as bbl
import master.masterDA as mda
import events.eventsDA as eda
def getBetSlip(betid):

    rtBet = bda.getBet(betid)

    names = rtBet["names"]
    content = rtBet["bet"]

    bet = dict(zip(names, content[0]))
    eventid = bet.get("eventid")
    rtEvent = eda.getEvent(eventid)

    betcontent = bet.get("bet")

    iswinner = bet.get("winner")



    eventnames = rtEvent["names"]
    eventevent = rtEvent["event"]

    event = dict(zip(eventnames, eventevent[0]))

    eventDesc = "{0}  @  {1}".format(event.get("awayteam"), event.get("hometeam"))
    eventTime = event.get("eventtime")
    eventDate = event.get("eventdate")


    embedVar = discord.Embed(title="BetID: {0}".format(bet.get("betid")), description="{0},    {1}    Time: {2}    Date: {3}".format(betcontent, eventDesc, eventTime, eventDate), color=0x1da1f2)
    embedVar.add_field(name="WAGER", value=bet.get("wager"), inline=True)
    embedVar.add_field(name="ODDS", value=bet.get("odds"), inline=True)

    if iswinner == 'Y':
        earnings = bbl.getPayout(bet.get("odds"), bet.get("wager"))
        embedVar.add_field(name="PAYOUT", value=earnings, inline=True)
    elif iswinner == 'N':
        earnings = bet.get("wager")*(-1)
        embedVar.add_field(name="PAYOUT", value=earnings, inline=True)
    else:
        earnings = bbl.getPayout(bet.get("odds"), bet.get("wager"))
        embedVar.add_field(name="POTENTIAL PAYOUT", value=earnings, inline=True)

    embedVar.add_field(name="TIMEPLACED", value=bet.get("timeplaced"), inline=False)

    return embedVar


    
    


def getBets(bets, names, option, userid):
    if option == 'TODAY':
        embedVar = discord.Embed(title="TODAYS BETS", description="todays bets are as follows..." , color=0x1da1f2)
        for x in bets:
            bet = dict(zip(names, x)) 
            username = mda.getUsername(bet.get("bettorid"))
            betInfo = bet.get("bet")
            odds = bet.get("odds")
            wager = bet.get("wager")
            payout = bbl.getPayout(odds, wager)
            eventtime = bet.get("eventtime")
            embedVar.add_field(name="betID: {0}".format(bet.get("betid")), value="User: {0} is betting: {1}   {2}  WAGER: {3}   TO WIN: {4}   {5}".format(username, betInfo, odds, wager, payout, eventtime), inline=False)

    else: 
        username = mda.getUsername(userid)
        embedVar = discord.Embed(title="{0} upcoming bets".format(username), description="{0} bets are as followed..".format(username) , color=0x1da1f2)
        for x in bets:
            bet = dict(zip(names, x)) 
            username = mda.getUsername(bet.get("bettorid"))
            betInfo = bet.get("bet")
            odds = bet.get("odds")
            wager = bet.get("wager")
            payout = bbl.getPayout(odds, wager)
            eventtime = bet.get("eventtime")
            embedVar.add_field(name="betID: {0}".format(bet.get("betid")), value="{0}   {1}  WAGER: {2}   TO WIN: {3}   {4}".format(betInfo, odds, wager, payout, eventtime), inline=False)

    return embedVar