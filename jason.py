#!/usr/bin/env python
#Check jason o's twitter status
import twitter, random, time

a = twitter.Api(consumer_key='e7DxXpnhlFcsgpH5YhU6Q', consumer_secret='syGPmhjDY7RXTlKALFQ8Tcb0h4gyOsONuTI5aks', access_token_key='231584757-v3jieem3vXnoKUVOKUOTrm1MPb3UJiEr4UW0J88p', access_token_secret='5ijAA3E1S3sHqDsCmgxg6PoJ15j3JwfDFbtJyntWgu7hF')
t = a.GetUserTimeline(screen_name='joertell', count=10)

r = random.Random()
r.seed(time.time())
print 'Wisdom of Jason: ' + r.choice(t).text.encode('utf8').strip()
