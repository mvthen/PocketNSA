import webapp2
from twilio import twiml
from twilio.rest import TwilioRestClient
from models import Company


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('q-back says suppp.')

class HelloMonkey(webapp2.RequestHandler):
    def post(self):
        r = twiml.Response()
        account_sid = "ACe77d9c1b662b932535ee1a28277cda39"
        auth_token = "0bbe3fb6b91364e4a6dd22eb2894ae96"
        client = TwilioRestClient(account_sid, auth_token)
        fromNum = self.request.get('From')
        #message = client.messages.get("")
        #print message.body

        r.say(fromNum)
        self.response.headers['Content-Type'] = 'text/xml'
        self.response.write(str(r))

class TextResponse(webapp2.RequestHandler):
    def post(self):
        r = twiml.Response()
        account_sid = "ACe77d9c1b662b932535ee1a28277cda39"
        auth_token = "0bbe3fb6b91364e4a6dd22eb2894ae96"
        client = TwilioRestClient(account_sid, auth_token)
        for message in client.messages.list():
            print message.body
        #fromNum = self.request.get('From')
        ##message = client.messages.get("")
        ##print message.body
        #
        #r.say(fromNum)
        self.response.headers['Content-Type'] = 'text/xml'
        self.response.write(str(r))

class AddCompanies(webapp2.RequestHandler):
    def get(self):
        company = Company(name='Target', number="987987")
        company.put()
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('added')

class SendSMS(webapp2.RequestHandler):
    def get(self):
        # replace with your credentials from: https://www.twilio.com/user/account
        account_sid = "ACe77d9c1b662b932535ee1a28277cda39"
        auth_token = "0bbe3fb6b91364e4a6dd22eb2894ae96"
        client = TwilioRestClient(account_sid, auth_token)
        # replace "to" and "from_" with real numbers
        rv = client.sms.messages.create(to="+19177038746",
                                        from_="+19177468448",
                                        body="Hello Monkey!")
        self.response.write(str(rv))
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello Monkey!')


app = webapp2.WSGIApplication([
                                  ('/twiml', HelloMonkey), ('/sms_response', TextResponse), ('/send_sms', SendSMS), ('/', MainPage), ('/addcompany', AddCompanies)],
                              debug=True)
