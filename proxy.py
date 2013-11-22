from twisted.web import proxy, http
from twisted.internet import reactor
#from twisted.python import log
import sys
#log.startLogging(sys.stdout)

import pickle
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
    #def allHeadersReceived(self):
    #    #print "hhhh"
    #    #super(LogProxy, self).allHeadersReceived()
    #    proxy.Proxy.allHeadersReceived(self)
    #    req = self.requests[-1]
    #    #sys.stderr.write(str(req) + '\n')
    #    sys.stderr.write(str(req.requestHeaders) + '\n')
    #    sys.stderr.write(str(req.path) + '\n')
    #    #pickle.dump(req, open('req.pickle', 'w'))

    def allContentReceived(self):
        proxy.Proxy.allContentReceived(self)
        req = self.requests[-1]
        #sys.stderr.write('method:' + str(req.method) + '\n')
        #sys.stderr.write('uri:' + str(req.uri) + '\n')
        #sys.stderr.write('path:' + str(req.path) + '\n')
        #sys.stderr.write('headers:' + str(req.requestHeaders) + '\n')
        info = {
            'method': req.method,
            'uri': req.uri,
            'path': req.path,
            'headers': req.getAllHeaders()
        }
        #sys.stdout.write(json.dumps(info) + '\n')
        logging.info(json.dumps(info) + '\n')

class ProxyFactory(http.HTTPFactory):
    protocol = LogProxy

reactor.listenTCP(4080, ProxyFactory())
reactor.run()
