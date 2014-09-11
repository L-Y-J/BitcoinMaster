__author__ = 'LI'

import ConfigParser

class URL:
    _urlTable = dict()

    def __init__(self):
        if len(self._urlTable) == 0:
            config = ConfigParser.ConfigParser()
            config.read("URL.ini")
            self._urlTable['pairs'] = config.get("pairs","url")
            self._urlTable['tickers'] = config.get("tickers","url")
            self._urlTable['ticker_root'] = config.get("ticker_root","url")
            self._urlTable['depth_root'] = config.get("depth_root","url")
            self._urlTable['trade_root'] = config.get("trade_root","url")

    def get_urlTable(self):
        return self._urlTable

if __name__ == '__main__':
    url = URL()
    print url.get_urlTable()