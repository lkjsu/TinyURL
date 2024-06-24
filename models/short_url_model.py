import base58
import collections
import time
import uuid

from db import Db
import models.sequencer as sequencer


class ShortUrlModel(Db):
    def __init__(self):

        super().__init__()
        self.sequencer = sequencer.Sequencer()

    def create_new_short_url(self, long_url):

        row = None
        short_url = None
        where_clause = ['original_url', memoryview(long_url.encode('utf8'))]
        rows = self.read('tinyurl', where_clause).fetchall()
        if not rows:
            short_url = self.sequencer.create_next_short_hash()
            rows = self.add('tinyurl', [memoryview(uuid.uuid4().bytes), memoryview(long_url.encode('utf8')), memoryview(short_url), time.time(), memoryview(uuid.uuid4().bytes)])
            return short_url.decode('utf8')
        row = rows[0]
        return row[2].decode('utf8')

    def get_original_url(self, short_url):
        params = ['short_url', memoryview(str.encode(short_url, 'utf8'))]
        rows = self.read('tinyurl', params).fetchall()
        result = rows[0][1].decode('utf8')
        return result

    def delete_short_url(self, short_url):
        params = ['short_url', memoryview(str.encode(short_url, 'utf8'))]
        rows = self.delete('tinyurl', params).fetchall()
        result = rows
        return result
