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

class RecordingTwimlet(webapp2.RequestHandler):
    def get(self):
        conf_name = self.request.get('conf_name')
        recording_xml = '<Response><Dial record="true"><Conference>'+conf_name+'</Conference> </Dial></Response>'
        self.response.headers['Content-Type'] = 'text/xml'
        self.response.write(recording_xml)

class TextResponse(webapp2.RequestHandler):

    def post(self):
        r = twiml.Response()
        account_sid = "ACe77d9c1b662b932535ee1a28277cda39"
        auth_token = "0bbe3fb6b91364e4a6dd22eb2894ae96"
        client = TwilioRestClient(account_sid, auth_token)
        bodyMessage = self.request.get('Body')

        returnCall = client.calls.create(to=self.request.get('From'),
                                from_="+19177468448",
                                url="http://twimlets.com/conference?Name="+self.request.get('From'))
        call = client.calls.create(to=self.request.get('Body'),
                                    from_="+19177468448",
                                    url="http://twimlets.com/conference?Name="+self.request.get('From'))

        recordingURL = "http://twimlets.com/echo?Twiml=%3C%3Fxml%20version%3D%221.0%22%20encoding%3D%22UTF-8%22%3F%3E%0A%3CResponse%3E%0A%20%20%3CDial%20record%3D%22true%22%3E%0A%20%20%20%20%3CConference%3E"+self.request.get('From')+"%3C%2FConference%3E%0A%20%20%3C%2FDial%3E%0A%3C%2FResponse%3E&"
        recordCall = client.calls.create(to="+19177461446",
                                       from_="+19177468448",
                                     url=recordingURL)


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
        rv = client.calls.create(to="+19177038746",
                                        from_="+19177468448",
                                        url="http://twimlets.com/conference")
        self.response.write(str(rv))
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello Monkey!')


app = webapp2.WSGIApplication([
                                  ('/twiml', HelloMonkey),('/recording', RecordingTwimlet), ('/sms_response', TextResponse), ('/send_sms', SendSMS), ('/', MainPage), ('/addcompany', AddCompanies)],
                              debug=True)
