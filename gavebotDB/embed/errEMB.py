import discord





def getError(errMessage):
    embedVar = discord.Embed(title="error", description=errMessage, color=0xcc0000)
    return embedVar