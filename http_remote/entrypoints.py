import argparse
import sys

from tornado.ioloop import IOLoop
from tornado.web import Application

from http_remote.application import handlers


def graceful_exit(loop):                                                       
    """                                                                        
    Used to gracefully exit from a Tornado IOLoop when CTRL-C is pressed.      

    This will start the loop and watch for a KeyboardInterrupt to be raised and 
    sys.exit without a large nasty stacktrace.                                 
    """                                                                        
    try:                                                                       
        loop.start()                                                           
    except KeyboardInterrupt:                                                  
        print('')                                                              
        sys.exit(0)  


def run_server():
    """
    Entrypoint to run the remote server.

    """
    parser = argparse.ArgumentParser(description='Run remote server')
    parser.add_argument('-p', '--port', dest='port', default=8080, type=int,
        help='What port to serve on, default 8080')

    args = parser.parse_args()

    application = Application(handlers)
    application.listen(args.port)

    print ('HTTP Remote server up and running on {0}'.format(args.port))
    print ('Hit <Ctrl-C> to stop')

    loop = IOLoop.instance()
    graceful_exit(loop)



if __name__ == '__main__':
    run_server()
