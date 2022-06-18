import discord


def getUserEMB(users, names):
    embedVar = discord.Embed(title="USERS INFORMATION", description="INFORMATION ABOUT USERS", color=0x1da1f2)

    for x in users:
        user = dict(zip(names, x))
        userid = user.get("userid")
        username = user.get("username")
        nickname = user.get("nickname")
        embedVar.add_field(name="UserID: {0}".format(userid), value="username: {0}     nickname: {1}       ".format(username, nickname), inline=False)

    return embedVar

    