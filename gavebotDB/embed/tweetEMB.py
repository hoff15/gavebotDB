import discord




def getTweet(tweet):
    embedVar = discord.Embed(title="@realDonaldTrump", description=tweet.get("content"), color=0x1da1f2)
    embedVar.add_field(name="Retweets", value=tweet.get("retweets"), inline=True)
    embedVar.add_field(name="Favs", value=tweet.get("favs"), inline=True)
    embedVar.add_field(name="Date", value=tweet.get("date"), inline=True)
    embedVar.set_thumbnail(url='https://pbs.twimg.com/profile_images/736392853992001537/eF4LJLkn_400x400.jpg')
    return embedVar