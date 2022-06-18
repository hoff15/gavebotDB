import datetime
import discord
from discord.ext import commands
import bets.betsBL as bbl
import trump.trumpBL as trbl
import master.masterDA as mda
import master.masterBL as mbl
import events.eventsBL as ebl
import embed.betsEMB as betsEMB
import events.eventsDA as eda
import embed.helpEMB as helpEMB
import tracker.trackerBL as tbl
import tracker.trackerDA as tda

bot = commands.Bot(command_prefix='&')

client = discord.Client()



# returns random trump tweet to user when he was president
@bot.command(name='trumprandom')
async def randomPrezTrumpTweet(ctx):
    isprez = "True"
    embed = trbl.getRandomTrumpTweet(isprez)

    await ctx.send(embed=embed)




@bot.event
async def on_message(message):
    
    if message.author == client.user:
        return

    
    userid = message.author.id
    username = message.author
    mbl.newUser(userid, username)


    await bot.process_commands(message)
    return



@bot.command(name='events')
async def getEvents(ctx):
    message = ctx.message.content
    league = message.split(" ")[1]
    if ebl.checkLeague(league) == False:
        response = "invalid league try again"
        await ctx.send(response)
        return
    elif league == 'LIVE':
        embed = ebl.getLiveEvents(league)
    else:
        embed = ebl.getUpcomingEventsByLeague(league)

    await ctx.send(embed=embed)



@bot.command(name="place")
async def placeBet(ctx):
    message = ctx.message.content
    userid = ctx.message.author.id
    odds = message.split("-o ")[1]
    odds = odds.split(" ")[0]
    wager = message.split("-w ")[1]
    wager = wager.split(" ")[0]
    bet = message.split("-b ")[1]
    event = message.split("-e ")[1]
    event = event.split(" ")[0]
    market = message.split("-m ")[1]
    market = market.split(" ")[0]
    contestIndicator = "-contest"

    if contestIndicator in message:
        contest = message.split("-contest ")[1]
        contestid = contest.split(" ")[0]
    else:
        contestid = '0'

    
    if mbl.checkContest(contestid) == 'False':
        response = "Contest not found try again"
        await ctx.send(response)
        return
    if mbl.checkMarket(market) == 'False':
        response = "INVALID market try again"
        await ctx.send(response)
        return
    if mbl.checkEvent(event) == 'False':
        response = "Invalid event try again"
        await ctx.send(response)
        return

    userbankroll = tda.getUserBankRollByContestId(userid, contestid)

    if(int(wager) > int(userbankroll)):
        response = "Wager exceeds current bankroll"
        await ctx.send(response)
        return
    
    response = bbl.placeBet(odds, wager, market, bet, event, userid, contestid)

    if response == 'False':
        rtResponse = "Bet not placed try again"
        await ctx.send(rtResponse)
        return

    else:
        rtResponse = "BET successfully placed!!!!\n"
        isABet="True"
        newbankroll = userbankroll - float(wager)
        tbl.updateUserTacker(userid, contestid, wager, newbankroll, isABet)
    rtResponse += "TO view betslip use command $slip '{0}'".format(response)

    await ctx.send(rtResponse)



@bot.command(name='slip')
async def getBetSlip(ctx):
    message = ctx.message.content
    betID = message.split(" ")[1]
    if bbl.checkBetId(betID) == 'False':
        response = "BETID DOES NOT EXSIST"
        await ctx.send(response)
        return

    embed = betsEMB.getBetSlip(betID)

    await ctx.send(embed=embed)



@bot.command(name='bets')
async def getBets(ctx):
    message = ctx.message.content
    userid = ctx.message.author.id
    command = "&bets"
    
    if command == message:
        response = "plz add option"
        await ctx.send(response)
    
    option = message.split(" ")[1]
    print(option)

    embed = bbl.getBets(option, userid)
    await ctx.send(embed=embed)



@bot.command(name='users')
async def getUsers(ctx):
    embed = mbl.getUsers()

    await ctx.send(embed=embed)


@bot.command(name='tail')
async def tail(ctx):
    message = ctx.message.content
    userid = ctx.message.author.id
    retDict = {}
    betid = message.split(", ")[0]
    betid = betid.split(" ")[1]
    wager = message.split(", ")[1]
    contestid='0'
    print(betid)
    print(wager)

    userbankroll = tda.getUserBankRollByContestId(userid, contestid)

    if(int(wager) > int(userbankroll)):
        response = "Wager exceeds current bankroll"
        await ctx.send(response)
        return
    
    retDict = bbl.tailBet(betid, wager, userid)

    response = retDict["response"]
    rownum = retDict["rownum"]

    if rownum == 'False':
        await ctx.send(response)
        return
    else:
        newres = "Bet tailed! to view slip.... $slip {0}".format(rownum)
        isABet = "False"
        bbl.increaseTails(betid)
        newbankroll = userbankroll - wager
        tbl.updateUserTacker(userid, contestid, wager, newbankroll, isABet)
        await ctx.send(newres)
        return



@bot.command(name='helpmah')
async def helpMah(ctx):
    embed = helpEMB.getHelp()
    await ctx.send(embed=embed)


@bot.command(name='markets')
async def getMarkets(ctx):
    embed = mbl.getMarkets()
    await ctx.send(embed=embed)



@bot.command(name="stats")
async def getStats(ctx):
    message = ctx.message.content
    userid = ctx.message.author.id
    option = message.split(" ")[1]
    contestid = '0'

    embed = tbl.getStats(userid, contestid, option)
    await ctx.send(embed=embed)



@bot.command(name="bankroll")
async def getCurrentBankroll(ctx):
    userid = ctx.message.author.id
    contestid ='0'

    currentbankroll = tda.getUserBankRollByContestId(userid, contestid)

    response = "{0}  units..".format(currentbankroll)
    await ctx.send(response)

@bot.command(name="leaderboard")
async def getLeaderboard(ctx):
    contestid = '0'

    embed = tbl.getLeaderboard(contestid)
    await ctx.send(embed=embed)


@bot.command(name="nickname")
async def nickname(ctx):
    userid = ctx.message.author.id
    message = ctx.message.content

    nickname = message.split("$nickname ")[0]
    nickname = nickname.split(" ")[1]
    print(nickname)
    response = mbl.setNickname(userid, nickname)

    await ctx.send(response)





bot.run('')