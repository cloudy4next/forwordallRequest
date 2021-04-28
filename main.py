from src.utils import *
from src.tk_app import app
from multiprocessing import freeze_support
# from winproxy import ProxySetting
import threading




if __name__ == '__main__':
    freeze_support()
    proxyPort = 8888
    proxyBinding = '127.0.0.1'
    proxyForwardTo = ('139.162.23.165', 443)
    proxyAuthentication = False 

    print(' * ForwardProxy')
    proxy = Proxy(proxyBinding, proxyPort)
    print(' * Listening on: ' + str(proxyBinding) + ' : ' + str(proxyPort))
    print(' * Forwarding to: ' + str(proxyForwardTo[0]) + ' : ' + str(proxyForwardTo[1]))


    ## // multi-threading //
    t1 = threading.Thread(target=app)
    t2 = threading.Thread(target=proxy.main_loop)
    t1.start()
    t2.start()