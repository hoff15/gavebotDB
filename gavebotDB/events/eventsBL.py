import events.eventsDA as eda
import embed.eventsEMB as eemb
import embed.errEMB as errEMB



def checkEventID(eventid):
    response = eda.checkEventID(eventid)

    return response


def checkLeague(league):
    leagues = eda.getLeagues()
    league = str(league)
    if league in leagues:
        return True
    else:
        return False
    


def getUpcomingEventsByLeague(league):
    resDict = {}
    
    if league == 'TODAY':
        resDict = eda.getTodayEvents()
    else:
        resDict = eda.getUpcomingEventsByLeague(league)


    names = resDict["names"]
    content = resDict["events"]
    if names == 'False':
        response = "ERROR ERROR ERROR ERROR ERROR ERROR"
        embed = errEMB.getError(response)
        return embed
    
    embed = eemb.getEventsEmbed(content, league, names)
    return embed
    




def getLiveEvents(league):
    resDict = {}
    
    resDict = eda.getLiveEvents()

    names = resDict["names"]
    content = resDict["events"]
    if names == 'False':
        response = "ERROR ERROR ERROR ERROR ERROR ERROR"
        embed = errEMB.getError(response)
        return embed
    
    embed = eemb.getEventsEmbed(content, league, names)
    return embed
    