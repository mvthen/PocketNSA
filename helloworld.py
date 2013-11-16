import webapp2
from twilio import twiml
from models import Company


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('q-back says suppp.')

class HelloMonkey(webapp2.RequestHandler):
    def post(self):
        r = twiml.Response()
        r.say("Hello Monkey!!")
        self.response.headers['Content-Type'] = 'text/xml'
        self.response.write(str(r))

class AddCompanies(webapp2.RequestHandler):
    def get(self):
        company = Company(name='Target', number="987987")
        company.put()
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('added')

app = webapp2.WSGIApplication([
                                  ('/twiml', HelloMonkey), ('/', MainPage), ('/addcompany', AddCompanies)],
                              debug=True)
