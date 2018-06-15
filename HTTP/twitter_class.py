from twython import Twython,TwythonError

class GettingTwitter:
    def __init__(self):
        self.APP_KEY = ''
        self.APP_SECRET = ''

    def get_data(self,keyword,count):
        try:
            twitter = Twython(app_key=self.APP_KEY, app_secret=self.APP_SECRET)
            data = twitter.search(q=keyword, count = count)
            return data["statuses"]

        except TwythonError:
            print("Fail to get data from Twitter")

if __name__ == "__main__":
    gt=GettingTwitter()
    twitter_list = gt.get_data('big data',30)
    for e in twitter_list:
        print(e['text'])