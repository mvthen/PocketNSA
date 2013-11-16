Twilio
======

Twilio appengine install instructions:


download google appengine python: https://developers.google.com/appengine/downloads#Google_App_Engine_SDK_for_Python

Install twilio google appengine client

Install virtualenv:
$ sudo easy_install pip
$ sudo pip install virtualenv
Set up a virtual python environment:
$ virtualenv --distribute venv
Activate virtualenv:
$ source venv/bin/activate
Use pip to install Twilio's Python library and dependencies:
$ pip install twilio
Deactivate your virtual environment:
$ deactivate
Link the Twilio library and its dependencies into your project:
$ ln -s venv/lib/python2.7/site-packages/twilio .
$ ln -s venv/lib/python2.7/site-packages/httplib2 .
$ ln -s venv/lib/python2.7/site-packages/six.py .


to run locally:
$path_to_appengine/dev_appserver.py .

to push to appengine:
$path_to_appengine/appcfg.py update .

On appengine:
http://q-back.appspot.com/

