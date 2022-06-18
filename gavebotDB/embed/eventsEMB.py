import discord
import events.eventsDA as eda

def getEventsEmbed(content, league, names):
    if league == 'LIVE':
        embedVar = discord.Embed(title="{0} events:".format(league), description="Events currently in play".format(league), color=0x1da1f2)
    else:
        embedVar = discord.Embed(title="{0} events:".format(league), description="Upcoming events for {0}".format(league), color=0x1da1f2)
        
    logoUrl = eda.getLeagueLogo(league)
    for x in content:
        event = dict(zip(names, x))
        awayTeam = event.get("awayteam")
        homeTeam = event.get("hometeam")
        eventtime = event.get("eventtime")
        eventdate = event.get("eventdate")
        embedVar.add_field(name="EventID: {0}".format(event.get("eventid")), value="{0}    @    {1}    Time: {2}    Date: {3}".format(awayTeam, homeTeam, eventtime, eventdate), inline=False)
    
    embedVar.set_thumbnail(url='{0}'.format(logoUrl))
    return embedVar