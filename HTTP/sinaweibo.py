#1.Weibo Requester Class
import pandas as pd
import urllib.request
import json

class SinaWeiboRequester:
    def __init__(self):
        self.base_url = 'https://api.weibo.com/2/{api}?page={page}&count={count}&access_token='

    def send_request(self,api,page=1,count=30):
        respons = urllib.request.urlopen(self.base_url.format(api=api,page=page,count=count))
        respons = respons.read().decode(respons.info().get_param('charset') or 'utf-8')
        data = json.loads(respons)
        return data

sina = SinaWeiboRequester()
status_json = sina.send_request('api接口')
status_json

#2.store response results into database
from sqlalchemy import create_engine，MetaData
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgres:123@localhost:5432/postgres')
meta = MetaData(bind=engine)
Session = sessionmaker(bind=engine)
session = Session

from sqlalchemy import Table,Column,String,Text,DataTime
weibo_table = Table('t_weibo',meta,
                    Column('id',String,primary_key=True),
                    Column('user_id', String),
                    Column('text', Text),
                    Column('created_at', DataTime())
                    )
meta.create_all()

from sqlalchemy.sql import insert
from datautil import parser
def insert_weibo(data):
    i = insert(weibo_table)
    for weibo in data:
        created_at = parser.parse(weibo.get('created_at'))
        i = i.values({'id':weibo.get('id'),
                    'user_id':weibo.get('user').get('id'),
                    'text':weibo.get('text'),
                    'created_at':created_at})
        session.execute(i)
    session.commit()

insert_weibo(status_json[‘statuses’])

#3.
status_data = json.dumps(status_json['statuses'])
weibo_df = pd.read_json(status_data)
weibo_df.head()

annotations_data = json_dumps(weibo_df.annotations[2])
annotations_df = pd.read_json(annotations_data)
annotations_df.tail()

weibo_df.user

user_table = Table('t_user', meta,
                    Column('id', String, primary_key=True),
                    Column('name', String),
                    Column('location', Text),
                    Column('description', Text),
                    Column('created_at', DataTime())
                    )
meta.create_all()

def insert_user(user):
    i = insert(user_table)
    created_at = parser.parse(user.get('created_at'))
    i = i.values({'id': user.get('id'),
                  'name': user.get('name'),
                  'location': user.get('location'),
                  'description': user.get('description'),
                  'created_at': created_at})
    session.execute(i)
    session.commit()

weibo_df.user.apply(insert_user)

