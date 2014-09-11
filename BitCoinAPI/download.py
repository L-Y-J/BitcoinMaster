__author__ = 'LI'
from urllib2 import urlopen
import json
import URL

class DownLoad:
    def __init__(self):
        pass

    def downLoad(self,URL,key,args = None):
        url = URL.get_urlTable().get(key)
        if (url==None):
            return

        if (args != None):
            if (isinstance(args,list)):
                url = url + args[0] + '/' + args[1]
            else:
                 url = url + args
        try:
            f = urlopen(url)
        except:
            return -1

        g = f.read()
        json_data = json.loads(g)
        return json_data


if __name__ == '__main__':
    url = URL.URL()
    d = DownLoad()
    args = ['ltc_btc','1']
    print d.downLoad(url,"trade_root",args)