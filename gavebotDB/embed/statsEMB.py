import discord
import master.masterDA as mda
def getStats(userstats):

        username = mda.getUsername(userstats.get("userid"))
        embedVar = discord.Embed(title="{0}  Stats!".format(username), description="" , color=0x1da1f2) 
        embedVar.add_field(name="Wins", value="{0}".format(userstats.get("wins")), inline=True)
        embedVar.add_field(name="Losses", value="{0}".format(userstats.get("losses")), inline=True)
        embedVar.add_field(name="Total Amount Wagered", value="{0}".format(userstats.get("amountwagered")), inline=True)
        startbankroll = userstats.get("startbankroll")
        currentbankroll = userstats.get("currentbankroll")
        profit = currentbankroll - startbankroll
        embedVar.add_field(name="Profit", value="{0}".format(profit), inline=True)

        return embedVar