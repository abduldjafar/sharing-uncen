from sqlalchemy import create_engine,MetaData,select
from sqlalchemy import Table, Column, String, MetaData, INTEGER, insert, update


class postgres(object):

    def __init__(self):
        self.dbUrl = "postgresql://postgres:postgres@localhost/postgres"
        self.engine = create_engine(self.dbUrl)
        self.connection = self.engine.connect()
        self.metadata = MetaData()

        tabelUser = Table(
                        'userhara', self.metadata,
                        Column('id', INTEGER,  primary_key=True),
                        Column('nama', String),
                        Column('hp', String),
                        Column("role", String),
                        Column("status",String)
                    )
        self.metadata.bind = self.engine
        self.metadata.create_all(self.engine)
        try:
            tabelUser.create()
        except:
            print("Table Sudah Ada !")
        self.tableUser = Table('userhara', self.metadata, autoload=True, autoload_with=self.engine)

    def chekUserExist(self,nohp):
        query = select([self.tableUser]).where(self.tableUser.columns.hp == nohp)
        data = self.connection.execute(query).fetchall()
        if len(data) == 0:
            return 0
        else:
            return 1

    def addNewUser(self,data):
        query = insert(self.tableUser).values(id=data[0],nama=data[1], hp=data[2], role=data[3], status=data[4])
        executeQuery = self.connection.execute(query)

