import discord
from httplib2 import FailedToDecompressContent

def getHelp():
    embedVar = discord.Embed(title="GAVEBOT HELP....!!! ", description="how to use gavebot", color=0x1da1f2)
    embedVar.add_field(name="$trumprandom", value="This command will return a random tweet from president trump himself", inline=False)
    embedVar.add_field(name="$events [option]", value="This command will show a list of events based on the option provided.... ", inline=False)
    embedVar.add_field(name="options", value="MLB ONLY FOR NOW", inline=True)
    embedVar.add_field(name="$place [-o -w -e -m] -b", value="Use this command to place a bet using the given flags as indicators for your odds, wager, eventid, market, bet", inline=False)
    embedVar.add_field(name="$place continued...", value="the only format rule for place is that the -b flag is the last flag in the command.. ", inline=True)
    embedVar.add_field(name="$place continued... values for -m flag", value="'M' should be used when placing a bet on a main market [spread, ml, total].....\n'TMP' should be used when placing a team prop bet\n'PP' should be used when placing a player prop bet", inline=True)
    embedVar.add_field(name="$place continued.. format for -b flag", value="the format after -b should look like [team or player][total points, spread, ML][category..points, hits, yards etc...]", inline=False)
    embedVar.add_field(name="$place continued.. examples for -b flag", value="Phillies ML\nJames Harden O 2.5 rebounds\n Eagles -6\nNYY@BOS O 10 runs,", inline=True)
    embedVar.add_field(name="$place examples", value="$place -e 3 -o -115 -w 2 -m M -b PHILLIES ML\n$place -e 6 -w 2 -o 200 -m PP -b stephen curry o 6 3s", inline=False)
    embedVar.add_field(name="$slip [betid]", value="This command will return a betslip for the stated betid", inline=False)
    embedVar.add_field(name="$bets [option]", value="This command will return bets depending on the option ", inline=True)
    embedVar.add_field(name="options ", value="ME, (any username), (any usernickname), TODAY", inline=True)
    embedVar.add_field(name="$users", value="This will return information about all users including username and nickname", inline=False)
    embedVar.add_field(name="$tail [betid], [wager]", value="This command will tail a bet with betid and wager", inline=False)
    embedVar.add_field(name="$markets", value="This command will return information about the markets you can place wagers on", inline=False)
    embedVar.add_field(name="$stats [option]", value="This command will show stats based on option ", inline=True)
    embedVar.add_field(name="options", value="Me, (any username), (any usernickname)", inline=True)
    embedVar.add_field(name="$bankroll", value="This command will return your current bankroll", inline=False)
    embedVar.add_field(name="$leaderboard", value="This command will return the current standings", inline=False)
    embedVar.add_field(name="$nickname [nickname]", value="This command will set user nickname to [nickname]", inline=False)
    
    return embedVar