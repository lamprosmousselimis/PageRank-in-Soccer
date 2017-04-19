import sqlite3 as sql
import numpy as np
from numpy import *;

# input parameters

league_id = '21518'
alpha = 0.85
input_list = ["2008/2009","2009/2010","2010/2011","2011/2012","2012/2013","2013/2014","2014/2015","2015/2016"] 
season = '"' + input("Select the input: " + ' '.join(input_list) + "\n") + '"'

def weights(a,b):
   "weights function given home goal a and away goal b in a match"
   
   return [a,b]

# read data from database
con = sql.connect('database.sqlite',isolation_level=None)
cur = con.cursor()
#league_id = '21518'
#season = '"2010/2011"'
sql="SELECT home_team_api_id, away_team_api_id, home_team_goal, away_team_goal FROM Match WHERE league_id=" + league_id + " and season =" + season
#print(sql)
cur.execute(sql)
result = cur.fetchall()
#print(result)
teams = []
for row in result:
#    print(row)   
    teams.append(row[0])
teams = list(set(teams))
#print(len(teams))
team_names = []
for row in teams:
	team_name = cur.execute("SELECT team_long_name FROM Team WHERE team_api_id= "+ str(row) )
	team_name = cur.fetchall()
	team_names.append(team_name[0])
#print(team_names)
#print(teams.index(8388))


# start the pagerank assembling and solving process

P=mat(zeros((20,20)))
for row in result:
	weight = weights(row[2],row[3])
	P[teams.index(row[0]),teams.index(row[1])]=weight[0]
	P[teams.index(row[1]),teams.index(row[0])]=weight[1]

for i in range(20):
    sum_column = sum(P[:,i])
    P[:,i] = P[:,i]/sum_column
#print(P)

I=identity(20)
v = np.full((20,1),1)/20
M = (I-alpha*P)
b = (1-alpha)*v
x = np.linalg.solve(M,b)
#print(x)
#print(teams)

#Given pagerank scores, print out rankings 

teams_score = list(zip(x,team_names))
#teams_score.sort()
#print(teams_score.transpose)
teams_sorted = sorted(teams_score, key=lambda score:score[0])
n=len(teams_score)
print('PageRank score\t Team name ')
for i in range(n):
	print(teams_sorted[n-1-i][0][0], teams_sorted[n-1-i][1][0])
#print(sortedteams)

con.close()
