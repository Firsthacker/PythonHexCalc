#!/usr/bin/env python

import webapp2      # default
import string       # for checking hex value
import os           # file access
import jinja2       # for html templates
from gaesessions import get_current_session # current session support (cookies)
from google.appengine.ext import db # google's datastorage

class History(db.Model):
    hexValue                    = db.StringProperty(multiline=True)
    decValue                    = db.StringProperty(multiline=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        session                 = get_current_session()
        hexValue                = session.get('hexValue', '')
        errMessage              = session.get('errMessage', '')
        resultMessage           = session.get('resultMessage', '')
        # db support
        self.query              = History.all()
        historyInfo             = ''
        for self.comment in self.query:
            historyInfo         = historyInfo + self.comment.hexValue + " -> " + self.comment.decValue + "; \n"
        # db support
        jinjaEnv                = jinja2.Environment(autoescape = True,
                                             loader = jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__),
                                             'templates')))
        templateVars            = { "hexValue": hexValue, "errMessage": errMessage,
                                    "resultMessage": resultMessage, "history": historyInfo }
        template                = jinjaEnv.get_template('index.html')
        self.response.out.write (template.render(templateVars))

    def post(self):
        hexValue                = self.request.get("hexValue")
        session                 = get_current_session()
        session['errMessage']   = ''
        session['resultMessage'] = ''
        session['hexValue']     = hexValue

        if all(c in string.hexdigits for c in hexValue) & len(hexValue) > 0:
            decValue            = int(hexValue, 16)
            session['resultMessage'] = "Dec value to " + hexValue + " = " + str(decValue)

            # storing for history
            self.comment        = History(hexValue = hexValue, decValue = str(decValue))
            self.comment.put    ()
        else:
            session['errMessage'] = "Invalid input"
        self.redirect           ("/")

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
