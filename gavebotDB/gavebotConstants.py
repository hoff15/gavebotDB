# SQL queries for gavebot

sql_GET_RANDOM_TRUMP_TWEET = 'SELECT * FROM trump ORDER BY RAND() LIMIT 1'

sql_GET_RANDOM_PREZ_TRUMP_TWEET = 'SELECT * FROM gavebot.trump where trump.date > DATE("2017-01-20") and trump.date < DATE("2021-01-20") ORDER BY RAND() LIMIT 1'

sql_INSERT_PICK = "INSERT INTO `gavebot`. `picks`(`pickid`, `userid`, `league`, `market`, `bet`, `odds`, `units`, `time`, `completed`, `winner`, `contestdate`, `tailed`, `tailedid`) VALUES('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '0', '0', '{8}', '0');"

sql_INSERT_PICK_TAIL = "INSERT INTO `gavebot`. `picks`(`pickid`, `userid`, `league`, `market`, `bet`, `odds`, `units`, `time`, `completed`, `winner`, `contestdate`, `tailed`, `tailedid`) VALUES('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '0', '0', '{8}', '1', '{9}');"

sql_GET_PICKS_ROWS_TOTAL = "SELECT COUNT(*) FROM picks"

sql_GET_X_AMT_OF_PICKS = "SELECT * FROM picks WHERE tailed = '0' ORDER BY contestdate DESC, time DESC LIMIT {0};"

sql_GET_USERNAME_FROM_USERID = "SELECT users.username FROM users WHERE users.userid = '{0}'"

sql_GET_DATE_PICKS = "SELECT * FROM picks WHERE picks.contestdate = '{0}' AND picks.tailed = '0' LIMIT 6";

sql_GET_USER_BETS = "SELECT * FROM picks WHERE picks.userid = '{0}' ORDER BY picks.contestdate DESC, picks.time DESC LIMIT 6;"

sql_GET_USER_IDS = "SELECT userid FROM users;"

sql_GET_PICK_BY_PICKID = "SELECT * FROM picks WHERE picks.pickid = '{0}'"

sql_INSERT_USER = "INSERT INTO `gavebotPROD`.`users` (`userid`, `username`) VALUES ('{0}', '{1}');"

sql_GET_LEAGUES = "SELECT league FROM league"

sql_GET_UPCOMING_EVENTS_BY_LEAGUE = "SELECT * FROM events WHERE leagueid IN ( SELECT leagueid FROM league WHERE league = '{0}' ) AND completed = 'N' AND started = 'N' ORDER BY eventtime ASC;"


sql_GET_LEAGUE_LOGO = "SELECT logo FROM league WHERE league ='{0}'"

sql_GET_TODAYS_EVENTS = "SELECT * FROM events WHERE eventdate = '{0}' AND completed = 'N' AND started = 'N' ORDER BY eventtime ASC;"

sql_GET_LIVE_EVENTS = "SELECT * FROM events WHERE completed = 'N' AND started ='Y' ORDER BY eventtime ASC;"

sql_GET_MARKETNICKNAME = "SELECT marketnickname FROM markets"

sql_GET_EVENTIDS = "SELECT eventid FROM events"

sql_INSERT_BET_NT_NF = "INSERT INTO `gavebotPROD`.`bets` (`eventid`, `timeplaced`, `bettorid`, `marketid`, `bet`, `odds`, `wager`, `winner`, `tails`, `contestid`) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', 'L', '0','{7}');"

sql_GET_MARKET_ID = "SELECT marketid FROM markets WHERE marketnickname = '{0}'"

sql_GET_BET_IDS = "SELECT betid FROM bets"

sql_GET_BET = "SELECT * FROM bets WHERE betid = '{0}'"

sql_GET_EVENT= "SELECT * FROM events WHERE eventid = '{0}'"


sql_GET_BETS_BY_DATE="SELECT a.betid, a.bettorid, a.bet, a.odds, a.wager, a.tails, b.eventtime FROM bets a LEFT JOIN events b ON a.eventid = b.eventid WHERE b.eventdate = '{0}' ORDER BY b.eventtime ASC"

sql_GET_USERNAME_BY_USERID="SELECT username FROM users WHERE userid ='{0}'"

sql_GET_UPCOMING_BETS_BY_USERID="SELECT a.betid, a.bettorid, a.bet, a.odds, a.wager, a.tails, b.eventtime FROM bets a LEFT JOIN events b ON a.eventid = b.eventid WHERE b.completed = 'N' AND b.started = 'N' AND a.bettorid = '{0}' ORDER BY b.eventtime ASC"


sql_GET_USERNAMES = "SELECT username FROM users"


sql_GET_NICKNAMES = "SELECT nickname FROM users"

sql_GET_USERID_BY_USERNAME = "SELECT userid FROM users WHERE username = '{0}'"

sql_GET_USERID_BY_NICKNAME = "SELECT userid FROM users WHERE nickname = '{0}'"

sql_GET_USERS = "SELECT * FROM users"

sql_INSERT_TAIL = "INSERT INTO `gavebotPROD`.`bets` (`eventid`, `timeplaced`, `bettorid`, `marketid`, `bet`, `odds`, `wager`, `winner`, `tails`, `tailedid`, `contestid`) VALUES ({0}, '{1}', '{2}', '{3}', '{4}', '{5}', {6}, 'L', 0, {7}, '{8}')"

sql_GET_TAILS_BY_BETID = "SELECT tails FROM bets WHERE betid={0}"

sql_UPDATE_TAILS = "UPDATE `gavebotPROD`.`bets` SET `tails` = '{0}' WHERE (`betid` = '{1}');"

sql_GET_MARKETS = "SELECT * FROM markets"


sql_GET_CONTESTIDS = "SELECT contestid FROM contests"

sql_ADD_USER_TO_TRACKER = "INSERT INTO `gavebotPROD`.`usertracker` (`userid`, `contestid`, `startbankroll`, `currentbankroll`, `betsplaced`, `betstailed`, `wins`, `losses`, `amountwagered`) VALUES ('{0}', '{1}', '{2}', '{3}', '0', '0', '0', '0', '0');"


sql_GET_USER_BANKROLL_BY_CONTESTID = "SELECT currentbankroll FROM usertracker WHERE userid = '{0}' AND contestid = '{1}'"
sql_GET_TAILSAMT_BY_USERID_CONTESTID = "SELECT betstailed FROM usertracker WHERE userid = '{0}' AND contestid = '{1}'"
sql_GET_BETSAMT_BY_USERID_CONTESTID = "SELECT betsplaced FROM usertracker WHERE userid = '{0}' AND contestid = '{1}'"
sql_GET_AMTWAGERED_BY_USERID_CONTESTID = "SELECT amountwagered FROM usertracker WHERE userid = '{0}' AND contestid = '{1}'"

sql_UPDATE_USER_TRACKER_TAIL = "UPDATE `gavebotPROD`.`usertracker` SET `currentbankroll` = '{0}', `betstailed` = '{1}', `amountwagered` = '{2}' WHERE (`userid` = '{3}') and (`contestid` = '{4}');"
sql_UPDATE_USER_TRACKER_BET = "UPDATE `gavebotPROD`.`usertracker` SET `currentbankroll` = '{0}', `betsplaced` = '{1}', `amountwagered` = '{2}' WHERE (`userid` = '{3}') and (`contestid` = '{4}');"

sql_GET_STATS_BY_USERID_CONTESTID = "SELECT * FROM usertracker WHERE userid = '{0}' AND contestid='{1}'"

sql_GET_LEADERBOARD_BY_CONTESTID ="SELECT * FROM usertracker WHERE contestid = {0} AND amountwagered > 0  ORDER BY currentbankroll DESC"

sql_SET_USERNICKNAME="UPDATE `gavebotPROD`.`users` SET `nickname` = '{0}' WHERE (`userid` = '{1}');"

# responses for gavebot
res_TRUMP_TWEET = '{date}        @realDonaldTrump\n{content}\nRetweets {retweets}        Favorites {favs}'