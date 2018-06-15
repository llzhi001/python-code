from twitter_class import GettingTwitter
from sqlalchemy import MetaData,create_engine,Table,Column,String,Text,DateTime,insert
from sqlalchemy.orm import sessionmaker
from datautil import parser

class PeristantData:
    def __init__(self):
        self.getting_twitter = GettingTwitter()

        self.database_type = 'postgresql'
        self.username = 'postgres'
        self.password = '123'
        self.databass_address = 'localhost'
        self.port = '5432'
        self.engine = create_engine('{database_type}://{username}:{password}@{address}:{port}/{database}'.format(
            database_type = self.database_type,
            username = self.username,
            password = self.password,
            address = self.databass_address,
            port = self.port,
            database = self.database
        ))

        self.meta_data = MetaData(bind=self.engine)
        self.session_maker = sessionmaker(bind=self.engine)
        self.session = self.session_maker()

    def create_table(self,table,name):
        twitter_table = Table(table_name,self.meta_data,
                              Column('id',String,primary_key=True),
                              Column('user_id',String),
                              Column('text',Text),
                              Column('created_at',DateTime),
                              extend_existing = True
                              )
        self.meta_data.create_all()
        return twitter_table

    def insert_twitter_data(self,data,table_name):
        i = insert(self.create_table(table_name))
        for twitter in data:
            create = parser.parse(twitter.get('created_at'))
            i = i.values({'id':twitter.get('id'),
                         'user_id':twitter.get('user').get('id'),
                         'text':twitter.get('text'),
                         'created_at':create})
            self.session.execute(i)
        self.session.commit()

if __name__ == '__main__':
    pd = PeristantData()
    twitter_data = pd.getting_twitter.get_data('big data',30)
    print(twitter_data)
    pd.insert_twitter_data(twitter_data,'t_twitter')
    print('30 twitters have been stored into database')
