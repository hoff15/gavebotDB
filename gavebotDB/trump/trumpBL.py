import trump.trumpDA as trumpDA
import embed.tweetEMB as tweetEMB
import embed.errEMB as errEMB

def getRandomTrumpTweet(isprez):
    resDict = {}
    resDict = trumpDA.getRandomTrumpTweet(isprez)
    names = resDict["names"]
    content = resDict["tweet"]
    if names == 'False':
        response = "ERROR ERROR ERROR ERROR ERROR ERROR"
        embed = errEMB.getError(response)
        return embed
    

    tweet = dict(zip(names, content[0]))
    embed = tweetEMB.getTweet(tweet)
    return embed
    

