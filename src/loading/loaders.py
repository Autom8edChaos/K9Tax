import pandas as pd
from abc import ABC


class RawLoader(ABC):
    def _load_raw(self, model):
        db = self.pw_db
        db.create_tables([model])
        
        data = self._fetch_all(self.col_mapping.keys())
        fields = self.col_mapping.values()

        # for record in data:
        #     model.insert(record, fields=fields)
        # return 
        
        with db.atomic() as txn:
            model.insert_many(data, fields=fields).execute()
            txn.commit()

class StagingLoader(ABC):
    def __init__(self, name_stg, peewee_db):
        self.pw_db = peewee_db
        self.connection = peewee_db.connection()
        self.name_stg = name_stg

    def load_staging(self, source):
        data = pd.read_csv(source)
        self._load_staging_data(data)
        
    def _load_staging_data(self, data):
        data.to_sql(self.name_stg, self.connection, if_exists='replace', index=False)
        
    def _fetch_all(self, columns: list):
        cursor = self.connection.execute(
            f'SELECT {",".join(columns)} FROM {self.name_stg}'
        )
        return cursor.fetchall()

class Loader(StagingLoader, RawLoader):

    def __init__(self, peewee_database):
        super().__init__(f'stg_{self.model.__name__}', peewee_database)
    
    def load_raw(self):
        self._load_raw(self.model)