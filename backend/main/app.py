import falcon
from backend.users.adduser import AddUser
from backend.users.otp import Otp

api = application = falcon.API()

adduser = AddUser()
otp = Otp()
api.add_route('/adduser',adduser)
api.add_route('/otp',otp)