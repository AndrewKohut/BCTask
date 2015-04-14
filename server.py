__author__ = 'Андрій'

import os, os.path
import cherrypy


class CherryServer:

    def start(self, webapp):
        conf = {
         '/': {
             'tools.staticdir.root': os.path.abspath(os.getcwd()),
         },

         '/static': {
             'tools.staticdir.on': True,
             'tools.staticdir.dir': './public'
         },
          'global': {
            'request.show_tracebacks':False,
            'engine.autoreload.on': False
          },

        }
        cherrypy.server.socket_host = '0.0.0.0'
        cherrypy.quickstart(webapp, '/', conf)

    def stop(self):
        cherrypy.engine.exit()