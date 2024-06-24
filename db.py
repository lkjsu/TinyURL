import sqlite3


"""
    Main layer that manages database handlers.
"""

class Db:
    def __init__(self):
        self.db = 'tinyurl.db'

    def add(self, table_name, params):
        result = None

        query = '''
            INSERT INTO %s (id, original_url, short_url, timestamp, user_id)
            VALUES (?,?,?,?,?)
            ''' %table_name
        try:
            with sqlite3.connect(self.db) as conn:
                cursor = conn.cursor()
                result = cursor.execute(query, params)
        except SyntaxError as se:
            print('Error inserting value', se)

        return result

    def read(self, table_name, params):
        result = None

        base_query = '''
            SELECT * FROM %s ''' % table_name

        where_clause = '''WHERE %s=?'''%params[0]

        query = base_query + where_clause

        try:
            with sqlite3.connect(self.db) as conn:
                cursor = conn.cursor()
                result = cursor.execute(query, (params[1],))
        except SyntaxError as se:
            print('Error reading value', se)

        return result

    def update(self, table_name, *params):
        result = None

        query = '''
            UPDATE %s
            SET short_url=?
            WHERE original_url=?
            '''
        try:
            with sqlite3.connect(self.db) as conn:
                cursor = conn.cursor()
                result = cursor.execute(query, (table_name, memoryview()))
        except SyntaxError as se:
            print('Error updating value', se)

    def delete(self, table_name, params):
        print(params[1], params)
        result = None

        base_query = '''DELETE FROM %s ''' % table_name

        where_clause = '''WHERE %s=?'''%params[0]

        query = base_query + where_clause
        print(query)
        try:
            with sqlite3.connect(self.db) as conn:
                cursor = conn.cursor()
                result = cursor.execute(query, (params[1],))
        except SyntaxError as se:
            print('Error reading value', se)
        
        return result

