from twython import Twython,TwythonError

twitter = Twython(app_key = '', app_secret='')

data = twitter.search(q='bigdata', count =5)
print(data)
all_data = data['statuses']
print(all_data)
