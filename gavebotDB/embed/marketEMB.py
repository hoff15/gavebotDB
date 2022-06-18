import discord

def getMarkets(content, names):
    embedVar = discord.Embed(title="MARKETS", description="Markets avaiable for betting", color=0x1da1f2)
    for x in content:
        markets = dict(zip(names, x))
        marketid = markets.get("marketid")
        market = markets.get("market")
        marketnickname = markets.get("marketnickname")
        embedVar.add_field(name="MarketID: {0}".format(marketid), value="Market: {0}     nickname used for place command:  {1}".format(market, marketnickname), inline=False)
    
    return embedVar