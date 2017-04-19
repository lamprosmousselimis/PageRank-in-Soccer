# PageRank-in-Soccer
Application of PageRank algorithm in top soccer leagues
-----------

PageRank algorithm measures the importance of a webpage according to its link structure. 

That is, if site A has a link to site B, then B shares a proportion of the importance of A.

This idea can also be applied in Soccer League, where the link structure is analogous to match results, and 
importance is analogous to the number of fans of each team. It can be summarized as a linear system
 ![image](https://github.com/yeliu0218/PageRank-in-Soccer/blob/master/chart.png)
where P is a column stochastic matrix, alpha is a scalar and v is a unit vector with equal components.

This code implements the PageRank scheme, with a user-defined function of interpreting the match results.
It provides the ranking of top soccer leagues in Europe from season 2008/2009 to 2015/2016, including 

Belgium Jupiler League 

England Premier League 

France Ligue 1

Germany 1. Bundesliga

Italy Serie A

Netherlands Eredivisie

Poland Ekstraklasa

Portugal Liga ZON Sagres

Scotland Premier League 

Spain LIGA BBVA

Switzerland Super League

The data comes from https://www.kaggle.com/hugomathien/soccer

# Run the code

Download the package, unzip database.sqlite.zip and put it in the same directory as in main.py.
Then type

`$ python3 main.py`

and select the season and league
It will show the ranking results.

You may also want to design your own scheme, i.e., the definition of P, which is realized by the function

```Python
def weights(a,b):
   "weights function given home goal a and away goal b in a match"
   return [a,b]
```
The input a and b are home goals and away goals of the two teams in a match, return values are their weight, by default
it is the same as input, which is a good but not the optimized solution.

alpha is set to be 0.85, but feel free to change it to any number within 0 and 1.

Below is an example of the results of Spain LIGA BBVA in season 2008/2009

2008/2009

PageRank score	 Team name 

0.0921131239914 FC Barcelona

0.0701640738674 Real Madrid CF

0.0694945842418 Valencia CF

0.0694696978911 Atlético Madrid

0.0660416832224 Villarreal CF

0.0611866690745 RCD Mallorca

0.0531571386832 RCD Espanyol

0.0499467376779 Racing Santander

0.0484823043838 Real Betis Balompié

0.0475067700837 Getafe CF

0.0473911925966 Real Sporting de Gijón

0.0434181792156 Sevilla FC

0.0424406573689 Málaga CF

0.0411173737056 RC Deportivo de La Coruña

0.0380688461971 UD Almería

0.0368904011387 Athletic Club de Bilbao

0.0351380749552 CA Osasuna

0.0299364604944 Real Valladolid

0.0298019465211 RC Recreativo

0.0282340846897 CD Numancia

I am trying to make the code more user-friendly. 












