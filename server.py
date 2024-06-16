import asyncio
import collections
import json
import tornado
import db

from models.short_url_model import ShortUrlModel


class TinyURL(tornado.web.RequestHandler):
    short_url_model = ShortUrlModel()
    
    def post(self):
        """
        TODO: This method uses a lookup table which could be moved
              to the actual model as a Step 1, then use the db to 
              save stuff.
        """
        try:
            payload = json.loads(self.request.body)
            long_url = payload['url']
            short_url = self.short_url_model.create_new_short_url(long_url)
            self.write({'short-url': 'http://localhost:8888/%s'%short_url})

        except Exception as e:
            print(e) 

    def get(self):
        try:
            # TODO: move this to a model.
            rows = db.Db().read('tinyurl', ['short_url', memoryview(str.encode(self.request.uri[1:], 'utf8'))]).fetchall()
            result = rows[0][1].decode('utf8')
            self.redirect(result)

        except Exception as e:
            print(e)

    def delete(self, id):
        pass


routes = [
    (r'/short-url', TinyURL),
    (r'/.*', TinyURL)

]


async def main():
    application = tornado.web.Application(routes)
    application.listen(8888)
    await asyncio.Event().wait()


if __name__=='__main__':
    asyncio.run(main())

