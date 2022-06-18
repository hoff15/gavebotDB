import mysql.connector

import gavebotConstants as gb

mydb = mysql.connector.connect(
    
)


cursor = mydb.cursor()


# Get Random Trump Tweet from database
def getRandomTrumpTweet(isprez):

    rtDict = {}
    

    if isprez == 'False':
        cursor.execute(gb.sql_GET_RANDOM_TRUMP_TWEET)
    elif isprez == 'True':
        cursor.execute(gb.sql_GET_RANDOM_PREZ_TRUMP_TWEET)


    tweet = cursor.fetchall()


    if tweet.__len__() < 1:
        rtDict["names"] = 'False'
        rtDict["tweet"] = 'False'
    else:
        rtDict["names"] = cursor.column_names
        rtDict["tweet"] = tweet
    
    return rtDict




