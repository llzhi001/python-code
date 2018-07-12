#api https://api.github.com/search/repositories?q=topic:crawler+language:python+created:2018-02-08
#message api https://api.pushover.net/1/messages.json?token=ay8tk6ugn9bo9bvg16pcqmoidwxb78&user=udmnrm5b6jzef8ae4fu292z7ve4a28&message=xxx

# get_info_list --- push_it

from datetime import datetime
import requests

def get_info_list():
    api = 'https://api.github.com/search/repositories?q='
    query = 'topic:crawler+language:python+'
    when = 'created:' + str(datetime.now()).split()[0]
    full_url = api + query + when
    r = requests.get(full_url)
    return r.json()['items']

def make_massage(repo_info):
    title = repo_info['name']
    url = repo_info['html_url']
    message = repo_info['description']
    token = 'ay8tk6ugn9bo9bvg16pcqmoidwxb78'
    user = 'udmnrm5b6jzef8ae4fu292z7ve4a28'
    api = 'https://api.pushover.net/1/messages.json?'
    template = 'token={token}&user={user}&message={msg}&title={t}&url={url}'
    query = template.format(
        token=token,
        user=user,
        msg=message,
        t=title,
        url=url
    )
    full_url = api + query
    return full_url

def push_it(message):
    requests.post(message)
    print('Done')

info_list = get_info_list()
for info in info_list:
    message = make_massage(info)
    push_it(message)