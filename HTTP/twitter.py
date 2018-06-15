from twython import Iwython,IwythonError

twitter = Iwython(app_key = '', app_secret='')

data = twitter.search(q='bigdata', count =5)
print(data)
all_data = data['statuses']
print(all_data)
