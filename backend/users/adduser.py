
import falcon
import json
from db.user import postgres

class AddUser(object):
    def on_post(self, req, resp):
        database = postgres()
        data = req.bounded_stream.read().decode('utf8')
        data = json.loads(data)
        dataMasuk = (int(data["id"]),data["nama"],data["hp"],data["role"],data["status"])
        try:
            database.addNewUser(dataMasuk)
            resp.status = falcon.HTTP_200
        except:
            resp.status = falcon.HTTP_500

