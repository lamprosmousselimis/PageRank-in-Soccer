# PageRank-in-Soccer
Application of PageRank algorithm in top soccer leagues

PageRank algorithm measures the importance of a webpage according to its link structure. 

That is, if site A has a link to site B, then B shares a proportion of the importance of A.

This idea can also be applied in Soccer League, where the link structure is analogous to match results, and 
importance is analogous to the number of fans of each team. It can be summarized as a linear system
 ![image](https://github.com/yeliu0218/PageRank-in-Soccer/blob/master/chart.png)
where P is a column stochastic matrix, alpha is a scalar and v is a unit vector with equal components

This code implements the PageRank scheme, with a user-defined function of interpreting the match results.
It provides the ranking of top soccer leagues in Europe from season 2008/2009 to 2015/2016, including 

Belgium Jupiler League， 

England Premier League， 

France Ligue 1， 

Germany 1. Bundesliga， 

Italy Serie A， 

Netherlands Eredivisie， 

Poland Ekstraklasa， 

Portugal Liga ZON Sagres， 

Scotland Premier League， 

Spain LIGA BBVA， 

Switzerland Super League

The data comes from https://www.kaggle.com/hugomathien/soccer

# Run the code

Download the package, unzip database.sqlite.zip and put it in the same directory as in main.py
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

I am trying to make the code more user-friendly. 













