import uuid 
import base58


"""
    Sequencer can be initialized as Sequencer()
    - for each entry you type Sequencer.entry(long_url)
"""


class Sequencer:
    def __init__(self):
        pass

    def check_uuid_in_db(self, uuid):
        pass

    def create_next_short_hash(self):
        try:
            unique_id = uuid.uuid4()
            bytesarray = bytearray(unique_id.bytes)
            short_url = base58.b58encode(bytesarray)

        except Exception as e:
            print("Class %s"%("Sequencer", e))

        return short_url

