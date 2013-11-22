from twisted.web import proxy, http
from twisted.internet import reactor
import json

logfile = 'log'

import logging
logging.basicConfig(
        format='[%(levelname)s][%(asctime)s]%(message)s',
        datefmt='%Y%m%d-%H%M%S',
        level = logging.DEBUG,
        filename = logfile
        )

class LogProxy(proxy.Proxy):
    def allContentReceived(self):
        # Modify default method to log important information
        # in a desired format
        proxy.Proxy.allContentReceived(self)
        req = self.requests[-1]
        info = {
            'method': req.method,
            'uri': req.uri,
            'path': req.path,
            'headers': req.getAllHeaders()
        }
        logging.info(json.dumps(info) + '\n')

class ProxyFactory(http.HTTPFactory):
    protocol = LogProxy

reactor.listenTCP(4080, ProxyFactory())
reactor.run()
