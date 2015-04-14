__author__ = 'Андрій'
from server import CherryServer
import cherrypy
import email_sender
from jinja2 import Template
import xml_parser


class PagesGenerator:

    @cherrypy.expose
    def index(self):
        return Template(open("pages\index.html", encoding="UTF-8").read()).\
            render(stickers=xml_parser.get_stickers())

    @cherrypy.expose
    def contact(self):
        return open("pages\contact.html", encoding="UTF-8")

    @cherrypy.expose
    def default(self, attr='abc'):
        return open("pages\\404.html")

    @cherrypy.expose
    def feedback(self, name, email, text):
        message = 'Feedback from: {0},\ne-mail address: {1}, \nfeedback body:\n\t{2}'.format(name, email,
                                                                                             text.lstrip().rstrip())
        email_sender.send(message)
        return "Success"


webapp = PagesGenerator()
server = CherryServer()
server.start(webapp)