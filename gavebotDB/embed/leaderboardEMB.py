import discord
import master.masterDA as mda

def getLeaderboard(content, names):
    counter = 1
    embedVar = discord.Embed(title="CURRENT STANDINGS", description="by profit", color=0x1da1f2)
    for x in content:

        user = dict(zip(names, x))
        userrank= counter
        wins = user.get("wins")
        losses = user.get("losses")
        currentbankroll = user.get("currentbankroll")
        startbankroll = user.get("startbankroll")
        profit = currentbankroll - startbankroll
        totalWagered = user.get("amountwagered")
        tails = user.get("betstailed")
        bets = user.get("betsplaced")
        username = mda.getUsername(user.get("userid"))

        embedVar.add_field(name="{0}.  {1}    Profit: {2} ".format(userrank, username, profit), value="Wins: {0}, Losses: {1}, Bankroll: {2}, Bets placed: {3}, Bets Tailed: {4} Total Wagered: {5}".format(wins, losses, currentbankroll, bets, tails, totalWagered), inline=False)
    

    return embedVar
